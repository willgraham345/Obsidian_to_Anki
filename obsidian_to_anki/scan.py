"""
Vault scanner and Anki snapshot. Populates the local DB.

No Anki connection required for --vault. --anki requires Anki running
with AnkiConnect on port 8765.

Usage (from obsidian_to_anki/):
    uv run python scan.py [vault_path] [--vault] [--anki] [--all]

    vault_path  Path to Obsidian vault (default: tests/complex-vault/)

    --vault     Scan vault and populate the notes DB.
    --anki      Query Anki and populate the anki_notes snapshot table.
    --all       Run --vault + --anki together.

    With no flags, --vault is implied.

Next step after scanning:
    uv run python diff.py <vault_path>   # generate anki_diff.json + anki_diff.md
    uv run python write.py --execute     # push changes to Anki
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from urllib.error import URLError

import yaml

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


# ── Frontmatter helper ────────────────────────────────────────────────────────

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


# ── Stage 1: vault scan ────────────────────────────────────────────────────────

def run_vault_scan(vault_path: str, db: NoteDB) -> tuple[int, int]:
    """Walk vault_path, parse notes, upsert into DB. Returns (files, notes)."""
    print(f"[vault] Scanning vault: {vault_path}")
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

            # Reconcile frontmatter → DB: restore anki_ids lost if DB was wiped
            fm_sync = _read_frontmatter_sync(filepath)
            if fm_sync:
                for note_row in db.get_notes_for_file(filepath):
                    if not note_row["anki_id"] and note_row["id"] in fm_sync:
                        db.mark_synced(note_row["id"], fm_sync[note_row["id"]])

            count = len(rf.notes_to_add) + len(rf.notes_to_edit)
            if count:
                rel = os.path.relpath(filepath, vault_path)
                print(f"  {rel}: {count} note(s)"
                      f"  (add={len(rf.notes_to_add)}, edit={len(rf.notes_to_edit)})")
                files_with_notes += 1
                total_notes += count

    os.chdir(start_dir)

    print(f"\n[vault] Scan complete — {files_with_notes} files, {total_notes} notes")
    rows = db._conn.execute(
        "SELECT note_type, COUNT(*) AS n FROM notes GROUP BY note_type ORDER BY n DESC"
    ).fetchall()
    print("[vault] Notes by type:")
    for row in rows:
        print(f"     {row['note_type']:40s}  {row['n']:>4d}")

    return files_with_notes, total_notes


# ── Stage 2: Anki snapshot ─────────────────────────────────────────────────────

def scan_anki(db: NoteDB) -> int:
    """Query AnkiConnect, populate anki_notes. Returns number of notes stored."""
    print("\n[anki] Connecting to Anki…")
    ac = AnkiConnect()

    try:
        note_ids: list[int] = ac.invoke("findNotes", query="")
    except (URLError, Exception) as exc:
        print(f"[anki] ERROR — cannot reach Anki: {exc}")
        print("[anki] Make sure Anki is running with AnkiConnect installed.")
        return 0

    print(f"[anki] {len(note_ids)} notes found in Anki")

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

    print(f"[anki] Stored {len(all_notes)} notes in anki_notes")

    linked = db.reconcile_orphans()
    if linked:
        print(f"[anki] Reconciled {linked} orphan(s) → vault note(s) by field match")

    summary = db.get_comparison_summary()
    print("[anki] Comparison vs vault:")
    for row in summary:
        print(f"       {row['status']:20s}  {row['n']:>4d}")

    return len(all_notes)


# ── CLI ────────────────────────────────────────────────────────────────────────

def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="scan",
        description=(
            "Vault scanner and Anki snapshot. Populates the local DB.\n\n"
            "With no flags, --vault is implied (vault scan only, no Anki needed).\n"
            "Run diff.py afterwards to generate the diff manifest."
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
        "--vault",
        action="store_true",
        help="Scan vault and populate the notes DB.",
    )
    parser.add_argument(
        "--anki",
        action="store_true",
        help="Query Anki and populate the anki_notes snapshot (requires AnkiConnect).",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Run --vault + --anki together.",
    )
    return parser


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()

    # Resolve which stages to run
    explicit  = args.vault or args.anki or args.all
    run_vault = args.vault or args.all or not explicit
    run_anki  = args.anki  or args.all

    db, _ = _init()

    vault_path = os.path.abspath(
        args.vault_path or globals.CONFIG_DATA.get("Vault path") or _DEFAULT_VAULT
    )
    if not os.path.isdir(vault_path):
        parser.error(f"vault_path is not a directory: {vault_path}")

    print(f"Loaded note types from config: {list(globals.CONFIG_DATA.get('CUSTOM_REGEXPS', {}).keys())}")
    print(f"Vault: {vault_path}\n")

    if run_vault:
        run_vault_scan(vault_path, db)

    if run_anki:
        scan_anki(db)

    db.close()
    print("\nDone.")


if __name__ == "__main__":
    main()
