# Plan: SQLite Note Database

## Context

Add an SQLite DB as an intermediary layer between Obsidian (source of truth) and Anki. The DB stores one row per parsed note with a stable UUID. If note content changes between scans, the old Anki card is deleted and a new one created (new anki_id, same UUID). Replaces data.json as primary persistence; data.json written as human-readable backup.

User answers: vault-relative path, field_1/field_2 columns, UUID primary key, DB primary + JSON backup.

---

## Schema

```sql
CREATE TABLE IF NOT EXISTS notes (
    id          TEXT PRIMARY KEY,   -- UUID (stable across content changes)
    anki_id     INTEGER,            -- Anki note ID; NULL until synced; changes on content edit
    file_path   TEXT NOT NULL,      -- vault-relative path (e.g. "deck/note.md")
    line_number INTEGER NOT NULL,   -- 1-based line of match start in file
    note_type   TEXT NOT NULL,      -- model name from config (e.g. "Basic", "Cloze")
    field_1     TEXT,               -- first field HTML (front / cloze text)
    field_2     TEXT,               -- second field HTML (back); NULL for single-field types
    image_paths TEXT,               -- JSON array of image filenames (basenames only)
    tags        TEXT,               -- JSON array of tag strings
    deck_name   TEXT,               -- target Anki deck
    created_at  TEXT NOT NULL,
    updated_at  TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS file_hashes (
    file_path   TEXT PRIMARY KEY,   -- vault-relative path
    sha256      TEXT NOT NULL,
    updated_at  TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS added_media (
    filename    TEXT PRIMARY KEY    -- media filenames already uploaded to Anki
);
```

---

## Files to Create / Modify

| File | Change |
|------|--------|
| `src/obsidian_to_anki/db.py` | **New** — `NoteDB` class, all SQL |
| `src/obsidian_to_anki/data.py` | Modified — use DB as primary, write JSON backup |
| `src/obsidian_to_anki/globals.py` | Add `NOTE_DB = None` |
| `src/obsidian_to_anki/file.py` | Capture line numbers; DB upsert + change detection in `scan_file()` |
| `src/obsidian_to_anki/app.py` | Initialize `NoteDB`, pass to `Data` |
| `tests/test_db.py` | **New** — unit tests for `NoteDB` |

---

## Implementation

### 1. `db.py` — NoteDB class

```python
class NoteDB:
    DB_PATH = ...  # alongside data.json: obsidian_to_anki/obsidian_to_anki.db

    def __init__(self, db_path=None): ...
    def close(self): ...

    # Notes CRUD
    def upsert_note(self, uuid, anki_id, file_path, line_number, note_type,
                    field_1, field_2, image_paths, tags, deck_name) -> None: ...
    def get_note(self, uuid) -> dict | None: ...
    def get_note_by_location(self, file_path, line_number, note_type) -> dict | None: ...
    def delete_note(self, uuid) -> None: ...
    def get_notes_for_file(self, file_path) -> list[dict]: ...

    # Anki sync
    def mark_synced(self, uuid, anki_id) -> None: ...

    # File hashes (replaces data.json "File Hashes")
    def get_file_hash(self, file_path) -> str | None: ...
    def set_file_hash(self, file_path, sha256) -> None: ...
    def get_all_file_hashes(self) -> dict: ...

    # Added media (replaces data.json "Added Media")
    def add_media(self, filename) -> None: ...
    def get_added_media(self) -> list: ...
```

DB file path follows same pattern as `data.py`: `__file__/../../obsidian_to_anki.db`.

### 2. `data.py` — DB primary, JSON backup

- `load_data_file()`: load from DB into globals; fall back to JSON on first run (migration)
- `update_data_file()`: read current DB state, dump to JSON as backup
- `create_data_file()`: create DB tables + empty JSON backup
- Keep `globals.ADDED_MEDIA` and `globals.FILE_HASHES` populated from DB (same interface)

### 3. `globals.py`

Add one line: `NOTE_DB = None`

### 4. `file.py` — line numbers + DB upsert

**Line number helper** (add to `File`):
```python
def _line_of(self, char_pos: int) -> int:
    return self.file[:char_pos].count('\n') + 1
```

**Vault-relative path helper** (add to `File`):
```python
def _vault_rel_path(self) -> str:
    if globals.CONFIG_DATA.get("Vault") and globals.VAULT_PATH_REGEXP.search(self.path):
        return globals.VAULT_PATH_REGEXP.search(self.path).group(1)
    return self.path
```

**Image extraction from HTML fields**:
```python
_IMG_SRC = re.compile(r'<img[^>]+src="([^"]+)"')

def _extract_images(fields: dict) -> list[str]:
    imgs = []
    for html in fields.values():
        imgs += _IMG_SRC.findall(html)
    return imgs
```

**DB upsert after each parsed note in `scan_file()`** — look up by (file_path, line_no, note_type); if content changed, delete old anki_id and re-add; store uuid→position mapping for post-sync `mark_synced()` calls.

### 5. `app.py` — initialize DB

In `App.__init__()`, after `Data()`:
```python
from .db import NoteDB
globals.NOTE_DB = NoteDB()
```

---

## Change Detection Logic

| DB state | Content match | Action |
|----------|--------------|--------|
| No existing record | — | Insert new UUID, add to Anki |
| Exists, same content | yes | Normal edit path |
| Exists, content changed | no | Delete old anki_id, re-add (new Anki ID, same UUID) |
| Exists, no anki_id yet | no | Update DB record only |

---

## data.json Backup Format (unchanged)

```json
{
  "Added Media": ["file.jpg", ...],
  "File Hashes": {"vault/path/note.md": "sha256..."}
}
```

---

## Verification

```bash
cd obsidian_to_anki
uv run pytest tests/test_db.py -vvs      # new DB tests
uv run pytest tests/ -vvs                 # full suite
```
