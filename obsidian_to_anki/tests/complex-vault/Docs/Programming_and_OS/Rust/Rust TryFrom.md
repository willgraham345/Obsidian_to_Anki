---
summary: A trait for type conversions that may fail in a controlled way. Reciprocal of `TryInto`.<br><br>Should be used when you're converting raw input into more structure, parsing, and domain-specific contraints (i.e. Age of a person can't be less than zero).
headings: ["[[#Examples]]", "[[#Media]]", "[[#Usage]]"]
type: note/keyword
same: ["[[Rust TryInto]]"]
similar: ["[[Rust From]]"]
concept_of: ["[[Rust type conversions]]"]
date created: Thursday, May 29th 2025, 11:35:53 am
date modified: Friday, June 27th 2025, 2:16:04 pm
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

[TryFrom in std::convert - Rust](https://doc.rust-lang.org/std/convert/trait.TryFrom.html)

## Usage
  `impl TryFrom<SourceType> for TargetType { ... }` ;;; Defines the trait for a fallible conversion between types, which returns a `Result<Self, Self::Error>` = #lang/data/casting/impl ^7272f1 
ID: 1751997628055




## Examples

[TryFrom and TryInto - Rust By Example](https://doc.rust-lang.org/rust-by-example/conversion/try_from_try_into.html)
```cpp
use std::convert::TryFrom;
use std::convert::TryInto;

#[derive(Debug, PartialEq)]
struct EvenNumber(i32);

impl TryFrom<i32> for EvenNumber {
    type Error = ();

    fn try_from(value: i32) -> Result<Self, Self::Error> {
        if value % 2 == 0 {
            Ok(EvenNumber(value))
        } else {
            Err(())
        }
    }
}
```
