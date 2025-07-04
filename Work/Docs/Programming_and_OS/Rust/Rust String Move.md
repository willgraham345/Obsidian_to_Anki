---
summary: Strings in rust have a special function Move, which is called when you assign data from one string to another. This can raise compile-time errors, typically because there are issues from
type: note/function
date created: Tuesday, August 20th 2024, 2:05:35 pm
date modified: Thursday, January 9th 2025, 9:30:13 am
---


```rust
let s1 = String::from("hello");
let s2 = s1;
```
- When we assign `s1` to `s2`, the `String` data is copied
	- This means that we copied the pointer, the length, and the capacity that are on the stack.
- There is an issue with this. When `s1` and `s2` go out of scope, they will try to free the same memory. This is known as a *double free* error and is one of the memory safety bugs.
	- To ensure memory safety, Rust considers `s1` as no longer valid. 
		- If you try and run it, you'll see this:
```rust
$ cargo run
   Compiling ownership v0.1.0 (file:///projects/ownership)
error[E0382]: borrow of moved value: `s1`
 --> src/main.rs:5:28
  |
2 |     let s1 = String::from("hello");
  |         -- move occurs because `s1` has type `String`, which does not implement the `Copy` trait
3 |     let s2 = s1;G
  |              -- value moved here
4 |
5 |     println!("{}, world!", s1);
  |                            ^^ value borrowed here after move
  |
  = note: this error originates in the macro `$crate::format_args_nl` which comes from the expansion of the macro `println` (in Nightly builds, run with -Z macro-backtrace for more info)
help: consider cloning the value if the performance cost is acceptable
  |
3 |     let s2 = s1.clone();
  |                ++++++++

For more information about this error, try `rustc --explain E0382`.
error: could not compile `ownership` due to previous error
```

Instead, we call this operation a *move*. We'd say that `s1` was *moved* into `s2`
