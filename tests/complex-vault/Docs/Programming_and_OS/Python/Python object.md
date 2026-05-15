---
summary:
headings:
  - "[[#Properties]]"
type: note/class
functions:
  - "[[Python object#ascii]]"
  - "[[Python object#callable()]]"
class_of:
  - "[[Python Data Types]]"
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Tuesday, November 11th 2025, 1:32:59 pm
tags: []
template: "[[base_note_template]]"
template-version: 1.0.0
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Properties

### methods
#### ascii
- Returns a string containing a printable representation of an object and escapes non-ASCII in string using `\x` `\u` or `\U` escapes

```python
string_printable_representation_of_object = ascii(object)
```

```python3
print(ascii("¥"))
```
- output: `\xa5`

#### callable()


Checks if an object is callable, and returns a boolean
```python3
# Python program to illustrate 
# callable() a test function
def Geek():
    return 5
 
# an object is created of Geek()
let = Geek
print(callable(let))
 
# a test variable
num = 5 * 5
print(callable(num))
```


