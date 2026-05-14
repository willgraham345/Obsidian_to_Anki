# TODO

## Phase 1 — Remove Block and Inline Note Types

Goal: atomics (RegexNotes) are the only note type going forward. Block and inline notes are removed.

### `file.py`
- [ ] Remove `_handle_block_note()` and `_handle_inline_note()` methods
- [ ] Remove block and inline scan loops from `scan_file()`:
  - `findignore(globals.NOTE_REGEXP, ...)` loop
  - `findignore(globals.INLINE_REGEXP, ...)` loop
- [ ] Remove lists: `id_indexes`, `uuid_for_add`, `inline_notes_to_add`, `uuid_for_inline_add`
- [ ] Remove `Note` and `InlineNote` imports
- [ ] Simplify `get_add_notes()` — only regex (atomic) notes remain
- [ ] Simplify `update_db_anki_ids()` — only `uuid_for_regex_add` / `regex_id_indexes` remain
- [ ] Remove `get_clear_tags()` / `get_add_tags()` if only used by block/inline path (verify first)

### `note.py`
- [ ] Remove `Note` class (block notes)
- [ ] Remove `InlineNote` class
- [ ] Keep `RegexNote` only

### `globals.py`
- [ ] Remove `NOTE_REGEXP`, `INLINE_REGEXP` compiled regexps
- [ ] Remove any frozen-fields, EMPTY_REGEXP logic tied only to block notes (verify scope)

### `tests/`
- [ ] Remove test cases covering block note parsing (`test_note.py` — `TestNote`, `TestInlineNote`)
- [ ] Remove test cases covering block/inline scanning in `test_file.py`
- [ ] Keep `TestRegexNote` and atomic-related file scan tests

---

## Phase 2 — Unified Atomic State Flow

### Design

Three systems unified into one pipeline:

```
TRIGGER: file hash changed OR new atomic discovered
    ↓
search() parses all atomics in file
    ↓
_atomic_state_flow(parsed, file_path, line_no) per atomic:
    ├── has anki_id in source?
    │   ├── YES → anki_id in anki_notes table?
    │   │   ├── YES → compute diff state (see states below)
    │   │   └── NO (stale_id) → similarity_search()
    │   │       ├── 1 match → state=stale_id, action=link  (queue interactive)
    │   │       └── 0 or N  → state=stale_id, action=review (queue review)
    │   └── NO → similarity_search()
    │       ├── 1 match → state=not_in_anki, action=link   (queue interactive)
    │       ├── 0       → state=not_in_anki, action=add
    │       └── N > 1   → state=not_in_anki, action=review (queue review)
    ↓
write notes.state + recommended_action to DB
    ↓
categorize into runtime lists (drives AnkiConnect requests):
    action=add        → notes_to_add
    action=update_*   → notes_to_edit
    action=link       → pending interactive confirm → on confirm: link + notes_to_edit
    action=review     → pending_review queue (NOT sent to Anki this run)
    action=none       → skip
    ↓
[if pending_review non-empty] → interactive CLI prompt (see Phase 3)
    ↓
write script executes actions → clear recommended_action for executed notes
```

### States (written to `notes.state`)

| State | Meaning |
|---|---|
| `synced` | All fields, type, deck match Anki |
| `modify_field_1` | field_1 differs from Anki (field_2 matches) |
| `modify_field_2` | field_2 differs from Anki (field_1 matches) |
| `modify_fields` | Both field_1 and field_2 differ from Anki |
| `modify_type` | note_type differs |
| `modify_deck` | deck differs; fields match |
| `not_in_anki` | No anki_id; similarity search found 0 matches |
| `stale_id` | Has anki_id but not in Anki; similarity search found 0 or N matches |
| `pending_review` | Ambiguous similarity result (multiple candidates) |

`orphan_in_anki` remains VIEW-only (no vault row to write state to).

### `recommended_action` values (cleared to NULL after write executes)

| Value | Meaning |
|---|---|
| `add` | Create new Anki card |
| `update_field_1` | Push field_1 to Anki |
| `update_field_2` | Push field_2 to Anki |
| `update_fields` | Push both fields to Anki |
| `update_type` | Delete old Anki card + re-add with new note type (Anki has no in-place retype) |
| `update_deck` | Move card to correct deck |
| `link` | Link vault note to matched Anki card (interactive confirm) |
| `review` | Queued for user decision (not auto-executed) |
| `none` | No action needed |
| NULL | Action executed and cleared by write script |

### Diff state priority (CASE order in VIEW)

```
1. not_in_anki      (anki_id IS NULL in vault)
2. stale_id         (anki_id not found in anki_notes)
3. modify_type      (note_type mismatch)
4. modify_fields    (both fields differ)
5. modify_field_1   (field_1 only differs)
6. modify_field_2   (field_2 only differs)
7. modify_deck      (deck differs; fields match)
8. synced
```

### `db.py` changes

- [ ] Add `recommended_action TEXT` column to `notes` table
- [ ] Add `_migrate()` entry for `recommended_action`
- [ ] Update `note_comparison` VIEW: split `modify_fields` → `modify_field_1` / `modify_field_2` / `modify_fields`
- [ ] Add `set_state_and_action(uuid, state, action)` method
- [ ] Add `clear_recommended_action(uuid)` method — called by write script after executing
- [ ] Add `get_pending_review()` → list of notes with `recommended_action = 'review'`
- [ ] Add `similarity_search(field_1, field_2, note_type)` method:
  - Strip file-stem suffix (`<br><b>...</b>`) from both vault and Anki fields before comparing
  - Match against `anki_notes` with no corresponding vault row (`orphan_in_anki` candidates)
  - For `stale_id` path also match against vault notes with `anki_id IS NULL`
  - Returns list of `anki_id` candidates; caller decides link vs. review based on count
- [ ] Remove `mark_to_modify()` (replaced by `set_state_and_action`)
- [ ] Remove `mark_stale()` (replaced by state flow)

### `file.py` changes

- [ ] Add `_atomic_state_flow(parsed, file_path, line_no)` method:
  - Implements the decision tree above
  - Calls `db.similarity_search()` when needed
  - Calls `db.set_state_and_action()`
  - Returns categorization: `add` / `edit` / `link` / `review` / `skip`
- [ ] Replace `_apply_change_detection()` with `_atomic_state_flow()` in `search()`
- [ ] Add `pending_review` list to `_setup_scan()`
- [ ] Populate `pending_review` from `_atomic_state_flow()` returns
- [ ] After scan: if `pending_review` non-empty, surface to Phase 3 interactive handler

### `note_comparison` VIEW update

Replace current `modify_fields` branch:

```sql
-- current (remove):
WHEN ... OR v.field_2 IS NOT a.field_2 THEN 'modify_fields'

-- replace with (three branches, in order):
WHEN strip(v.field_1) != strip(a.field_1) AND strip(v.field_2) != strip(a.field_2) THEN 'modify_fields'
WHEN strip(v.field_1) != strip(a.field_1)                                           THEN 'modify_field_1'
WHEN strip(v.field_2) != strip(a.field_2)                                           THEN 'modify_field_2'
```

Where `strip()` = remove `<br><b>...</b>` suffix (file stem injection).

---

## Phase 3 — Interactive CLI Review Queue

Goal: when `pending_review` items exist after a scan, pause and prompt user before executing writes.

- [ ] Add `diff` subcommand (or flag) that outputs pending state without writing:
  - Show `recommended_action != 'none'` and `!= NULL` items grouped by action type
  - Output as Markdown subheadings (per plan.md preference — no tables)
- [ ] Add `--resolve-review` flag to interactive prompt for `review` items:
  - Present each queued atomic: show vault content vs. each candidate Anki match
  - Options per item:
    1. Link to candidate (sets `action=link`)
    2. Add as new card (sets `action=add`, strips stale_id if present)
    3. Skip this run (leave as `review`)
- [ ] Write script clears `recommended_action` to NULL after successful execution

---

## Phase 4 — Tests

- [ ] Unit tests for `_atomic_state_flow()` covering all branches
- [ ] Unit tests for `db.similarity_search()` with stem-stripping
- [ ] Unit tests for updated `note_comparison` VIEW (`modify_field_1`, `modify_field_2`, `modify_fields`)
- [ ] Unit tests for `recommended_action` lifecycle (set → execute → cleared)
- [ ] Integration test: hash change → state flow → correct categorization → correct recommended_action
