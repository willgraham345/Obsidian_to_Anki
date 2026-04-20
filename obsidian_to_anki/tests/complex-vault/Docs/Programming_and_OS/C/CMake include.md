---
type: note
---
# Background
Load and run CMake code from a file or module.
- Variable reads and writes access the scope of the caller
[include docs](https://cmake.org/cmake/help/latest/command/include.html#command:include)

# Usage
```cmake
include(<file|module> [OPTIONAL] [RESULT_VARIABLE <var>]
                      [NO_POLICY_SCOPE])
```
- If `OPTIONAL` is present, then no error is raised if the file does not exist. 
- If a module is specified instead of a file, then the file with the name `<modulename>.cmake` is searched first in `CMAKE_MODULE_PATH`, then in the CMake module directory. 