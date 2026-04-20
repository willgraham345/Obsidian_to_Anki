---
summary: How you segment projects into smaller units, and minimize dependencies.
type: note/concept
date created: Monday, March 31st 2025, 11:45:55 am
date modified: Tuesday, April 29th 2025, 3:18:28 pm
keywords:
  - "[[Rust Self]]"
tags:
  - lang/scope
  - lang/scope/dependency
  - lang/scope/module
  - lang/scope/namespace
  - lang/scope/visibility
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
  `mod m {}` ;;; Defines a module, get a definitionn inside of `{}` = #lang/scope/module 
ID: 1751997628384



  `mod m` ;;; Define a module, gets definition from `m.rs` or `m/mod.rs` = #lang/scope/module 
ID: 1751997628388



  `a::b` ;;; Namespace path = #lang/scope/namespace 
ID: 1751997628393



      `::b` = Search `b` in `crate root`, `ext. prelude`, or `global path`
      `crate::b` = Search within the crate root (can also be done with `self` and `super`)
  `use a::b;` Use `b` directly in this scope without requiring `a` anymore. ;;; #lang/scope/namespace = `use a::{b,c}` Same, but also include `c` 
ID: 1751997628397



  `pub use a::b` ;;; Bring `a::b` into scope and reexport from here = #lang/scope/namespace  
ID: 1751997628401



  `pub T` ;;; Make `T` visible from outside it's module = #lang/scope/visibility 
ID: 1751997628406



  `extern crate a` ;;; Declare a dependency on crate `a` = #lang/scope/dependency 
ID: 1751997628410



  `use super::b` ;;; Add item `b` from the parent module, and bring it into scope = #lang/scope/namespace  
ID: 1751997628414



  `use crate::b` ;;; Add item `b` from the root of the current crate, and bring it into scope = #lang/scope/namespace  
ID: 1751997628419


