---
type: note/concept
ai_generated: true
summary: C++ conditional branching
headings:
  - "[[#Syntax]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, April 9th 2026, 12:00:00 pm
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
---

# Summary


# Additional Background
## Syntax
 `if (cond) { ... }` ;;; Basic if statement
 `if (cond) { ... } else { ... }` ;;; if/else branch
 `if (c1) { ... } else if (c2) { ... } else { ... }` ;;; if/else if/else chain
 `x = (cond) ? a : b` ;;; Ternary: x = a if cond true, b if false
 `var = (conditional) ? 5 : 6` = Make a conditional that assigns `var` to `5` if true, and `6` if false.

```cpp 
variable = (condition) ? condition_is_true : condition_is_false;
```

Curly brackets can be omitted if there is only one statement following the condition 

```cpp
if (number == 7)
  std::cout << "Lucky!\n";

```