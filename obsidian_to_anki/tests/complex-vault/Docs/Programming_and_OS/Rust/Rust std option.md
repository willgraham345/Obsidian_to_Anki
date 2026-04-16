---
summary: Represents an optional value. Rust uses optional pointers, rather than using `null` pointers.<br><br>Every option is either `Some` (contains value) or `None` and does not. `Option` types are very common, and can often be paired with pattern matching.
headings: ["[[#Concepts of Note]]"]
type: note/class
date created: Thursday, May 22nd 2025, 10:30:30 am
date modified: Monday, July 14th 2025, 2:31:05 pm
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
  `option_var.expect("custom error message")` ;;; From an option variable, get the `Some` variant or panic with a custom message = #lang/control_flow/option 
ID: 1751997628097



  `option_var.unwrap()` ;;; From an option variable, get the `Some` variant or panic with a generic message. Note, if there is a `None` value here, it WILL cause the program to panic. Generally recommended to avoid this in production as it will cause unexpected program termination. = #lang/control_flow/option 
ID: 1751997628102

## Concepts of Note

### `Some` and `None`
- Options have a value (`Some`) or don't have a value (`None`). 

### Question mark operator
- Hides boilerplate of propagating value up the call stack. 
- Ending the expression with `?` will result in the `Some`'s unwrapped value, unless the result is `None`, in which case the `None` is returned early from the enclosing function.

