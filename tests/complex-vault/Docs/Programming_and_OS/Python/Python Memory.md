---
summary: Python's interpreter manages the allocation/deallocation of memory, by managing a private heap where all objects and data structures are located.
headings:
  - "[[#Concepts of Note]]"
type: note/concept
implements:
  - "[[CS Embedded Computing]]"
  - "[[CS Memory]]"
concept_of:
  - "[[Python]]"
date created: Thursday, December 11th 2025, 10:17:19 am
date modified: Thursday, December 11th 2025, 10:29:02 am
template: "[[base_note_template]]"
template-version: 1.0.1
used_by:
  - "[[Python Embedded]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
### Private Heap
- Python has a heap of all Python objects and data structures.
- Ensured internally by the python memory manager.
- At the lowest level, a raw memory allocator ensures there's enough room in the private heap for storing all python-related data. This interacts with the memory manager of the OS.
- The user has no control over this--the [[Python Interpreter]] is in charge.