---
summary: All data types have an alignment specified in bytes. The alignment of a type specifies what addresses are valid to store the value at.
headings:
type: note/concept
implements: ["[[PT Discriminant]]"]
concept_of: ["[[Rust]]"]
date created: Tuesday, July 1st 2025, 11:56:20 am
date modified: Saturday, November 8th 2025, 12:03:55 pm
template:
template-version:
used_by: ["[[Rust enum]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[repr(Rust) - The Rustonomicon](https://doc.rust-lang.org/nomicon/repr-rust.html)

  `#[repr(u16)]` ;;; Sets the data layout to be using `u16` for each discriminant. This will format each `enum` to be grouped together as a `u16`. = #lang/memory/layout 
ID: 1751997628504


