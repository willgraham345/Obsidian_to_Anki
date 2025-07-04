---
type: note
---
# Background
- Esssentially tells CMake that it should look in these additional directories for more stuff to do. 
- Adds a subdirectory to build
- If [[CMake EXCLUDE_FROM_ALL]] option is used, the generated project will not appear in the top-level Makefile or IDE project file. 
	- This is useful for generating sub-projects that do not make sense as part of the main build process.

# Usage
- [`add_subdirectory()`](https://cmake.org/cmake/help/latest/command/add_subdirectory.html#command:add_subdirectory "add_subdirectory")
```cmake
add_subdirectory(source_dir [binary_dir] [EXCLUDE_FROM_ALL] [SYSTEM])
```