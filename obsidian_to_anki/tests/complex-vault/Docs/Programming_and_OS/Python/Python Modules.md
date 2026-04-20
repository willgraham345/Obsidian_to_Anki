---
summary: Typically contained within a single python file. Can be thought of as a specific file within a filesystem, while a Python package is a file directory. All packages are modules but not all modules are packages.
type: note/concept
headings:
  - "[[#Concepts of Note]]"
  - "[[#Flashcards]]"
  - "[[#Properties]]"
  - "[[#Usage]]"
concepts:
  - "[[Python Packages]]"
concept_of:
  - "[[Python Scoping Rules]]"
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Thursday, March 5th 2026, 9:50:26 am
implementations:
  - "[[Python ModuleType]]"
item_of:
  - "[[Python Scoping Rules]]"
items:
  - "[[Python dunder members]]"
keywords:
  - "[[Python import]]"
tags: [lang/meta/attributes/modules, lang/scope/module, lang/scope/namespace]
template: "[[base_note_template]]"
template-version: 1.0.0
used_by:
  - "[[Python Package Managers]]"
uses:
  - "[[Python __init__ file]]"
  - "[[Python dunder functions and methods]]"
  - "[[Python sys#modules]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[5. The import system — Python 3.14.0 documentation](https://docs.python.org/3/reference/import.html#package-path-rules)

## Concepts of Note
Python modules are `.py` that contain python code. Modules are used to group related code together
- Each module in python has its own private namespace. 
	- That same namespace is used as the global namespace by *all* functions defined within the module. 
	- The author of a module can use global variable in the module without worry about accidental clashes with a user's global variables.

Packages/modules are defined with a `__init__.py` file.

Modules can import other modules.

## Flashcards %% fold %% 
󰠗  Can python modules contain executable statements? ;; Yes =
󰠗  How does Python speed up loading modules? ;; It creates the `__pycache__` directory, where the version encodes the format of the compiled file.  = 
󰠗 Are all python packages python modules? Is the reverse true? ;; Yes, and no. Packages are similar to directories, and modules are similar to files. 
