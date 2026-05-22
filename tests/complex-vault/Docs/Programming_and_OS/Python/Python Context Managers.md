---
summary: Using resources (file ops, database stuff) is made easier when you have a manager for the resource. The manager should handle releasing memory from acquired connections to avoid memory leaks. Most common way is using the `with` keyword.
type: note/concept
headings:
  - "[[#Concepts of Note]]"
  - "[[#Concepts of Note]]"
concepts:
  - "[[Python with]]"
concept_of:
  - "[[Python]]"
date created: Wednesday, April 23rd 2025, 12:51:53 pm
date modified: Thursday, January 22nd 2026, 2:46:19 pm
libraries:
  - "[[Python contextlib]]"
template: "[[base_note_template]]"
template-version: 1.0.2
---

# Summary
󰙎 Python Context Managers ;;; Using resources (file ops, database stuff) is made easier when you have a manager for the resource. The manager should handle releasing memory from acquired connections to avoid memory leaks. Most common way is using the `with` keyword. A “context manager” is something that implements the `__enter__()` or `__exit__()` dunder methods.
# Additional Background
## Concepts of Note
- Somewhat similar to [[Python try except else finally]], 