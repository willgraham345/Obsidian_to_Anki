---
summary: Rules of thumb:<br>- `panic` is most useful for tests and unrecoverable errors, `unimplemented` is usually better<br>- `Option` type is great, with `unwrap` being used in prototyping, and `expect` used  more frequently.<br>- When there's a chance things can go wrong, use `Result`.<br>- The question mark operator is great for error handling.
headings:
  - "[[#Diagrams]]"
  - "[[#Usage]]"
type: note/workflow
uses:
  - "[[Rust std option]]"
  - "[[Rust std result]]"
date created: Wednesday, May 7th 2025, 11:20:29 am
date modified: Thursday, May 22nd 2025, 3:45:05 pm
keywords:
  - "[[Rust question mark operator]]"
workflow_of:
  - "[[Rust Control_Flow]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Diagrams
![[rust_error_handling.svg]]

## Usage

### Rust Result Usage
![[Rust std result#Usage]]

### Simple implementation in main
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

### Matching on different errors