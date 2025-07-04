---
summary: How you segment projects into smaller units, and minimize dependencies.
type: note/concept
date created: Monday, March 31st 2025, 11:45:55 am
date modified: Tuesday, April 29th 2025, 3:18:28 pm
keywords:
  - "[[Rust Self]]"
tags:
  - code/rust/organization
  - code/rust/organization/dependency
  - code/rust/organization/module
  - code/rust/organization/namespace
  - code/rust/organization/visibility
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
- [p] `mod m {}` = Defines a module, get a definitionn inside of `{}` = #code/rust/organization/module
<!--ID: 1751434090480-->

- [p] `mod m` = Define a module, gets definition from `m.rs` or `m/mod.rs` = #code/rust/organization/module
<!--ID: 1751434090484-->

- [p] `a::b` = Namespace path = #code/rust/organization/namespace
<!--ID: 1751434090487-->

      `::b` = Search `b` in `crate root`, `ext. prelude`, or `global path`
      `crate::b` = Search within the crate root (can also be done with `self` and `super`)
- [p] `use a::b;` Use `b` directly in this scope without requiring `a` anymore. = #code/rust/organization/namespace = `use a::{b,c}` Same, but also include `c`
<!--ID: 1751434090492-->

- [p] `pub use a::b` = Bring `a::b` into scope and reexport from here = #code/rust/organization/namespace 
<!--ID: 1751434090496-->

- [p] `pub T` = Make `T` visible from outside it's module = #code/rust/organization/visibility
<!--ID: 1751434090500-->

- [p] `extern crate a` = Declare a dependency on crate `a` = #code/rust/organization/dependency
<!--ID: 1751434090507-->

- [p] `use super::b` = Add item `b` from the parent module, and bring it into scope = #code/rust/organization/namespace 
<!--ID: 1751434090514-->

- [p] `use crate::b` = Add item `b` from the root of the current crate, and bring it into scope = #code/rust/organization/namespace 
<!--ID: 1751434090518-->
