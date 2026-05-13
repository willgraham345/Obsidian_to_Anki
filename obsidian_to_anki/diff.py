"""
Reads the note_comparison DB view and outputs a diff manifest.

Requires a vault scan (scan.py --vault) and Anki snapshot (scan.py --anki).

Usage (from obsidian_to_anki/):
    uv run python diff.py [vault_path] [--clean-up]
                          [--output-json FILE] [--output-md FILE]

    vault_path      Path to Obsidian vault — used for relative paths in markdown.
    --output-json   JSON manifest consumed by write.py (default: anki_diff.json).
    --output-md     Human-readable markdown preview (default: anki_diff.md).

Workflow
--------
    uv run python scan.py --vault <vault>   # populate notes table
    uv run python scan.py --anki            # populate anki_notes table
    uv run python diff.py <vault>           # generate anki_diff.json + anki_diff.md
    # review anki_diff.md, then:
    uv run python write.py                  # execute from anki_diff.json
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from obsidian_to_anki import globals          # noqa: E402
from obsidian_to_anki.config import Config    # noqa: E402
from obsidian_to_anki.db import NoteDB        # noqa: E402

_DEFAULT_VAULT   = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "tests", "complex-vault")
)
_DEFAULT_JSON = "anki_diff.json"
_DEFAULT_MD   = "anki_diff.md"


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
    return db


# ── Helpers ────────────────────────────────────────────────────────────────────

def _strip_html(text: str | None, max_len: int = 80) -> str:
    if not text:
        return ""
    plain = re.sub(r"<[^>]+>", "", text).replace("\n", " ").strip()
    return (plain[:max_len] + "…") if len(plain) > max_len else plain



def _lookup_uuid(db: NoteDB, row: dict) -> str | None:
    file_path = row.get("file_path")
    if not file_path:
        return None
    match = db._conn.execute(
        "SELECT id FROM notes WHERE file_path = ? AND note_type = ? AND field_1 = ?",
        (file_path, row.get("note_type"), row.get("vault_field_1")),
    ).fetchone()
    return match["id"] if match else None


# ── Core: build diff buckets ───────────────────────────────────────────────────

def _deck_from_path(file_path: str | None, vault_path: str) -> str:
    """Resolve Anki deck for a note file.

    Priority:
      1. [Folder Decks] regex patterns matched against vault-relative path
      2. Fallback: globals.UNMATCHED_DECK

    file_path is stored vault-relative in the DB (e.g. Docs/Python/notes.md).
    """
    if not file_path:
        return globals.UNMATCHED_DECK

    norm = file_path.replace("\\", "/")

    folder_decks = globals.CONFIG_DATA.get("FOLDER_DECKS", [])
    for pattern, deck_name in folder_decks:
        if pattern.search(norm):
            return deck_name

    return globals.UNMATCHED_DECK


def build_diff(db: NoteDB, vault_path: str) -> dict:
    """Read note_comparison and stale notes, return structured diff dict."""
    rows = db.get_comparison_rows(exclude_synced=True)
    managed_types: set[str] = set(globals.CONFIG_DATA.get("ATOMICS", {}).keys())

    diff: dict[str, list[dict]] = {
        "add": [],
        "update": [],
        "restale": [],
        "orphan": [],
        "modify_deck": [],
        "stale": [],
    }

    for r in rows:
        status = r["status"]

        if status in ("not_in_anki", "stale_id"):
            uuid = _lookup_uuid(db, r)
            fp = r.get("file_path")
            entry = {
                "uuid":      uuid,
                "note_type": r.get("note_type") or "",
                "deck_name": _deck_from_path(fp, vault_path),
                "field_1":   r.get("vault_field_1"),
                "field_2":   r.get("vault_field_2"),
                "tags":      _parse_tags(r.get("vault_tags")),
                "file_path": fp,
            }
            if status == "stale_id":
                diff["restale"].append(entry)
            else:
                diff["add"].append(entry)

        elif status == "modified":
            uuid = _lookup_uuid(db, r)
            fp = r.get("file_path")
            diff["update"].append({
                "uuid":      uuid,
                "anki_id":   r.get("anki_id"),
                "note_type": r.get("note_type") or "",
                "deck_name": _deck_from_path(fp, vault_path),
                "field_1":   r.get("vault_field_1"),
                "field_2":   r.get("vault_field_2"),
                "file_path": fp,
            })

        elif status == "modify_deck":
            uuid = _lookup_uuid(db, r)
            fp = r.get("file_path")
            diff["modify_deck"].append({
                "uuid":       uuid,
                "anki_id":    r.get("anki_id"),
                "note_type":  r.get("note_type") or "",
                "vault_deck": r.get("vault_deck"),
                "anki_deck":  r.get("anki_deck"),
                "field_1":    r.get("vault_field_1"),
                "file_path":  fp,
            })

        elif status == "orphan_in_anki":
            note_type = r.get("note_type") or ""
            if managed_types and note_type not in managed_types:
                continue  # not managed by this tool — skip
            diff["orphan"].append({
                "anki_id":   r.get("anki_id"),
                "note_type": note_type,
                "field_1":   r.get("anki_field_1"),
                "field_2":   r.get("anki_field_2"),
                "deck_name": r.get("anki_deck") or "",
            })

    stale_notes = db.get_stale_notes()
    for n in stale_notes:
        diff["stale"].append({
            "uuid":      n["id"],
            "note_type": n["note_type"],
            "field_1":   n["field_1"],
            "file_path": n["file_path"],
        })

    return diff


def resolve_modifications(diff: dict, db: NoteDB) -> dict:
    """Interactively resolve each modified note.

    For each entry in diff["update"], shows a vault-vs-Anki field diff and
    prompts the user:
      [u]pdate  — push vault version to Anki  (marks state='to_modify' in DB)
      [s]kip    — leave for later             (removed from this diff run)
      [r]evert  — accept Anki version         (DB updated to match Anki; note synced)

    Returns a new diff dict with only the [u]pdate-approved entries remaining
    in the "update" bucket.
    """
    updates = diff.get("update", [])
    if not updates:
        print("No modified notes to resolve.")
        return diff

    approved: list[dict] = []
    total = len(updates)

    for i, entry in enumerate(updates, 1):
        uuid      = entry.get("uuid")
        anki_id   = entry.get("anki_id")
        note_type = entry.get("note_type") or "Unknown"
        fp        = entry.get("file_path") or ""

        vault_f1 = _strip_html(entry.get("field_1"))
        vault_f2 = _strip_html(entry.get("field_2"))

        # Look up Anki fields from DB snapshot
        anki_f1 = anki_f2 = ""
        if anki_id:
            row = db._conn.execute(
                "SELECT field_1, field_2 FROM anki_notes WHERE anki_id = ?",
                (anki_id,),
            ).fetchone()
            if row:
                anki_f1 = _strip_html(row["field_1"])
                anki_f2 = _strip_html(row["field_2"])

        print(f"\n{'─'*60}")
        print(f"Note {i}/{total} — {note_type}")
        if fp:
            print(f"  {fp}")
        print(f"  Vault F1: {vault_f1}")
        print(f"  Anki  F1: {anki_f1}")
        if vault_f2 or anki_f2:
            print(f"  Vault F2: {vault_f2}")
            print(f"  Anki  F2: {anki_f2}")

        while True:
            choice = input("\n  [u]pdate Anki  [s]kip  [r]evert DB to Anki: ").strip().lower()
            if choice in ("u", "update"):
                if uuid:
                    db.mark_to_modify(uuid)
                approved.append(entry)
                break
            elif choice in ("s", "skip"):
                break
            elif choice in ("r", "revert"):
                if uuid:
                    db.revert_note_to_anki(uuid)
                break
            else:
                print("  Invalid — enter u, s, or r.")

    new_diff = dict(diff)
    new_diff["update"] = approved
    return new_diff


def _parse_tags(raw: str | None) -> list[str]:
    if not raw:
        return []
    try:
        return json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        return []


# ── JSON output ────────────────────────────────────────────────────────────────

def write_json(diff: dict, vault_path: str, output_path: str) -> None:
    payload = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "vault_path": vault_path,
        **diff,
    }
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)
    print(f"[json] Written to: {output_path}")


# ── Markdown output ────────────────────────────────────────────────────────────

def write_markdown(diff: dict, vault_path: str, output_path: str) -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    total = sum(len(v) for v in diff.values())

    counts = [
        ("add",              len(diff["add"])),
        ("update",           len(diff["update"])),
        ("re-add (stale ID)", len(diff["restale"])),
        ("modify deck",      len(diff.get("modify_deck", []))),
        ("orphan",           len(diff["orphan"])),
        ("stale (deleted)",  len(diff.get("stale", []))),
    ]

    lines: list[str] = [
        "# Anki Diff\n",
        f"\nGenerated: {now}  \n",
        f"Vault: `{vault_path}`\n",
        "\n---\n",
        "\n## Summary\n",
    ]
    for label, n in counts:
        lines.append(f"\n- {label}: {n}")
    lines.append(f"\n- **total: {total}**\n")

    if total == 0:
        lines.append("\n> Nothing to do — all notes are synced.\n")
    else:
        _md_section_add(lines, "Add", diff["add"], vault_path)
        _md_section_update(lines, "Update", diff["update"], vault_path)
        _md_section_add(lines, "Re-add (Stale ID)", diff["restale"], vault_path)
        _md_section_modify_deck(lines, "Modify Deck", diff.get("modify_deck", []))
        _md_section_orphan(lines, "Orphan (Delete from Anki)", diff["orphan"])
        _md_section_stale(lines, "Stale (File Deleted)", diff.get("stale", []))

    content = "".join(lines) + "\n"
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as fh:
        fh.write(content)
    print(f"[md]   Written to: {output_path}")


def _md_note_entry(lines: list[str], r: dict, vault_path: str) -> None:
    """Append a single note block (### heading + fields) to lines."""
    note_type = r.get("note_type") or "Unknown"
    fp = r.get("file_path") or ""
    rel = _rel(fp, vault_path) if fp else ""
    lines.append(f"\n### {note_type}")
    if rel:
        lines.append(f"\n`{rel}`\n")
    else:
        lines.append("\n")


def _md_section_add(lines: list[str], title: str, rows: list[dict], vault_path: str) -> None:
    if not rows:
        return
    lines.append(f"\n\n## {title} ({len(rows)})\n")
    for r in rows:
        _md_note_entry(lines, r, vault_path)
        f1 = _strip_html(r.get("field_1"))
        f2 = _strip_html(r.get("field_2"))
        deck = r.get("deck_name") or ""
        if f1:
            lines.append(f"\n**Field 1:** {f1}")
        if f2:
            lines.append(f"\n**Field 2:** {f2}")
        if deck:
            lines.append(f"\n**Deck:** {deck}")
        lines.append("\n")


def _md_section_update(lines: list[str], title: str, rows: list[dict], vault_path: str) -> None:
    if not rows:
        return
    lines.append(f"\n\n## {title} ({len(rows)})\n")
    for r in rows:
        _md_note_entry(lines, r, vault_path)
        vf1 = _strip_html(r.get("field_1"))
        vf2 = _strip_html(r.get("field_2"))
        af1 = _strip_html(r.get("anki_field_1"))
        af2 = _strip_html(r.get("anki_field_2"))
        deck = r.get("deck_name") or ""
        if vf1 or af1:
            lines.append(f"\n**Vault F1:** {vf1}")
            lines.append(f"\n**Anki F1:**  {af1}")
        if vf2 or af2:
            lines.append(f"\n**Vault F2:** {vf2}")
            lines.append(f"\n**Anki F2:**  {af2}")
        if deck:
            lines.append(f"\n**Deck:** {deck}")
        lines.append("\n")


def _md_section_modify_deck(lines: list[str], title: str, rows: list[dict]) -> None:
    if not rows:
        return
    lines.append(f"\n\n## {title} ({len(rows)})\n")
    for r in rows:
        note_type = r.get("note_type") or "Unknown"
        fp = r.get("file_path") or ""
        f1 = _strip_html(r.get("field_1"))
        vault_deck = r.get("vault_deck") or ""
        anki_deck  = r.get("anki_deck") or ""
        lines.append(f"\n### {note_type}")
        if fp:
            lines.append(f"\n`{fp}`\n")
        else:
            lines.append("\n")
        if f1:
            lines.append(f"\n**Field 1:** {f1}")
        lines.append(f"\n**Vault Deck:** {vault_deck}")
        lines.append(f"\n**Anki Deck:**  {anki_deck}")
        lines.append("\n")


def _md_section_orphan(lines: list[str], title: str, rows: list[dict]) -> None:
    if not rows:
        return
    lines.append(f"\n\n## {title} ({len(rows)})\n")
    for r in rows:
        note_type = r.get("note_type") or "Unknown"
        anki_id   = r.get("anki_id") or ""
        f1 = _strip_html(r.get("field_1"))
        f2 = _strip_html(r.get("field_2"))
        deck = r.get("deck_name") or ""
        lines.append(f"\n### {note_type} (Anki ID: {anki_id})\n")
        if f1:
            lines.append(f"\n**Field 1:** {f1}")
        if f2:
            lines.append(f"\n**Field 2:** {f2}")
        if deck:
            lines.append(f"\n**Deck:** {deck}")
        lines.append("\n")


def _md_section_stale(lines: list[str], title: str, rows: list[dict]) -> None:
    if not rows:
        return
    lines.append(f"\n\n## {title} ({len(rows)})\n")
    for r in rows:
        note_type = r.get("note_type") or "Unknown"
        fp = r.get("file_path") or ""
        f1 = _strip_html(r.get("field_1"))
        lines.append(f"\n### {note_type}")
        if fp:
            lines.append(f"\n`{fp}`\n")
        else:
            lines.append("\n")
        if f1:
            lines.append(f"\n**Field 1:** {f1}")
        lines.append("\n")


def _rel(file_path: str | None, vault_path: str) -> str:
    if not file_path:
        return ""
    try:
        return os.path.relpath(file_path, vault_path)
    except ValueError:
        return file_path


# ── CLI ────────────────────────────────────────────────────────────────────────

def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="diff",
        description=(
            "Generate Anki diff from the DB comparison view.\n\n"
            "Outputs anki_diff.json (consumed by write.py) and anki_diff.md (human review).\n"
            "Requires: scan.py --vault and scan.py --anki run first."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "vault_path",
        nargs="?",
        default=None,
        help="Path to Obsidian vault. Falls back to 'Vault path' in config if omitted.",
    )
    parser.add_argument(
        "--output-json",
        default=_DEFAULT_JSON,
        metavar="FILE",
        help=f"JSON manifest output (default: {_DEFAULT_JSON}).",
    )
    parser.add_argument(
        "--output-md",
        default=_DEFAULT_MD,
        metavar="FILE",
        help=f"Markdown preview output (default: {_DEFAULT_MD}).",
    )
    parser.add_argument(
        "--resolve",
        action="store_true",
        help=(
            "Interactively resolve modified notes before writing the diff. "
            "For each modified note, prompts: [u]pdate Anki / [s]kip / [r]evert DB to Anki."
        ),
    )
    return parser


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()

    db = _init()

    _vault_raw = args.vault_path or globals.CONFIG_DATA.get("Vault")
    if not _vault_raw:
        parser.error(
            "No vault path provided. Either pass vault_path as an argument "
            "or set 'Vault path' in the [Obsidian] section of obsidian_to_anki_config.ini."
        )
    vault_path = os.path.abspath(_vault_raw)

    vault_count = db._conn.execute("SELECT COUNT(*) FROM notes").fetchone()[0]
    anki_count  = db._conn.execute("SELECT COUNT(*) FROM anki_notes").fetchone()[0]
    if not vault_count:
        print("No vault notes in DB. Run: uv run python scan.py --vault <vault_path>")
        db.close()
        sys.exit(1)
    if not anki_count:
        print("No Anki snapshot in DB. Run: uv run python scan.py --anki")
        db.close()
        sys.exit(1)

    diff = build_diff(db, vault_path)

    if args.resolve:
        diff = resolve_modifications(diff, db)

    db.close()

    total = sum(len(v) for v in diff.values())
    print(f"Diff: add={len(diff['add'])}, update={len(diff['update'])}, "
          f"restale={len(diff['restale'])}, modify_deck={len(diff['modify_deck'])}, "
          f"orphan={len(diff['orphan'])}, stale={len(diff['stale'])}  (total={total})")

    write_json(diff, vault_path, args.output_json)
    write_markdown(diff, vault_path, args.output_md)

    print("\nDone.")


if __name__ == "__main__":
    main()
