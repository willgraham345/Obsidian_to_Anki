---
summary: Rules of thumb:<br>- `panic` is most useful for tests and unrecoverable errors, `unimplemented` is usually better<br>- `Option` type is great, with `unwrap` being used in prototyping, and `expect` used  more frequently.<br>- When there's a chance things can go wrong, use `Result`.<br>- The question mark operator is great for error handling.
headings:
  - "[[#Concepts of Note]]"
  - "[[#Diagrams]]"
  - "[[#Usage]]"
  - "[[#Examples]]"
type: note/process
date created: Wednesday, May 7th 2025, 11:20:29 am
date modified: Tuesday, September 23rd 2025, 3:26:18 pm
keywords:
  - "[[Rust question mark operator]]"
uses:
  - "[[Rust std option]]"
  - "[[Rust std result]]"
process_of:
  - "[[Rust Control Flow]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
󰠗  What three traits does a defined error type need to implement? ;; `Debug, Display, Error` = #lang/control_flow/errors/error-handling #lang/control_flow/errors 
<!--ID: 1759154339851-->

Rules of thumb
- `panic!` for programming errors ("bugs")
- Best avoid `unwrap()` in production code
	- `unwrap()` converts a recoverable error into a `panic!()`. 
	- You can usually avoid `unwrap()`.

## Usage

### Rust Result Usage
![[Rust std result#Usage]]

### Written Error Type

## Examples
### Simple Error Matching
```rust
use std::fs::File;

fn main() {
    let greeting_file_result = File::open("hello.txt");

    let greeting_file = match greeting_file_result {
        Ok(file) => file,
        Err(error) => panic!("Problem opening the file: {error:?}"),
    };
}
```
- When the result is `Ok`, the code will return the inner value out of the `Ok` variant, and assign that to the `greeting_file`.
	- The other arm of the `match` handles case when we get `Err` value from `File::open`. In this case, we call `panic!`. This will panic no matter why it failed.

## Diagrams
![[rust_error_handling.svg | 500]]
