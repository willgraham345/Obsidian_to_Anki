---
summary: How python retrieves symbols, manages namespaces, packages, modules, and information in general.
type: note/concept
headings:
  - "[[#Concepts of Note]]"
  - "[[#Examples]]"
  - "[[#Usage]]"
functions:
  - "[[Python dunder functions and methods#globals()]]"
concepts:
  - "[[Python Modules]]"
  - "[[Python namespace]]"
  - "[[Python Packages]]"
similar:
  - "[[Cpp Scoping Rules]]"
  - "[[Rust Scoping Rules]]"
concept_of:
  - "[[Python]]"
date created: Tuesday, November 11th 2025, 2:28:27 pm
date modified: Thursday, December 11th 2025, 12:13:00 pm
items:
  - "[[Python __init__ file]]"
  - "[[Python dunder members#__builtins__]]"
  - "[[Python dunder members#__builtins__]]"
  - "[[Python dunder members#__init__]]"
  - "[[Python Modules]]"
  - "[[Python Package Managers]]"
  - "[[Python Packages]]"
  - "[[Python pyi files]]"
keywords:
  - "[[Python import]]"
libraries:
  - "[[Python importlib]]"
tags:
  - lang/scope
template: "[[base_note_template]]"
template-version: 1.0.0
uses:
  - "[[Python Modules]]"
  - "[[Python Package Managers]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- Python has [[Python Modules]], and its subtype [[Python Packages]].

- Python has a global symbol table, which is a dictionary representing all the global variables in the current module/script.

### Python module search path
Does the following search
1. Current directory
2. Build-in module list
3. Inside `sys.path` directories

### Packages in multiple directories

## Usage

 `globals()` ;;; Function which provides the global symbol table, a dictionary of all global variables in the current module/script.
 `a = globals()["taco"]` ;;; Check if the `a` name is in a global space
 `import modA as B` ;;; Imports module `modA` with an alias `B`.
 `from folder import modFile` ;;; Import a file living in the `.folder/modFile`, when your entrypoint is at `.`
 `from modFile import *` ;;; Import everything from a file living at `.modFile` when your entrypoint is in the same directory.
 `from modFile import A` ;;; Import `A` from `.modFile`.
 `from .. import formats` ;;; Import package `formats` that is within the parent directory of your current file.

  `if __name__ == "__main__":` ;;; Entrypoint to execute a module as a script.

| Method              | Advantages                              | Disadvantages                               |
| ------------------- | --------------------------------------- | ------------------------------------------- |
| `sys.path.append()` | Simple and straightforward              | Changes are session-specific                |
| `os.chdir()`        | Changes are permanent for the session   | Can have side effects in multithreaded code |
| Relative imports    | Useful for complex directory structures | Can be confusing if overused                |
| `imp` module        | Provides low-level import functions     | More complex than other methods             |
| `importlib` module  | Allows programmatic imports             | Requires the module name as a string        |

### Relative Imports
```python
# Suppose you have the following directory structure:
#
# my_project/
# ├── main.py
# └── my_module/
#     └── sub_module.py

# You can use a relative import in main.py to import sub_module.py like this:
from .my_module import sub_module
```

### Dir function
Returns all properties and methods present within a module
```python
import json
json_details = dir(json)
print(json_details)
```

## Examples
### Using `globals()`
```python
print(globals())
print("")

p,q,r,s=10,100,1000,10000
print(globals())
# OUTPUT:
# `{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__':`  
# `<class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {},`  
# `'__builtins__': <module 'builtins' (built-in)>}`  
#   
# `{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__':`  
# `<class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {},`  
# `'__builtins__': <module 'builtins' (built-in)>, 'p': 10, 'q': 100, 'r': 1000,'s':10000}` %%
```
