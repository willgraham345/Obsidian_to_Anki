---
tags: note/python
type: note
---
# Description
- f-strings are made to make string interpolation much easier, instead of requiring the `str.format()` function.

# Syntax
- Begin a string with `f`, and put `{}` where you'd like your value to be (this also supports simple operations like + and - )
- You can also add a format specifier

## Syntax Of F-string
### Basic
```python
val = 1
print(f"Iteration is at {val}")
```
OUTPUT: `Iteration is at 1`
### Decimal Points
```python
number = 3.14159265
print(f"{number:.2f}")
```
OUTPUT = `3.14`
### Example of F-string
```python
# Prints today's date with help
# of datetime library
import datetime
today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")
```
OUTPUT: `April 04, 2018`
