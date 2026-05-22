---
summary:
type: note/keyword
headings:
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Friday, March 6th 2026, 10:12:48 am
keyword_of:
  - "[[Python Operators]]"
  - "[[Python]]"
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
used_by:
  - "[[Python Dict]]"
  - "[[Python Functions]]"
  - "[[Python List]]"
---

# Summary
󰙎 Python Unpacking Operator ;;; The single asterisk `*` (for iterables), and the double asterisk (`**`) for dictionaries. Useful for unpacking, function calls, and function definitions.

# Additional Background
## Concepts of Note
- Used in definition/assignment -> `*`/`**` will collect
- Used in call/literal --> `*`/`**` will expand

## Usage
### Unpacking into Variables
```python
a, *b, c = [1, 2, 3, 4, 5]
# a = 1, b = [2, 3, 4], c = 5
```

### Function Calls
```python
def add(x, y, z):
    return x + y + z

nums = [1, 2, 3]
add(*nums)  # same as add(1, 2, 3)
```

```python
def greet(name, greeting):
    print(f"{greeting}, {name}!")

data = {"name": "Alice", "greeting": "Hello"}
greet(**data)  # same as greet(name="Alice", greeting="Hello")
```

### Merging Dictionaries
```python
defaults = {"color": "blue", "size": 10}
overrides = {"size": 20, "weight": 5}
merged = {**defaults, **overrides}
# {"color": "blue", "size": 20, "weight": 5}
# Note: later keys win on conflict
```

### Function Definitions