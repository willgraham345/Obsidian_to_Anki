---
summary: Macros with the `macro_rules!` at the front. Allows you to write control structures that take expressions, compare result to patterns, and running code associated with that pattern.
headings:
  - "[[#Concepts of Note]]"
type: note/concept
date created: Tuesday, April 22nd 2025, 11:55:25 am
date modified: Tuesday, April 22nd 2025, 11:57:28 am
concept_of:
  - "[[Rust macros]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- Similar to [[Rust match]] statements (control structures that take expression, and compare result to patterns, running code associated with that pattern)
- Compare a value to patterns associated with code. The *value* is the literal rust source code passed to the macro, the patterns are compared with the structure of that source code.

## Example
```
#[macro_export]
macro_rules! vec {
    ( $( $x:expr ),* ) => {
        {
            let mut temp_vec = Vec::new();
            $(
                temp_vec.push($x);
            )*
            temp_vec
        }
    };
}
```
- `#[macro_export]` signifies that the macro should be made available wherever the crate in which the macro is defined is brought into scope.
- 