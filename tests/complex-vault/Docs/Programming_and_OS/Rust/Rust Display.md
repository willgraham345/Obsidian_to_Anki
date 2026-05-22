---
summary: A trait which will automatically implement the `ToString` trait for the type as well. Similar to `Debug`, but meant for user-facing output.
headings:
  - "[[#Concepts of Note]]"
  - "[[#Examples]]"
  - "[[#null]]"
  - "[[#Properties]]"
  - "[[#Usage]]"
type: note/interface
similar:
  - "[[Rust Debug]]"
date created: Tuesday, September 23rd 2025, 3:35:29 pm
date modified: Tuesday, September 23rd 2025, 3:42:35 pm
interface_of:
  - "[[Rust std fmt]]"
item_of:
  - "[[Rust std fmt]]"
used_by:
  - "[[Rust std error]]"
methods:
  - "[[#fmt()]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- 

## Properties

### fmt()
- Formats the value using a given formatter. 
- Should return `Err` if and only if the provided `Formatter` returns `Err`. This is considered an infallible operation.
- See [[#Examples]]

## Usage

## Examples
```rust
use std::fmt;

struct Point {
    x: i32,
    y: i32,
}

impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}

let origin = Point { x: 0, y: 0 };

assert_eq!(format!("The origin is: {origin}"), "The origin is: (0, 0)");
```

