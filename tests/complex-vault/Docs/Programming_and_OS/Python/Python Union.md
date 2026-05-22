---
type: note/class
headings:
aliases: []
class_of:
  - "[[Python typing]]"
date created: Wednesday, March 11th 2026, 11:00:46 am
date modified: Wednesday, March 11th 2026, 11:04:39 am
id: Python Union
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
---

# Summary
󰙎 Python Union ;;; Union type syntax (PEP 604) and legacy `typing.Union`

# Additional Background

## Concepts of Note
󰙎 union type ;;; a type that accepts any of several alternatives

## Syntax
- `type1 | type2` (PEP 604)
- `typing.Union[type1, type2]` (legacy)
- Nested unions, optional (`type | None`).

## Usage
```python
# New syntax with generics
def process(value: int | str | list[int]) -> None:
    ...

# Legacy syntax with generics
from typing import Union, List
def process(value: Union[int, str, List[int]]) -> None:
    ...
```
- Works with `typing.get_args` / `typing.get_origin`.
- Prefer `|` on Python 3.10+ for readability.

## Diagrams
![[Python Union.png]]
