"""
Standalone vault scanner — no Anki connection required.

Walks the complex-vault recursively, parses notes using the existing config,
upserts each note into the persistent obsidian_to_anki.db, then prints a summary.

This is the proving ground: populate and inspect the DB before syncing to Anki.

Usage (from obsidian_to_anki/):
    uv run python scan_vault.py
"""

import os
import re
import sys
import json
import sqlite3

# ── Make src importable ────────────────────────────────────────────────────────
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from obsidian_to_anki import globals
from obsidian_to_anki.config import Config
from obsidian_to_anki.db import NoteDB
from obsidian_to_anki.file import File
from obsidian_to_anki.note import RegexNote

VAULT_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "tests", "complex-vault")
)

# ── 1. Init persistent DB (proving ground before Anki sync) ──────────────────
db = NoteDB()          # writes to obsidian_to_anki.db next to this file
globals.NOTE_DB = db

# ── 2. Load config (no Anki needed) ───────────────────────────────────────────
config = Config()
try:
    config.load_config()
except Exception as e:
    print(f"Config error: {e}")
    sys.exit(1)

# ── 3. Bootstrap FIELDS_DICT without Anki ─────────────────────────────────────
#
# Inspect each custom regexp: the number of non-tag/id capture groups maps to
# the fields needed. We assign generic names "Field 1", "Field 2", … if the
# note type isn't known.
#
# For the "Test" type (3 groups → Front, Back, Extra) we use real names.
KNOWN_FIELDS = {
    "Test":                           ["Front", "Back", "Tags"],
    "Basic":                          ["Front", "Back"],
    "Basic (and reversed card)":      ["Front", "Back"],
    "Basic (optional reversed card)": ["Front", "Back", "Add Reverse"],
    "Basic (type in the answer)":     ["Front", "Back"],
    "Cloze":                          ["Text", "Extra"],
}

CUSTOM_REGEXPS = globals.CONFIG_DATA.get("CUSTOM_REGEXPS", {})
fields_dict = {}
for note_type, pattern in CUSTOM_REGEXPS.items():
    if note_type in KNOWN_FIELDS:
        fields_dict[note_type] = KNOWN_FIELDS[note_type]
    elif pattern:
        # Count capture groups in the base pattern (rough heuristic)
        groups = re.compile(pattern).groups
        fields_dict[note_type] = [f"Field {i+1}" for i in range(groups)]
    else:
        fields_dict[note_type] = KNOWN_FIELDS.get(note_type, ["Front", "Back"])

globals.FIELDS_DICT = fields_dict
globals.EXISTING_IDS = []          # no existing Anki notes
globals.FILE_HASHES = {}           # treat every file as new

print(f"Loaded note types: {list(fields_dict.keys())}")
print(f"Vault: {VAULT_PATH}\n")

# ── 4. Build compiled regexps ──────────────────────────────────────────────────
from obsidian_to_anki.app import App  # noqa: E402 — just for gen_regexp

def gen_regexp():
    """Compile all regexps — identical to App.gen_regexp()."""
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

gen_regexp()

# ── 5. Walk vault, scan each file ─────────────────────────────────────────────
total_notes = 0
files_with_notes = 0
start_dir = os.getcwd()

for root, dirs, files in os.walk(VAULT_PATH):
    # Skip hidden directories
    dirs[:] = [d for d in dirs if not d.startswith(".")]
    md_files = [f for f in files if f.endswith(".md")]
    if not md_files:
        continue

    os.chdir(root)
    for filename in sorted(md_files):
        filepath = os.path.join(root, filename)
        try:
            rf = File(filepath)
            rf.scan_file()
        except Exception as e:
            print(f"  [ERROR] {filename}: {e}")
            continue

        count = len(rf.notes_to_add) + len(rf.notes_to_edit)
        if count:
            rel = os.path.relpath(filepath, VAULT_PATH)
            print(f"  {rel}: {count} note(s)  "
                  f"(add={len(rf.notes_to_add)}, edit={len(rf.notes_to_edit)})")
            files_with_notes += 1
            total_notes += count

os.chdir(start_dir)

# ── 6. Summary from DB ────────────────────────────────────────────────────────
print(f"\n{'='*60}")
print(f"Scan complete")
print(f"  Files with notes : {files_with_notes}")
print(f"  Notes parsed     : {total_notes}")

# Query DB directly for a rich summary
conn = db._conn
rows = conn.execute(
    "SELECT note_type, COUNT(*) as n FROM notes GROUP BY note_type ORDER BY n DESC"
).fetchall()
print(f"\nNotes by type:")
for row in rows:
    print(f"  {row['note_type']:40s}  {row['n']:>4d}")

print(f"\nSample rows (first 10):")
print(f"  {'UUID':36s}  {'type':8s}  {'line':4s}  {'field_1 (first 50 chars)'}")
print(f"  {'-'*36}  {'-'*8}  {'-'*4}  {'-'*50}")
for row in conn.execute(
    "SELECT id, note_type, line_number, file_path, field_1, image_paths FROM notes LIMIT 10"
).fetchall():
    f1 = (row["field_1"] or "")[:50].replace("\n", " ")
    imgs = json.loads(row["image_paths"] or "[]")
    img_str = f"  [{len(imgs)} img]" if imgs else ""
    print(f"  {row['id']}  {row['note_type'][:8]:8s}  {row['line_number']:4d}  {f1}{img_str}")

db.close()
print()
