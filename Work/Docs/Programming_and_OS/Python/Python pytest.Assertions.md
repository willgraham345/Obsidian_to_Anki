---
tags: note/python
type: note
---
# Background
Checks that return either true or false status. 
- If an assertion fails in a test method, then that method execution is stopped there. Remaining code within that method is not executed and Pytest assertions will continue with the next text method

# Examples
```python
assert "hello" == "Hai" # is an assertion failure.
assert 4==4 # is a successful assertion
assert True # is a successful assertion
assert False # is an assertion failure.
```