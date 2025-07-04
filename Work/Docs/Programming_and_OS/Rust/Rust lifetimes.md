---
summary: Rust lifetimes are a construct the compiler uses to ensure all references can borrow what they reference. Put simply, making sure that references can return what they're referencing.
headings: ["[[#Concepts of Note]]", "[[#Syntax]]", "[[#Usage]]"]
type: note/concept
classes: ["[[Rust static lifetime]]"]
concepts: ["[[Rust lifetime elision]]"]
concept_of: ["[[Rust Ownership]]"]
date created: Tuesday, April 29th 2025, 4:43:44 pm
date modified: Friday, June 27th 2025, 2:42:29 pm
tags: [term/rust]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
are are are are are are are are are are are are are are are are are are are are are are are are are are are are are are are - [I] Generic lifetime annotations (lifetimes) = Adding specific lifetime annotations into the code, to help the compiler and borrow checker know when things can be released. = #term/rust 
```rust
let a: u8 = 5;
let b: &u8 = &5
```
- Rust lifetimes are to make sure that `a` will "outlive" `b`.
	- If `b` is alive for longer than `a`, there's a chance that the underlying data can't be returned.

### Default lifetimes
- Rust tries to make it easier for us to use it, so it omits "default" lifetimes. This is covered more in [[Rust lifetime elision]]

## Usage
- [p] `foo<'a>` = Implements lifetime `'a` on `foo`. = #code/rust/scoping/lifetimes
<!--ID: 1751434090533-->


## Syntax
### Explicit Annotation (Generic lifetime annotation)
```rust
// `print_refs` takes two references to `i32` which have different
// lifetimes `'a` and `'b`. These two lifetimes must both be at
// least as long as the function `print_refs`.
fn print_refs<'a, 'b>(x: &'a i32, y: &'b i32) {
    println!("x is {} and y is {}", x, y);
}

// A function which takes no arguments, but has a lifetime parameter `'a`.
fn failed_borrow<'a>() {
    let _x = 12;

    // ERROR: `_x` does not live long enough
    let _y: &'a i32 = &_x;
    // Attempting to use the lifetime `'a` as an explicit type annotation 
    // inside the function will fail because the lifetime of `&_x` is shorter
    // than that of `_y`. A short lifetime cannot be coerced into a longer one.
}

fn main() {
    // Create variables to be borrowed below.
    let (four, nine) = (4, 9);
    
    // Borrows (`&`) of both variables are passed into the function.
    print_refs(&four, &nine);
    // Any input which is borrowed must outlive the borrower. 
    // In other words, the lifetime of `four` and `nine` must 
    // be longer than that of `print_refs`.
    
    failed_borrow();
    // `failed_borrow` contains no references to force `'a` to be 
    // longer than the lifetime of the function, but `'a` is longer.
    // Because the lifetime is never constrained, it defaults to `'static`.
}
```