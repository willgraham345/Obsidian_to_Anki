---
type: note
---
# Background
Prints values for properties of the given target, source files, directories, tests, or cache entries

# Usage
## Print stuff about targets
```cmake
include(CMakePrintHelpers) # Needed to get the function to work
cmake_print_properties(TARGETS foo bar PROPERTIES
                       LOCATION INTERFACE_INCLUDE_DIRECTORIES)
```
- Prints the `LOCATION` and `INTERFACE_INCLUDE_DIRECTORIES` for both targets `foo` and `bar`

## Print name of each variable followed by value
```cmake
include(CMakePrintHelpers) # Needed to get the function to work
cmake_print_variables(CMAKE_C_COMPILER CMAKE_MAJOR_VERSION DOES_NOT_EXIST)
```