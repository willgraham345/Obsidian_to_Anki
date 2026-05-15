---
summary: Linux lets you break down root permissions into smaller more manageable sections. A series of C preprocessor macros which define what capabilities the process can or should have when running on the machine. The capabilities manual page details what they perform. Capabilities are defined in <linux/capability.h>.
type: note/concept
headings: ["[[#Concepts of Note]]"]
concept_of: ["[[Linux Processes]]"]
date created: Tuesday, January 6th 2026, 11:21:09 am
date modified: Tuesday, January 6th 2026, 12:12:02 pm
tags: [cs/linux, cs/linux/permissions, todo/refactor]
template: "[[base_note_template]]"
template-version: 1.0.1
tools: ["[[Linux getpcaps]]", "[[Linux setcap]]", "[[Linux SGID]]", "[[Linux SUID]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[Linux Capabilities: Setting and Modifying Permissions \| Baeldung on Linux](https://www.baeldung.com/linux/set-modify-capability-permissions) 

## Concepts of Note
Every process has several "sets" of capabilities
󰙎 Permitted capabilities ;; The "master list" of capabilities the process is allowed to use
󰙎 Effective capabilities ;; The capabilities the process is *actually using* right now to pass kernel security checks
󰙎 Inheritable capabilities ;; Capabilities (permissions) that can be passed down to child processes.