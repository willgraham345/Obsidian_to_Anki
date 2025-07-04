---
type: note
---
# Background
- Tells CMake to create an executable using the specified source files. 

# Usage
- [`add_executable()`](https://cmake.org/cmake/help/latest/command/add_executable.html#command:add_executable "add_executable")
## Making an Executable
```cmake
add_executable(one two.cpp three.h)
```
- `one` is the name of the executable file generated, and the name of the CMake target created.
- Source file comes next (add as many as you like, and CMake will only compile source file extensions)
- Headers will for most intents and purposes be ignored. The only reason to add them is to get them to show up in IDEs. 
- See more about this in [[CMake Workflow]]