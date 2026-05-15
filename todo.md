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
- `src/obsidian_to_anki/` → `src/atomics/` (directory rename)
- `pyproject.toml` — project name + scripts entry point
- `scan.py`, `write.py`, `show.py` — `sys.path.insert` + all `from obsidian_to_anki import ...`
- `tests/` — all imports
- `CLAUDE.md` — references

### New targets — abstraction needed first

All new targets share a prerequisite: a `Writer` protocol with `add / update / delete` methods. `AnkiWriter` wraps current `write.py` logic; new writers implement same interface. Without this, each target becomes its own fork of `write.py`.

- **Navi**: `field_1` → `%` description, `field_2` → command. Pure-file output, no live process. Simplest new target.
- **Repeater**: Read the repo before designing — format unknown.
- **SQLite output**: Could re-use `NoteDB` schema or emit a separate export DB.
- **Postgres**: Lowest priority; same shape as SQLite but with driver dependency.
