---
summary: Variables set by your Linux environment
type: note/item
headings: ["[[#Properties]]"]
members:
functions: ["[[Linux environment variables#[[Linux export]]]]"]
variables: ["[[Linux environment variables#LD_LIBRARY_PATH]]"]
implements: ["[[CS Environments]]"]
date created: Monday, November 25th 2024, 5:44:50 pm
date modified: Thursday, January 29th 2026, 2:00:14 pm
template: "[[base_note_template]]"
template-version: 1.0.1
tools: ["[[Linux export]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background


## Properties

##### LD_LIBRARY_PATH
󰫧 :
- description: Used to by dynamic linker/loader to find shared libraries required by a program at runtime. Colon-separated list of directories that are searched before standard system library paths (`/lib` and `/usr/lib`)
	- Default state for this is unset in most Linux distributions.
󰫧 end:

### Tools/functions
##### [[Linux export]]