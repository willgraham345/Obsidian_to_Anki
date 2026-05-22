---
summary: List of directories, represented with forward slashes, showing what is included with include() or find_package() before checking default modules that come with CMake.
type: note/item/variable
headings: ["[[#Examples]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, January 8th 2026, 5:29:39 pm
template: "[[base_note_template]]"
template-version: 1.0.1
used_by: ["[[CMake find_package]]", "[[CMake include]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

Path to search for additional CMake modules

[`CMAKE_MODULE_PATH`](https://cmake.org/cmake/help/latest/variable/CMAKE_MODULE_PATH.html#variable:CMAKE_MODULE_PATH "CMAKE_MODULE_PATH")

## Examples
Many repos have a bunch of `*.cmake` files with functions to help in development. Adding this directory to the [[CMake CMAKE_MODULE_PATH]] is helpful in loading them.