"""
Standalone vault scanner, Anki snapshot, and diff reporter.

No Anki connection is required for --db. --snapshot requires Anki running
with AnkiConnect on port 8765.

Usage (from obsidian_to_anki/):
    uv run python scan_vault.py [vault_path] [--db] [--snapshot] [--output [FILE]] [--all]

    vault_path  Path to Obsidian vault (default: tests/complex-vault/)

    --db        Scan vault and populate the notes DB.
    --snapshot  Query Anki and populate the anki_notes snapshot table.
    --output    Write diff markdown table to FILE (default: vault_diff.md).
    --all       Run --db + --snapshot + --output together.

    With no flags, --db is implied.

PlantUML diagram: docs/sequence_scan_vault.puml

Statuses produced by the note_comparison VIEW
----------------------------------------------
not_in_anki     Vault note has no anki_id — never synced.
stale_id        Vault note has an anki_id but it is absent from the Anki
                snapshot (deleted from Anki, or snapshot is outdated).
modified        Both sides have the note but field content differs.
synced          Both sides agree on content.
orphan_in_anki  Note exists in Anki but has no matching vault record.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from urllib.error import URLError

# ── Make src importable ────────────────────────────────────────────────────────
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from obsidian_to_anki import globals                          # noqa: E402
from obsidian_to_anki.anki_connect import AnkiConnect         # noqa: E402
from obsidian_to_anki.config import Config                    # noqa: E402
from obsidian_to_anki.db import NoteDB                        # noqa: E402
from obsidian_to_anki.file import File                        # noqa: E402

_DEFAULT_VAULT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "tests", "complex-vault")
)
_DEFAULT_OUTPUT = "vault_diff.md"

# ── Known field names for common note types ────────────────────────────────────
_KNOWN_FIELDS: dict[str, list[str]] = {
    "Test":                           ["Front", "Back", "Tags"],
    "Basic":                          ["Front", "Back"],
    "Basic (and reversed card)":      ["Front", "Back"],
    "Basic (optional reversed card)": ["Front", "Back", "Add Reverse"],
    "Basic (type in the answer)":     ["Front", "Back"],
    "Cloze":                          ["Text", "Extra"],
}


# ── Helpers ────────────────────────────────────────────────────────────────────

def _init(db_path: str | None = None) -> tuple[NoteDB, Config]:
    """Initialise global state (config + DB) shared by all stages."""
    db = NoteDB(db_path)
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
        if note_type in _KNOWN_FIELDS:
            fields_dict[note_type] = _KNOWN_FIELDS[note_type]
        elif pattern:
            n_groups = re.compile(pattern).groups
            fields_dict[note_type] = [f"Field {i + 1}" for i in range(n_groups)]
        else:
            fields_dict[note_type] = _KNOWN_FIELDS.get(note_type, ["Front", "Back"])

    globals.FIELDS_DICT = fields_dict
    globals.EXISTING_IDS = []
    globals.FILE_HASHES = {}

    _gen_regexp()
    return db, config


def _gen_regexp() -> None:
    """Compile all regexps from CONFIG_DATA (mirrors App.gen_regexp)."""
    globals.NOTE_REGEXP = re.compile(
        r"^" + globals.CONFIG_DATA["NOTE_PREFIX"]
        + r".*?\n([\s\S]*?\n)"
        + globals.CONFIG_DATA["NOTE_SUFFIX"]
        + r"\n?",
        flags=re.MULTILINE,
    )
    globals.DECK_REGEXP = re.compile(
        r"^" + globals.CONFIG_DATA["DECK_LINE"] + r"(?:\n|: )(.*)",
        flags=re.MULTILINE,
    )
    globals.EMPTY_REGEXP = re.compile(
        r"^" + globals.CONFIG_DATA["NOTE_PREFIX"]
        + r"\n(?:<!--)?" + globals.ID_PREFIX
        + r"[\s\S]*?\n" + globals.CONFIG_DATA["NOTE_SUFFIX"],
        flags=re.MULTILINE,
    )
    globals.TAG_REGEXP = re.compile(
        r"^" + globals.CONFIG_DATA["TAG_LINE"] + r"(?:\n|: )(.*)",
        flags=re.MULTILINE,
    )
    globals.INLINE_REGEXP = re.compile(
        globals.CONFIG_DATA["INLINE_PREFIX"]
        + r"(.*?)"
        + globals.CONFIG_DATA["INLINE_SUFFIX"],
    )
    globals.INLINE_EMPTY_REGEXP = re.compile(
        globals.CONFIG_DATA["INLINE_PREFIX"]
        + r"\s+(?:<!--)?" + globals.ID_PREFIX + r".*?"
        + globals.CONFIG_DATA["INLINE_SUFFIX"],
    )
    vault = globals.CONFIG_DATA.get("Vault", "")
    globals.VAULT_PATH_REGEXP = re.compile(
        re.escape(vault) + r".*" if vault else r"^$"
    )
    globals.FROZEN_REGEXP = re.compile(
        globals.CONFIG_DATA["FROZEN_LINE"] + r" - (.*?):\n((?:[^\n][\n]?)+)"
    )


def _strip_html(text: str | None, max_len: int = 80) -> str:
    """Strip HTML tags and truncate for table display."""
    if not text:
        return ""
    plain = re.sub(r"<[^>]+>", "", text).replace("\n", " ").strip()
    return (plain[:max_len] + "…") if len(plain) > max_len else plain


def _md_cell(text: str) -> str:
    return text.replace("|", "\\|")


# ── Stage 1: vault scan ────────────────────────────────────────────────────────

def run_db_scan(vault_path: str, db: NoteDB) -> tuple[int, int]:
    """Walk vault_path, parse notes, upsert into DB. Returns (files, notes)."""
    print(f"[db] Scanning vault: {vault_path}")
    files_with_notes = 0
    total_notes = 0
    start_dir = os.getcwd()

    for root, dirs, files in os.walk(vault_path):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        md_files = sorted(f for f in files if f.endswith(".md"))
        if not md_files:
            continue
        os.chdir(root)
        for filename in md_files:
            filepath = os.path.join(root, filename)
            try:
                rf = File(filepath)
                rf.scan_file()
            except Exception as exc:
                print(f"  [WARN] {os.path.relpath(filepath, vault_path)}: {exc}")
                continue

            count = len(rf.notes_to_add) + len(rf.notes_to_edit)
            if count:
                rel = os.path.relpath(filepath, vault_path)
                print(f"  {rel}: {count} note(s)"
                      f"  (add={len(rf.notes_to_add)}, edit={len(rf.notes_to_edit)})")
                files_with_notes += 1
                total_notes += count

    os.chdir(start_dir)

    print(f"\n[db] Scan complete — {files_with_notes} files, {total_notes} notes")
    rows = db._conn.execute(
        "SELECT note_type, COUNT(*) AS n FROM notes GROUP BY note_type ORDER BY n DESC"
    ).fetchall()
    print("[db] Notes by type:")
    for row in rows:
        print(f"     {row['note_type']:40s}  {row['n']:>4d}")

    return files_with_notes, total_notes


# ── Stage 2: Anki snapshot ─────────────────────────────────────────────────────

def run_anki_snapshot(db: NoteDB) -> int:
    """Query AnkiConnect, populate anki_notes. Returns number of notes stored."""
    print("\n[snapshot] Connecting to Anki…")
    ac = AnkiConnect()

    try:
        note_ids: list[int] = ac.invoke("findNotes", query="")
    except (URLError, Exception) as exc:
        print(f"[snapshot] ERROR — cannot reach Anki: {exc}")
        print("[snapshot] Make sure Anki is running with AnkiConnect installed.")
        return 0

    print(f"[snapshot] {len(note_ids)} notes found in Anki")

    # Fetch note details in chunks of 50
    all_notes: list[dict] = []
    chunk_size = 50
    for i in range(0, len(note_ids), chunk_size):
        chunk = note_ids[i : i + chunk_size]
        infos = ac.invoke("notesInfo", notes=chunk)
        all_notes.extend(infos)

    # Collect all card IDs to map notes → decks
    all_card_ids: list[int] = []
    note_to_cards: dict[int, list[int]] = {}
    for note in all_notes:
        cards = note.get("cards", [])
        note_to_cards[note["noteId"]] = cards
        all_card_ids.extend(cards)

    deck_map: dict[int, str] = {}
    if all_card_ids:
        for i in range(0, len(all_card_ids), chunk_size):
            chunk = all_card_ids[i : i + chunk_size]
            card_infos = ac.invoke("cardsInfo", cards=chunk)
            for ci in card_infos:
                deck_map[ci["cardId"]] = ci.get("deckName", "")

    # Populate DB
    db.clear_anki_notes()
    for note in all_notes:
        nid: int = note["noteId"]
        ordered = sorted(note.get("fields", {}).values(), key=lambda f: f["order"])
        field_1 = ordered[0]["value"] if ordered else None
        field_2 = ordered[1]["value"] if len(ordered) > 1 else None
        tags: list[str] = note.get("tags", [])
        cards = note_to_cards.get(nid, [])
        deck_name = deck_map.get(cards[0], "") if cards else ""
        db.upsert_anki_note(
            anki_id=nid,
            note_type=note.get("modelName", ""),
            field_1=field_1,
            field_2=field_2,
            tags=tags,
            deck_name=deck_name,
            mod_timestamp=note.get("mod"),
        )

    print(f"[snapshot] Stored {len(all_notes)} notes in anki_notes")

    summary = db.get_comparison_summary()
    print("[snapshot] Comparison vs vault:")
    for row in summary:
        print(f"           {row['status']:20s}  {row['n']:>4d}")

    return len(all_notes)


# ── Stage 3: markdown diff output ─────────────────────────────────────────────

def run_diff_output(db: NoteDB, output_path: str, vault_path: str) -> None:
    """Write a markdown diff table to output_path."""
    anki_count = db._conn.execute(
        "SELECT COUNT(*) FROM anki_notes"
    ).fetchone()[0]

    summary = db.get_comparison_summary()
    rows = db.get_comparison_rows(exclude_synced=True)

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    lines: list[str] = [
        "# Obsidian–Anki Diff\n",
        f"Generated: {now}  \n",
        f"Vault: `{vault_path}`  \n",
        f"Anki snapshot: {anki_count} notes\n",
        "\n---\n",
        "\n## Summary\n",
        "\n| Status | Count |",
        "\n|--------|-------|",
    ]
    for row in summary:
        lines.append(f"\n| {row['status']} | {row['n']} |")

    if not rows:
        lines.append("\n\n> All notes are synced — no differences found.\n")
    else:
        lines += [
            "\n\n## Non-Synced Notes\n",
            "\n| Status | Note Type | File Path"
            " | Vault Field 1 | Vault Field 2"
            " | Anki Field 1 | Anki Field 2"
            " | Tags | Deck |",
            "\n|--------|-----------|-----------|"
            "---------------|---------------"
            "|--------------|--------------|"
            "------|------|",
        ]
        for r in rows:
            vault_tags_raw = r.get("vault_tags") or r.get("anki_tags") or "[]"
            try:
                tag_list = json.loads(vault_tags_raw)
                tags_str = " ".join(tag_list)
            except (json.JSONDecodeError, TypeError):
                tags_str = str(vault_tags_raw)

            rel_path = ""
            if r.get("file_path"):
                try:
                    rel_path = os.path.relpath(r["file_path"], vault_path)
                except ValueError:
                    rel_path = r["file_path"]

            lines.append(
                f"\n| {r['status']}"
                f" | {_md_cell(r.get('note_type') or '')}"
                f" | {_md_cell(rel_path)}"
                f" | {_md_cell(_strip_html(r.get('vault_field_1')))}"
                f" | {_md_cell(_strip_html(r.get('vault_field_2')))}"
                f" | {_md_cell(_strip_html(r.get('anki_field_1')))}"
                f" | {_md_cell(_strip_html(r.get('anki_field_2')))}"
                f" | {_md_cell(tags_str)}"
                f" | {_md_cell(r.get('vault_deck') or r.get('anki_deck') or '')}"
                f" |"
            )

    content = "".join(lines) + "\n"
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as fh:
        fh.write(content)

    print(f"\n[output] Diff written to: {output_path}")
    print(f"[output] {len(rows)} non-synced rows included")


# ── CLI ────────────────────────────────────────────────────────────────────────

def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="scan_vault",
        description=(
            "Vault scanner, Anki snapshot, and diff reporter.\n\n"
            "With no flags, --db is implied (vault scan only, no Anki needed).\n"
            "Use --all to run all three stages in sequence."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "vault_path",
        nargs="?",
        default=_DEFAULT_VAULT,
        help=f"Path to Obsidian vault (default: {_DEFAULT_VAULT})",
    )
    parser.add_argument(
        "--db",
        action="store_true",
        help="Scan vault and populate the notes DB.",
    )
    parser.add_argument(
        "--snapshot",
        action="store_true",
        help="Query Anki and populate the anki_notes snapshot (requires AnkiConnect).",
    )
    parser.add_argument(
        "--output",
        nargs="?",
        const=_DEFAULT_OUTPUT,
        metavar="FILE",
        help=f"Write diff markdown table to FILE (default: {_DEFAULT_OUTPUT}).",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help=f"Run --db + --snapshot + --output {_DEFAULT_OUTPUT}.",
    )
    return parser


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()

    vault_path = os.path.abspath(args.vault_path)
    if not os.path.isdir(vault_path):
        parser.error(f"vault_path is not a directory: {vault_path}")

    # Resolve which stages to run
    explicit = args.db or args.snapshot or (args.output is not None) or args.all
    run_db       = args.db       or args.all or not explicit
    run_snapshot = args.snapshot or args.all
    run_output   = (args.output is not None) or args.all
    output_path  = args.output if args.output is not None else _DEFAULT_OUTPUT

    print(f"Loaded note types from config: {list(globals.CONFIG_DATA.get('CUSTOM_REGEXPS', {}).keys())}")
    print(f"Vault: {vault_path}\n")

    db, _ = _init()

    if run_db:
        run_db_scan(vault_path, db)

    if run_snapshot:
        run_anki_snapshot(db)

    if run_output:
        anki_count = db._conn.execute("SELECT COUNT(*) FROM anki_notes").fetchone()[0]
        if not anki_count and not run_snapshot:
            print(
                "\n[output] No Anki snapshot found in DB."
                " Run with --snapshot first, or use --all."
            )
        else:
            run_diff_output(db, output_path, vault_path)

    db.close()
    print("\nDone.")


if __name__ == "__main__":
    main()
