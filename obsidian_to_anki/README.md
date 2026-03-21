# obsidian-to-anki

A CLI tool for syncing flashcard-style patterns from Obsidian markdown notes to Anki via the [AnkiConnect](https://ankiweb.net/shared/info/2055492159) addon.

## Prerequisites

- [Anki](https://apps.ankiweb.net/) running with the AnkiConnect addon installed (default port: 8765)
- Python 3.12+
- [uv](https://docs.astral.sh/uv/)

## Install

```bash
cd obsidian_to_anki
uv sync
```

## First Run (generate config)

Run the CLI with no arguments to generate the default config file:

```bash
uv run obs2anki
```

This creates `obsidian_to_anki_config.ini` in your current directory with sections `[Syntax]`, `[Defaults]`, `[Obsidian]`, and `[Custom Regexps]`.

## Configure Custom Regex Patterns

Open `obsidian_to_anki_config.ini` and make the following changes.

### 1. Enable regex mode

In `[Defaults]`, set:

```ini
[Defaults]
Regex = True
```

Without this, custom regex patterns are silently ignored.

### 2. Add your patterns to `[Custom Regexps]`

Each key must match an Anki note type name **exactly**. Capture groups map positionally to note fields (first group → first field, second group → second field).

```ini
[Custom Regexps]
Basic = ^󰠗 (.+?) ;; (.+)
Term = ^󰙎 (.+?) ;;; (.+)
Code = ^`(.+?)` ;;; (.+)
```

| Config key | Anki note type | Fields | Pattern matches |
|------------|---------------|--------|-----------------|
| `Basic` | Basic (built-in) | Front / Back | `󰠗 question ;; answer` |
| `Term` | Term (create it) | Term / Definition | `󰙎 term ;;; description` |
| `Code` | Code (create it) | Snippet / Description | `` `code snippet` ;;; description `` |

> **Note:** The icons before `question` and `term` are Nerd Font glyphs (U+F0297 and U+F0257). They require a Nerd Font to display correctly, but the patterns will still match as long as the characters are present in the file.

### 3. Create the Term and Code note types in Anki

For `Basic`, Anki's built-in note type works out of the box. For `Term` and `Code`, create them manually:

1. In Anki, go to **Tools → Manage Note Types → Add**
2. Choose "Add: Basic" as the starting point
3. Name it `Term`, then edit its fields to be `Term` and `Definition` (in that order)
4. Repeat for `Code` with fields `Snippet` and `Description`

Field order must match capture group order in your regex.

## Example Vault Note

```markdown
# Biology Chapter 3

These are my study notes for the chapter.

󰠗 What is mitosis? ;; Cell division producing two genetically identical daughter cells

The cell cycle has several phases worth memorizing.

󰙎 Interphase ;;; The period between cell divisions; includes G1, S, and G2 phases

Here's a useful Python snippet for data analysis:

`df.groupby('col').agg({'val': 'sum'})` ;;; Group a DataFrame by a column and sum another
```

## Run the Sync

Sync a single file:

```bash
uv run obs2anki /path/to/note.md
```

Sync an entire vault recursively:

```bash
uv run obs2anki /path/to/vault -R
```

## How It Works

1. `obs2anki` scans each `.md` file line by line
2. Lines matching a `[Custom Regexps]` pattern are captured — capture groups populate note fields in order
3. Notes are sent to Anki via AnkiConnect in two stages: new notes are added, then existing notes are updated
4. File hashes are tracked so unchanged files are skipped on re-runs

## CLI Flags

| Flag | Description |
|------|-------------|
| `-f` / `--file` | Target a single file |
| `-d` / `--dir` | Target a directory |
| `-r` / `--regex` | Override regex mode on/off |
| `-R` / `--recurse` | Recurse into subdirectories |
| `-u` / `--update` | Force update even if file hash unchanged |
| `-c` / `--config` | Path to a custom config file |
| `-m` / `--mediaupdate` | Re-sync media attachments |

## Verification

1. Add test lines to a `.md` file using each pattern above
2. Run `uv run obs2anki path/to/test.md`
3. Open Anki and confirm the cards appeared in the correct deck with the correct fields populated
