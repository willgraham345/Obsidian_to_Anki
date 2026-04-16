---
summary: A crate which provides a `quote!` macro, which turns Rust syntax tree data into tokens of source code
headings: ["[[#Concepts of Note]]"]
type: note/item
date created: Tuesday, September 2nd 2025, 12:26:36 pm
date modified: Tuesday, September 2nd 2025, 12:29:29 pm
used_by: ["[[Rust syn DeriveInput]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[quote in quote - Rust](https://docs.rs/quote/latest/quote/macro.quote.html)

## Concepts of Note

- `#var` is var syntax interpolation. Typically means variable `var`
- Requires a type to implement the `ToTokens` trait.