---
summary: Cpp lets you symbolically represent addresses, as well as creation of dynamic data structures through their use. Enables you to call-by-reference and create/manipulate dynamic data structures. See runtime allocation for anything related to `new` and `delete` operations.
type: note/concept
concepts:
  - "[[Cpp as if rule]]"
  - "[[Cpp const]]"
  - "[[Cpp delete]]"
  - "[[Cpp new]]"
  - "[[Cpp references]]"
  - "[[Cpp Runtime Allocation]]"
  - "[[Cpp rvalue]]"
  - "[[Cpp value categories]]"
  - "[[Cpp.Smart Pointers]]"
components:
  - "[[Cpp pointers]]"
  - "[[Cpp references]]"
  - "[[Cpp std stack]]"
associations:
  - "[[Cpp Variables and Containers]]"
concept_of:
  - "[[Cpp]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, June 19th 2025, 1:42:15 pm
libraries:
  - "[[Cpp std cstdlib]]"
  - "[[Cpp std memory]]"
  - "[[Cpp std new]]"
---

![[Pasted.image.20240327092729.png | 500]]

# Usage
| expression | can be read as                                                          |
| ---------- | ----------------------------------------------------------------------- |
| `*x`       | pointed to by `x`                                                       |
| `&x`       | address of `x`                                                          |
| `x.y`      | member `y` of object `x`                                                |
| `x->y`     | member `y` of object pointed to by `x`                                  |
| `(*x).y`   | member `y` of object pointed to by `x` (equivalent to the previous one) |
| `x[0]`     | first object pointed to by `x`                                          |
| `x[1]`     | second object pointed to by `x`                                         |
| `x[n]`     | (`n+1`)th object pointed to by `x`                                      |

## Null Pointers
- You can initialize a pointer to `0` or `NULL` pointing it to nothing
- Dereferencing a null pointer causes a `STATUS_ACCESS_VIOLATION` exception



