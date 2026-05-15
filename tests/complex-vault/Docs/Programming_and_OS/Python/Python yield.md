---
summary: Turns a function into a function generator, and the function generator returns an iterator.
type: note/keyword
headings:
  - "[[#Concepts of Note]]"
similar:
  - "[[Python return]]"
date created: Monday, December 8th 2025, 10:39:46 am
date modified: Wednesday, March 4th 2026, 4:03:14 pm
keyword_of:
  - "[[Python Keywords]]"
tags: [lang/control_flow/generators]
template: "[[base_note_template]]"
template-version: 1.0.0
used_by:
  - "[[Python Iterable]]"
---

# Summary
󰙎 Python yield ;;; Turns a function into a function generator, and the function generator returns an iterator.

# Additional Background
## Concepts of Note
󰠗 How are the `return` and `yield` keywords different in Python? ;; The `return` keyword prevents further execution. The `yield` keyword returns results so far, and continues to the next step.
󰠗 What is the return value for a function with `yield` statements? ;; A list of values, one item for each `yield`.