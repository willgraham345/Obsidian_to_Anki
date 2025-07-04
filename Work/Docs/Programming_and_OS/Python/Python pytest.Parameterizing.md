---
tags: note/python
type: note
---
# Background
A way to run tests against multiple sets of inputs

# Usage
```python
@pytest.mark.parameterize
```

## Example
```python
import pytest

@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output):
   assert 11*num == output
```