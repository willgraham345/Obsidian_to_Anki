---
type: note/concept
headings:
  - "[[#Usage]]"
concept_of:
  - "[[Python pytest]]"
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Thursday, March 5th 2026, 2:11:51 pm
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
---

# Summary
󰙎 Python pytest parameterizing ;;; A way to run tests against multiple sets of inputs

# Additional Background
## Usage
 `@pytest.mark.parameterize("num", out",[(1,3),(2,4)])` ;;; Decorator that will parameterize a test in python with `num` equal to sequence: `1, 2` and `out` equal to sequence: `3, 4`

## Example
```python
import pytest

@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output):
   assert 11*num == output
```
