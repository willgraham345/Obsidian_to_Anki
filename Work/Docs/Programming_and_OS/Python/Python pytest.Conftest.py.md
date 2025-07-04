---
tags: note/python
type: note
---
# Background
`conftest.py` is a file created to enable fixture functions to be accessible across multiple test files. 
- Tests will look for fixtures within the same file. As the fixture is not found in the file, it will check for the fixture in `conftest.py` file. 

# Example
```python
import pytest

@pytest.fixture
def input_value():
   input = 39
   return input
```