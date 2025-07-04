---
type: note
---
# Background
 - Rust will not create two mutable references to `s` will fail within the same scope.
	- Rust can prevent data races at compile time.
	- To get around this, you can use curly brackets to create a new scope, allowing for multiple mutable references (just not simultaneous ones)
- You also cannot have a mutable reference while we have an immutable one to the same value.
	- Users of an immutable reference doesn't expect the value to suddenly change out from under them. 
- A reference's scope starts from where it is introduced and continues through the last time that reference is used. 

# Usage
## Mutable Reference in a Function
```rust
fn main() {
    let mut s = String::from("hello");

    change(&mut s); //You can only create ONE mutable reference to a value
}

fn change(some_string: &mut String) {
    some_string.push_str(", world");
}
```
### Creating Multiple Non-simultaneous Mutable References
```rust
    let mut s = String::from("hello");
    {
        let r1 = &mut s;
    } // r1 goes out of scope here, so we can make a new reference with no problems.
    let r2 = &mut s;
```