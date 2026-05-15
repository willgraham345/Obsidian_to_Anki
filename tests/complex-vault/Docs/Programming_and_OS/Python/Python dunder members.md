---
summary: Dunder fields are accessible within all classes.
headings:
  - "[[#Properties]]"
type: note/item
members:
  - "[[Python dunder members#__all__]]"
  - "[[Python dunder members#__builtins__]]"
  - "[[Python dunder members#__init__]]"
  - "[[Python dunder members#__path__]]"
methods:
  - "[[Python dunder members#__name__]]"
similar:
  - "[[Python dunder functions and methods]]"
concept_of:
  - "[[Python OOP]]"
date created: Wednesday, November 12th 2025, 5:23:59 pm
date modified: Wednesday, December 3rd 2025, 1:23:27 pm
item_of:
  - "[[Python Modules]]"
  - "[[Python OOP]]"
  - "[[Python Scoping Rules]]"
items:
template: "[[base_note_template]]"
template-version: 1.0.0
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Properties
#### __all__
  `__all__` ;;; Variable that specifies what should be imported from the module when using `from {a} import *`. = #lang/oop/class/member/dunder #lang/scope/module 
  `__all__ ``=`` ["echo", "surround", "reverse"]` ;;; Specify that `echo`, `surround`, and `reverse` functions should be imported when using `from {module} import *`. = #lang/oop/class/member/dunder #lang/scope/module 

#### __name__
  `__name__` ;;; Dunder field that contains the name of the Python module you are in. = #lang/oop/class/member/dunder 

#### __path__
  `__path__` ;;; Attribute on modules that should be a possibly empty sequence of strings. These strings enumerate locations where the package's submodules will be found. If a module *has* this attribute, it is a package. = #lang/scope/packages

#### __init__
- #todo/refactor 

#### __builtins__
  `__builtins__` ;;; Reference to the module builtins which contains globally-accessible code not requiring any imports. This can be implemented as a __builtins__.pyi rather than builtins.pyi.
	- 
- Contains built-in functions (len, abs, print), built-in exceptions (ValueError, TypeError), and built-in constants.
- (implemented in C inside the Python interpreter)
- Can
