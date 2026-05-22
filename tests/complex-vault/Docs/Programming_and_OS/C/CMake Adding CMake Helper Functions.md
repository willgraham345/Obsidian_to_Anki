---
summary:
type: note
headings:
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, January 30th 2026, 11:51:14 am
template:
template-version:
---

# Background
Can be great for finding and adding certain modules.

[Common helpers repo](https://github.com/CLIUtils/cmake)

# Usage
## Adding a cmake folder to your CMake path
```cmake
set(CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake" ${CMAKE_MODULE_PATH})
```
