# obsidian-to-anki

CLI tool that syncs flashcard patterns from Obsidian markdown to Anki via [AnkiConnect](https://ankiweb.net/shared/info/2055492159).

## Prerequisites

- Anki running with AnkiConnect addon (port 8765)
- Python 3.12+
- [uv](https://docs.astral.sh/uv/)

## Install

```bash
cd obsidian_to_anki
uv sync
```

## Workflow

Three scripts run in sequence. All run from `obsidian_to_anki/`.

```bash
uv run python scan.py --all          # 1. snapshot vault + Anki into local DB
uv run python diff.py                # 2. compare → produce anki_diff.json + anki_diff.md
# review anki_diff.md, then:
uv run python write.py --execute     # 3. push changes to Anki
```

### scan.py

Populates the local SQLite DB. With no flags, `--vault` is implied.

| Flag | Description |
|------|-------------|
| `vault_path` | Path to vault. Falls back to `Vault path` in config. |
| `--vault` | Scan vault markdown files → populate `notes` table. |
| `--anki` | Query AnkiConnect → populate `anki_notes` snapshot table. Requires Anki running. |
| `--all` | Run `--vault` + `--anki` together. |
| `--prune-stale` | Remove DB notes whose vault file no longer exists (cleanup after deletes/moves). |

### diff.py

Compares vault notes against the Anki snapshot. Produces `anki_diff.json` (consumed by `write.py`) and `anki_diff.md` (human-readable review). Requires both `--vault` and `--anki` scans to have run.

| Flag | Description |
|------|-------------|
| `vault_path` | Path to vault. Falls back to config. |
| `--output-json FILE` | Override JSON manifest path (default: `anki_diff.json`). |
| `--output-md FILE` | Override markdown preview path (default: `anki_diff.md`). |

### write.py

Executes changes from `anki_diff.json` against Anki. Default is dry-run.

| Flag | Description |
|------|-------------|
| `--manifest FILE` | Override manifest path (default: `anki_diff.json`). |
| `--execute` | Actually write to Anki. Without this, prints what would happen. |
| `--delete-orphans` | Delete Anki notes flagged as orphans in the manifest. Requires `--execute`. |

## Config (`obsidian_to_anki_config.ini`)

Generated on first run of any script. Key sections:

### `[Custom Regexps]`

Each key is an Anki note type name (exact match). Capture groups map positionally to note fields.

```ini
[Custom Regexps]
Code = ^ (.*?) ;;; (.*?)
Term = ^󰙎 (.*?) ;; (.*?)
DuoTerm = ^󰙎 (.*?) ;;; (.*?)
Quiz = ^󰠗 (.*?) ;; (.*?)
```

### `[File Stem Notes]`

Note types listed here get the source filename appended to `field_1` as `<br><b>Filename</b>`. Useful for notes that appear in many files (e.g. `Code`, `Cmd`).

```ini
[File Stem Notes]
Code = True
Cmd = True
```

### `[Folder Decks]`

Maps vault folder glob patterns to Anki deck names.

```ini
[Folder Decks]
Docs/Programming_and_OS/Python/* = Python
Docs/ComputerScience.* = ComputerScience
```

### `[Obsidian]`

| Key | Description |
|-----|-------------|
| `Vault path` | Absolute path to vault root. |
| `Vault name` | Name used in Obsidian deep-links. |
| `Add file link` | Append an `obsidian://` link to `field_1`. |

### `[Defaults]`

| Key | Description |
|-----|-------------|
| `Regex` | Must be `True` to use `[Custom Regexps]`. |
| `Anki Path` | Path to Anki executable (used for auto-launch). |
| `Anki Profile` | Anki profile name to open. |

## Example Vault Note

```markdown
󰙎 Polymorphism ;; Ability of different objects to respond to the same interface differently

󰠗 What is a heap? ;; Dynamic memory region; allocated at runtime via malloc/new
```

## Legacy CLI (`obs2anki`)

The original single-file sync CLI is still available:

```bash
uv run obs2anki /path/to/file.md        # sync single file
uv run obs2anki /path/to/vault -R       # sync vault recursively
```

| Flag | Description |
|------|-------------|
| `-f` / `--file` | Target a single file. |
| `-d` / `--dir` | Target a directory. |
| `-R` / `--recurse` | Recurse into subdirectories. |
| `-r` / `--regex` | Override regex mode on/off. |
| `-u` / `--update` | Force update even if file hash unchanged. |
| `-c` / `--config` | Path to custom config file. |
| `-m` / `--mediaupdate` | Re-sync media attachments. |
