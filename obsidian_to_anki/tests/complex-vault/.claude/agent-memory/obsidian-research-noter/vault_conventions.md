---
name: vault conventions for technical reference notes
description: H2 heading choices, inline patterns, and link conventions observed in Docs/ notes
type: project
---

Technical reference notes in `Docs/` use a subset of `full_schema.md` headings. Most useful H2s for API/library notes:
- `## Concepts of Note` — key terms, related notes, brief orientation
- `## Usage` — function/method list, API surface
- `## Header Files` — per-header breakdown (common for C/networking notes)
- `## Data Structures` — struct field tables
- `## Domains and Socket Types` — constants/enums (naming varies by domain)
- `## Socket Options` — config values (use `variable_config_template` style)
- `## TCP Lifecycles` — process steps (use `process_template` ` start:` / ` end:` blocks)
- `## Non-Blocking I/O and Multiplexing` — comparison tables
- `## Error Handling` — errno table
- `## Flashcards` — `󰠗 question ;; answer` cards

Inline patterns (Third Schema):
- Term definition: `󰙎 term ;;; description`
- Code snippet:  `` `code` ;;; description ``
- Flashcard: `󰠗 question ;; answer`
- Always `;;;` (3) for terms/code, `;;` (2) for flashcards

Common recurring link targets in Networks_Signals_Protocols:
- `[[Networking socket]]` — parent concept
- `[[Network POSIX]]` — POSIX standardisation note
- `[[Networking UDP]]` — UDP protocol
- `[[TCP Protocol Suite]]` — TCP detail
- `[[OSI Transport Layer 4]]` — transport layer context
- `[[Networking DNS]]` — DNS resolution

Header file notes live in `Docs/Programming_and_OS/C/`:
- `[[C netinet|Linux netinet]]` — netinet/in.h
- `[[sys socket.h]]` — sys/socket.h (note exists by link name, may not have file)
- `[[sys un.h]]` — sys/un.h (same caveat)

**Why:** Derived from reading existing note front-matter and vault file structure during Berkeley Sockets note expansion.
**How to apply:** Use these heading choices and link targets when creating or expanding notes in Docs/Networks_Signals_Protocols/ or Docs/Programming_and_OS/C/.
