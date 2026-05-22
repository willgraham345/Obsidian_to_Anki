---
type: note/concept
headings:
date created: Tuesday, February 24th 2026, 4:59:19 pm
date modified: Wednesday, March 18th 2026, 9:08:42 pm
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
tool_of:
  - "[[CMake]]"
used_by:
  - "[[CMake target_sources]]"
---

# Summary
󰙎 CMake file sets ;; Introduced in 3.23, provides a modern, structured way to manage files (like headers/C++ modules) with specific targets using the `target_sources()` command. Lets you specify scope, types, and automated include directories.

# Additional Background
- [File Sets — CMake docs](https://cmake.org/cmake/help/latest/command/target_sources.html#file-sets)
- Used via [[CMake target_sources]] `FILE_SET` subcommand
- Requires CMake ≥ 3.23

## Concepts of Note

󰙎 FILE_SET ;;; A named collection of files attached to a target with a given type and visibility.

󰙎 TYPE ;;; Kind of file set: `HEADERS` (default, for public headers) or `CXX_MODULES` (C++20 modules); determines install behavior.

󰙎 BASE_DIRS ;;; Root directories used to compute relative install paths; defaults to `CMAKE_CURRENT_SOURCE_DIR`.

󰙎 Visibility ;;; [[CMake PRIVATE]] / [[CMake PUBLIC]] / [[CMake INTERFACE]] control whether the file set propagates to consumers; see [[CMake visibility]].

󰙎 Auto include dirs ;;; PUBLIC/INTERFACE HEADERS file sets automatically add BASE_DIRS to the target's include path for consumers — no `target_include_directories()` needed.

## Usage

 `target_sources(<target> PUBLIC FILE_SET HEADERS BASE_DIRS <dir> FILES <files>)` ;;; Attach public headers to a target; consumers automatically get BASE_DIRS on their include path.

 `target_sources(<target> PRIVATE FILE_SET HEADERS BASE_DIRS <dir> FILES <files>)` ;;; Attach headers used only internally — not propagated to consumers.

 `target_sources(<target> PUBLIC FILE_SET CXX_MODULES FILES <files>)` ;;; Attach C++20 module sources; requires CMake ≥ 3.28 for full support.

## Examples

### Library with public headers
```cmake
add_library(mylib STATIC mylib.cpp)
target_sources(mylib
  PUBLIC
    FILE_SET HEADERS
    BASE_DIRS include
    FILES include/mylib/mylib.h)
```
Consumers of `mylib` automatically get `include/` on their include path.

### Executable consuming a library's file set
```cmake
add_executable(myapp main.cpp)
target_link_libraries(myapp PRIVATE mylib)
```
`myapp` inherits the PUBLIC HEADERS file set from `mylib`; headers resolve without any extra include setup.

### C++20 module (CXX_MODULES)
```cmake
target_sources(mylib
  PUBLIC
    FILE_SET CXX_MODULES
    FILES src/mylib.cppm)
```
Full C++20 module support requires CMake ≥ 3.28.
