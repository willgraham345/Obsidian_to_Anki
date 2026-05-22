---
type: note/item
headings:
  - "[[#Examples]]"
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Wednesday, March 4th 2026, 3:09:45 pm
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
item_of:
  - "[[Python pytest]]"
---

# Summary
󰙎 Python pytest assertions ;;; If an assertion fails in a test method, method execution is stopped there. Remining code within the method isn't executed, and pytest assertions will continue with next test method.

# Additional Background

## Examples


```python
assert "hello" == "Hai" # is an assertion failure.
assert 4==4 # is a successful assertion
assert True # is a successful assertion
assert False # is an assertion failure.
```
