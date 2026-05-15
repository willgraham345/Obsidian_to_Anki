---
summary: "Made to make string interpolation easier instead of requiring `str.format()`. Begin with an `f` and put `{}` where you want your variable. "
headings: ["[[#Syntax]]"]
type: note/concept
similar: ["[[Python String]]"]
concept_of: ["[[Python Basics]]", "[[Python Input and Output]]"]
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Thursday, November 13th 2025, 3:26:45 pm
tags: []
template: "[[base_note_template]]"
template-version: 1.0.0
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

- Begin a string with `f`, and put `{}` where you'd like your value to be (this also supports simple operations like + and - )
- You can also add a format specifier

## Syntax
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
