"""
Execute pending Anki changes from the anki_diff table.

Usage (from repo root):
    uv run python write.py [--delete-orphans]

    --delete-orphans   Also delete orphaned Anki notes (operation='delete').
                       Off by default.

Workflow:
    uv run python scan.py /vault --anki   # populate notes + anki_notes + anki_diff
    uv run python show.py                 # preview pending changes
    uv run python write.py                # push changes to Anki
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from urllib.error import URLError

import yaml

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from atomics import globals          # noqa: E402
from atomics.anki_connect import AnkiConnect  # noqa: E402
from atomics.config import Config    # noqa: E402
from atomics.db import NoteDB        # noqa: E402
from atomics.utils import strip_html # noqa: E402

# ── Known field names for common note types ────────────────────────────────────
_KNOWN_FIELDS: dict[str, list[str]] = {
    "Test":                           ["Front", "Back", "Tags"],
    "Basic":                          ["Front", "Back"],
    "Basic (and reversed card)":      ["Front", "Back"],
    "Basic (optional reversed card)": ["Front", "Back", "Add Reverse"],
    "Basic (type in the answer)":     ["Front", "Back"],
    "Cloze":                          ["Text", "Extra"],
}


# ── Init ───────────────────────────────────────────────────────────────────────

def _init() -> NoteDB:
    db = NoteDB()
    globals.NOTE_DB = db
    config = Config()
    try:
        config.load_config()
    except Exception as exc:
        print(f"Config error: {exc}")
        sys.exit(1)

    custom = globals.CONFIG_DATA.get("ATOMICS", {})
    fields_dict: dict[str, list[str]] = {}
    for note_type, pattern in custom.items():
        if note_type in _KNOWN_FIELDS:
            fields_dict[note_type] = _KNOWN_FIELDS[note_type]
        elif pattern:
            n_groups = re.compile(pattern).groups
            fields_dict[note_type] = [f"Field {i + 1}" for i in range(n_groups)]
        else:
            fields_dict[note_type] = _KNOWN_FIELDS.get(note_type, ["Front", "Back"])

    globals.FIELDS_DICT = fields_dict
    return db


# ── Helpers ────────────────────────────────────────────────────────────────────

def _resolve_model_fields(ac: AnkiConnect, entries: list[dict]) -> None:
    """Query AnkiConnect for real field names and update globals.FIELDS_DICT."""
    note_types: set[str] = set()
    for e in entries:
        nt = e.get("note_type")
        if nt and e.get("operation") in ("add", "update", "relink"):
            note_types.add(nt)

    for nt in note_types:
        try:
            fields = ac.invoke("modelFieldNames", modelName=nt)
            if fields:
                globals.FIELDS_DICT[nt] = fields
        except Exception:
            pass


def _abs_file_path(fp: str) -> str:
    if os.path.isabs(fp):
        return fp
    vault = globals.CONFIG_DATA.get("Vault", "")
    return os.path.join(vault, fp) if vault else fp


def _find_existing_anki_note(
    db: NoteDB, field_1: str | None, note_type: str
) -> int | None:
    if field_1 is None:
        return None

    rows = db._conn.execute(
        "SELECT anki_id FROM anki_notes WHERE note_type = ? AND field_1 = ?",
        (note_type, field_1),
    ).fetchall()
    if rows:
        claimed = {
            r["anki_id"] for r in db._conn.execute(
                "SELECT anki_id FROM notes WHERE anki_id IS NOT NULL"
            ).fetchall()
        }
        unclaimed = [r["anki_id"] for r in rows if r["anki_id"] not in claimed]
        return unclaimed[0] if unclaimed else rows[0]["anki_id"]

    plain = strip_html(field_1)
    if not plain:
        return None
    candidates = db._conn.execute(
        "SELECT anki_id, field_1 FROM anki_notes WHERE note_type = ?",
        (note_type,),
    ).fetchall()
    matches = [r["anki_id"] for r in candidates if strip_html(r["field_1"]) == plain]
    if not matches:
        return None
    claimed = {
        r["anki_id"] for r in db._conn.execute(
            "SELECT anki_id FROM notes WHERE anki_id IS NOT NULL"
        ).fetchall()
    }
    unclaimed = [aid for aid in matches if aid not in claimed]
    return unclaimed[0] if unclaimed else matches[0]


def _field_map(note_type: str, field_1: str | None, field_2: str | None) -> dict:
    names = globals.FIELDS_DICT.get(note_type) or _KNOWN_FIELDS.get(note_type, ["Front", "Back"])
    result = {}
    if len(names) >= 1 and field_1 is not None:
        result[names[0]] = field_1
    if len(names) >= 2 and field_2 is not None:
        result[names[1]] = field_2
    return result


def _parse_tags(raw) -> list:
    if not raw:
        return []
    if isinstance(raw, list):
        return raw
    try:
        return json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        return []


# ── Execute ────────────────────────────────────────────────────────────────────

def _ensure_decks(ac: AnkiConnect, entries: list[dict]) -> None:
    decks: set[str] = set()
    for e in entries:
        if e.get("operation") in ("add", "update", "relink"):
            d = e.get("deck_name")
            if d:
                decks.add(d)
    for deck in decks:
        try:
            ac.invoke("createDeck", deck=deck)
        except Exception as exc:
            print(f"[warn] createDeck {deck!r}: {exc}")


def execute(db: NoteDB, ac: AnkiConnect, delete_orphans: bool = False) -> dict:
    entries = db.get_diff_entries()
    results = {
        "added": 0, "updated": 0, "re_typed": 0, "relinked": 0,
        "reconciled": 0, "deleted": 0, "deck_changed": 0, "errors": [],
    }

    add_entries    = [e for e in entries if e["operation"] == "add"]
    relink_entries = [e for e in entries if e["operation"] == "relink"]
    update_entries = [e for e in entries if e["operation"] == "update"]
    retype_entries = [e for e in entries if e["operation"] == "retype"]
    deck_entries   = [e for e in entries if e["operation"] == "move_deck"]
    orphan_entries = [e for e in entries if e["operation"] == "delete"]

    # Relink: verify stale anki_id against live Anki; reconnect if still exists,
    # else promote to add so review history is preserved when possible.
    for entry in relink_entries:
        anki_id  = entry.get("anki_id")
        entry_id = entry["id"]
        if anki_id:
            try:
                info = ac.invoke("notesInfo", notes=[anki_id])
                if info and info[0].get("noteId"):
                    db.mark_synced(entry_id, anki_id)
                    db.clear_recommended_action(entry_id)
                    db.delete_diff_entry(entry_id)
                    results["relinked"] += 1
                    continue
            except Exception:
                pass
        # Note gone from Anki — add as new card
        add_entries.append(entry)

    _ensure_decks(ac, add_entries)

    for entry in add_entries:
        entry_id  = entry["id"]
        note_type = entry.get("note_type", "")
        deck_name = entry.get("deck_name") or globals.UNMATCHED_DECK
        fields    = _field_map(note_type, entry.get("field_1"), entry.get("field_2"))
        tags      = _parse_tags(entry.get("tags"))
        try:
            new_id = ac.invoke("addNote", note={
                "deckName":  deck_name,
                "modelName": note_type,
                "fields":    fields,
                "tags":      tags,
                "options":   {"allowDuplicate": False},
            })
            if new_id:
                db.mark_synced(entry_id, new_id)
                db.clear_recommended_action(entry_id)
            db.delete_diff_entry(entry_id)
            results["added"] += 1
        except Exception as exc:
            if "duplicate" in str(exc).lower():
                existing_id = _find_existing_anki_note(db, entry.get("field_1"), note_type)
                if existing_id:
                    db.mark_synced(entry_id, existing_id)
                    db.clear_recommended_action(entry_id)
                    db.delete_diff_entry(entry_id)
                    results["reconciled"] += 1
                    continue
            label = (entry.get("field_1") or "")[:40]
            results["errors"].append(f"addNote ({label!r}): {exc}")

    update_total = len(update_entries)
    for i, entry in enumerate(update_entries, 1):
        if i % 25 == 0 or i == update_total:
            print(f"  update {i}/{update_total}…")
        anki_id = entry.get("anki_id")
        if not anki_id:
            continue
        note_type = entry.get("note_type", "")
        fields    = _field_map(note_type, entry.get("field_1"), entry.get("field_2"))
        try:
            ac.invoke("updateNoteFields", note={"id": anki_id, "fields": fields})
            db.update_anki_note_fields(anki_id, entry.get("field_1"), entry.get("field_2"))
            deck_name = entry.get("deck_name")
            if deck_name:
                note_info = ac.invoke("notesInfo", notes=[anki_id])
                card_ids = note_info[0].get("cards", []) if note_info else []
                if card_ids:
                    ac.invoke("changeDeck", cards=card_ids, deck=deck_name)
            db.clear_recommended_action(entry["id"])
            db.delete_diff_entry(entry["id"])
            results["updated"] += 1
        except Exception as exc:
            results["errors"].append(f"updateNoteFields (id={anki_id}): {exc}")

    retype_total = len(retype_entries)
    for i, entry in enumerate(retype_entries, 1):
        if i % 25 == 0 or i == retype_total:
            print(f"  retype {i}/{retype_total}…")
        old_anki_id = entry.get("anki_id")
        entry_id    = entry["id"]
        note_type   = entry.get("note_type", "")
        deck_name   = entry.get("deck_name") or globals.UNMATCHED_DECK
        fields      = _field_map(note_type, entry.get("field_1"), entry.get("field_2"))
        tags        = _parse_tags(entry.get("tags"))
        try:
            if old_anki_id:
                ac.invoke("deleteNotes", notes=[old_anki_id])
            new_id = ac.invoke("addNote", note={
                "deckName":  deck_name,
                "modelName": note_type,
                "fields":    fields,
                "tags":      tags,
                "options":   {"allowDuplicate": False},
            })
            if new_id:
                db.mark_synced(entry_id, new_id)
                db.clear_recommended_action(entry_id)
            db.delete_diff_entry(entry_id)
            results["re_typed"] += 1
        except Exception as exc:
            label = (entry.get("field_1") or "")[:40]
            results["errors"].append(f"retype ({label!r}): {exc}")

    for entry in deck_entries:
        anki_id   = entry.get("anki_id")
        deck_name = entry.get("deck_name")
        if not anki_id or not deck_name:
            continue
        try:
            note_info = ac.invoke("notesInfo", notes=[anki_id])
            card_ids = note_info[0].get("cards", []) if note_info else []
            if card_ids:
                ac.invoke("changeDeck", cards=card_ids, deck=deck_name)
            db.clear_recommended_action(entry["id"])
            db.delete_diff_entry(entry["id"])
            results["deck_changed"] += 1
        except Exception as exc:
            results["errors"].append(f"changeDeck (id={anki_id}): {exc}")

    orphan_ids = [e["anki_id"] for e in orphan_entries if e.get("anki_id")]
    if orphan_ids:
        if delete_orphans:
            try:
                ac.invoke("deleteNotes", notes=orphan_ids)
                for e in orphan_entries:
                    db.delete_diff_entry(e["id"])
                results["deleted"] += len(orphan_ids)
            except Exception as exc:
                results["errors"].append(f"deleteNotes ({len(orphan_ids)} notes): {exc}")
        else:
            print(f"[warn] Skipped deletion of {len(orphan_ids)} orphan(s) — pass --delete-orphans to enable")

    return results


# ── CLI ────────────────────────────────────────────────────────────────────────

def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="write",
        description=(
            "Execute pending Anki changes from the anki_diff table.\n\n"
            "Run scan.py first to populate the diff table, then show.py to\n"
            "preview, then this script to apply."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--delete-orphans",
        action="store_true",
        dest="delete_orphans",
        help="Also delete orphaned Anki notes (operation='delete' in anki_diff).",
    )
    return parser


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()

    db = _init()

    summary = db.get_diff_summary()
    if not summary:
        print("Nothing pending — anki_diff table is empty. Run scan.py first.")
        db.close()
        return

    total = sum(r["n"] for r in summary)
    print("Pending changes:")
    for row in summary:
        print(f"  {row['operation']:12s}  {row['n']:>4d}")
    print(f"  {'total':12s}  {total:>4d}")

    orphan_count = next((r["n"] for r in summary if r["operation"] == "delete"), 0)
    if orphan_count and not args.delete_orphans:
        print(f"\n[warn] {orphan_count} orphan(s) queued for deletion — pass --delete-orphans to apply them")

    print("\nConnecting to Anki…")
    try:
        ac = AnkiConnect()
        ac.invoke("version")
    except (URLError, Exception) as exc:
        print(f"ERROR — cannot reach Anki: {exc}")
        print("Make sure Anki is running with AnkiConnect installed.")
        db.close()
        sys.exit(1)

    entries = db.get_diff_entries()
    _resolve_model_fields(ac, entries)

    results = execute(db, ac, delete_orphans=args.delete_orphans)
    db.close()

    print(f"\nDone — added={results['added']}, updated={results['updated']}, "
          f"re_typed={results['re_typed']}, relinked={results['relinked']}, "
          f"reconciled={results['reconciled']}, "
          f"deck_changed={results['deck_changed']}, deleted={results['deleted']}")
    if results["errors"]:
        print(f"\nErrors ({len(results['errors'])}):")
        for err in results["errors"]:
            print(f"  {err}")


if __name__ == "__main__":
    main()
