---
summary: Computer security facility in the Linux kernel, allowing a process to make a one-way transition into a "secure" state where it cannot make any system calls except exit(), sigreturn(), read(), and write() to already-open file descriptors. This doesn't virtualize system resources, but isolates the process from them entirely.
headings:
type: note/concept
associations: ["[[Linux Kernel cgroups]]"]
concept_of: ["[[Linux]]"]
date created: Wednesday, October 8th 2025, 11:46:35 am
date modified: Wednesday, October 8th 2025, 11:48:37 am
item_of: ["[[Cybersecurity]]", "[[Linux Kernel]]"]
template: "[[base_note_template]]"
template-version: 1.0.0
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

[seccomp - Wikipedia](https://en.wikipedia.org/wiki/Seccomp)