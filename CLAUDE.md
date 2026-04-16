# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Python CLI tool (`obs2anki`) that syncs flashcards written in Obsidian markdown to Anki via the AnkiConnect API. This is a rewrite of the original Obsidian plugin (`original-plugin/`) — the Python package under `obsidian_to_anki/` is the active development target.

**Repo layout:** The root `pyproject.toml` and `uv.lock` are stubs — ignore them. All real code lives under `obsidian_to_anki/`.

## Commands

All commands run from `obsidian_to_anki/`:

```bash
uv sync                                           # install deps
uv run pytest tests/                              # run all tests
uv run pytest -vvs tests/test_note.py             # single test file
uv run pytest -vvs tests/test_note.py::TestName   # single test
uv build                                          # build package
uv run obs2anki /path/to/file.md                  # sync a file
uv run obs2anki /path/to/dir -R                   # sync directory recursively
```

CLI flags: `-f/--file`, `-d/--dir`, `-r/--regex`, `-R/--recurse`, `-u/--update`, `-c/--config`, `-m/--mediaupdate`

## Architecture

Source: `obsidian_to_anki/src/obsidian_to_anki/`

### Data Flow

```
Markdown → File.scan_file() → Note.parse() → FormatConverter.format() → AnkiConnect API → Anki
```

### Modules

| Module | Role |
|---|---|
| `__main__.py` | Entry point; auto-launches Anki if AnkiConnect not responding on port 8765 |
| `app.py` | CLI orchestrator — loads config/data, queries Anki for note types, processes files, executes two-stage requests |
| `config.py` | Manages `obsidian_to_anki_config.ini` (syntax delimiters, defaults, custom regexps) |
| `globals.py` | Shared mutable state: compiled regexes, note templates, media dict, field mappings, config data |
| `file.py` | Scans a single markdown file for block/inline/regex notes; categorizes into add/edit/delete; writes IDs back to file |
| `directory.py` | Iterates files in a directory, skips unchanged (by hash), builds batched AnkiConnect requests |
| `note.py` | Three note classes: `Note` (block), `InlineNote` (single-line), `RegexNote` (custom pattern) — all produce `Note_and_id` namedtuples |
| `format_converter.py` | Pipeline: math conversion → protect math/code → cloze conversion → markdown→HTML → restore math → extract/encode media → fix paths |
| `anki_connect.py` | HTTP wrapper for AnkiConnect (JSON over POST to localhost:8765, API version 6); handles WSL host detection |
| `data.py` | Persists `obsidian_to_anki_data.json` — tracks file SHA256 hashes and added media for incremental syncing |
| `utils.py` | Helpers: atomic file write, base64 encoding, cloze detection, span/ignore utilities, Anki process launcher |

### Two-Stage Request Process

The core sync mechanism in `directory.py` and `app.py`:

**Stage 1:** `getTags`, `storeMediaFile`, `addNote` (new notes → get IDs), `notesInfo`, `updateNoteFields`, `deleteNotes`

**Stage 2:** `changeDeck`, `removeTags`, `addTags`

New notes must be added first (stage 1) to obtain their IDs before deck/tag operations (stage 2).

### Note Types

1. **Block notes** — Multi-line, delimited by `START`/`END`, fields labeled by line prefix
2. **Inline notes** — Single-line between `STARTI`/`ENDI` markers, fields separated by `:`
3. **Regex notes** — Matched by custom regexes from `[Custom Regexps]` config section; capture groups map positionally to Anki fields

### Format Conversion Pipeline (`FormatConverter.format()`)

1. Convert Obsidian math delimiters (`$...$` → `\(...\)`, `$$...$$` → `\[...\]`)
2. Extract and protect math blocks from markdown parser
3. Extract and protect code blocks (inline and fenced)
4. Convert curly-brace cloze syntax to Anki cloze format (if CurlyCloze enabled)
5. Parse markdown → HTML (extensions: fenced_code, footnotes, md_in_html, tables, nl2br, sane_lists)
6. Restore math blocks (HTML-escaped)
7. Detect images/audio → base64 encode → add to `globals.MEDIA`
8. Fix media `src` attributes to basenames (Anki expects just filenames)
9. Strip wrapping `<p>` tags

### Global State

`globals.py` holds shared mutable state populated during initialization:
- `CONFIG_DATA` — parsed config values (delimiters, deck, regex mode, etc.)
- `FIELDS_DICT` — Anki model name → field names mapping
- `NOTE_DICT_TEMPLATE` — default note structure for AnkiConnect
- `MEDIA` — media files to upload (filename → base64 data)
- `EXISTING_IDS`, `ADDED_MEDIA`, `FILE_HASHES` — loaded from data.json
- Compiled regexes: `NOTE_REGEXP`, `INLINE_REGEXP`, `DECK_REGEXP`, `TAG_REGEXP`, `EMPTY_REGEXP`, etc.

**Testing note:** Tests that touch global state must reset it in setup fixtures.

## Configuration

### `obsidian_to_anki_config.ini`
Created on first run. Sections:
- `[Syntax]` — Note delimiters (START/END, STARTI/ENDI, TARGET DECK, FILE TAGS, DELETE, FROZEN)
- `[Defaults]` — Deck name, default tag, CurlyCloze toggle, regex mode, Anki path/profile
- `[Obsidian]` — Vault name, file link toggle
- `[Custom Regexps]` — Per-note-type regex patterns (e.g., `Basic = ^󰠗 (.+?) ;; (.+)`)

### `obsidian_to_anki_data.json`
Runtime persistence: `{"Added Media": [...], "File Hashes": {...}}`

Both files are gitignored.

## Dependencies

- Python ≥3.12
- `markdown` ≥3.8.2 — markdown→HTML parsing
- `pytest` ≥8.4.1 — testing
- Build system: Hatchling
- Package manager: **uv** (not poetry)
- Requires: Anki running with [AnkiConnect](https://ankiweb.net/shared/info/2055492159) addon

## The Original Plugin (`original-plugin/`)

The TypeScript/JS Obsidian plugin that this project is ported from. Uses Rollup bundling, Showdown for markdown, and XMLHttpRequest for AnkiConnect. The Python rewrite mirrors its architecture (two-stage requests, file hashing, same note syntax) but runs as a standalone CLI instead of an Obsidian plugin.

Reference only — not under active development.

## Current State

The Python rewrite is in progress. FIXME comments in `app.py` and `config.py` mark incomplete initialization paths. The `__init__.py` main flow is partially commented out pending refactoring. Core modules (note parsing, format conversion, file scanning, AnkiConnect wrapper) are functional and well-tested.

## Tests

10 test files under `obsidian_to_anki/tests/` covering all modules. Tests mock AnkiConnect and file I/O. Global state is reset in fixtures for isolation.
