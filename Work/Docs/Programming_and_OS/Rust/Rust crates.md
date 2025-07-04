---
summary: Crates are units of compilation and linking. They also have versioning, distribution, and runtime loading. A crate contains a tree of nested module scopes. The top level of the tree is a module that is anonymous (from the point of view of paths within the module) and any item within a crate has a canonical module path denoting its location within the crate's module tree.
type: note/concept
concepts:
  - "[[Rust modules]]"
components:
  - "[[Rust crate_name]]"
associations:
  - "[[Rust source files]]"
  - "[[Rust Items]]"
concept_of:
  - "[[Rust Build Pipeline]]"
date created: Friday, March 21st 2025, 10:24:32 am
date modified: Tuesday, April 29th 2025, 4:33:53 pm
tags:
  - term/rust
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of note
A crate with a `main` function can be compiled to an executable
- [I] Crate = Unit of compilation/linking. Contains a tree of nested module scopes, where level of the tree is a module that is anonymous to any item within a crate. = #term/rust 