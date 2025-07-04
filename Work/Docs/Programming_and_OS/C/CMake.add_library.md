---
summary: Causes a library to be built from the associated source files.
implements:
  - "[[CMake target]]"
concepts: []
aliases: []
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, October 15th 2024, 5:54:26 pm
tags: []
type: note/function
---
# Background
- Adds a library called `<name>` to be built from the source files in the command invocation. 
	- If no source files are specified, it will create what is a temporary empty library. Can be filled with [[CMake.target_link_libraries]]

# Usage
```cmake
`add_library(<name> [<type>] [EXCLUDE_FROM_ALL] <sources>...)
```
- By default, makes a `STATIC` library unless a type is invoked

## Making a Library
```cmake
add_library(foo STATIC foo1.c foo2.c)
```
- `foo` is now available for use as a library name everywhere else in the project.
	- CMake will now how to expand the name into the library when needed. 
You get to pick type of library:
- Often you'll need to make a fictional target, that is, one where nothing needs to be compiled (i.e. a header-only library). That is an INTERFACE library. 
- You can also make an `ALIAS` library with an existing library, which simply gives you a new name for a target.

## Adding Object Libraries
See [[CMake target#Object Libraries]] for background
```cmake
add_library(A OBJECT a.cpp)
add_library(B OBJECT b.cpp)
add_library(Combined $<TARGET_OBJECTS:A> $<TARGET_OBJECTS:B>)
```
- `A` and `B` object files are now in the library `Combined`. Object libraries may contain sources (and headers) that compile to object files. 

## Change default type of library
Enable shared libs by default with [[CMake.BUILD_SHARED_LIBS]]