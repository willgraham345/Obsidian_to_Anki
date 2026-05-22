---
summary: Every element must have the same type, and arrays have a fixed length at compile time. Useful for when you want data on the stack, and when you want to ensure you have a fixed number of elements.
headings: ["[[#Concepts of Note]]", "[[#Usage]]"]
type: note/concept
implements: ["[[Rust AsMut]]", "[[Rust AsRef]]", "[[Rust Borrow]]", "[[Rust BorrowMut]]", "[[Rust Clone]]", "[[Rust Copy]]", "[[Rust Debug]]", "[[Rust Hash]]", "[[Rust PartialEq]]", "[[Rust PartialOrd]]", "[[Rust std IntoIterator]]"]
similar: ["[[Rust ]]"]
associations: ["[[Rust slice]]"]
date created: Wednesday, January 8th 2025, 4:53:09 pm
date modified: Friday, September 19th 2025, 1:30:00 pm
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
󰠗  What conditions/constraints does `expr` need to manipulate to be used as `[expr; N]`? ;; `expr` must either be a `const` value, or implement the `Copy` trait. = #lang/data/array 
<!--ID: 1759154339857-->

  `let mut a: [i32; 3] ``=`` [0;3]` ;;; Create a mutable array `a` with type `i32`, initialized to `[0, 0, 0]` = #lang/data/array 
<!--ID: 1759154339861-->

  `let b:[expr; N]` ;;; Declare an array `b`, with `expr` copied `N` times. = #lang/data/array 
<!--ID: 1759154339865-->


## Usage

```rust
fn main() {
	let a = [1, 2, 3, 4, 5];
}
```

### Accessing array elements
```rust
fn main() {
    let a = [1, 2, 3, 4, 5];
    let first = a[0];
    let second = a[1];
}
```
