---
type: note
---
# Background
Sets the name of the project
- Also sets variables:
	- [[CMake.PROJECT_SOURCE_DIR]], [[CMake.PROJECT_BINARY_DIR]], [[Cmake PROJECT_IS_TOP_LEVEL]]

## Languages
- By default, the only enabled languages are `C` an `CXX`
- You can use `NONE` to disable all langauges. 
- Add more langauges with [[CMake enable_language]]
## Subprojects
- See [[CMake.add_subdirectory]] for more info on making subprojects
# Usage
- [`project()`](https://cmake.org/cmake/help/latest/command/project.html#command:project "project")
```cmake
project(Tutorial VERSION 1.0)
```
## Setting a Project
```cmake
project(MyProject VERSION 1.0
                  DESCRIPTION "Very nice project"
                  LANGUAGES CXX)
```
- Name of the project is the first argument, whitespace doesn't matter
- `LANGUAGES` can be `C`, `CXX`, `Fortran`, `ASM`, `CUDA`, `CSharp`, and `SWIFT`. 
	- `C CXX` is the default. 
	- [Setting a Project Documentation](https://cmake.org/cmake/help/latest/command/project.html)