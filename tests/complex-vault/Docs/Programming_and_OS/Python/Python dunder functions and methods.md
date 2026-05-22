---
summary:
type: note/item
headings:
  - "[[#Concepts of Note]]"
  - "[[#Properties]]"
functions:
  - "[[Python dunder functions and methods#call()]]"
  - "[[Python dunder functions and methods#delattr()]]"
  - "[[Python dunder functions and methods#getattr()]]"
  - "[[Python dunder functions and methods#hasattr()]]"
  - "[[Python dunder functions and methods#issubclass()]]"
  - "[[Python dunder functions and methods#setattr()]]"
  - "[[Python dunder functions and methods#super()]]"
methods:
similar:
  - "[[Python dunder members]]"
  - "[[Python builtin functions]]"
concept_of:
  - "[[Python OOP]]"
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Wednesday, December 17th 2025, 2:29:38 pm
function_of:
  - "[[Python Functions]]"
items:
  - "[[Python __builtins__]]"
tags:
  - lang/oop/generics
  - lang/scope/existence_checking
  - lang/scope/visibility
template: "[[base_note_template]]"
template-version: 1.0.0
used_by:
  - "[[Python OOP]]"
uses:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- Available in the Built in [[Python namespace]]

## Properties
### Functions
#### Collections
##### dict()
##### list()
##### tuple()
##### set()

##### frozenset()
#### Iterations
#### Strings



#### Math Functions
#### Object functions
##### call()
 `def __call__(self, a: int)` ;;; Define how class `c` will deal with `C(5)` *after* it has been instantiated. i.e., how do you modify the function called when you call this class?

##### delattr()

##### dir()
 `dir()` ;;; Returns a list of strings representing every name currently defined in the *global* scope.
 `dir(taco)` ;;; Return a list of strings with what is defined in the `taco` namespace.

##### getattr()
 `getattr(a, 'o')` ;;; Gets the value of attribute `a` from the specified object `o`
- Similar to [[#setattr()]], [[#hasattr()]], and [[#delattr()]]

##### globals()
Returns *reference* to the global namespace dict. This means you can add new variables if you save and return its value.

##### hasattr()

##### hash()

##### isinstance()
 `isinstance(a, (int, float))` ;;; Check if `a` is of type `int` or `float` in python. 
- Uses duck typing (if it looks like a duck and quacks like a duck, it's a duck).

##### issubclass()

##### locals()
- Returns a *copy* to the local namespace dict. You *can't* edit this one locally.

##### len()

##### super()

##### setattr()
