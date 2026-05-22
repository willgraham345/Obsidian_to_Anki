---
summary: Tells the preprocessor to insert the contents of another file into the source code at the point where the `#include` is found.
type: note/keyword
headings:
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
aliases:
  - C include
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, January 29th 2026, 5:24:04 pm
template: "[[base_note_template]]"
template-version: 1.0.1
uses:
  - "[[CMake add_library]]"
  - "[[CMake target_include_directories]]"
  - "[[CMake target_link_libraries]]"
associations:
  - "[[CMake add_dependencies]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- Include directs the preprocessor how to grab other files.
- Include directives are typically used to include the C header files for C functions that are held outside of the current source file
More info [here](https://stackoverflow.com/questions/21593/what-is-the-difference-between-include-filename-and-include-filename)

## Usage
 `#include <file>` ;;; Tells the preprocessor to include `file` by looking through directories pre-designated by compiler/IDE. Usually used for header files or C standard library files.
 `#include "file"` ;;; Tells preprocessor to include `file` by searching through implementation-defined manner. Typically used for programmer-defined headers. Typically includes the same directory as the source file.


