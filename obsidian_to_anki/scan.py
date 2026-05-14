"""
Vault scanner, Anki snapshot, and diff manifest generator.

No Anki connection required for vault-only scan. --anki requires Anki running
with AnkiConnect on port 8765.

Usage (from obsidian_to_anki/):
    uv run python scan.py [vault_path] [--anki] [--force]
                          [--output-json FILE] [--output-md FILE]
                          [--resolve] [--resolve-review]

    vault_path      Path to Obsidian vault (falls back to 'Vault path' in config).
                    Vault scan runs by default when a path is resolvable.

    --anki          Also snapshot Anki. When vault data exists, automatically
                    generates anki_diff.json + anki_diff.md for write.py.
    --force         Scan all vault files even if their hash is unchanged.
    --output-json   JSON manifest consumed by write.py (default: anki_diff.json).
    --output-md     Human-readable markdown preview (default: anki_diff.md).
    --resolve       Interactively approve each modified note before writing diff.
    --resolve-review  Interactively link review-queued notes before writing diff.

Workflow:
    uv run python scan.py /vault --anki   # full pipeline → anki_diff.json
    uv run python write.py --execute      # push changes to Anki
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import uuid as _uuid_mod
from datetime import datetime, timezone
from urllib.error import URLError

import yaml

# ── Make src importable ────────────────────────────────────────────────────────
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from obsidian_to_anki import globals                          # noqa: E402
from obsidian_to_anki.anki_connect import AnkiConnect         # noqa: E402
from obsidian_to_anki.config import Config                    # noqa: E402
from obsidian_to_anki.db import NoteDB                        # noqa: E402
from obsidian_to_anki.file import File                        # noqa: E402

# ── Constants ──────────────────────────────────────────────────────────────────

_DEFAULT_JSON = "anki_diff.json"
_DEFAULT_MD   = "anki_diff.md"

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

    for root, dirs, files in os.walk(vault_path):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        md_files = sorted(f for f in files if f.endswith(".md"))
        if not md_files:
            continue
        os.chdir(root)
        for filename in md_files:
            filepath = os.path.join(root, filename)
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
    """Read note_comparison and stale notes, return structured diff dict."""
    rows = db.get_comparison_rows(exclude_synced=True)
    managed_types: set[str] = set(globals.CONFIG_DATA.get("ATOMICS", {}).keys())

    diff: dict[str, list[dict]] = {
        "add": [],
        "update": [],
        "retype": [],
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
            # Skip notes queued for interactive resolution — user must run --resolve-review first
            if uuid:
                note = db.get_note(uuid)
                if note and note.get("recommended_action") in ("review", "link"):
                    continue
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

        elif status in ("modify_fields", "modify_field_1", "modify_field_2"):
            # Skip HTML-only diffs — Anki normalises stored HTML so vault and
            # Anki raw values differ even when visible content is identical.
            if (_plain(r.get("vault_field_1")) == _plain(r.get("anki_field_1"))
                    and _plain(r.get("vault_field_2")) == _plain(r.get("anki_field_2"))):
                continue
            uuid = _lookup_uuid(db, r)
            fp = r.get("file_path")
            diff["update"].append({
                "uuid":        uuid,
                "anki_id":     r.get("anki_id"),
                "note_type":   r.get("note_type") or "",
                "deck_name":   _deck_from_path(fp, vault_path),
                "field_1":     r.get("vault_field_1"),
                "field_2":     r.get("vault_field_2"),
                "anki_field_1": r.get("anki_field_1"),
                "anki_field_2": r.get("anki_field_2"),
                "file_path":   fp,
            })

        elif status == "modify_type":
            uuid = _lookup_uuid(db, r)
            fp = r.get("file_path")
            diff["retype"].append({
                "uuid":      uuid,
                "anki_id":   r.get("anki_id"),
                "note_type": r.get("note_type") or "",
                "deck_name": _deck_from_path(fp, vault_path),
                "field_1":   r.get("vault_field_1"),
                "field_2":   r.get("vault_field_2"),
                "tags":      _parse_tags(r.get("vault_tags")),
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
                continue
            diff["orphan"].append({
                "anki_id":   r.get("anki_id"),
                "note_type": note_type,
                "field_1":   r.get("anki_field_1"),
                "field_2":   r.get("anki_field_2"),
                "deck_name": r.get("anki_deck") or "",
            })

    stale_notes = db.get_notes_by_state("stale")
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
      [u]pdate  — push vault version to Anki
      [s]kip    — leave for later (removed from this diff run)
      [r]evert  — accept Anki version (DB updated to match Anki; note synced)

    Returns a new diff dict with only the [u]pdate-approved entries remaining.
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

        vault_f1 = _strip_html(entry.get("field_1"), max_len=200)
        vault_f2 = _strip_html(entry.get("field_2"), max_len=200)

        anki_f1 = anki_f2 = ""
        if anki_id:
            row = db._conn.execute(
                "SELECT field_1, field_2 FROM anki_notes WHERE anki_id = ?",
                (anki_id,),
            ).fetchone()
            if row:
                anki_f1 = _strip_html(row["field_1"], max_len=200)
                anki_f2 = _strip_html(row["field_2"], max_len=200)

        print(f"\n{'─'*60}")
        print(f"Note {i}/{total} — {note_type}")
        if fp:
            print(f"  {fp}")
        if vault_f1 == anki_f1 and vault_f2 == anki_f2:
            print("  [HTML-only diff — visible content is identical]")
            print(f"  F1: {vault_f1}")
        else:
            print(f"  Vault F1: {vault_f1}")
            print(f"  Anki  F1: {anki_f1}")
        if vault_f2 or anki_f2:
            if vault_f1 != anki_f1 or vault_f2 != anki_f2:
                print(f"  Vault F2: {vault_f2}")
                print(f"  Anki  F2: {anki_f2}")

        while True:
            choice = input("\n  [u]pdate Anki  [s]kip  [r]evert DB to Anki: ").strip().lower()
            if choice in ("u", "update"):
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


def resolve_review(db: NoteDB, diff: dict, vault_path: str) -> dict:
    """Interactively resolve notes queued for ambiguous similarity matches.

    For each note with recommended_action = 'review' or 'link':
      [1..N]  Link to that candidate
      [a]dd   Add as new card
      [s]kip  Leave for next run
    """
    items = db.get_review_queue()
    if not items:
        print("No review-queue items.")
        return diff

    total = len(items)
    for i, note in enumerate(items, 1):
        uuid      = note["id"]
        note_type = note["note_type"]
        fp        = note["file_path"] or ""
        f1_raw    = note.get("field_1")
        f2_raw    = note.get("field_2")
        action    = note.get("recommended_action", "review")

        candidate_ids = db.similarity_search(f1_raw, f2_raw, note_type)
        candidates = []
        for cid in candidate_ids:
            row = db._conn.execute(
                "SELECT anki_id, field_1, field_2, deck_name FROM anki_notes WHERE anki_id = ?",
                (cid,),
            ).fetchone()
            if row:
                candidates.append(dict(row))

        print(f"\n{'─'*60}")
        print(f"Review {i}/{total} — {note_type}  [{action}]")
        if fp:
            print(f"  {fp}")
        print(f"  Vault F1: {_strip_html(f1_raw)}")
        f2_disp = _strip_html(f2_raw)
        if f2_disp:
            print(f"  Vault F2: {f2_disp}")

        if candidates:
            for j, c in enumerate(candidates, 1):
                cf1  = _strip_html(c["field_1"])
                cf2  = _strip_html(c.get("field_2") or "")
                deck = c.get("deck_name") or ""
                line = f"  [{j}] Anki {c['anki_id']}: {cf1}"
                if cf2:
                    line += f" / {cf2}"
                if deck:
                    line += f"  [{deck}]"
                print(line)
        else:
            print("  (no candidates found — may have changed since last scan)")

        print("  [a] Add as new card   [s] Skip this run")

        while True:
            choice = input("  Choice: ").strip().lower()
            if choice.isdigit():
                j = int(choice) - 1
                if 0 <= j < len(candidates):
                    c = candidates[j]
                    db.mark_synced(uuid, c["anki_id"])
                    db.clear_recommended_action(uuid)
                    print(f"  → Linked to Anki ID {c['anki_id']}")
                    break
                print(f"  Invalid — enter 1–{max(1, len(candidates))}, a, or s.")
            elif choice in ("a", "add"):
                db.set_state_and_action(uuid, "not_in_anki", "add")
                deck = _deck_from_path(fp, vault_path)
                diff["add"].append({
                    "uuid":      uuid,
                    "note_type": note_type,
                    "deck_name": deck,
                    "field_1":   f1_raw,
                    "field_2":   f2_raw,
                    "tags":      _parse_tags(note.get("tags")),
                    "file_path": fp,
                })
                print("  → Queued for add")
                break
            elif choice in ("s", "skip"):
                print("  → Skipped")
                break
            else:
                print("  Invalid — enter a number, a, or s.")

    return diff


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


def write_markdown(diff: dict, vault_path: str, output_path: str) -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    total = sum(len(v) for v in diff.values())

    counts = [
        ("add",               len(diff["add"])),
        ("update",            len(diff["update"])),
        ("re-type",           len(diff.get("retype", []))),
        ("re-add (stale ID)", len(diff["restale"])),
        ("modify deck",       len(diff.get("modify_deck", []))),
        ("orphan",            len(diff["orphan"])),
        ("stale (deleted)",   len(diff.get("stale", []))),
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
        _md_section_retype(lines, "Re-type (Delete + Re-add)", diff.get("retype", []), vault_path)
        _md_section_add(lines, "Re-add (Stale ID)", diff["restale"], vault_path)
        _md_section_modify_deck(lines, "Modify Deck", diff.get("modify_deck", []))
        _md_section_orphan(lines, "Orphan (Delete from Anki)", diff["orphan"])
        _md_section_stale(lines, "Stale (File Deleted)", diff.get("stale", []))

    content = "".join(lines) + "\n"
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as fh:
        fh.write(content)
    print(f"[md]   Written to: {output_path}")


def _rel(file_path: str | None, vault_path: str) -> str:
    if not file_path:
        return ""
    try:
        return os.path.relpath(file_path, vault_path)
    except ValueError:
        return file_path


def _md_note_entry(lines: list[str], r: dict, vault_path: str) -> None:
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


def _md_section_retype(lines: list[str], title: str, rows: list[dict], vault_path: str) -> None:
    if not rows:
        return
    lines.append(f"\n\n## {title} ({len(rows)})\n")
    for r in rows:
        _md_note_entry(lines, r, vault_path)
        f1 = _strip_html(r.get("field_1"))
        note_type = r.get("note_type") or ""
        deck = r.get("deck_name") or ""
        if f1:
            lines.append(f"\n**Field 1:** {f1}")
        lines.append(f"\n**New Type:** {note_type}")
        if deck:
            lines.append(f"\n**Deck:** {deck}")
        lines.append("\n")


def _md_section_modify_deck(lines: list[str], title: str, rows: list[dict]) -> None:
    if not rows:
        return
    lines.append(f"\n\n## {title} ({len(rows)})\n")
    for r in rows:
        note_type  = r.get("note_type") or "Unknown"
        fp         = r.get("file_path") or ""
        f1         = _strip_html(r.get("field_1"))
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


# ── CLI ────────────────────────────────────────────────────────────────────────

def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="scan",
        description=(
            "Vault scanner, Anki snapshot, and diff manifest generator.\n\n"
            "Vault scan runs by default when a vault path is resolvable.\n"
            "Add --anki to snapshot Anki and generate anki_diff.json for write.py."
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
            "Also snapshot Anki and generate diff manifest (requires AnkiConnect). "
            "When vault data exists, automatically produces anki_diff.json + anki_diff.md."
        ),
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Scan all vault files even if their hash is unchanged since the last scan.",
    )
    parser.add_argument(
        "--output-json",
        default=_DEFAULT_JSON,
        metavar="FILE",
        help=f"JSON manifest output path (default: {_DEFAULT_JSON}).",
    )
    parser.add_argument(
        "--output-md",
        default=_DEFAULT_MD,
        metavar="FILE",
        help=f"Markdown preview output path (default: {_DEFAULT_MD}).",
    )
    parser.add_argument(
        "--resolve",
        action="store_true",
        help=(
            "Interactively resolve modified notes before writing the diff. "
            "Prompts: [u]pdate Anki / [s]kip / [r]evert DB to Anki."
        ),
    )
    parser.add_argument(
        "--resolve-review",
        action="store_true",
        dest="resolve_review",
        help=(
            "Interactively resolve notes queued for review (ambiguous similarity matches). "
            "For each: choose a candidate to link, add as new card, or skip."
        ),
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
            "or set 'Vault path' in the [Obsidian] section of obsidian_to_anki_config.ini."
        )
    vault_path = os.path.abspath(_vault_raw)
    if not os.path.isdir(vault_path):
        parser.error(f"vault_path is not a directory: {vault_path}")

    print(f"Loaded note types from config: {list(globals.CONFIG_DATA.get('ATOMICS', {}).keys())}")
    print(f"Vault: {vault_path}\n")

    run_vault_scan(vault_path, db, force=args.force)

    if args.anki:
        scan_anki(db)

        vault_count = db._conn.execute("SELECT COUNT(*) FROM notes").fetchone()[0]
        anki_count  = db._conn.execute("SELECT COUNT(*) FROM anki_notes").fetchone()[0]

        if not vault_count:
            print("\n[diff] No vault notes in DB — skipping diff.")
        elif not anki_count:
            print("\n[diff] No Anki snapshot in DB — skipping diff.")
        else:
            print("\n[diff] Generating diff manifest…")
            diff = build_diff(db, vault_path)

            if args.resolve_review:
                diff = resolve_review(db, diff, vault_path)

            if args.resolve:
                diff = resolve_modifications(diff, db)

            pending_review = len(db.get_review_queue())

            total = sum(len(v) for v in diff.values())
            print(
                f"\n[diff] add={len(diff['add'])}, update={len(diff['update'])}, "
                f"retype={len(diff.get('retype', []))}, restale={len(diff['restale'])}, "
                f"modify_deck={len(diff.get('modify_deck', []))}, "
                f"orphan={len(diff['orphan'])}, stale={len(diff['stale'])}  (total={total})"
            )
            if pending_review:
                print(
                    f"[diff] {pending_review} note(s) need interactive resolution. "
                    "Re-run with --resolve-review."
                )

            write_json(diff, vault_path, args.output_json)
            write_markdown(diff, vault_path, args.output_md)

    db.close()
    print("\nDone.")


if __name__ == "__main__":
    main()
