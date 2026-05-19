"""
Execute pending Anki changes from the anki_diff table.

Usage (from repo root):
    uv run python write.py [--dry-run] [--detail] [--delete-orphans]

    --dry-run        Preview pending changes without connecting to Anki.
    --detail         With --dry-run: show full field content (default: truncated).
    --delete-orphans Also delete orphaned Anki notes (operation='delete').
                     Off by default.

Workflow:
    uv run python scan.py /vault --anki   # populate notes + anki_notes + anki_diff
    uv run python write.py --dry-run      # preview pending changes
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
from atomics.anki_connect import AnkiConnect, Action  # noqa: E402
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
        if nt and e.get("operation") in ("add", "update", "relink", "retype"):
            note_types.add(nt)

    for nt in note_types:
        try:
            fields = ac.invoke(Action.MODEL_FIELD_NAMES, modelName=nt)
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


# ── Dry-run display ────────────────────────────────────────────────────────────

def _plain(text: str | None, max_len: int = 80) -> str:
    if not text:
        return ""
    plain = re.sub(r"<[^>]+>", "", text).replace("\n", " ").strip()
    return (plain[:max_len] + "…") if len(plain) > max_len else plain


def _field_names(note_type: str) -> tuple[str, str]:
    names = globals.FIELDS_DICT.get(note_type) or _KNOWN_FIELDS.get(note_type)
    if not names:
        custom = globals.CONFIG_DATA.get("ATOMICS", {})
        pattern = custom.get(note_type)
        if pattern:
            n = re.compile(pattern).groups
            names = [f"Field {i + 1}" for i in range(n)]
    names = names or ["Field 1", "Field 2"]
    f2 = names[1] if len(names) > 1 else "Field 2"
    return names[0], f2


def _show_diff(label: str, vault_val, anki_val, max_len: int) -> None:
    v = _plain(vault_val, max_len)
    a = _plain(anki_val, max_len) if anki_val is not None else None
    if a is None:
        print(f"    {label:<10}  →  {v}")
    elif v == a:
        print(f"    {label:<10}  [=]  {v}")
    else:
        print(f"    {label}:")
        print(f"      ←  {a}")
        print(f"      →  {v}")


def _show_delete_field(label: str, val, max_len: int) -> None:
    print(f"    {label:<10}  ✕  {_plain(val, max_len)}")


_DRY_OP_LABELS = {
    "add":       "ADD",
    "relink":    "RELINK",
    "update":    "UPDATE",
    "retype":    "RETYPE",
    "move_deck": "MOVE DECK",
    "delete":    "DELETE (orphan)",
    "stale":     "STALE",
}
_DRY_OP_ORDER = ["add", "relink", "update", "retype", "move_deck", "delete", "stale"]


def _dry_run(db: NoteDB, ac: AnkiConnect, delete_orphans: bool, detail: bool) -> None:
    entries = db.get_diff_entries()
    _resolve_model_fields(ac, entries)

    by_op: dict[str, list[dict]] = {}
    for e in entries:
        by_op.setdefault(e["operation"], []).append(e)

    total = sum(len(v) for v in by_op.values())
    sep = "─" * 60
    print(f"\n{sep}\nDRY RUN — no changes applied\n{sep}")
    print(f"Pending ({total} total):")
    for op in _DRY_OP_ORDER:
        n = len(by_op.get(op, []))
        if n:
            print(f"  {_DRY_OP_LABELS[op]:20s}  {n:>4d}")

    max_len = 120 if detail else 70

    # Live-resolve relink entries via NOTES_INFO
    relink_resolved: dict[int, dict | None] = {}
    for e in by_op.get("relink", []):
        anki_id = e.get("anki_id")
        if not anki_id:
            continue
        try:
            info = ac.invoke(Action.NOTES_INFO, notes=[anki_id])
            relink_resolved[anki_id] = (
                info[0] if (info and info[0] and info[0].get("noteId")) else None
            )
        except Exception:
            relink_resolved[anki_id] = None

    for op in _DRY_OP_ORDER:
        group = by_op.get(op, [])
        if not group:
            continue
        label = _DRY_OP_LABELS[op]
        if op == "delete" and not delete_orphans:
            label += "  — skipped (pass --delete-orphans to apply)"
        print(f"\n{sep}\n{label} ({len(group)})\n{sep}")

        for e in group:
            note_type = e.get("note_type") or "Unknown"
            anki_id   = e.get("anki_id")
            fp        = e.get("file_path") or ""
            deck      = e.get("deck_name") or ""
            vault_f1  = e.get("field_1")
            vault_f2  = e.get("field_2")
            f1_lbl, f2_lbl = _field_names(note_type)

            # Header
            parts = [f"  [{note_type}]"]
            if anki_id:
                suffix = " (not found in Anki)" if (
                    op == "relink" and relink_resolved.get(anki_id) is None
                ) else ""
                parts.append(f"  anki:{anki_id}{suffix}")
            if fp:
                parts.append(f"  ←  {fp}" if anki_id else f"  {fp}")
            print("".join(parts))

            # Action
            if op == "add":
                print(f"    ▶ {Action.ADD_NOTE}")
            elif op == "update":
                print(f"    ▶ {Action.UPDATE_NOTE_FIELDS}")
            elif op == "relink":
                if relink_resolved.get(anki_id) is not None:
                    print(f"    ▶ {Action.NOTES_INFO} → {Action.UPDATE_NOTE_FIELDS}")
                else:
                    print(f"    ▶ {Action.NOTES_INFO} → {Action.ADD_NOTE}")
            elif op == "retype":
                print(f"    ▶ {Action.DELETE_NOTES} → {Action.ADD_NOTE} [{note_type}]")
            elif op == "move_deck":
                print(f"    ▶ {Action.CHANGE_DECK}")
            elif op in ("delete", "stale"):
                flag = "" if delete_orphans else " (skipped)"
                print(f"    ▶ {Action.DELETE_NOTES}{flag}")

            # Deck
            if deck:
                if op == "move_deck":
                    anki_note = db.get_anki_note(anki_id) if anki_id else None
                    old_deck  = anki_note["deck_name"] if anki_note else "?"
                    print(f"    deck:  {old_deck} → {deck}")
                else:
                    print(f"    deck:  {deck}")

            # Fields
            if op == "add":
                print(f"    {f1_lbl:<10}  →  {_plain(vault_f1, max_len)}")
                if vault_f2 is not None:
                    print(f"    {f2_lbl:<10}  →  {_plain(vault_f2, max_len)}")

            elif op == "update":
                anki_note = db.get_anki_note(anki_id) if anki_id else None
                af1 = anki_note["field_1"] if anki_note else None
                af2 = anki_note["field_2"] if anki_note else None
                _show_diff(f1_lbl, vault_f1, af1, max_len)
                if vault_f2 is not None or af2 is not None:
                    _show_diff(f2_lbl, vault_f2, af2, max_len)

            elif op == "relink":
                note_data = relink_resolved.get(anki_id)
                if note_data:
                    ordered = sorted(
                        note_data["fields"].items(), key=lambda kv: kv[1]["order"]
                    )
                    af1 = ordered[0][1]["value"] if ordered else None
                    af2 = ordered[1][1]["value"] if len(ordered) > 1 else None
                    _show_diff(f1_lbl, vault_f1, af1, max_len)
                    if vault_f2 is not None or af2 is not None:
                        _show_diff(f2_lbl, vault_f2, af2, max_len)
                else:
                    print(f"    {f1_lbl:<10}  →  {_plain(vault_f1, max_len)}")
                    if vault_f2 is not None:
                        print(f"    {f2_lbl:<10}  →  {_plain(vault_f2, max_len)}")

            elif op in ("delete", "stale"):
                anki_note = db.get_anki_note(anki_id) if anki_id else None
                f1 = anki_note["field_1"] if anki_note else vault_f1
                f2 = anki_note["field_2"] if anki_note else vault_f2
                _show_delete_field(f1_lbl, f1, max_len)
                if f2 is not None:
                    _show_delete_field(f2_lbl, f2, max_len)

            elif op == "retype":
                anki_note = db.get_anki_note(anki_id) if anki_id else None
                if anki_note:
                    _show_delete_field(f1_lbl, anki_note["field_1"], max_len)
                    if anki_note.get("field_2"):
                        _show_delete_field(f2_lbl, anki_note["field_2"], max_len)
                print(f"    {f1_lbl:<10}  →  {_plain(vault_f1, max_len)}")
                if vault_f2 is not None:
                    print(f"    {f2_lbl:<10}  →  {_plain(vault_f2, max_len)}")


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
            ac.invoke(Action.CREATE_DECK, deck=deck)
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

        if not anki_id:
            add_entries.append(entry)
            continue

        # Block 1: check if note still exists in Anki
        info = None
        try:
            info = ac.invoke(Action.NOTES_INFO, notes=[anki_id])
        except Exception as exc:
            results["errors"].append(f"notesInfo (relink id={anki_id}): {exc}")
            continue  # can't verify — leave diff entry in place

        note_data = info[0] if (info and info[0] and info[0].get("noteId")) else None

        if note_data:
            # Block 2: update in place if content differs
            try:
                ordered = sorted(
                    note_data.get("fields", {}).items(),
                    key=lambda kv: kv[1]["order"],
                )
                anki_f1 = ordered[0][1]["value"] if ordered else None
                anki_f2 = ordered[1][1]["value"] if len(ordered) > 1 else None
                vault_f1 = entry.get("field_1")
                vault_f2 = entry.get("field_2")
                if vault_f1 != anki_f1 or vault_f2 != anki_f2:
                    field_names = [name for name, _ in ordered]
                    fields = {}
                    if field_names and vault_f1 is not None:
                        fields[field_names[0]] = vault_f1
                    if len(field_names) > 1 and vault_f2 is not None:
                        fields[field_names[1]] = vault_f2
                    ac.invoke(Action.UPDATE_NOTE_FIELDS, note={"id": anki_id, "fields": fields})
                    db.update_anki_note_fields(anki_id, vault_f1, vault_f2)
                db.mark_synced(entry_id, anki_id)
                db.clear_recommended_action(entry_id)
                db.delete_diff_entry(entry_id)
                results["relinked"] += 1
            except Exception as exc:
                results["errors"].append(f"relink update (id={anki_id}): {exc}")
                # Note exists — do NOT promote to add
        else:
            # Note truly gone from Anki — safe to re-add
            add_entries.append(entry)

    _ensure_decks(ac, add_entries)

    for entry in add_entries:
        entry_id  = entry["id"]
        note_type = entry.get("note_type", "")
        deck_name = entry.get("deck_name") or globals.UNMATCHED_DECK
        fields    = _field_map(note_type, entry.get("field_1"), entry.get("field_2"))
        tags      = _parse_tags(entry.get("tags"))
        try:
            new_id = ac.invoke(Action.ADD_NOTE, note={
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
            ac.invoke(Action.UPDATE_NOTE_FIELDS, note={"id": anki_id, "fields": fields})
            db.update_anki_note_fields(anki_id, entry.get("field_1"), entry.get("field_2"))
            deck_name = entry.get("deck_name")
            if deck_name:
                note_info = ac.invoke(Action.NOTES_INFO, notes=[anki_id])
                card_ids = note_info[0].get("cards", []) if note_info and note_info[0] else []
                if card_ids:
                    ac.invoke(Action.CHANGE_DECK, cards=card_ids, deck=deck_name)
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
                ac.invoke(Action.DELETE_NOTES, notes=[old_anki_id])
            new_id = ac.invoke(Action.ADD_NOTE, note={
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
            note_info = ac.invoke(Action.NOTES_INFO, notes=[anki_id])
            card_ids = note_info[0].get("cards", []) if note_info and note_info[0] else []
            if card_ids:
                ac.invoke(Action.CHANGE_DECK, cards=card_ids, deck=deck_name)
            db.clear_recommended_action(entry["id"])
            db.delete_diff_entry(entry["id"])
            results["deck_changed"] += 1
        except Exception as exc:
            results["errors"].append(f"changeDeck (id={anki_id}): {exc}")

    orphan_ids = [e["anki_id"] for e in orphan_entries if e.get("anki_id")]
    if orphan_ids:
        if delete_orphans:
            try:
                ac.invoke(Action.DELETE_NOTES, notes=orphan_ids)
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
            "Run scan.py first to populate the diff table, then use --dry-run\n"
            "to preview, then run without flags to apply."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--dry-run", "-n",
        action="store_true",
        dest="dry_run",
        help="Preview what write will do without applying any changes (requires Anki running).",
    )
    parser.add_argument(
        "--detail",
        action="store_true",
        help="With --dry-run: show full field content (default: truncated at 70 chars).",
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

    print("\nConnecting to Anki…")
    try:
        ac = AnkiConnect()
        ac.invoke(Action.VERSION)
    except (URLError, Exception) as exc:
        print(f"ERROR — cannot reach Anki: {exc}")
        print("Make sure Anki is running with AnkiConnect installed.")
        db.close()
        sys.exit(1)

    if args.dry_run:
        _dry_run(db, ac, delete_orphans=args.delete_orphans, detail=args.detail)
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
