---
summary: All data types have an alignment specified in bytes. The alignment of a type specifies what addresses are valid to store the value at.
headings: 
type: note/concept
implements: ["[[PT Discriminant]]"]
date created: Tuesday, July 1st 2025, 11:56:20 am
date modified: Tuesday, July 1st 2025, 11:58:04 am
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[repr(Rust) - The Rustonomicon](https://doc.rust-lang.org/nomicon/repr-rust.html)

- [p] `#[repr(u16)]` = Sets the data layout to be using `u16` for each discriminant. = #rust/data/layout
<!--ID: 1751434089973-->
