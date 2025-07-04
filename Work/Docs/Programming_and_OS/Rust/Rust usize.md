---
summary: Unsigned integer datatype, determined by how many bytes it takes up in size.
headings: 
type: note/keyword
associations:
  - "[[Rust slice]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`
# Additional Background
[usize - Rust](https://doc.rust-lang.org/nightly/std/primitive.usize.html)
## Concepts of Note
The size of this primitive is how many bytes it takes to reference any location in memory. For example, on a 32 bit target, this is 4 bytes and on a 64 bit target, this is 8 bytes.