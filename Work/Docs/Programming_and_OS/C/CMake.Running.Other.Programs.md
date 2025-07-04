---
type: note
---
# Background

# Usage
## Run a process and access results
`execute_process`
- Generally a good idea to avoid hard coding a program path into CMake.
- Can also use `${CMAKE_COMMAND}` `find_package(git)` or `find_program` to get access to a command to run
- Use `RESULT_VARIABLE` to check the return code and `OUTPUT_VARIABLE` to get the output. 

### Example that updates all git submodules
```cmake
find_package(Git QUIET)

if(GIT_FOUND AND EXISTS "${PROJECT_SOURCE_DIR}/.git")
    execute_process(COMMAND ${GIT_EXECUTABLE} submodule update --init --recursive
                    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
                    RESULT_VARIABLE GIT_SUBMOD_RESULT)
    if(NOT GIT_SUBMOD_RESULT EQUAL "0")
        message(FATAL_ERROR "git submodule update --init --recursive failed with ${GIT_SUBMOD_RESULT}, please checkout submodules")
    endif()
endif()
```
## Running command at build time
[Running a command at build time](https://cliutils.gitlab.io/modern-cmake/chapters/basics/programs.html)
## Including Common Utilities
See link above