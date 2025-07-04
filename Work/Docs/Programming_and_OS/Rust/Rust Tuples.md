---
summary: General way of grouping together a number of values with a variety of types into one compound type. Tuples have a fixed length, and each position in the tuple has a type.
type: note/concept
similar: ["[[Rust Structs]]"]
concept_of: ["[[Rust DataTypes]]"]
date created: Wednesday, January 8th 2025, 4:51:43 pm
date modified: Wednesday, January 8th 2025, 4:53:01 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
# Usage
```rust
let tup: (i32, i64, u8) = (500, 6.4, 1); //declaration and initializatino
let (x, y, z) = tup; // get individual value out of a tuple
```

## Accessing individual elements
```rust
fn main() { 
	let x: (i32, f64, u8) = (500, 6.4, 1);
	let five_hundred = x.0;
	let six_point_four = x.1;
	let one = x.2;
}
```
