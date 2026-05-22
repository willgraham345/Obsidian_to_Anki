---
summary: Contiguous growable array type. Slices of vectors are read only objects,
headings: ["[[#Media]]"]
type: note/item
date created: Friday, April 18th 2025, 11:27:50 am
date modified: Wednesday, October 8th 2025, 1:48:30 pm
function_of: ["[[Rust macros]]"]
item_of: ["[[Rust std collections]]", "[[Rust std]]", "[[Rust Variables and Type System]]"]
tags: [lang/meta/attributes/macros, lang/data/vector]
template: "[[base_note_template]]"
template-version: 1.0.0
---

 
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Usage
  `let v ``=`` Vec::new([1, 2, 3])` ;;; Create a rust vector `v` of type `i32` with values `[1, 2, 3]`. = #lang/data/vector 
<!--ID: 1759154339800-->

  `let v ``=`` Vec::<Box<dyn A>>::new(b)` ;;; Create a rust vector `v` of values that implement trait `A` with values `b`. = #lang/data/vector 
<!--ID: 1759154339805-->

## Media
[Vec in std  vec - Rust](https://doc.rust-lang.org/std/vec/struct.Vec.html)
[std  vec - Rust](https://doc.rust-lang.org/std/vec/)
