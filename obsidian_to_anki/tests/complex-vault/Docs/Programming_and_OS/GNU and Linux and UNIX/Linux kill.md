---
summary: Kills a process through the PID.
type: note/tool
headings:
  - "[[#Syntax]]"
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Tuesday, February 3rd 2026, 10:24:03 am
function_of:
  - "[[Linux Processes]]"
  - "[[Linux util-linux]]"
template: "[[base_note_template]]"
template-version: 1.0.1
same:
  - "[[Linux pkill]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Syntax
```shell
kill [OPTIONS] [PID]...
```

### Options:
- `1` (`HUP`) - Reload a process.
- `9` (`KILL`) - Kill a process.
- `15` (`TERM`) - Gracefully stop a process.
- `-l` (list) - Gets a list of all signals

### Signal Specification 
1. Using number (e.g., `-1` or `-s 1`).
2. Using the “SIG” prefix (e.g., `-SIGHUP` or `-s SIGHUP`).
3. Without the “SIG” prefix (e.g., `-HUP` or `-s HUP`).

### Example
```shell
kill -1 PID_NUMBER
kill -SIGHUP PID_NUMBER
kill -HUP PID_NUMBER
```