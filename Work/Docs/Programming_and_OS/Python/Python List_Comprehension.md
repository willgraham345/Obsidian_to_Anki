---
tags: [note/python]
type: note
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Sunday, September 8th 2024, 11:58:21 pm
---
# Background
Easier way to create lists. 

# Usage
```python
[<expression> for <item> in <list> <if conditional>]
```

### Example
```python
# List comprehension for the squares of all even numbers between 0 and 9
result = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]
```

