---
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Wednesday, October 16th 2024, 11:07:49 am
type: note
---
# Background
Adds compile definitions to a [[CMake target]]
- Target must have been created by [[CMake.add_executable]] or [[CMake.add_library]] and must NOT be an [[CMake ALIAS target]]

# Usage
- [`target_compile_definitions()`](https://cmake.org/cmake/help/latest/command/target_compile_definitions.html#command:target_compile_definitions "target_compile_definitions")
```
target_compile_definitions(<target>
  <INTERFACE|PUBLIC|PRIVATE> [items1...]
  [<INTERFACE|PUBLIC|PRIVATE> [items2...] ...])
```