---
type: note/workflow
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, January 3rd 2025, 11:48:28 am
workflow_of: ["[[Cpp GoogleTest Invoking Tests]]"]
---
# Background


# Usage
## Declaring a dependency on GoogleTest
### Example
```cmake
cmake_minimum_required(VERSION 3.14)
project(my_project)

# GoogleTest requires at least C++14
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/03597a01ee50ed33e9dfd640b249b4be3799d395.zip
)
# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)
```
- That huge number at the end of the `URL` arg is the Git commit hash. 

## Create and Run a Binary
If you have the dependency set up

