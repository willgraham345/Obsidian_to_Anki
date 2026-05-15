---
summary: 
date created: Tuesday, August 20th 2024, 2:05:35 pm
date modified: Thursday, October 24th 2024, 3:45:34 pm
type: note
---
# Background
- The `println!` macro will let us use specifiers to print our struct in a way that is useful for debugging.

# Usage
## Debug Trait
Adding a `Debug` trait and printing the `Rectangle` instance using debug formatting
- To add debug formatting, we need to opt into this by adding outer attribute `#[derive(Debug)]`
```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!("rect1 is {:?}", rect1);
}
```
`OUTPUT`
```shell
$ cargo run
   Compiling rectangles v0.1.0 (file:///projects/rectangles)
    Finished dev [unoptimized + debuginfo] target(s) in 0.48s
     Running `target/debug/rectangles`
rect1 is Rectangle { width: 30, height: 50 }
```

## Debug Macro
Using the `dbg!` macro we can print to `stderr` as opposed to `stdout` like `println!`
```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let scale = 2;
    let rect1 = Rectangle {
        width: dbg!(30 * scale),
        height: 50,
    };

    dbg!(&rect1);
}
```
`OUTPUT`
``` shell
$ cargo run
   Compiling rectangles v0.1.0 (file:///projects/rectangles)
    Finished dev [unoptimized + debuginfo] target(s) in 0.61s
     Running `target/debug/rectangles`
[src/main.rs:10] 30 * scale = 60
[src/main.rs:14] &rect1 = Rectangle {
    width: 60,
    height: 50,
}

```