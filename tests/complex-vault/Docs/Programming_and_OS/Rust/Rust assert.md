---
summary: Asserts that a boolean expression is true at runtime, invoking a `panic!` macro if the expression cannot be evaluated to `true` at runtime.
headings: ["[[#Concepts of Note]]"]
type: note/item
date created: Friday, March 21st 2025, 10:10:39 am
date modified: Tuesday, August 5th 2025, 10:35:18 am
function_of: ["[[Rust macros]]"]
uses: ["[[Rust panic]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
󰠗  What helpful macro returns a `panic!` at runtime if its expression doesn't evaluate to `true`? ;; `assert!(condition, msg)` = #lang/control_flow/assert 
<!--ID: 1758253289081-->

  `assert!(condition, "condition was false :(")` ;;; Creates a runtime-check on the `condition` boolean, outputting a panic with the message "condition was false :(" if `condition` evaluated to `false`. = #lang/control_flow/assert 
<!--ID: 1758253289088-->

