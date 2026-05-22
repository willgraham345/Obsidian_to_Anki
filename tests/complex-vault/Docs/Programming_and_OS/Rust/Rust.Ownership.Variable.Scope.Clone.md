---
type: note
---
# Background
### Variables and Data Interacting with Clone
#### Stack-Only Data: Copy
If we do want to deeply copy the heap data of the `String`, not just the stack data, we can use a common method called `clone`
```rust
let x = 5;
let y = x;
```
Integers are a known size at compile time and are stored entirely on the stack. There isn't much of a difference between this and a deeper copy. Calling `clone` wouldn't do anything different than the usual shallow copying. 

Rust has a special annotation called the `Copy` trait which can be placed on types that are stored on the stack. If a type implements the `Copy` trait, variables that use it do not move, but are trivially copied, making them still valid after assignment to another variable. 
