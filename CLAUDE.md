# Obsidian to Anki

A CLI tool that converts Obsidian markdown notes into Anki flashcards via the AnkiConnect API.

## Project Layout

```
obsidian_to_anki/
├── src/obsidian_to_anki/   # Main package
│   ├── __main__.py          # CLI entry point (main_entry_point)
│   ├── app.py               # App orchestrator (arg parsing, request generation)
│   ├── config.py            # INI config read/write and syntax parsing
│   ├── data.py              # JSON persistence (file hashes, media list)
│   ├── globals.py           # Shared global variables
│   ├── anki_connect.py      # AnkiConnect HTTP API wrapper (port 8765)
│   ├── directory.py         # Directory scanning and batch processing
│   ├── file.py              # File-level note extraction and hashing
│   ├── note.py              # Note parsing → AnkiConnect dict format
│   ├── format_converter.py  # Markdown→HTML, math, cloze formatting
│   └── utils.py             # Helpers: base64, port waiting, Anki launch
└── tests/                   # pytest test suite
obsidian_to_anki_config.ini  # User config (syntax, defaults, custom regexps)
obsidian_to_anki_data.json   # Runtime state (file hashes, added media)
```

## CLI

```bash
obs2anki [path] [options]

Options:
  -c, --config      Open config file for editing
  -u, --update      Update config file (queries Anki for note types)
  -r, --regex       Use custom regex syntax
  -m, --mediaupdate Force re-add media files
  -R, --recurse     Recurse into subdirectories
```

## Development Setup

```bash
cd obsidian_to_anki
pip install -e .
# or with poetry:
poetry install
```

## Running Tests

```bash
cd obsidian_to_anki
pytest tests/
```

## Architecture Notes

- **AnkiConnect** must be running on port 8765 (Anki desktop app with addon installed)
- `Config` reads/writes `obsidian_to_anki_config.ini`; sections: `[Syntax]`, `[Obsidian]`, `[Defaults]`, `[Custom Regexps]`
- `Data` reads/writes `obsidian_to_anki_data.json` for incremental sync (SHA256 file hashes skip unchanged files)
- `App.__init__` and `Config.__init__` have known FIXME initialization errors — fix these before adding features that depend on them
- The legacy monolithic `obsidian_to_anki.py` at the repo root is the original single-file version; the `obsidian_to_anki/` directory is the refactored package

## Key Data Flow

```
.md file → file.scan_file() → note.Note.parse() → anki_connect.invoke() → Anki DB
                                                                         ↓
                                                          data.update_data_file() (hash cache)
```
