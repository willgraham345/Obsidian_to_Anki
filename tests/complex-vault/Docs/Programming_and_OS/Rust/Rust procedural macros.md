---
summary: "Has three types: attribute-like macros, function-like macros, and custom derive macros."
headings: ["[[#Concepts of Note]]", "[[#Media]]"]
type: note/concept
concepts: ["[[Rust attributes]]", "[[Rust derive macros]]"]
concept_of: ["[[Rust macros]]"]
date created: Friday, April 18th 2025, 11:13:46 am
date modified: Monday, August 18th 2025, 3:15:48 pm
used_by: ["[[Rust Functions]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
- Custom `#derive`
- Similar to attributes
	- macros that define custom attributes usable on any item
- Function-like macros that look like function calls but operate on the tokens specified as their argument

## Concepts of Note
󰙎  Procedural macros ;;; Has three types: attribute-like macros, function-like macros, and custom derive macros. = #lang/macros/procedural 
<!--ID: 1758253288646-->


### Attribute-like macros
### Function-like macros
Macros can take in a variable number of arguments, which is not possible with functions.
- ![[Rust macros#Macros vs Functions]]

### Custom derive macros
See [[Rust derive macros]]

## Media
[Macros - The Rust Programming Language](https://doc.rust-lang.org/stable/book/ch20-05-macros.html)
