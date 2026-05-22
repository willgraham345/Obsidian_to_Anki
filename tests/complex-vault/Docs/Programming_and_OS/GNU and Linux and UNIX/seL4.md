---
summary: Highly assured and fast operating system kernel. Relies on a mathematical proof that it behaves exactly as specified, enforcing strong boundaries with high performance.
headings:
  - "[[#Concepts of Note]]"
type: note/system
date created: Tuesday, December 2nd 2025, 10:24:00 am
date modified: Tuesday, December 2nd 2025, 10:24:48 am
template: "[[base_note_template]]"
template-version: 1.0.0
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note

Accordingly, seL4 supports only the core primitives that need to run at a high privilege:

- Threads
- Address spaces
- Inter-process communication (IPC)
- Notifications  
- Device primitives
- Capability spaces

seL4 does not provide many things normally expected from a full-featured OS, such as:

- Memory management
- Synchronization
- Drivers
- File System
- Loadable Executables