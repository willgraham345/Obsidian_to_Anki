---
summary: Module providing runtime support for type hints.
type: note/library
headings:
  - "[[#Concepts of Note]]"
  - "[[#Examples]]"
  - "[[#Flashcards]]"
  - "[[#Properties]]"
  - "[[#Usage]]"
functions:
  - "[[Python typing#cast()]]"
classes:
  - "[[Python TypedDict]]"
  - "[[Python TypeVar]]"
  - "[[Python object]]"
  - "[[Python Mapping]]"
  - "[[Python Union]]"
date created: Tuesday, November 11th 2025, 2:31:18 pm
date modified: Thursday, December 11th 2025, 1:22:58 pm
library_of:
  - "[[Python Data Types]]"
  - "[[Python]]"
tags:
  - lang/meta/attributes/typesystem
  - lang/meta/typing
  - lang/meta/typing/explicit
  - lang/scope/alias
  - todo/refactor
template: "[[base_note_template]]"
template-version: 1.0.0
uses:
  - "[[Python asterisk]]"
concepts:
  - "[[Python Protocols]]"
similar:
  - "[[Python types]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[Specification for the Python type system — typing documentation](https://typing.python.org/en/latest/spec/index.html)
- [typing — Support for type hints — Python 3.14.0 documentation](https://docs.python.org/3/library/typing.html)
 
- add the following:
	- `TYPE_CHECKING`
	- `Callable`

## Concepts of Note
Built in typing is supported to a limited extent in python 3.8supported to a limited extent in python 

## Examples
### Define a generic fn args
```python
class Copyable:
    def copy[T: Copyable](self: T) -> T:
        # return a copy of self

class C(Copyable): ...
c = C()
c2 = c.copy()  # type here should be C
```

### Variadic number of args
See [[Python asterisk]] for how this works.

## Usage
  `type Vector = list[float]` ;;; Define a type alias `Vector` that has a `list` of `float`s. = 
  `Vector: TypeAlias = list[float]` ;;; Backwards compatible way of defining a type alias `Vector` that contains a `list` of `float`s. =  
  `a: List = [1, 2, 3]` ;;; Create `a` which is of type `List` with `[1,2,3]`. =
  `isinstance(a, list)` ;;; Return a `bool` if `a` is of type `list`. =  

## Properties
##### cast()
Cast a value to a type.
`cast(dt`

## Flashcards
󰠗  What is the difference between `tuple` and `Tuple` in python? ;; The `tuple` datatype refers to the built-in tuple type, while `Tuple` refers to the type hints that come from python. =
