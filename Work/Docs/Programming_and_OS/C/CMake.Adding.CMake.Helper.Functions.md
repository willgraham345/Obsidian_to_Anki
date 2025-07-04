---
type: note
---
# Background
Can be great for finding and adding certain modules.

[Common helpers repo](https://github.com/CLIUtils/cmake)

# Usage
## Adding a cmake folder to your CMake path
```cmake
set(CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake" ${CMAKE_MODULE_PATH})
```
