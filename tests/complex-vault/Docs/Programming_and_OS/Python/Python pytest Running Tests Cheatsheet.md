---
summary:
type: note/process
headings:
  - "[[#Usage]]"
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Wednesday, February 11th 2026, 1:21:58 pm
tags: []
template: "[[base_note_template]]"
template-version: 1.0.1
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
```shell
pytest [options] [file_or_dir] [file_or_dir] ...
```

During test execution, any output sent to `stdout` and `stderr` is captured. To show this, 

## Usage


### Output Options
| Option | Description |
| ---- | ---- |
| `--show-capture` | Shows output captured from `stdout`/`stderr` |
| `-s` | Shows stdout and stderr |
| `-x` | Stop after first failure |
| `-k "expression"` | Only run tests that match expression (and fixtures) |
| `-rs` | Show extra summary info for SKIPPED |
| `-r chars` | Show extra test summary info as specified by chars: (f)ailed, (E)error, (s)skipped, (x)failed, (X)passed, (w)pytest-warnings (p)passed, (P)passed with output, (a)all except pP. |
| `-v` | Verbose |
| `-q, --quiet` | Less verbose |
| `-l, --showlocals` | Show local variables in tracebacks |

### Traceback Options
| Option | Description |
| ---- | ---- |
| `--tb=short` | Makes a shorter traceback |
| `--tb=line` | Makes an even shorter traceback |
|  |  |
