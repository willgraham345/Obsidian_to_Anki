"""
Standalone vault scanner — no Anki connection required.

Walks the complex-vault recursively, parses regex notes using the existing
config, upserts each note into an in-memory SQLite DB, then prints a summary.

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
from obsidian_to_anki.file import RegexFile
from obsidian_to_anki.note import RegexNote

VAULT_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "tests", "complex-vault")
)

# ── 1. Init in-memory DB ───────────────────────────────────────────────────────
db = NoteDB(":memory:")
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
    """Replicate App.gen_regexp() without instantiating App."""
    note_prefix = globals.CONFIG_DATA["NOTE_PREFIX"]
    note_suffix = globals.CONFIG_DATA["NOTE_SUFFIX"]
    globals.NOTE_REGEXP = re.compile(
        note_prefix + r"([\s\S]*?)" + note_suffix, re.MULTILINE
    )
    inline_prefix = globals.CONFIG_DATA["INLINE_PREFIX"]
    inline_suffix = globals.CONFIG_DATA["INLINE_SUFFIX"]
    globals.INLINE_REGEXP = re.compile(
        inline_prefix + r"([\s\S]*?)" + inline_suffix
    )
    deck_line = globals.CONFIG_DATA["DECK_LINE"]
    globals.DECK_REGEXP = re.compile(
        r"^" + deck_line + r"(?:\n|: )(.*)", re.MULTILINE
    )
    tag_line = globals.CONFIG_DATA["TAG_LINE"]
    globals.TAG_REGEXP = re.compile(
        r"^" + tag_line + r"(?:\n|: )(.*)", re.MULTILINE
    )
    frozen_line = globals.CONFIG_DATA["FROZEN_LINE"]
    globals.FROZEN_REGEXP = re.compile(
        r"^" + frozen_line + r" - (.*?):\n((?:[^\n][\n]?)+)", re.MULTILINE
    )
    vault = globals.CONFIG_DATA.get("Vault", "")
    if vault:
        globals.VAULT_PATH_REGEXP = re.compile(
            re.escape(vault) + r"[/\\](.*)"
        )
    else:
        globals.VAULT_PATH_REGEXP = re.compile(r"^$")  # never matches

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
            rf = RegexFile(filepath)
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
