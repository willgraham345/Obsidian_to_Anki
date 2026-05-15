"""
Vault scanner, Anki snapshot, and diff generator.

The vault is the source of truth. The DB caches vault state (notes table) and
Anki state (anki_notes table). Scanning updates the vault snapshot; diff
compares notes vs anki_notes and writes pending changes to the anki_diff table.

Usage (from repo root):
    uv run python scan.py [vault_path] [--anki] [--force]

    vault_path   Path to Obsidian vault (falls back to 'Vault path' in config).
    --anki       Force Anki snapshot refresh (runs automatically when Anki Path is set in config).
    --force      Scan all vault files even if their hash is unchanged.

Workflow:
    uv run python scan.py /vault --anki   # refresh both snapshots
    uv run python scan.py /vault          # re-scan vault only, diff from cached Anki
    uv run python show.py                 # preview pending changes
    uv run python write.py                # push changes to Anki
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import uuid as _uuid_mod
from difflib import SequenceMatcher
from urllib.error import URLError

import yaml

# ── Make src importable ────────────────────────────────────────────────────────
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from atomics import globals                          # noqa: E402
from atomics.anki_connect import AnkiConnect         # noqa: E402
from atomics.config import Config                    # noqa: E402
from atomics.db import NoteDB                        # noqa: E402
from atomics.file import File                        # noqa: E402

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
    globals.EXISTING_IDS = [
        row["anki_id"]
        for row in db._conn.execute("SELECT anki_id FROM anki_notes").fetchall()
    ]
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
        re.escape(vault) + r"/(.*)" if vault else r"^$"
    )
    globals.FROZEN_REGEXP = re.compile(
        globals.CONFIG_DATA["FROZEN_LINE"] + r" - (.*?):\n((?:[^\n][\n]?)+)"
    )


# ── Frontmatter helper ─────────────────────────────────────────────────────────

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


# ── Atomic ID ──────────────────────────────────────────────────────────────────

def add_atomic_id(file_path: str, db: NoteDB) -> str:
    """Ensure file has `atomic_id` in YAML frontmatter. Return the UUID.

    Writes frontmatter once on first call. Subsequent calls are no-ops.
    Must run BEFORE File.scan_file() so line numbers are stable after the write.
    """
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

    if "atomic_id" in fm:
        atomic_id = str(fm["atomic_id"])
    else:
        atomic_id = str(_uuid_mod.uuid4())
        fm["atomic_id"] = atomic_id
        fm_str = yaml.safe_dump(fm, default_flow_style=False, allow_unicode=True).rstrip()
        with open(file_path, "w", encoding="utf-8") as fh:
            fh.write(f"---\n{fm_str}\n---\n{body}")

    db.set_file_atomic_id(file_path, atomic_id)
    return atomic_id


# ── Stale detection ────────────────────────────────────────────────────────────

def find_vault_modifications(db: NoteDB, vault_path: str) -> tuple[int, int]:
    """Mark notes stale when their vault file no longer exists.

    Absolute-path entries (test-vault contamination) are still deleted since
    they were never real vault data. Returns (abs_removed, stale_marked).
    """
    cur = db._conn.execute("DELETE FROM notes WHERE file_path LIKE '/%'")
    abs_removed = cur.rowcount
    db._conn.commit()

    rows = db._conn.execute(
        "SELECT DISTINCT file_path FROM notes WHERE file_path NOT LIKE '/%' AND state != 'stale'"
    ).fetchall()
    stale_marked = 0
    for row in rows:
        full = os.path.join(vault_path, row["file_path"])
        if not os.path.isfile(full):
            for note in db.get_notes_for_file(row["file_path"]):
                db.set_state_and_action(note["id"], "stale", "review")
                stale_marked += 1
    return abs_removed, stale_marked


# ── Stage 1: vault scan ────────────────────────────────────────────────────────

def run_vault_scan(vault_path: str, db: NoteDB, force: bool = False) -> tuple[int, int]:
    """Walk vault_path, parse notes, upsert into DB. Returns (files, notes)."""
    print(f"[vault] Scanning vault: {vault_path}")
    files_with_notes = 0
    total_notes = 0
    files_skipped = 0
    start_dir = os.getcwd()

    folder_decks = globals.CONFIG_DATA.get("FOLDER_DECKS", [])

    for root, dirs, files in os.walk(vault_path):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        md_files = sorted(f for f in files if f.endswith(".md"))
        if not md_files:
            continue
        os.chdir(root)
        for filename in md_files:
            filepath = os.path.join(root, filename)
            if folder_decks:
                norm = filepath.replace("\\", "/")
                if not any(pat.search(norm) for pat, _ in folder_decks):
                    continue
            try:
                with open(filepath, "rb") as fh:
                    current_hash = hashlib.sha256(fh.read()).hexdigest()
                if not force and db.get_file_hash(filepath) == current_hash:
                    files_skipped += 1
                    continue
                add_atomic_id(filepath, db)
                rf = File(filepath)
                rf.scan_file()
                db.set_file_hash(filepath, current_hash)
            except Exception as exc:
                print(f"  [WARN] {os.path.relpath(filepath, vault_path)}: {exc}")
                continue

            # Reconcile frontmatter → DB: restore anki_ids lost if DB was wiped
            fm_sync = _read_frontmatter_sync(filepath)
            if fm_sync:
                for note_row in db.get_notes_for_file(filepath):
                    if not note_row["anki_id"] and note_row["id"] in fm_sync:
                        db.mark_synced(note_row["id"], fm_sync[note_row["id"]])

            n_add    = len(rf.notes_to_add)
            n_edit   = len(rf.notes_to_edit)
            n_skip   = len(rf.notes_skipped)
            n_review = len(rf.pending_review)
            count    = n_add + n_edit + n_skip + n_review
            if count:
                rel = os.path.relpath(filepath, vault_path)
                parts = []
                if n_add:    parts.append(f"add={n_add}")
                if n_edit:   parts.append(f"edit={n_edit}")
                if n_skip:   parts.append(f"skip={n_skip}")
                if n_review: parts.append(f"review={n_review}")
                print(f"  {rel}: {count} note(s)  ({', '.join(parts)})")
                files_with_notes += 1
                total_notes += count

    os.chdir(start_dir)

    skip_msg = f", {files_skipped} skipped (unchanged)" if files_skipped else ""
    print(f"\n[vault] Scan complete — {files_with_notes} files, {total_notes} notes{skip_msg}")
    rows = db._conn.execute(
        "SELECT note_type, COUNT(*) AS n FROM notes GROUP BY note_type ORDER BY n DESC"
    ).fetchall()
    print("[vault] Notes by type:")
    for row in rows:
        print(f"     {row['note_type']:40s}  {row['n']:>4d}")

    return files_with_notes, total_notes


def parse_files(vault_path: str, db: NoteDB, force: bool = False) -> tuple[int, int]:
    """Alias for run_vault_scan — name matches plan.md process step 3."""
    return run_vault_scan(vault_path, db, force=force)


def compare_vault_modifications(db: NoteDB, exclude_synced: bool = True) -> list[dict]:
    """Return state comparison rows — plan.md process step 4."""
    return db.get_comparison_rows(exclude_synced=exclude_synced)


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

    relinked = db.reconcile_stale_ids()
    if relinked:
        print(f"[anki] Re-linked {relinked} stale anki_id(s) to new orphan note(s)")

    summary = db.get_comparison_summary()
    print("[anki] Comparison vs vault:")
    for row in summary:
        print(f"       {row['status']:20s}  {row['n']:>4d}")

    return len(all_notes)


# ── Stage 3: Diff ──────────────────────────────────────────────────────────────

def _strip_html(text: str | None, max_len: int = 80) -> str:
    if not text:
        return ""
    plain = re.sub(r"<[^>]+>", "", text).replace("\n", " ").strip()
    return (plain[:max_len] + "…") if len(plain) > max_len else plain


def _plain(text: str | None) -> str:
    """Strip HTML tags without truncating — used for content equality checks."""
    if not text:
        return ""
    return re.sub(r"<[^>]+>", "", text).replace("\n", " ").strip()


def _content_ratio(a: str | None, b: str | None) -> float:
    """Return 0–1 similarity between two field strings (plain-text, no HTML)."""
    pa, pb = _plain(a), _plain(b)
    if not pa and not pb:
        return 1.0
    return SequenceMatcher(None, pa, pb).ratio()


def _lookup_uuid(db: NoteDB, row: dict) -> str | None:
    file_path = row.get("file_path")
    if not file_path:
        return None
    match = db._conn.execute(
        "SELECT id FROM notes WHERE file_path = ? AND note_type = ? AND field_1 = ?",
        (file_path, row.get("note_type"), row.get("vault_field_1")),
    ).fetchone()
    return match["id"] if match else None


def _deck_from_path(file_path: str | None, vault_path: str) -> str:
    """Resolve Anki deck for a note file via FOLDER_DECKS patterns, else UNMATCHED_DECK."""
    if not file_path:
        return globals.UNMATCHED_DECK
    norm = file_path.replace("\\", "/")
    for pattern, deck_name in globals.CONFIG_DATA.get("FOLDER_DECKS", []):
        if pattern.search(norm):
            return deck_name
    return globals.UNMATCHED_DECK


def _parse_tags(raw: str | None) -> list[str]:
    if not raw:
        return []
    try:
        return json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        return []


def build_diff(db: NoteDB, vault_path: str) -> dict:
    """Read note_comparison and stale notes, populate anki_diff table, return counts dict."""
    db.clear_diff()

    rows = db.get_comparison_rows(exclude_synced=True)
    managed_types: set[str] = set(globals.CONFIG_DATA.get("ATOMICS", {}).keys())

    diff: dict[str, list[dict]] = {
        "add": [],
        "update": [],
        "retype": [],
        "relink": [],
        "orphan": [],
        "modify_deck": [],
        "stale": [],
    }

    for r in rows:
        status = r["status"]

        if status in ("not_in_anki", "stale_id"):
            uuid = _lookup_uuid(db, r)
            fp = r.get("file_path")
            operation = "relink" if status == "stale_id" else "add"
            stale_anki_id = r.get("anki_id") if status == "stale_id" else None
            entry_id = uuid or str(_uuid_mod.uuid4())
            deck = _deck_from_path(fp, vault_path)
            tags = _parse_tags(r.get("vault_tags"))
            db.upsert_diff_entry(
                id=entry_id, operation=operation,
                note_type=r.get("note_type") or "", deck_name=deck,
                field_1=r.get("vault_field_1"), field_2=r.get("vault_field_2"),
                tags=tags, anki_id=stale_anki_id, file_path=fp,
            )
            entry = {
                "uuid": uuid, "note_type": r.get("note_type") or "",
                "deck_name": deck, "field_1": r.get("vault_field_1"),
                "field_2": r.get("vault_field_2"), "tags": tags, "file_path": fp,
            }
            if status == "stale_id":
                diff["relink"].append(entry)
            else:
                diff["add"].append(entry)

        elif status in ("modify_fields", "modify_field_1", "modify_field_2"):
            if (_plain(r.get("vault_field_1")) == _plain(r.get("anki_field_1"))
                    and _plain(r.get("vault_field_2")) == _plain(r.get("anki_field_2"))):
                continue
            # Corrupt link: vault and Anki content share < 50% similarity — bad anki_id.
            if _content_ratio(r.get("vault_field_1"), r.get("anki_field_1")) < 0.5:
                uuid = _lookup_uuid(db, r)
                if uuid:
                    db.set_state_and_action(uuid, "not_in_anki", None)
                continue
            uuid = _lookup_uuid(db, r)
            fp = r.get("file_path")
            entry_id = uuid or str(_uuid_mod.uuid4())
            deck = _deck_from_path(fp, vault_path)
            db.upsert_diff_entry(
                id=entry_id, operation="update",
                note_type=r.get("note_type") or "", deck_name=deck,
                field_1=r.get("vault_field_1"), field_2=r.get("vault_field_2"),
                tags=None, anki_id=r.get("anki_id"), file_path=fp,
            )
            diff["update"].append({
                "uuid": uuid, "anki_id": r.get("anki_id"),
                "note_type": r.get("note_type") or "", "deck_name": deck,
                "field_1": r.get("vault_field_1"), "field_2": r.get("vault_field_2"),
                "anki_field_1": r.get("anki_field_1"), "anki_field_2": r.get("anki_field_2"),
                "file_path": fp,
            })

        elif status == "modify_type":
            uuid = _lookup_uuid(db, r)
            fp = r.get("file_path")
            entry_id = uuid or str(_uuid_mod.uuid4())
            deck = _deck_from_path(fp, vault_path)
            tags = _parse_tags(r.get("vault_tags"))
            db.upsert_diff_entry(
                id=entry_id, operation="retype",
                note_type=r.get("note_type") or "", deck_name=deck,
                field_1=r.get("vault_field_1"), field_2=r.get("vault_field_2"),
                tags=tags, anki_id=r.get("anki_id"), file_path=fp,
            )
            diff["retype"].append({
                "uuid": uuid, "anki_id": r.get("anki_id"),
                "note_type": r.get("note_type") or "", "deck_name": deck,
                "field_1": r.get("vault_field_1"), "field_2": r.get("vault_field_2"),
                "tags": tags, "file_path": fp,
            })

        elif status == "modify_deck":
            uuid = _lookup_uuid(db, r)
            fp = r.get("file_path")
            entry_id = uuid or str(_uuid_mod.uuid4())
            vault_deck = r.get("vault_deck")
            db.upsert_diff_entry(
                id=entry_id, operation="move_deck",
                note_type=r.get("note_type") or "", deck_name=vault_deck,
                field_1=r.get("vault_field_1"), field_2=None,
                tags=None, anki_id=r.get("anki_id"), file_path=fp,
            )
            diff["modify_deck"].append({
                "uuid": uuid, "anki_id": r.get("anki_id"),
                "note_type": r.get("note_type") or "",
                "vault_deck": vault_deck, "anki_deck": r.get("anki_deck"),
                "field_1": r.get("vault_field_1"), "file_path": fp,
            })

        elif status == "orphan_in_anki":
            note_type = r.get("note_type") or ""
            if managed_types and note_type not in managed_types:
                continue
            anki_id = r.get("anki_id")
            entry_id = f"delete:{anki_id}"
            db.upsert_diff_entry(
                id=entry_id, operation="delete",
                note_type=note_type, deck_name=r.get("anki_deck") or "",
                field_1=r.get("anki_field_1"), field_2=r.get("anki_field_2"),
                tags=None, anki_id=anki_id, file_path=None,
            )
            diff["orphan"].append({
                "anki_id": anki_id, "note_type": note_type,
                "field_1": r.get("anki_field_1"), "field_2": r.get("anki_field_2"),
                "deck_name": r.get("anki_deck") or "",
            })

    stale_notes = db.get_notes_by_state("stale")
    for n in stale_notes:
        db.upsert_diff_entry(
            id=n["id"], operation="stale",
            note_type=n["note_type"], deck_name=None,
            field_1=n["field_1"], field_2=None,
            tags=None, anki_id=None, file_path=n["file_path"],
        )
        diff["stale"].append({
            "uuid": n["id"], "note_type": n["note_type"],
            "field_1": n["field_1"], "file_path": n["file_path"],
        })

    return diff




# ── CLI ────────────────────────────────────────────────────────────────────────

def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="scan",
        description=(
            "Vault scanner, Anki snapshot, and diff generator.\n\n"
            "The vault is the source of truth. The DB caches vault state (notes)\n"
            "and Anki state (anki_notes). Scanning updates the vault snapshot;\n"
            "diff compares it to the Anki snapshot and writes pending changes to\n"
            "the anki_diff table. Run write.py to execute those changes.\n\n"
            "Use --anki to refresh the Anki snapshot (requires AnkiConnect running)."
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
        "--anki",
        action="store_true",
        help=(
            "Force Anki snapshot refresh. Runs automatically when 'Anki Path' is set "
            "in config — only needed to override when the path is not configured."
        ),
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Scan all vault files even if their hash is unchanged since the last scan.",
    )
    return parser


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()

    db, _ = _init()

    _vault_raw = args.vault_path or globals.CONFIG_DATA.get("Vault")
    if not _vault_raw:
        parser.error(
            "No vault path provided. Either pass vault_path as an argument "
            "or set 'Vault path' in the [Obsidian] section of atomics_config.ini."
        )
    vault_path = os.path.abspath(_vault_raw)
    if not os.path.isdir(vault_path):
        parser.error(f"vault_path is not a directory: {vault_path}")

    print(f"Loaded note types from config: {list(globals.CONFIG_DATA.get('ATOMICS', {}).keys())}")
    print(f"Vault: {vault_path}\n")

    run_vault_scan(vault_path, db, force=args.force)

    anki_configured = bool(globals.CONFIG_DATA.get("Path"))
    if args.anki or anki_configured:
        scan_anki(db)

    vault_count = db._conn.execute("SELECT COUNT(*) FROM notes").fetchone()[0]
    anki_count  = db._conn.execute("SELECT COUNT(*) FROM anki_notes").fetchone()[0]

    if not vault_count:
        print("\n[diff] No vault notes in DB — skipping diff.")
    elif not anki_count:
        print("\n[diff] No Anki snapshot in DB — set 'Anki Path' in config or run with --anki.")
    else:
        print("\n[diff] Building diff…")
        diff = build_diff(db, vault_path)

        total = sum(len(v) for v in diff.values())
        print(
            f"\n[diff] add={len(diff['add'])}, update={len(diff['update'])}, "
            f"retype={len(diff.get('retype', []))}, relink={len(diff['relink'])}, "
            f"move_deck={len(diff.get('modify_deck', []))}, "
            f"delete={len(diff['orphan'])}, stale={len(diff['stale'])}  (total={total})"
        )
        print("[diff] Pending changes written to anki_diff table. Run write.py to apply.")

    db.close()
    print("\nDone.")


if __name__ == "__main__":
    main()
