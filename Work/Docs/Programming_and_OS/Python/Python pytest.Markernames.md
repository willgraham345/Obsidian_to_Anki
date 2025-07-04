---
tags: note/python
type: note
---
# Background
- Used to help group tests in a file
- To use markers, we have to import pytest module in the testfile. We can define our own marker names to run the tests having those marker names

# Usage
```python
@pytest.mark.<markername>
```

Running
```bash
pytest -m <markername> -v
```