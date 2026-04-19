"""
Standalone Anki snapshot — requires Anki running with AnkiConnect.

Queries all notes from Anki, stores them in the anki_notes table of the
persistent obsidian_to_anki.db, then prints a comparison summary against
the vault state in the notes table.

Usage (from obsidian_to_anki/):
    uv run python snapshot_anki.py
"""

import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from obsidian_to_anki.anki_connect import AnkiConnect
from obsidian_to_anki.db import NoteDB

CHUNK = 50  # notesInfo / cardsInfo batch size

anki = AnkiConnect()
db = NoteDB()


def _chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


# ── 1. Fetch all note IDs ─────────────────────────────────────────────────────
print("Fetching note IDs from Anki...")
try:
    note_ids = anki.invoke("findNotes", query="")
except Exception as e:
    print(f"Cannot reach Anki: {e}")
    sys.exit(1)

print(f"  {len(note_ids)} notes found")

# ── 2. Batch notesInfo ────────────────────────────────────────────────────────
print("Fetching note details...")
notes_raw = []
for chunk in _chunks(note_ids, CHUNK):
    notes_raw += anki.invoke("notesInfo", notes=chunk)

# ── 3. Collect all card IDs for deck lookup ───────────────────────────────────
all_card_ids = []
note_to_first_card = {}  # anki_id → first card id
for note in notes_raw:
    cards = note.get("cards", [])
    if cards:
        note_to_first_card[note["noteId"]] = cards[0]
        all_card_ids.extend(cards)

# ── 4. Batch cardsInfo → build card_id → deck_name map ───────────────────────
print("Fetching deck info...")
card_to_deck = {}
for chunk in _chunks(all_card_ids, CHUNK):
    for card in anki.invoke("cardsInfo", cards=chunk):
        card_to_deck[card["cardId"]] = card.get("deckName")

# ── 5. Populate anki_notes ────────────────────────────────────────────────────
print("Writing snapshot to DB...")
db.clear_anki_notes()

for note in notes_raw:
    ordered = sorted(note["fields"].values(), key=lambda f: f["order"])
    field_1 = ordered[0]["value"] if ordered else None
    field_2 = ordered[1]["value"] if len(ordered) > 1 else None

    first_card = note_to_first_card.get(note["noteId"])
    deck_name = card_to_deck.get(first_card) if first_card else None

    db.upsert_anki_note(
        anki_id=note["noteId"],
        note_type=note["modelName"],
        field_1=field_1,
        field_2=field_2,
        tags=note.get("tags", []),
        deck_name=deck_name,
        mod_timestamp=note.get("mod"),
    )

print(f"\nAnki snapshot complete — {len(notes_raw)} notes stored")

# ── 6. Comparison summary ─────────────────────────────────────────────────────
rows = db.get_comparison_summary()
if rows:
    print("\nComparison vs vault:")
    for row in rows:
        print(f"  {row['status']:20s}  {row['n']:>4d}")
else:
    print("\n(No vault notes to compare — run scan_vault.py first)")

db.close()
print()
