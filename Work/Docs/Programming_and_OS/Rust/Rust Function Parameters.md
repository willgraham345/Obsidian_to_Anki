---
summary: Parameters for functions, which must have a declared type in each parameter.
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Thursday, October 24th 2024, 3:40:00 pm
type: note/component
concept_of:
  - "[[Rust Functions]]"
---
# Background
We can define parameters which are special variables that are part of the function's signature. 
- Parameters *must* have a declared type in each parameter.

# Usage
## Basic
```rust
fn another_function(x : i32, unit_label: char) {
	println("The value of x is: {x}{unit_label}");
}
```