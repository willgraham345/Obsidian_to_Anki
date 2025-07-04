---
summary: A pointer type that uniquely owns a heap allocation of type `T`.
headings: ["[[#Concepts of Note]]", "[[#Usage]]"]
type: note/class
associations: ["[[Rust ThinBox]]"]
date created: Friday, June 27th 2025, 5:16:34 pm
date modified: Friday, June 27th 2025, 5:19:43 pm
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[std::boxed - Rust](https://doc.rust-lang.org/std/boxed/index.html)

## Concepts of Note
Boxes provide ownership for allocation, and drop their contents when they go out of scope. Boxes also ensure that they never allocate more than `isize::MAX` bytes.

## Usage
- [p] `let boxed: Box<u8>` `=` `Box::new(val);` = Moves a value from the stack to the heap by creating a `Box` = #code/rust/ownership 
<!--ID: 1751434090610-->
