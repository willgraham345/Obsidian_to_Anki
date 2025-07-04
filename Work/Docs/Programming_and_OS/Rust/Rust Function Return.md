---
summary: In Rust, the return value of a function is synonymous with the value of the final expression in the block of the body of a function. You can return early from a function by using the `return` keyword and specifying a value, but most functions return the last expression implicitly.
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Thursday, October 24th 2024, 3:47:26 pm
type: note
concept_of:
  - "[[Rust Functions]]"
---
# Usage

## Example Return a Value with an Expression
```rust
fn five() -> i32 {
    5
}

fn main() {
    let x = five();

    println!("The value of x is: {x}");
}
```

## Example Wrong Return Using a Statement
```rust
fn main() {
    let x = plus_one(5);

    println!("The value of x is: {x}");
}

fn plus_one(x: i32) -> i32 {
    x + 1;
}
```
- `x+1;` turns it into a statement, and therefore into an incompatible thing. 