---
summary: Specifies where the executable target should look for include files
implements:
  - "[[CMake target]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, October 15th 2024, 5:49:19 pm
type: note/function
---
`VIEW[**{summary}**][text(renderMarkdown)]`

# Usage
- [`target_include_directories()`](https://cmake.org/cmake/help/latest/command/target_include_directories.html#command:target_include_directories "target_include_directories")
Syntax
```cmake
target_include_directories(Tutorial PUBLIC
							"${PROJECT_BINARY_DIR}"
							)
```

## Specify include directories that are required when linking to a library
```cmake
add_library(foo foo.cxx)
target_include_directories(foo PUBLIC
                           "${CMAKE_CURRENT_BINARY_DIR}"
                           "${CMAKE_CURRENT_SOURCE_DIR}"
                           )
```
- Anything that links to the target will automatically have `foo`'s binary and source as directories
	- The order of the include directories brought in through [[CMake Usage Requirements for a Library]], will match the order of the targets in the [[CMake.target_link_libraries]] call. 