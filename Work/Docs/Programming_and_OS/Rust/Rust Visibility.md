---
summary: Which things are and are not "visible" to the outside modules/crates/functions.
headings: 
type: note/concept
concept_of: ["[[Rust Scoping Rules]]", "[[Rust]]"]
date created: Monday, April 28th 2025, 12:59:14 pm
date modified: Tuesday, April 29th 2025, 4:36:52 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
- [p] `pub(super)` = Says that whatever item follows is only visible to the parent module, and nothing further.