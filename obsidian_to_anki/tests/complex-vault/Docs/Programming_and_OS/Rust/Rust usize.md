---
summary: A primitive integer type used for indexing collections (arrays and vectors). The size (memory footprint) of this primitive is how many bytes it takes to store reference to any location in memory based on the system architecture. On a 32-bit structure, a pointer is 4 bytes. On a 64-bit structure, a pointer is 8 bytes. It ensures your code is portable into a variety of embedded systems.
headings: ["[[#Flashcards]]"]
type: note/keyword
similar: ["[[Rust isize]]"]
associations: ["[[Rust slice]]"]
date created: Friday, May 30th 2025, 6:59:03 am
date modified: Thursday, October 9th 2025, 3:36:45 pm
template: "[[base_note_template]]"
template-version: 1.0.0
used_by: ["[[Rust Array]]", "[[Rust Enumerate]]", "[[Rust References and Pointers]]", "[[Rust Vec]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[usize - Rust](https://doc.rust-lang.org/nightly/std/primitive.usize.html)

## Concepts of Note
- The size of this primitive is how many bytes it takes to reference any location in memory. For example, on a 32 bit target, this is 4 bytes and on a 64 bit target, this is 8 bytes.

### Use cases
- `usize`/`isize` are used to address every byte of memory in your machine. They only change size depending on the width of the memory addresses on your machine. 
- `usize` has a **value** that is different from it's size. The value can be calculated and used 

## Flashcards
󰠗  When would you want to use `usize`? ;; During indexing, size, and count operations that relate to memory. = #lang/memory 
󰠗  Explain everything going on when you index like this: `x[0]`. ;; The `x` is indexed with the `std::ops::Index` trait, using a `usize` value of `0`. 
