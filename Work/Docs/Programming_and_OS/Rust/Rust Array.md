---
summary: Every element must have the same type, and arrays have a fixed length at compile time. Useful for when you want data on the stack, and when you want to ensure you have a fixed number of elements.
type: note/concept
similar:
  - "[[Rust ]]"
concept_of:
  - "[[Rust DataTypes]]"
date created: Wednesday, January 8th 2025, 4:53:09 pm
date modified: Wednesday, January 8th 2025, 4:56:15 pm
associations:
  - "[[Rust slice]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
# Usage
```rust
fn main() {
	let a = [1, 2, 3, 4, 5];
}
```

## Accessing array elements
```rust
fn main() {
    let a = [1, 2, 3, 4, 5];
    let first = a[0];
    let second = a[1];
}
```