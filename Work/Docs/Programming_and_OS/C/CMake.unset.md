---
type: note
---
# Background
Removes a normal variable from the current scope, causing it to become undefined. If `CACHE` is present, then a cache variable is removed instead of a normal variable.
- If [[CMake.PARENT_SCOPE]] is present, then the variable is removed from the scope above the current scope.
[Docs](https://cmake.org/cmake/help/latest/command/unset.html#command:unset)

# Usage
```cmake
unset(ENV{<variable>})
```