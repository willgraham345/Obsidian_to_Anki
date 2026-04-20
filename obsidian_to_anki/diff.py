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


def _md_cell(text: str) -> str:
    return text.replace("|", "\\|")


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
    """Derive Anki deck from the file's folder hierarchy relative to vault root.

    e.g. <vault>/Docs/Python/notes.md  →  Docs::Python
         <vault>/Python/notes.md        →  Python
         <vault>/notes.md               →  Default
    """
    if not file_path:
        return globals.CONFIG_DATA.get("Deck", "Default")
    try:
        rel = os.path.relpath(file_path, vault_path)
    except ValueError:
        return globals.CONFIG_DATA.get("Deck", "Default")
    parts = rel.replace("\\", "/").split("/")[:-1]  # drop filename
    parts = [p for p in parts if p and p != "."]
    if not parts:
        return globals.CONFIG_DATA.get("Deck", "Default")
    return "::".join(parts)


def build_diff(db: NoteDB, vault_path: str) -> dict:
    """Read note_comparison, return structured diff dict.

    Orphans are always included but filtered to note types managed by this
    tool (i.e. types present in the [Custom Regexps] config section).
    """
    rows = db.get_comparison_rows(exclude_synced=True)
    managed_types: set[str] = set(globals.CONFIG_DATA.get("CUSTOM_REGEXPS", {}).keys())

    diff: dict[str, list[dict]] = {
        "add": [],
        "update": [],
        "restale": [],
        "orphan": [],
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

    return diff


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

    lines: list[str] = [
        "# Anki Diff Preview\n",
        f"Generated: {now}  \n",
        f"Vault: `{vault_path}`  \n",
        "\n---\n",
        "\n## Summary\n",
        "\n| Action | Count |",
        "\n|--------|-------|",
        f"\n| add | {len(diff['add'])} |",
        f"\n| update | {len(diff['update'])} |",
        f"\n| re-add (stale) | {len(diff['restale'])} |",
        f"\n| delete (orphan) | {len(diff['orphan'])} |",
        f"\n| **total** | **{total}** |",
    ]

    if total == 0:
        lines.append("\n\n> Nothing to do — all notes are synced.\n")
    else:
        _md_section(lines, "Add", diff["add"], vault_path, show_anki=False)
        _md_section(lines, "Update", diff["update"], vault_path, show_anki=True)
        _md_section(lines, "Re-add (Stale ID)", diff["restale"], vault_path, show_anki=False)
        _md_section_orphan(lines, "Delete (Orphan)", diff["orphan"])

    content = "".join(lines) + "\n"
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as fh:
        fh.write(content)
    print(f"[md]   Written to: {output_path}")


def _md_section(
    lines: list[str],
    title: str,
    rows: list[dict],
    vault_path: str,
    show_anki: bool,
) -> None:
    if not rows:
        return
    lines.append(f"\n\n## {title}\n")
    if show_anki:
        lines += [
            "\n| Note Type | File | Vault F1 | Vault F2 | Anki F1 | Anki F2 | Deck |",
            "\n|-----------|------|----------|----------|---------|---------|------|",
        ]
    else:
        lines += [
            "\n| Note Type | File | Field 1 | Field 2 | Deck |",
            "\n|-----------|------|---------|---------|------|",
        ]
    for r in rows:
        rel = _rel(r.get("file_path"), vault_path)
        if show_anki:
            lines.append(
                f"\n| {_md_cell(r.get('note_type',''))}"
                f" | {_md_cell(rel)}"
                f" | {_md_cell(_strip_html(r.get('field_1')))}"
                f" | {_md_cell(_strip_html(r.get('field_2')))}"
                f" | {_md_cell(_strip_html(r.get('anki_field_1','')))}"
                f" | {_md_cell(_strip_html(r.get('anki_field_2','')))}"
                f" | {_md_cell(r.get('deck_name',''))} |"
            )
        else:
            lines.append(
                f"\n| {_md_cell(r.get('note_type',''))}"
                f" | {_md_cell(rel)}"
                f" | {_md_cell(_strip_html(r.get('field_1')))}"
                f" | {_md_cell(_strip_html(r.get('field_2')))}"
                f" | {_md_cell(r.get('deck_name',''))} |"
            )


def _md_section_orphan(lines: list[str], title: str, rows: list[dict]) -> None:
    if not rows:
        return
    lines.append(f"\n\n## {title}\n")
    lines += [
        "\n| Anki ID | Note Type | Field 1 | Field 2 | Deck |",
        "\n|---------|-----------|---------|---------|------|",
    ]
    for r in rows:
        lines.append(
            f"\n| {r.get('anki_id','')}"
            f" | {_md_cell(r.get('note_type',''))}"
            f" | {_md_cell(_strip_html(r.get('field_1')))}"
            f" | {_md_cell(_strip_html(r.get('field_2')))}"
            f" | {_md_cell(r.get('deck_name',''))} |"
        )


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
    return parser


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()

    db = _init()

    vault_path = os.path.abspath(
        args.vault_path or globals.CONFIG_DATA.get("Vault path") or _DEFAULT_VAULT
    )

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
    db.close()

    total = sum(len(v) for v in diff.values())
    print(f"Diff: add={len(diff['add'])}, update={len(diff['update'])}, "
          f"restale={len(diff['restale'])}, orphan={len(diff['orphan'])}  (total={total})")

    write_json(diff, vault_path, args.output_json)
    write_markdown(diff, vault_path, args.output_md)

    print("\nDone.")


if __name__ == "__main__":
    main()
