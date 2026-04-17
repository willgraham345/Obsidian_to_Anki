# Plan: Anki Snapshot Table + Comparison View

## Context

The DB currently tracks only the *vault* state (parsed notes, file hashes, media). There's no record of what Anki actually holds. Adding an `anki_notes` snapshot table enables side-by-side comparison — surfacing notes that are out of sync, orphaned in Anki, or not yet pushed.

User choices (confirmed via clarification):
- Populated by a **manual standalone script** (not auto on every sync)
- Fields per note: anki_id, note_type, field_1, field_2, tags, deck_name, mod_timestamp
- Comparison surfaces as both a **SQL VIEW** and a **scan_vault.py summary report**

---

## Change 1: `anki_notes` table + `note_comparison` VIEW in db.py

**File:** `src/obsidian_to_anki/db.py`

### Table schema (added to `_create_tables`)
```sql
CREATE TABLE IF NOT EXISTS anki_notes (
    anki_id       INTEGER PRIMARY KEY,
    note_type     TEXT NOT NULL,
    field_1       TEXT,
    field_2       TEXT,
    tags          TEXT,    -- JSON array
    deck_name     TEXT,
    mod_timestamp INTEGER,
    synced_at     TEXT NOT NULL
);
```

### VIEW (also added to `_create_tables`)
SQLite 3.39+ supports FULL OUTER JOIN. Joined on `anki_id`:

```sql
CREATE VIEW IF NOT EXISTS note_comparison AS
SELECT
    COALESCE(v.anki_id, a.anki_id)     AS anki_id,
    COALESCE(v.note_type, a.note_type) AS note_type,
    v.file_path,
    v.field_1   AS vault_field_1,
    a.field_1   AS anki_field_1,
    v.field_2   AS vault_field_2,
    a.field_2   AS anki_field_2,
    v.tags      AS vault_tags,
    a.tags      AS anki_tags,
    v.deck_name AS vault_deck,
    a.deck_name AS anki_deck,
    a.mod_timestamp,
    CASE
        WHEN a.anki_id IS NULL                        THEN 'not_in_anki'
        WHEN v.anki_id IS NULL                        THEN 'orphan_in_anki'
        WHEN v.field_1 IS NOT a.field_1
          OR v.field_2 IS NOT a.field_2               THEN 'modified'
        ELSE 'synced'
    END AS status
FROM notes v
FULL OUTER JOIN anki_notes a ON v.anki_id = a.anki_id;
```

### New NoteDB methods to add

```python
def upsert_anki_note(self, anki_id, note_type, field_1, field_2,
                     tags, deck_name, mod_timestamp) -> None:
    ...  # INSERT OR REPLACE INTO anki_notes ...

def clear_anki_notes(self) -> None:
    """Wipe table before re-snapshot so stale notes don't linger."""

def get_comparison_summary(self) -> list[dict]:
    """Returns rows of {status, count} from the note_comparison VIEW."""
    # SELECT status, COUNT(*) as n FROM note_comparison GROUP BY status ORDER BY n DESC
```

---

## Change 2: New standalone script `snapshot_anki.py`

**Location:** `obsidian_to_anki/snapshot_anki.py` (sibling of `scan_vault.py`)

### Flow

1. Init `NoteDB()` (persistent DB) and `Config().load_config()`
2. Instantiate `AnkiConnect`; call `invoke("findNotes", query="")` → list of all note IDs
3. Batch `notesInfo` in chunks of 50 → list of note dicts
4. **Field extraction**: `notesInfo` returns `fields` as `{name: {value, order}}`. Sort by `order`, take index 0 = field_1, index 1 = field_2 (None if fewer than 2 fields):
   ```python
   ordered = sorted(note["fields"].values(), key=lambda f: f["order"])
   field_1 = ordered[0]["value"] if ordered else None
   field_2 = ordered[1]["value"] if len(ordered) > 1 else None
   ```
5. **Deck lookup**: `notesInfo` returns `cards` (list of card IDs). Collect all card IDs → batch `cardsInfo` → build `{card_id: deck_name}` → map each note's first card to its deck.
6. `db.clear_anki_notes()` then `db.upsert_anki_note(...)` for every note
7. Print snapshot + comparison summary

### Report printed
```
Anki snapshot complete — 1504 notes stored

Comparison vs vault:
  synced            1201
  modified            87
  not_in_anki         42
  orphan_in_anki     174
```

---

## Change 3: scan_vault.py prints comparison if snapshot exists

**File:** `obsidian_to_anki/scan_vault.py`

After the existing DB summary block, add:
```python
anki_count = conn.execute("SELECT COUNT(*) FROM anki_notes").fetchone()[0]
if anki_count:
    print(f"\nComparison vs Anki snapshot ({anki_count} Anki notes):")
    for row in conn.execute(
        "SELECT status, COUNT(*) as n FROM note_comparison GROUP BY status ORDER BY n DESC"
    ).fetchall():
        print(f"  {row['status']:20s}  {row['n']:>4d}")
else:
    print("\n(No Anki snapshot — run snapshot_anki.py to populate anki_notes)")
```

---

## Critical Files

| File | Change |
|------|--------|
| `src/obsidian_to_anki/db.py` | Add `anki_notes` table + `note_comparison` VIEW + 3 new methods |
| `snapshot_anki.py` (new) | Standalone script — queries Anki, populates `anki_notes`, prints report |
| `scan_vault.py` | Print comparison summary at end |

No changes to `app.py`, `directory.py`, `note.py`, or `file.py`.

---

## Verification

```bash
cd obsidian_to_anki

# 1. Populate vault side; should see "(No Anki snapshot)" message
uv run python scan_vault.py

# 2. Populate Anki side (Anki must be running with AnkiConnect)
uv run python snapshot_anki.py
# → prints snapshot count + comparison summary

# 3. Re-run vault scan — should now show comparison block
uv run python scan_vault.py

# 4. Query VIEW directly
sqlite3 obsidian_to_anki.db \
  "SELECT status, COUNT(*) FROM note_comparison GROUP BY status;"

# 5. Tests still pass (no existing tests touch anki_notes)
uv run pytest tests/ -q
```
