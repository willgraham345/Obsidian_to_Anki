---
summary: Sets the name of a project
type: note
headings: ["[[#Concepts of Note]]", "[[#Examples]]", "[[#Properties]]", "[[#Usage]]"]
variables: ["[[CMake project#[[PROJECT_BINARY_DIR]]]]", "[[CMake project#PROJECT_IS_TOP_LEVEL]]", "[[CMake project#PROJECT_SOURCE_DIR]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, January 9th 2026, 6:25:56 pm
template: "[[base_note_template]]"
template-version: 1.0.1
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
Sets the name of the project
- Also sets variables:
	- [[PROJECT_SOURCE_DIR]], [[PROJECT_BINARY_DIR]], [[PROJECT_IS_TOP_LEVEL]]

## Concepts of Note

You can 
- By default, the only enabled languages are `C` an `CXX`
- You can use `NONE` to disable all langauges. 
- Add more langauges with [[CMake enable_language]]

### Subprojects
- See [[CMake add_subdirectory]] for more info on making subprojects

## Properties

### Variables
##### [[PROJECT_SOURCE_DIR]]
##### [[PROJECT_BINARY_DIR]]
##### [[PROJECT_IS_TOP_LEVEL]]


## Usage

- [`project()`](https://cmake.org/cmake/help/latest/command/project.html#command:project "project")
 `project(Tutorial VERSION 1.0)` ;;; Sets the name of the cmake project to "Tutorial" and the version number to 1.0.

## Examples


```cmake
project(MyProject VERSION 1.0
                  DESCRIPTION "Very nice project"
                  LANGUAGES CXX)
```
- Name of the project is the first argument, whitespace doesn't matter
- `LANGUAGES` can be `C`, `CXX`, `Fortran`, `ASM`, `CUDA`, `CSharp`, and `SWIFT`. 
	- `C CXX` is the default. 
	- [Setting a Project Documentation](https://cmake.org/cmake/help/latest/command/project.html)
