---
type:
headings:
  - "[[#Examples]]"
similar:
  - "[[Python pytest monkeypatch]]"
class_of:
  - "[[Python unittest mock]]"
date created: Thursday, March 5th 2026, 10:33:15 am
date modified: Thursday, March 5th 2026, 10:33:43 am
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
next:
  - "[[Python MagicMock]]"
---

# Summary
󰙎 Python Mock ;;; Unittesting mocks within python.

# Additional Background

## Examples

```python
from unittest.mock import Mock  
  
# Creating a Mock object  
mock = Mock()  
  
# Setting a return value for a method  
mock.some_method.return_value = 'Hello, World!'  
  
# Calling the method  
result = mock.some_method()  
  
# Asserting the method was called  
assert mock.some_method.called  
assert result == 'Hello, World!'
```