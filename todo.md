# Todo

- [x] Rename uv tool to "atomics" rather than "obsidian_to_anki"
- [ ] Start on new building functionality for new "targets"
  - [ ] [Navi](https://github.com/denisidoro/navi) (higher priority)
  - [ ] [Repeater](https://github.com/shaankhosla/repeater) (higher priority)
  - [ ] SQLite database
  - [ ] Postgres database
  - [ ]  Add feature to remove all cards in anki that are NOT in the sqlite database. This would be restoring functionality to the --delete-orphans. I've had a few moments where that's not quite happening correctly. For example, I modify an atomic within the vault, and the original card remains in Anki. This will need to be a more careful process, since this has the potential to ruin lots of stuff within Anki.

---

## Claude's notes

### Effort assessment

| Item | Effort | Notes |
|---|---|---|
| Fix --delete-orphans | Low-Med | Bug is bounded; logic exists |
| Rename to "atomics" | Low | Mechanical, no logic change |
| Navi target | Med | Pure-file writer, simpler than Anki |
| Repeater target | Med | Need to read repo first |
| SQLite output target | Med | DB layer already exists |
| Postgres output target | High | Blocked on abstraction layer |
| Fix `app.py` FIXME | High | May be worth formal deprecation instead |

### --delete-orphans gap (the modify-then-linger bug)

`write.py` flag exists and executes deletes correctly. Gap is upstream in `scan.py:build_diff()`:

1. Orphans only queued for deletion when `note_type in managed_types`. If ATOMICS config doesn't list a type, cards escape silently.
2. When a note is modified and hits a line-number cascade, the old anki_id can linger as `stale` rather than being promoted to `orphan_in_anki` — so the original card stays in Anki while a new one gets added.

Fix path: audit `build_diff` stale→orphan promotion; add round-trip test for "modify note in vault → old card gone, updated card exists." High blast radius — needs dry-run gate before real deletes.

### Rename to "atomics"

Files to touch:
- `src/obsidian_to_anki/` → `src/atomics/` (done)
- `pyproject.toml` — project name + scripts entry point
- `scan.py`, `write.py`, `show.py` — `sys.path.insert` + all `from atomics import ...`
- `tests/` — all imports
- `CLAUDE.md` — references

### Untested edge cases report

#### Critical

**`note.py:70-75` — magic return sentinel**
`parse()` returns integer `1` (not raises, not None) when Cloze note has no cloze syntax. Callers check `if parsed == 1` — type-unsafe. `Note` and `InlineNote` variants of this path not tested; only `RegexNote` covered.
Missing: `parse()` returning `1` for `Note` + `InlineNote`; same input with `CurlyCloze=False` (must not return `1`).

**`file.py:179-259` — `_atomic_state_flow()` branch coverage**
7+ routing branches (add/edit/review/link/retype/skip). Several paths untested:
- Stale ID + zero similarity matches → re-add
- Stale ID + multiple matches → `review`
- Valid ID + deck differs only → `modify_deck`
- Valid ID + field_1 differs, field_2 same → `modify_field_1`
- Valid ID + field_2 differs only → `modify_field_2`
- `effective_id=None` + single match → `link`
- `effective_id=None` + type mismatch → `retype`

**`app.py` — main sync workflow entirely untested**
`test_app.py` explicitly marks main flows as TODO. Two-stage request cycle, config/data error recovery, CLI flag handling all untested.
Missing: `--update` flag path; `--recurse` directory walk; config load failure → retry; data load failure → retry; `result[0]`/`result[2:]` hardcoded index assumptions (`app.py:123-124`).

**`format_converter.py:106-116` — cloze counter reset**
`CLOZE_UNSET_NUM` is a mutable class variable. If `format()` is called twice, second call restarts cloze numbering correctly only if reset fires. Not tested.
Missing: two consecutive `format()` calls; math block containing `{curly}` (cloze shouldn't touch protected math); code block containing `$math$`; paragraph strip when field has exactly 2 `<p>` tags.

**`db.py:418-718` — reconciliation ambiguous match paths**
`similarity_search`, `find_anki_note_by_content`, `reconcile_orphans`, `reconcile_stale_ids` all have multi-stage fallbacks.
Missing: `similarity_search` where stem-strip → empty string; `find_anki_note_by_content` Stage 1 ambiguous → must return None; `reconcile_orphans` Pass 1 ambiguous → Pass 2 skipped (`line 646`); `_dedup_notes` with two rows sharing same `anki_id`.

---

#### Moderate

**`utils.py:39-52` — `write_safe()` when original absent**
`os.rename(path, bak_path)` fails if path doesn't exist yet (first write). `string_insert()` has no bounds check on positions.

**`format_converter.py` — Obsidian syntax**
`![[embedded_note]]` and `[[wikilink]]` not tested through format pipeline.

**`anki_connect.py:72-79` — network failures + strict field count**
`parse()` requires exactly 2 fields — breaks if AnkiConnect adds a field. Network timeout (`URLError`) and connection-refused not tested.

**`config.py:142` — invalid regex in `[Custom Regexps]`**
`re.compile(pattern)` with no error handling. Malformed pattern crashes with no useful message.

**`directory.py:117-143` — partial batch failure**
`note_ids` parsed via `AnkiConnect.parse()` but `card_ids` assigned directly — inconsistent. No test for partial batch failure (one add fails).

**`scan.py` / `diff.py` — missing diff buckets**
`relink`, `delete`, `modify_deck` buckets never populated in tests. Unicode/emoji in field content not tested.

---

#### Minor

**`data.py:68` — silent JSON migration failure**
`json.JSONDecodeError` / `OSError` swallowed silently with no log.

**`file.py:12` — regex cache unbounded**
`_regex_cache` dict at module level; no size limit, no invalidation. Shared across all `File` instances.

**`scan.py` — filename edge cases**
Spaces, unicode filenames, symlinks to `.md` files, and atomic ID collisions not tested.

---

### New targets — abstraction needed first

All new targets share a prerequisite: a `Writer` protocol with `add / update / delete` methods. `AnkiWriter` wraps current `write.py` logic; new writers implement same interface. Without this, each target becomes its own fork of `write.py`.

- **Navi**: `field_1` → `%` description, `field_2` → command. Pure-file output, no live process. Simplest new target.
- **Repeater**: Read the repo before designing — format unknown.
- **SQLite output**: Could re-use `NoteDB` schema or emit a separate export DB.
- **Postgres**: Lowest priority; same shape as SQLite but with driver dependency.
