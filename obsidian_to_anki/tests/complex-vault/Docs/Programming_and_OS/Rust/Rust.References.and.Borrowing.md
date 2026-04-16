---
type: note
---
# Background
- A reference is like a pointer in that it's an address we can follow to access data stored within the address. 
- Unlike a pointer, a reference is guaranteed to point to a valid value of a particular type for the life of that reference.
- If we try and modify something while we are borrowing it, it will NOT let it work

## Example of Borrowing In a Function
```rust
fn main() {
    let s1 = String::from("hello");
    let len = calculate_length(&s1); // refers to s1, but does not own it -> value will not be dropped when the reference stopped being used
    println!("The length of '{}' is {}.", s1, len);
}

fn calculate_length(s: &String) -> usize {
    s.len()
}
```
- All the tuple code in the variable declaration and the function return value is gone. 
- We pass `&s1` into `calculate_length`, and take `&String` rather than `String`
	- ![[trpl04-05.svg]]

| Operation     | Operator |
| ------------- | -------- |
| Referencing   | `&`      |
| Dereferencing | `*`      |


