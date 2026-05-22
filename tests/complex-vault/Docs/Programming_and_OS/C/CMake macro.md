---
summary:
type: note/concept
headings:
  - "[[#Examples]]"
similar:
  - "[[CMake function]]"
concept_of:
  - "[[CMake]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Monday, March 9th 2026, 4:09:27 pm
item_of:
  - "[[CMake]]"
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
uses:
  - "[[CMake cmake_parse_arguments]]"
---

# Summary
󰙎 CMake macro ;;; Almost identical to [[CMake function]], but it doesn't push & pop new variable scope. Arguments are replaced as strings prior to execution, similar to C/C++.

# Additional Background
Supports defining macros that take variable argument lists.
- Can be useful if you want to define a macro that has optional arguments or multiple signatures. 
	- Variable arguments can be referenced by using `ARGC`, `ARGV0`, `ARGV1`, etc. (see [[Cpp argv argc envp]] for more info)

## Usage
 `macro(InstallBall ball1 ball2)`
      `other_fn(ball1 ball2)`
      `endmacro()` ;;; Creates a macro called `InstallBall`, which takes in 2 arguments (`ball1`, `ball2`). This macro calls `other_fn` with both args before ending.

## Examples
### Create a macro titled `assert`
```cmake
# define a simple macro
macro(assert TEST COMMENT)
  if(NOT ${TEST})
    message("Assertion failed: ${COMMENT}")
  endif()
endmacro()

# use the macro
find_library(FOO_LIB foo /usr/local/lib)
assert(${FOO_LIB} "Unable to find library foo")
```
- The first part of the macro is a value to test, the second is a comment to print out if the test fails

### Example Variable-list macro
```cmake
# define a macro that takes at least two arguments
# (the formal arguments) plus an optional third argument
macro(assert TEST COMMENT)
  if(NOT ${TEST})
    message("Assertion failed: ${COMMENT}")

    # if called with three arguments then also write the
    # message to a file specified as the third argument
    if(${ARGC} MATCHES 3)
      file(APPEND ${ARGV2} "Assertion failed: ${COMMENT}")
    endif()

  endif()
endmacro()

# use the macro
find_library(FOO_LIB foo /usr/local/lib)
assert(${FOO_LIB} "Unable to find library foo")
```
- Two required arguments to the macro are `TEST` and `COMMENT`. 
