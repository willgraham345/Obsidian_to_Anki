---
summary: The API for system-specific parameters and functions for whatever machine python is running on. Always available, and all variables are read-only (unless explicitly noted).
type: note/library
headings:
  - "[[#Properties]]"
functions:
  - "[[Python sys#exception]]"
  - "[[Python sys#exit]]"
variables:
  - "[[Python sys#argv]]"
  - "[[Python sys#audit]]"
  - "[[Python sys#implementation]]"
  - "[[Python sys#modules]]"
  - "[[Python sys#platform]]"
down:
  - "[[Docs/Programming_and_OS/Python/Python sys.Command]]"
classes:
processes:
  - "[[Python exit program]]"
  - "[[Python interpreter settings]]"
  - "[[Python runtime environment info]]"
  - "[[Python stdio input and output redirection]]"
  - "[[Python sys CLI Arg Retrieval]]"
  - "[[Python sys Module Reloads]]"
similar:
  - "[[Python argparse]]"
  - "[[Python os]]"
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Thursday, December 11th 2025, 10:46:45 am
tags: []
template: "[[base_note_template]]"
template-version: 1.0.0
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[sys — System-specific parameters and functions — Python 3.14.2 documentation](https://docs.python.org/3/library/sys.html#sys.path)

## Properties
### Functions
##### exception
When called while an exception handler is executing, returns the exception that was caught by the handler.

##### exit
- Raise a [[Python SystemExit]] exception.

### Variables
##### argv
CLI args passed into Python
[sys — System-specific parameters and functions — Python 3.14.2 documentation](https://docs.python.org/3/library/sys.html#sys.path)

##### audit
##### implementation
Contains information about the implementation of currently running Python interpreter.
[sys — System-specific parameters and functions — Python 3.14.2 documentation](https://docs.python.org/3/library/sys.html#sys.path)

##### platform
String containing a platform identifier. These are `linux`, `wasi`, `win32`, `darwin`, and other stuff. See [link](https://docs.python.org/3/library/sys.html#sys.platform) for details

##### modules
Dictionary that maps the module names to modules which have already been loaded. Can be manipulated to force reloading of modules and other tricks.  