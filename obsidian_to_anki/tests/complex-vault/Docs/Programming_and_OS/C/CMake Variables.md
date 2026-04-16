---
summary:
type: note/concept
headings:
  - "[[#Concepts of Note]]"
  - "[[#Properties]]"
  - "[[#Usage]]"
functions:
  - "[[CMake cmake_print_variables]]"
  - "[[CMake set]]"
  - "[[CMake string]]"
  - "[[CMake unset]]"
variables:
  - "[[CMake Variables#[[CMake PARENT_SCOPE]]]]"
down:
concepts:
  - "[[CMake visibility]]"
similar:
  - "[[CMake visibility]]"
concept_of:
  - "[[CMake]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Monday, March 9th 2026, 10:33:23 am
item_of:
  - "[[CMake]]"
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
uses:
  - "[[Graphviz]]"
---

# Summary
󰙎 CMake Variables ;;; 

# Additional Background
[CMake Variables Manual](https://cmake.org/cmake/help/latest/manual/cmake-variables.7.html#manual:cmake-variables(7))

> [!WARNING]
> Avoiding naming variables `CMAKE_`, `_CMAKE_`, and that begin with `_`. CMake reserves these variables for itself. All CMake variables are stored internally as strings.

## Concepts of Note
### Variable types
1. Normal variable
2. Cache entry
3. Environment variable

### Variable Scope
Block scope
Function scope
Directory scope
Persistent cache

#### Environment variables
Just like normal variables, except with global scope and never cached. [Link](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#id32)

## Usage
### Accessing Variables
```cmake
	set(Foo a b c)    # 3 unquoted args -> value is "a;b;c"
	command(${Foo})   # unquoted arg replaced by a;b;c
	                  # and expands to three arguments
	command("${Foo}") # quoted arg value is "a;b;c"
	set(Foo "")       # 1 quoted arg -> value is empty string
	command(${Foo})   # unquoted arg replaced by empty string
	                  # and expands to zero arguments
	command("${Foo}") # quoted arg value is empty string
```

### Checking if a Variable has been Set
```cmake
	if(NOT DEFINED ${VAR_NAME})
```