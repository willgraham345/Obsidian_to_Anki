# Test Fix Plan

**Status as of 2026-04-16**  
8 tests failing. Details below.

---

## Remaining Failures

### 1. `test_file.py::TestFile::test_scan_file`

**Error:** `AttributeError: 'File' object has no attribute 'target_deck'`

**Root cause:** The test mocks `setup_target_deck` and `setup_global_tags` so they don't actually set `self.target_deck` / `self.global_tags`. But `scan_file()` calls those via `_setup_scan()` then immediately uses `self.target_deck`.

**Fix needed (in test):** Add before `scan_file()`:
```python
file_instance.target_deck = "Default"
file_instance.global_tags = ""
```

---

### 2. `test_file.py::TestRegexFile::test_scan_file_regex`

**Error:** `assert [] == [12345]`

**Root cause:** File content is `<!--id:12345-->` but EMPTY_REGEXP is `r"^## \n(?:<!--)?ID: (\d+)..."` — doesn't match old `<!--id:-->` format. Also the TestRegexFile fixture EMPTY_REGEXP (line 287) has **no capture group** for the digit:
```python
globals.EMPTY_REGEXP = re.compile(r"^## \n(?:<!--)?" + re.escape("ID: ") + r"[\s\S]*?\n## ", re.MULTILINE)
```
`scan_file()` calls `int(match.group(1))` which would fail with `IndexError` once the regex actually matches.

**Fix needed:**
1. Update EMPTY_REGEXP in TestRegexFile fixture to add `(\d+)` capture group (same as TestFile fixture already has):
   ```python
   globals.EMPTY_REGEXP = re.compile(r"^## \n(?:<!--)?ID: (\d+)[\s\S]*?\n## ", re.MULTILINE)
   ```
2. Update `file_content` in the test from `<!--id:12345-->` to `## \nID: 12345\n## ` format.

---

### 3. `test_file.py::TestRegexFile::test_search`

**Error:** `TypeError: first argument...` (full error not yet captured)

**Root cause:** Likely related to `findignore` mock or `RegexNote` mock interaction. The test sets up `mock_findignore.side_effect` with 4 match lists, but it's unclear if `search()` calls `findignore` exactly 4 times. Need to run with `-v` to see the full traceback.

**Debugging needed:** Run `uv run pytest tests/test_file.py::TestRegexFile::test_search -v` to see full error.

**Suspected fix:** The `findignore` call signature or `re.compile(regexp)` step inside `search()` may be the issue. Also check that `file_instance.target_deck` and `file_instance.global_tags` are set.

---

### 4. `test_file.py::TestRegexFile::test_fix_newline_ids`

**Error:** AssertionError — result doesn't match expected

**Root cause:** `_drop_first_char` in `file.py` drops only ONE character from the match:
```python
@staticmethod
def _drop_first_char(m):
    return m.group()[1:]
```
For `\n\nID: 123`, drops `\n` → `\nID: 123` ✓  
For `\r\n\r\nID: 456`, drops `\r` → `\n\r\nID: 456` ✗ (expected `\r\nID: 456`)

The test expects double newlines to collapse to a single newline unit (preserving the newline *style*, `\r\n` or `\n`).

**Fix needed (in source `file.py`):** Change `_drop_first_char` to drop the first captured GROUP (which is `(\r\n|\r|\n)`), not just one character:
```python
@staticmethod
def _drop_first_char(m):
    first_newline = m.group(1)
    return m.group()[len(first_newline):]
```

---

### 5. `test_file.py::TestRegexFile::test_write_ids_regex`

**Error:**
```
Expected: string_insert(<MagicMock>, [(10, '\nID: 101\n'), (20, '\nID: 102\n')])
Actual:   string_insert('original content', <zip object>)
```

Two sub-issues:
- **Sub-issue A:** `file_instance.file` is referenced AFTER `write_ids()` was called, so it contains the mock return value, not `'original content'`. Same bug as was fixed in `TestFile::test_write_ids` — need to capture `original_file = file_instance.file` before calling `write_ids()`.
- **Sub-issue B:** `RegexFile.write_ids()` passes a `zip` object to `string_insert`, but the test expects a `list`. Either fix the source to use `list(zip(...))`, or adjust the test assertion.

**Fix needed:**
1. In test: `original_file = file_instance.file` before `write_ids()`; use `original_file` in assertion.
2. In source `file.py` (line ~393): change `zip(...)` to `list(zip(...))` in `RegexFile.write_ids()`.

---

### 6. `test_directory.py::TestDirectory::test_parse_requests_1`

**Error:** `StopIteration` — mock side_effect exhausted during nested `AnkiConnect.parse()` calls.

**Root cause:** `parse_requests_1()` calls `AnkiConnect.parse()` multiple times in a nested fashion:
- Outer call: `parse(note_ids_response)` → expected to return a list
- Inner call: `parse(each_item)` → expected to return card info
- The mock `side_effect` has values in the wrong format (strings, not lists), and the outer parse returns a string which is then iterated character-by-character, consuming all side_effect items.

**Fix needed (in test):** Redesign the `side_effect` so:
- First call to `parse()` (outer) returns a list (e.g., `[item1, item2]`)
- Subsequent calls (inner, per-item) return appropriate values

Need to read `parse_requests_1()` source in `directory.py` carefully to understand the call sequence, then build `side_effect` accordingly.

**Unresolved:** Full structure of nested calls not yet mapped out. Run with `-v` and check `directory.py::parse_requests_1` source to understand the call sequence.

---

### 7. `test_format_converter.py::TestFormatConverter::test_fix_image_src`

**Error:**
```
assert '<img alt="" src="image.png">>\n...' == '<img alt="" src="image.png">\n...'
```
Double `>>` — the `>` at the end of the original `<img>` tag is included in the replaced content PLUS the original `>` also remains.

**Root cause:** The test mocks `path_to_filename` to return `'<img alt="" src="image.png">'` (WITH closing `>`), but `IMAGE_REGEXP` match in `fix_image_src()` doesn't include the closing `>` in its match span. So when the match is replaced with the mock return value (which includes `>`), the original `>` also stays, giving `>>`.

**Fix needed (in test):** Remove trailing `>` from mock return values:
```python
mock_path_to_filename.side_effect = [
    '<img alt="" src="image.png"',
    '<img alt="" src="https://example.com/remote.jpg"'
]
```

OR check what `path_to_filename` actually returns (does it include `>` or not?), then align the mock accordingly.

---

### 8. `test_format_converter.py::TestFormatConverter::test_format_removes_paragraph_tags`

**Error:**
```
assert '<p>Multiple paragraphs</p>\n<p>Second paragraph</p>' == '<p>Multiple paragraphs</p><p>Second paragraph</p>'
```
Newline between paragraphs in actual output — the markdown parser inserts `\n` between `</p>` and `<p>`.

**Root cause:** The source fix (count `PARA_OPEN` == 1) is correct for preventing stripping, but the test assertion expects no newline between paragraphs. The markdown-to-HTML converter inserts a newline.

**Fix needed (in test):** Update the assertion to match actual markdown output with newline:
```python
assert result == "<p>Multiple paragraphs</p>\n<p>Second paragraph</p>"
```

---

## Summary Table

| # | Test | Fix location | Fix type |
|---|------|-------------|----------|
| 1 | TestFile::test_scan_file | test | Add `target_deck`/`global_tags` attrs |
| 2 | TestRegexFile::test_scan_file_regex | test (fixture + test content) | Add capture group to EMPTY_REGEXP; update file_content |
| 3 | TestRegexFile::test_search | test (TBD after debugging) | Unknown — needs investigation |
| 4 | TestRegexFile::test_fix_newline_ids | source `file.py` | Fix `_drop_first_char` to use group length |
| 5 | TestRegexFile::test_write_ids_regex | test + source | Capture `original_file`; use `list(zip(...))` |
| 6 | TestDirectory::test_parse_requests_1 | test | Redesign nested parse mock side_effect |
| 7 | TestFormatConverter::test_fix_image_src | test | Remove trailing `>` from mock return values |
| 8 | TestFormatConverter::test_format_removes_paragraph_tags | test | Update assertion to include `\n` between paragraphs |

---

## Files Already Fixed (Earlier Sessions)

- `src/obsidian_to_anki/anki_connect.py` — reordered parse() field checks
- `src/obsidian_to_anki/data.py` — fixed DATA_PATH `..` count
- `src/obsidian_to_anki/format_converter.py` — SOUND_REGEXP, CLOZE_REGEXP, para strip
- `src/obsidian_to_anki/app.py` — NOTE_REGEXP title consumption
- `src/obsidian_to_anki/file.py` — vault URL `group(1)`
- `src/obsidian_to_anki/note.py` — InlineNote tags, lstrip, added `parse()`
- `tests/test_utils.py` — ANKI_CLOZE_REGEXP, write_safe, contained_in, findignore, load_anki
- `tests/test_config.py` — removed wrong setdefault assertions
- `tests/test_app.py` — ArgumentParser mock, gen_regexp assertion, doubled side_effects
- `tests/test_file.py` (TestFile) — NOTE_REGEXP `.+?`, EMPTY_REGEXP capture group, scan_file content, write_ids original_file capture
- `tests/test_directory.py` — added os.getcwd/chdir/scandir mocks to 3 tests
