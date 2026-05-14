# Terms

**vault** — Obsidian directory of `.md` files. Source of truth.

**note / atomic** — A single flashcard definition parsed from a vault file. Identified by a UUID stored in the file's YAML frontmatter (`atomic_id`).

**note type** — Anki model name (e.g. `Basic`, `Cloze`). Determines field names.

**anki_id** — Integer ID assigned by Anki when a note is added. Links vault note to Anki note.

**snapshot** — Point-in-time copy of Anki state stored in `anki_notes` table. Refreshed with `scan.py --anki`.

**diff** — Set of changes between vault snapshot (`notes`) and Anki snapshot (`anki_notes`). Written to `anki_diff` table by `scan.py`.

**anki_diff table** — SQLite table of pending writes. Each row is one operation to apply on the next `write.py` run. Cleared per operation on success.

**operation** — Type of change in `anki_diff`. One of: `add`, `update`, `retype`, `restale`, `move_deck`, `delete`, `stale`.

**orphan** — Anki note with no matching vault entry (`operation=delete`).

**stale** — Vault note whose source file has been deleted (`operation=stale`). Not pushed to Anki automatically.

**relink** — Vault note with an `anki_id` not found in the local snapshot. Write queries Anki directly: if the note still exists, the DB link is restored (no new card, history preserved); if truly gone, it is added as a new card.

**target** — Write destination. Currently only Anki. Each target gets its own diff table (`anki_diff`, future `notion_diff`, etc.).
