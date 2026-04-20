---
type:
headings:
  - "[[#Concepts of Note]]"
  - "[[#Diagrams]]"
  - "[[#Examples]]"
prev:
  - "[[Python Mock]]"
class_of:
  - "[[Python unittest mock]]"
date created: Thursday, March 5th 2026, 10:32:02 am
date modified: Thursday, March 5th 2026, 5:03:03 pm
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
---

# Summary
󰙎 Python MagicMock ;;; An extended version of [[Python unittest mock]]'s [[Python Mock]]. Provides default implementations of many/most magic methods.

# Additional Background
## Concepts of Note
### When to Use Mock vs. MagicMock

Use `Mock` when:
- You are testing interactions with standard methods and attributes.
- You want more control over what is mocked and avoid unintended behavior from automatically mocked magic methods.

Use `**MagicMock**` when:
- You need to mock an object that uses magic methods extensively (e.g., objects implementing custom behavior for operations like `__add__`, `__getitem__`, etc.).
- You prefer convenience and reduced boilerplate for setting up such mocks.

## Examples
```python
from unittest.mock import MagicMock

# Creating a MagicMock object
magic_mock = MagicMock()

# Setting a return value for a magic method
magic_mock.__str__.return_value = 'MagicMocked!'

# Calling the magic method
result = str(magic_mock)

# Asserting the magic method was called
assert magic_mock.__str__.called
assert result == 'MagicMocked!'
```

## Diagrams
![[Python MagicMock.png]]