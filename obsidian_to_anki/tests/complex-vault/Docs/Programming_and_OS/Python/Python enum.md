---
summary: Define constant values in python with this class.
type: note/class/enum
headings:
  - "[[#Concepts of Note]]"
  - "[[#Examples]]"
  - "[[#Flashcards]]"
similar:
  - "[[Python IntEnum]]"
  - "[[Python StrEnum]]"
  - "[[Python IntFlag]]"
  - "[[Python EnumDict]]"
class_of:
  - "[[Python Data Types]]"
date created: Tuesday, November 18th 2025, 5:37:51 pm
date modified: Tuesday, December 16th 2025, 12:07:53 pm
tags:
  - lang/data/dict
  - lang/data/enumeration
  - lang/data/enumeration/discriminant
  - lang/data/enumeration/variant
template: "[[base_note_template]]"
template-version: 1.0.0
uses:
  - "[[Python ReprEnum]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[enum — Support for enumerations — Python 3.14.2 documentation](https://docs.python.org/3/library/enum.html)
## Concepts of Note
- From the `enum`

  `class Season(Enum)` ;;; Define an enum class `Season`. = 
  `print(Season.FALL.name)` ;;; Print out the name of the `Season`'s `FALL` variant. = 
  `print(Season.FALL.value)` ;;; Print out the value of the `Season`'s `FALL` variant. =  

## Examples

```python
from enum import Enum

class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4

print(Season.SUMMER)  
print(Season.SUMMER.name)
print(Season.SUMMER.value)
```

## Flashcards

󰠗  Are enums hashable in python? ;; Yes, they are hashable (can be used within dictionaries) =
