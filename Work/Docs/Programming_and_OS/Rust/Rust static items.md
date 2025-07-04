---
summary: Similar to a constant, except that it represents an allocated object in the program that is initialized with the init expression. All references and raw pointers to the static refer to the same object.<br><br>Static items have the `static` lifetime
headings: ["[[#Concepts of Note]]"]
type: note/component
similar: ["[[Rust constant items]]"]
date created: Wednesday, May 7th 2025, 12:54:52 pm
date modified: Wednesday, May 7th 2025, 12:58:57 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- [I] [Mutable statics](https://doc.rust-lang.org/reference/items/static-items.html#statics--generics) = Allowed to be modified by the program. An `unsafe` block is required when reading/writing a mutable static variable.

- [Statics and Generics](https://doc.rust-lang.org/reference/items/static-items.html#statics--generics)