---
summary:
type: note/library
headings:
  - "[[#Concepts of Note]]"
implements:
  - "[[Linux syscall]]"
similar:
date created: Thursday, August 14th 2025, 12:40:08 pm
date modified: Friday, March 6th 2026, 3:42:10 pm
item_of:
tags:
  - cs/linux/process/file_descriptor
  - cs/posix
template:
template-version:
used_by:
  - "[[poll.puml]]"
  - "[[POSIX]]"
  - "[[UNIX File Descriptor]]"
  - "[[Linux execvp]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
󰙎  unistd.h ;;; The header file which defines the entire POSIX operating system API. Made largely of system call wrapper functions (fork, pipe) and I/O primitives (read, write, close). Generally less portable, as they're specific to posix compliant stuff. =  
<!--ID: 1758253289210-->


[unistd.h - Wikipedia](https://en.wikipedia.org/wiki/Unistd.h)

## Concepts of Note
- Different from [[C stdio|Cpp stdio]], as `<stdio.h>` abstracts much of the OS-related stuff. The `<unistd.h>` is directly tied to POSIX-compliant machines.
