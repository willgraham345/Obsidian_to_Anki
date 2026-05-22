---
summary: Change the file or directory mpermissions. Controls read, write, execute (rwx) access. Defines access for the user (u), group (g), and others (o). Allows for fine-grained security control.
type: note/tool
headings: ["[[#Concepts of Note]]", "[[#Concepts of Note]]"]
similar: ["[[Linux chgrp]]", "[[Linux chown]]", "[[Linux usermod]]"]
date created: Thursday, January 22nd 2026, 3:30:59 pm
date modified: Friday, January 23rd 2026, 10:30:32 am
template: "[[base_note_template]]"
template-version: 1.0.1
used_by: ["[[Linux Cybersecurity]]", "[[Linux Security]]"]
uses: ["[[Linux File Permissions]]", "[[Linux File System Types]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
### Common situations for each access group
`644` -> Owner gets `r+w`, everyone else gets read
``

### Octal notation
Adding:
	`read` -> 4
	`write` -> 2
	`execute` -> 1

Sums:
	3 -> write and execute
	5 -> Read and execute
	6 -> Read and write
	7 -> Full permission

### User, group, others
- User -> Who owns the file
- Group -> Group that owns the file
- Others -> Everyone else


| Mode        | Owner | Group | Others | Typical use for scripts                                  |
| ----------- | ----- | ----- | ------ | -------------------------------------------------------- |
| 700 | rwx   | ---   | ---    | Private script (only you can run/edit).                  |
| 711 | rwx   | --x   | --x    | Executable/traverse only; contents not readable.         |
| 744 | rwx   | r--   | r--    | You edit & run; others can read (not execute).           |
| 750 | rwx   | r-x   | ---    | Team-only executable; hidden from others.                |
| 754 | rwx   | r-x   | r--    | Exec for group, read-only for others.                    |
| 755 | rwx   | r-x   | r-x    | Common: everyone can run, only you edit.                 |
| 775 | rwx   | rwx   | r-x    | Shared within a group (both owner & group can edit/run). |



