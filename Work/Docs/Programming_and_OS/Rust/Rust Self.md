---
summary: Keyword referring to the instance of the struct/enum being called. It references the current module and mark the receiver of a method.
headings: ["[[#Commands]]", "[[#Concepts of Note]]", "[[#Examples]]"]
type: note/keyword
date created: Friday, April 4th 2025, 1:44:05 pm
date modified: Tuesday, April 29th 2025, 3:18:46 pm
tags: [code/rust/ownership, term/rust]
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
### Self vs self
- [I] Self = refers to the current type being implemented/defined. It may be used in: trait definitions (refers to type implementing trait), in an impl (type being implemented), or in the definition of a struct/enum/union (refers to the type being defined). = #term/rust  = `fn new() -> Self`
- [I] self = Refers to the current method's subject = #term/rust = `fn f(self) { ... }`. Equal to `fn f(self: Self) { ... }`

## Commands
- [p] `self` = Takes ownership of instance, used for consuming/transforming = #code/rust/ownership  
<!--ID: 1751434090460-->

- [p] `&self` = Immutable borrow of instance, used for getters & non-mutating operations= #code/rust/ownership  
- [p] `&mut self` = Mutable borrow of instance, used for setters & other operations= #code/rust/ownership  

## Examples
```rust
use std::io::{self, Read};
// Is the same as:
use std::io;
use std::io::Read;
```

```rust
struct Counter {
    count: i32,
}
impl Counter {
    fn new() -> Self {
        Self { count: 0 }
    }

    fn get(&self) -> i32 {
        self.count  // read-only access
    }

    fn increment(&mut self) {
        self.count += 1;  // mutably borrowed
    }

    fn consume(self) {
        println!("Consumed with count = {}", self.count);  // takes ownership
    }
}
```
