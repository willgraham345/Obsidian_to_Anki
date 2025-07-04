---
summary: 
headings: 
type: 
date created: Tuesday, August 20th 2024, 2:05:35 pm
date modified: Monday, April 28th 2025, 12:58:24 pm
concept_of:
  - "[[Rust Structs]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Examples
- In the `User` struct definition we used the owned `String` type rather than the `&str` string slice type. 
- We did this so each instance of the struct owns all its own data and for that data to be valid as long as the entire struct is valid. 
- It's also possible for structs to store references to data owned by someone else. 
	- For us to do that, we need to know the use of *lifetimes*
		- If you try to store a reference in a struct without specifying lifetimes it won't work.

### Example of not working
```rust
struct User {
    active: bool,
    username: &str,
    email: &str,
    sign_in_count: u64,
}

fn main() {
    let user1 = User {
        active: true,
        username: "someusername123",
        email: "someone@example.com",
        sign_in_count: 1,
    };
}
```

#### Compiler's Complaints
```rust
$ cargo run
   Compiling structs v0.1.0 (file:///projects/structs)
error[E0106]: missing lifetime specifier
 --> src/main.rs:3:15
  |
3 |     username: &str,
  |               ^ expected named lifetime parameter
  |
help: consider introducing a named lifetime parameter
  |
1 ~ struct User<'a> {
2 |     active: bool,
3 ~     username: &'a str,
  |

error[E0106]: missing lifetime specifier
 --> src/main.rs:4:12
  |
4 |     email: &str,
  |            ^ expected named lifetime parameter
  |
help: consider introducing a named lifetime parameter
  |
1 ~ struct User<'a> {
2 |     active: bool,
3 |     username: &str,
4 ~     email: &'a str,
  |

For more information about this error, try `rustc --explain E0106`.
error: could not compile `structs` due to 2 previous errors

```