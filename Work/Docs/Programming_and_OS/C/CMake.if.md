---
type: note
---
# Background
- Creates a conditional within CMake

# Usage

- [`if()`](https://cmake.org/cmake/help/latest/command/if.html#command:if "if")
```
if(<condition>)
  <commands>
elseif(<condition>) # optional block, can be repeated
  <commands>
else()              # optional block
  <commands>
endif()
```