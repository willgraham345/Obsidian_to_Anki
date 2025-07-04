---
type: note
---
# Background
Should be the first line of every CMakeLists, huge thing

# Usage
- [`cmake_minimum_required()`](https://cmake.org/cmake/help/latest/command/cmake_minimum_required.html#command:cmake_minimum_required "cmake_minimum_required")
```cmake
cmake_minimum_required(VERSION 3.1)
```
- `VERSION` is a special keyword for this function. 
- Starting with `3.12`, you can support a range. 
## New projects should do the following
```cmake
cmake_minimum_required(VERSION 3.7...3.29)

if(${CMAKE_VERSION} VERSION_LESS 3.12)
    cmake_policy(VERSION ${CMAKE_MAJOR_VERSION}.${CMAKE_MINOR_VERSION})
endif()
```
## If old MSVC version, use this:
```cmake
cmake_minimum_required(VERSION 3.7)

if(${CMAKE_VERSION} VERSION_LESS 3.29)
    cmake_policy(VERSION ${CMAKE_MAJOR_VERSION}.${CMAKE_MINOR_VERSION})
else()
    cmake_policy(VERSION 3.29)
endif()
```