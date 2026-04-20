---
summary: It can simplify code to mask all different errors with a single type of custom error.
headings:
  - "[[#Concepts of Note]]"
  - "[[#Workflows]]"
type: note/interface
similar:
  - "[[Rust anyhow Error]]"
date created: Friday, June 27th 2025, 4:27:29 pm
date modified: Tuesday, September 23rd 2025, 3:35:15 pm
used_by:
  - "[[Rust std result]]"
uses:
  - "[[Rust Debug]]"
  - "[[Rust Display]]"
associations:
  - "[[Rust Ok]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- Errors are in one of two camps:
	1. Handled programmatically (consumer inspects the error, internal structure needs to be exposed to a reasonable degree)
	2. The error is propagated and displayed to the user (The consumer doesn't expect the error beyond the `fmt::Display`, so internal structure can be encapsulated)

### Processes
### Writing a quick and easy error message
