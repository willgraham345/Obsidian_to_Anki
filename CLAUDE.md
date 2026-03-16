# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repo contains two components:
1. **`original-plugin/`** — The original Obsidian plugin (TypeScript/JS) that inspired this project
2. **`obsidian_to_anki/`** — A Python CLI rewrite (active development), converting Obsidian markdown flashcards to Anki via the AnkiConnect API

The Python package is the primary focus. It requires Anki running with the AnkiConnect addon (port 8765).

## Commands

All commands run from `obsidian_to_anki/`:

```bash
# Install dependencies
poetry install

# Run all tests
pytest tests/

# Run a single test file
pytest -vvs tests/test_note.py

# Run a single test
pytest -vvs tests/test_note.py::TestNoteParsing::test_basic_note

# Build the package
poetry build

# Run the CLI
poetry run obs2anki /path/to/file.md
poetry run obs2anki /path/to/dir -R   # recursive
```

CLI flags: `-f/--file`, `-d/--dir`, `-r/--regex`, `-R/--recurse`, `-u/--update`, `-c/--config`, `-m/--mediaupdate`

## Architecture

The Python package lives in `obsidian_to_anki/src/obsidian_to_anki/`.

**Data flow:**
```
Markdown file → File.scan_file() → Note.parse() → FormatConverter → AnkiConnect API → Anki
```

**Key modules:**

| Module | Role |
|--------|------|
| `__main__.py` | Entry point; starts Anki if needed |
| `app.py` | CLI parsing, config setup, orchestrates file/directory scanning |
| `config.py` | INI config management (`obsidian_to_anki_config.ini`) |
| `globals.py` | Global state — note templates, compiled regexes, media tracking, field dicts |
| `file.py` | Parses notes out of a single file |
| `directory.py` | Iterates files, builds two-stage AnkiConnect request batches |
| `note.py` | Converts note text to AnkiConnect format |
| `format_converter.py` | Markdown→HTML, math, images, cloze syntax conversion |
| `anki_connect.py` | HTTP wrapper for the AnkiConnect API |
| `data.py` | JSON data file tracking media and file hashes (`obsidian_to_anki_data.json`) |

**Two-stage request process:** Stage 1 adds notes and retrieves IDs; Stage 2 updates existing notes using those IDs. This is the core sync mechanism in `directory.py`.

**File hashing** (`data.py`) skips unchanged files on re-runs.

**Global state** in `globals.py` is reset in test fixtures — tests that touch global state must reset it in setup.

## Configuration

- `obsidian_to_anki_config.ini` — Created on first run; sections: `[Syntax]`, `[Defaults]`, `[Obsidian]`, `[Custom Regexps]`
- `obsidian_to_anki_data.json` — Runtime data; tracks processed files and media

Both files are gitignored.

## Current State

The Python rewrite is in progress. Several `FIXME` comments mark incomplete initialization paths in `app.py` and `config.py`. Some imports and main-flow code are commented out pending refactoring.
