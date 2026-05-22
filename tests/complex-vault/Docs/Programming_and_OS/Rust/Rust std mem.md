---
summary: Functions for dealing with memory. Size, alignment of types, initializing, and manipulating memory.
headings:
  - "[[#Flashcards]]"
  - "[[#Properties]]"
type: note/library/module
functions:
  - "[[#transmute_copy]]"
  - "[[#transmute]]"
date created: Monday, September 29th 2025, 10:04:02 pm
date modified: Monday, September 29th 2025, 10:29:06 pm
interfaces:
  - "[[Rust TransmuteFrom]]"
items:
  - "[[Rust Discriminant]]"
library_of:
  - "[[Rust std]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Properties

### Functions
#### transmute
- Reinterpret the bits of a value of one type as another type.

#### transmute_copy
- [transmute\_copy in std::mem - Rust](https://doc.rust-lang.org/std/mem/fn.transmute_copy.html)

## Flashcards
󰠗  What function in Rust is roughly equivalent to the Cpp `reinterpret_cast`? ;; Rust `std::mem::transmute` = #lang/memory #lang/data/casting 
<!--ID: 1759377309176-->
