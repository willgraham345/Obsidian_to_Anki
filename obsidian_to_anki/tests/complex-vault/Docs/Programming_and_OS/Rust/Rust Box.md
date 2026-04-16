---
summary: A pointer type that uniquely owns a heap allocation of type `T`.
type: note/class
headings:
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
implements:
  - "[[CS Dynamic dispatch]]"
associations:
  - "[[Rust Rc]]"
  - "[[Rust RefCell]]"
  - "[[Rust ThinBox]]"
date created: Friday, June 27th 2025, 5:16:34 pm
date modified: Tuesday, March 3rd 2026, 11:56:09 am
tags: [lang/data/ownership, lang/data/pointers/smart, lang/functions, lang/memory/heap, lang/memory/pointers]
template:
template-version:
used_by:
  - "[[Rust trait]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[std::boxed - Rust](https://doc.rust-lang.org/std/boxed/index.html)

## Concepts of Note
Boxes provide ownership for allocation, and drop their contents when they go out of scope. Boxes also ensure that they never allocate more than `isize::MAX` bytes.

## Usage
  `let boxed: Box<u8>` `=` `Box::new(val);` ;;; Moves a value from the stack to the heap by creating a `Box` =  
ID: 1751997628544

󰠗  What data type points to memory on the heap? ;; `Box` = 
<!--ID: 1758253288974-->


󰠗  How do you deal with a function which returns an object of unknown size? ;; Put the object into a `Box` (or other smart pointer) and return `Box<T>` =  
<!--ID: 1758253288981-->

