---
summary: Indications to the compiler when borrows are valid, when resources can be freed, and when variables are created/destroyed.
headings: ["[[#Concepts of Note]]", "[[#Usage]]"]
type: note/concept
concepts: ["[[Rust Ownership]]", "[[Rust Visibility]]"]
associations: ["[[Rust Variables]]"]
concept_of: ["[[Rust]]"]
date created: Tuesday, April 29th 2025, 4:38:00 pm
date modified: Thursday, May 22nd 2025, 3:26:31 pm
keywords: ["[[Rust type]]"]
tags: [term/rust]
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- [I] RAII = Resource acquisition is initialization. When object goes out of scope, destructor is called and owned resources are freed = #term/rust 
![[Rust impl#^fa0a60]]
![[Rust impl#Inherent implementations]]

## Usage
### Examples
```rust
// raii.rs
fn create_box() {
    // Allocate an integer on the heap
    let _box1 = Box::new(3i32);

    // `_box1` is destroyed here, and memory gets freed
}
```