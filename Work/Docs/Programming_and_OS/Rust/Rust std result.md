---
summary: Error handling type. An enum containing two variants describing "Ok" and "Error". Results must be used.
headings:
  - "[[#Concepts of Note]]"
  - "[[#Examples]]"
  - "[[#Usage]]"
type: note/class
associations:
  - "[[Rust Enum Generics]]"
  - "[[Rust std option]]"
class_of:
  - "[[Rust std]]"
date created: Friday, April 4th 2025, 12:18:04 pm
date modified: Friday, June 27th 2025, 4:27:03 pm
used_by:
  - "[[Rust error handling]]"
uses:
  - "[[Rust match]]"
  - "[[Rust question mark operator]]"
  - "[[Rust std error]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- Panic typically leaves without any kind of a helpful error message 

- A ([[Set Theory#^3fb4e7 |sum type]]), similar to all other enums in Rust 

### Mapping
- We generally want to return the error to the caller. Using `map`, `and_then` and other combinations contain complete listings
- You don't technically need a match statement. The match statement provides branch logic, typically used for logging, recovering, or transforming the data.

### Result vs Option
- Use Option when there is only one way your thing can fail, use Result when there are a variety of ways your thing can fail
	- Result can be thought of as a "generalized" option.

## Usage
[std  result - Rust](https://doc.rust-lang.org/std/result/)
- [p] `let trial_value` `=` `tryval()?; OK(T)` = A way to chain multiple Result statements together without writing match statements. The idea here is to chain multiple `?` statements and return `Ok(val)` at the end. = #code/rust/control_flow/result ^ddb0f2
<!--ID: 1751434090190-->

- [p] `OK(T) => other statements` = An Ok variant--which answers "did the result op work?")--and contains the success value `T`. `T` can be used later in statements. = #code/rust/control_flow/result 
<!--ID: 1751434090195-->

- [p] `Err(Error) => other statements` = An Error variant (did the result work?) which contains the failure value `Error`. This can be used to potentially return early (`return Err(e)`), or kick into something else.  = #code/rust/control_flow/result 
<!--ID: 1751434090199-->

```rust
enum Result<T, E> {
   Ok(T),
   Err(E),
}
```

## Examples
### Rust by Example
```rust
use std::num::ParseIntError;

// As with `Option`, we can use combinators such as `map()`.
// This function is otherwise identical to the one above and reads:
// Multiply if both values can be parsed from str, otherwise pass on the error.
fn multiply(first_number_str: &str, second_number_str: &str) -> Result<i32, ParseIntError> {
    first_number_str.parse::<i32>().and_then(|first_number| {
        second_number_str.parse::<i32>().map(|second_number| first_number * second_number)
    })
}

fn print(result: Result<i32, ParseIntError>) {
    match result {
        Ok(n)  => println!("n is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    // This still presents a reasonable answer.
    let twenty = multiply("10", "2");
    print(twenty);

    // The following now provides a much more helpful error message.
    let tt = multiply("t", "2");
    print(tt);
}
```

### ChatGPT
```rust 
fn parse_number(input: &str) -> Result<i32, std::num::parseIntError> {
	let num = input.parse()?; //Auto-propagate the error
	Ok(num) //returns result
}
```