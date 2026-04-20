"""
Executes Anki writes from a diff manifest produced by diff.py.

Usage (from obsidian_to_anki/):
    uv run python write.py [--manifest FILE] [--execute]

    --manifest   JSON manifest from diff.py (default: anki_diff.json).
    --execute    Actually write changes to Anki. Default is dry-run.

Workflow
--------
    uv run python scan.py --vault <vault>   # populate notes table
    uv run python scan.py --anki            # populate anki_notes table
    uv run python diff.py <vault>           # generate anki_diff.json + anki_diff.md
    # review anki_diff.md, then:
    uv run python write.py --execute        # push changes to Anki
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

from obsidian_to_anki import globals          # noqa: E402
from obsidian_to_anki.anki_connect import AnkiConnect  # noqa: E402
from obsidian_to_anki.config import Config    # noqa: E402
from obsidian_to_anki.db import NoteDB        # noqa: E402

_DEFAULT_MANIFEST = "anki_diff.json"

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

    custom = globals.CONFIG_DATA.get("CUSTOM_REGEXPS", {})
    fields_dict: dict[str, list[str]] = {}
    for note_type, pattern in custom.items():
        import re
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

def _resolve_model_fields(ac: AnkiConnect, manifest: dict) -> None:
    """Query AnkiConnect for real field names and update globals.FIELDS_DICT."""
    note_types: set[str] = set()
    for key in ("add", "update", "restale"):
        for entry in manifest.get(key, []):
            nt = entry.get("note_type")
            if nt:
                note_types.add(nt)

    for nt in note_types:
        try:
            fields = ac.invoke("modelFieldNames", modelName=nt)
            if fields:
                globals.FIELDS_DICT[nt] = fields
        except Exception:
            pass  # leave existing fallback in place


def _field_map(note_type: str, field_1: str | None, field_2: str | None) -> dict:
    names = globals.FIELDS_DICT.get(note_type) or _KNOWN_FIELDS.get(note_type, ["Front", "Back"])
    result = {}
    if len(names) >= 1 and field_1 is not None:
        result[names[0]] = field_1
    if len(names) >= 2 and field_2 is not None:
        result[names[1]] = field_2
    return result


# ── Frontmatter helpers ────────────────────────────────────────────────────────

_FM_RE = re.compile(r'^---\n(.*?)\n---\n', re.DOTALL)


def _read_frontmatter_sync(file_path: str) -> dict[str, int]:
    """Return anki_sync dict from YAML frontmatter, or {} if absent."""
    try:
        with open(file_path, encoding="utf-8") as fh:
            content = fh.read()
    except OSError:
        return {}
    m = _FM_RE.match(content)
    if not m:
        return {}
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return {}
    return {str(k): int(v) for k, v in fm.get("anki_sync", {}).items()}


def _write_frontmatter_sync(file_path: str, sync_map: dict[str, int]) -> None:
    """Upsert anki_sync into the file's YAML frontmatter (preserves other keys)."""
    with open(file_path, encoding="utf-8") as fh:
        content = fh.read()

    m = _FM_RE.match(content)
    if m:
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError:
            fm = {}
        body = content[m.end():]
    else:
        fm = {}
        body = content

    fm.setdefault("anki_sync", {})
    fm["anki_sync"].update(sync_map)

    fm_str = yaml.safe_dump(fm, default_flow_style=False, allow_unicode=True).rstrip()
    new_content = f"---\n{fm_str}\n---\n{body}"

    with open(file_path, "w", encoding="utf-8") as fh:
        fh.write(new_content)


# ── Execute ────────────────────────────────────────────────────────────────────

def _ensure_decks(ac: AnkiConnect, manifest: dict) -> None:
    """Create any decks referenced in the manifest that don't yet exist."""
    decks: set[str] = set()
    for key in ("add", "update", "restale"):
        for entry in manifest.get(key, []):
            d = entry.get("deck_name")
            if d:
                decks.add(d)
    for deck in decks:
        try:
            ac.invoke("createDeck", deck=deck)
        except Exception as exc:
            print(f"[warn] createDeck {deck!r}: {exc}")


def execute(manifest: dict, ac: AnkiConnect, db: NoteDB) -> dict:
    results = {"added": 0, "updated": 0, "re_added": 0, "deleted": 0, "errors": []}
    _ensure_decks(ac, manifest)

    # file_path → {uuid: anki_id} for frontmatter writes
    fm_updates: dict[str, dict[str, int]] = {}

    # stale → treat as add after clearing anki_id in DB
    for entry in manifest.get("restale", []):
        uuid = entry.get("uuid")
        if uuid:
            db._conn.execute("UPDATE notes SET anki_id = NULL WHERE id = ?", (uuid,))
            db._conn.commit()
        manifest.setdefault("_restale_add", []).append(entry)

    add_entries = manifest.get("add", []) + manifest.get("_restale_add", [])
    is_restale  = {id(e) for e in manifest.get("_restale_add", [])}

    for entry in add_entries:
        note_type = entry.get("note_type", "")
        deck_name = entry.get("deck_name") or globals.CONFIG_DATA.get("Deck", "Default")
        fields    = _field_map(note_type, entry.get("field_1"), entry.get("field_2"))
        tags      = entry.get("tags") or []
        try:
            new_id = ac.invoke("addNote", note={
                "deckName":  deck_name,
                "modelName": note_type,
                "fields":    fields,
                "tags":      tags,
                "options":   {"allowDuplicate": False},
            })
            if new_id and entry.get("uuid"):
                db.mark_synced(entry["uuid"], new_id)
                fp = entry.get("file_path")
                if fp:
                    fm_updates.setdefault(fp, {})[entry["uuid"]] = new_id
            if id(entry) in is_restale:
                results["re_added"] += 1
            else:
                results["added"] += 1
        except Exception as exc:
            label = (entry.get("field_1") or "")[:40]
            results["errors"].append(f"addNote ({label!r}): {exc}")

    for entry in manifest.get("update", []):
        anki_id = entry.get("anki_id")
        if not anki_id:
            continue
        note_type = entry.get("note_type", "")
        fields    = _field_map(note_type, entry.get("field_1"), entry.get("field_2"))
        try:
            ac.invoke("updateNoteFields", note={"id": anki_id, "fields": fields})
            # Move to correct deck if it has changed
            deck_name = entry.get("deck_name")
            if deck_name:
                note_info = ac.invoke("notesInfo", notes=[anki_id])
                card_ids = note_info[0].get("cards", []) if note_info else []
                if card_ids:
                    ac.invoke("changeDeck", cards=card_ids, deck=deck_name)
            results["updated"] += 1
            fp = entry.get("file_path")
            uuid = entry.get("uuid")
            if fp and uuid:
                fm_updates.setdefault(fp, {})[uuid] = anki_id
        except Exception as exc:
            results["errors"].append(f"updateNoteFields (id={anki_id}): {exc}")

    orphan_ids = [e["anki_id"] for e in manifest.get("orphan", []) if e.get("anki_id")]
    if orphan_ids:
        if results.get("_delete_orphans"):
            try:
                ac.invoke("deleteNotes", notes=orphan_ids)
                results["deleted"] += len(orphan_ids)
            except Exception as exc:
                results["errors"].append(f"deleteNotes ({len(orphan_ids)} notes): {exc}")
        else:
            print(f"[warn] Skipped deletion of {len(orphan_ids)} orphan(s) — pass --delete-orphans to enable")

    # Write anki_sync frontmatter to affected vault files
    fm_errors = 0
    for fp, sync_map in fm_updates.items():
        try:
            _write_frontmatter_sync(fp, sync_map)
        except Exception as exc:
            results["errors"].append(f"frontmatter ({fp}): {exc}")
            fm_errors += 1
    if fm_updates:
        written = len(fm_updates) - fm_errors
        print(f"[fm] Wrote anki_sync frontmatter to {written}/{len(fm_updates)} files")

    return results


# ── CLI ────────────────────────────────────────────────────────────────────────

def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="write",
        description=(
            "Execute Anki writes from a diff manifest (anki_diff.json).\n\n"
            "Default: dry-run — shows what would be done without touching Anki.\n"
            "Use --execute to push changes."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--manifest",
        default=_DEFAULT_MANIFEST,
        metavar="FILE",
        help=f"JSON manifest from diff.py (default: {_DEFAULT_MANIFEST}).",
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Actually write changes to Anki.",
    )
    parser.add_argument(
        "--delete-orphans",
        action="store_true",
        dest="delete_orphans",
        help="Also delete orphaned Anki notes listed in the manifest. Requires --execute.",
    )
    return parser


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()

    if not os.path.exists(args.manifest):
        print(f"Manifest not found: {args.manifest}")
        print("Run: uv run python diff.py <vault_path>")
        sys.exit(1)

    with open(args.manifest, encoding="utf-8") as fh:
        manifest = json.load(fh)

    add_count     = len(manifest.get("add", []))
    update_count  = len(manifest.get("update", []))
    restale_count = len(manifest.get("restale", []))
    orphan_count  = len(manifest.get("orphan", []))
    total         = add_count + update_count + restale_count + orphan_count

    print(f"Manifest: {args.manifest}")
    print(f"Generated: {manifest.get('generated', 'unknown')}")
    print(f"Mode: {'EXECUTE' if args.execute else 'DRY-RUN'}")
    print(f"\nPending: add={add_count}, update={update_count}, "
          f"restale={restale_count}, orphan={orphan_count}  (total={total})")

    if not args.execute:
        print("\nDry-run — no changes made. Pass --execute to write.")
        return

    if total == 0:
        print("\nNothing to do.")
        return

    if orphan_count and not args.delete_orphans:
        print(f"\n[warn] Manifest has {orphan_count} orphan(s). Pass --delete-orphans to delete them.")

    print("\nConnecting to Anki…")
    try:
        ac = AnkiConnect()
        ac.invoke("version")
    except (URLError, Exception) as exc:
        print(f"ERROR — cannot reach Anki: {exc}")
        print("Make sure Anki is running with AnkiConnect installed.")
        sys.exit(1)

    db = _init()
    _resolve_model_fields(ac, manifest)
    manifest["_delete_orphans"] = args.delete_orphans
    results = execute(manifest, ac, db)
    db.close()

    print(f"\nDone — added={results['added']}, updated={results['updated']}, "
          f"re_added={results['re_added']}, deleted={results['deleted']}")
    if results["errors"]:
        print(f"\nErrors ({len(results['errors'])}):")
        for err in results["errors"]:
            print(f"  {err}")


if __name__ == "__main__":
    main()
