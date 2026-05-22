---
summary: 'Similar to traditional monolithic operating systems, microkernels place as much OS functionality as possible in user-level processes called "servers" instead of inside the kernel. '
headings:
  - "[[#Concepts of Note]]"
type: note/system
date created: Tuesday, December 2nd 2025, 10:21:49 am
date modified: Tuesday, December 2nd 2025, 10:23:26 am
template: "[[base_note_template]]"
template-version: 1.0.0
implementations:
  - "[[seL4]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
When apps or servers want to access the services provided by a server, they make the request using IPC. (reduces privilege of the OS.