---
summary: Causes a library to be built from associated source files.
type: note/function
headings:
  - "[[#Concepts of Note]]"
  - "[[#Syntax]]"
  - "[[#Usage]]"
implements:
  - "[[CMake Libraries]]"
  - "[[CMake target]]"
next:
  - "[[CMake target_sources]]"
aliases: []
associations:
  - "[[CMake target_link_options]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Wednesday, March 18th 2026, 8:49:11 pm
function_of:
  - "[[CMake Libraries]]"
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
used_by:
  - "[[CMake Libraries]]"
  - "[[CMake project]]"
  - "[[Cpp include|C include]]"
---

# Summary
󰙎 CMake add_library ;;; Defines a library target.

# Additional Background
- Adds a library called `<name>` to be built from the source files in the command invocation. 
	- If no source files are specified, it will create what is a temporary empty library. Can be filled with [[CMake target_link_libraries]]

## Concepts of Note
- [[CMake Libraries]]

## Usage
 `add_library(foo STATIC foo1.c foo2.c)` ;;; Creates library `foo` that is static, from files `foo1.c` and `foo2.c`

### Adding Object Libraries
See [[CMake target#Object Libraries]] for background
```cmake
add_library(A OBJECT a.cpp)
add_library(B OBJECT b.cpp)
add_library(Combined $<TARGET_OBJECTS:A> $<TARGET_OBJECTS:B>)
```
- `A` and `B` object files are now in the library `Combined`. Object libraries may contain sources (and headers) that compile to object files. 

## Syntax


```cmake
`add_library(<name> [<type>] [EXCLUDE_FROM_ALL] <sources>...)
```
- By default, makes a `STATIC` library unless a type is invoked

## Change default type of library
Enable shared libs by default with [[CMake BUILD_SHARED_LIBS]]
