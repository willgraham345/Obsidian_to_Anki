---
summary: Statements perform an action and return a value. Expressions evaluate to a resultant example.
date created: Tuesday, August 20th 2024, 2:05:35 pm
date modified: Thursday, October 24th 2024, 3:37:32 pm
type: note
---
# Background
- Statements are instructions that perform some action and do not return a value.
- Expressions evaluate to a resultant value. Let’s look at some examples.

## Example
Statement
```rust
fn main() {
    let y = 6;
}
```
- Function definitions are also statements
Expression
```rust
fn main() {
    let y = {
        let x = 3;
        x + 1
    };

    println!("The value of y is: {y}");
}
```
- In other languages, you can write `x = y = 6`, but not in Rust. 
- `x+1` doesn't have a semicolon at the end. Expressions do not include ending semicolons. If you add a semicolon to the end of an expression, you turn it into a statement, and it will not then return a value. 