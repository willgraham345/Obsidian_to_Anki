---
type: note/function
headings:
  - "[[#Concepts of Note]]"
  - "[[#Examples]]"
  - "[[#Examples]]"
  - "[[#Flashcards]]"
  - "[[#Syntax]]"
  - "[[#Usage]]"
similar:
  - "[[CMake option]]"
prev:
  - "[[CMake set]]"
date created: Monday, March 9th 2026, 4:20:01 pm
date modified: Wednesday, March 11th 2026, 5:31:59 pm
processes: []
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
used_by:
  - "[[CMake function]]"
  - "[[CMake macro]]"
  - "[[CMake option]]"
---

# Summary
󰙎 cmake_parse_arguments ;;; Meant for simplified handling of optional args. Works for both macros and functions. Creates variables for options, one-value, and multi-value arguments, with the prefix in front.

# Additional Background
[cmake\_parse\_arguments — CMake 4.3.0-rc2 Documentation](https://cmake.org/cmake/help/latest/command/cmake_parse_arguments.html)

## Concepts of Note
󰙎 cmake_parse_arguments ;;; parses a caller‑provided argument list (`ARGN`) into prefixed variables for options, one‑value, and multi‑value arguments.

Variables in a function: [[CMake function#variables]]

## Usage
 `cmake_parse_arguments(<PREFIX> <OPTIONS> <ONE_VALUE_ARGS> <MULTI_VALUE_ARGS> <ARGN>)` ;;; typical call inside a CMake function or macro.

### Functions only
 `cmake_parse_arguments(PARSE_ARGV <N> <prefix> <options> <one_value_keywords> <multi_value_keywords>)` ;;; Parse the arguments within a function that come from the `ARGV#` variables of the calling function. Parsing begins with the `N`th argument.

## Syntax
`cmake_parse_arguments(<PREFIX> <OPTIONS> <ONE_VALUE_ARGS> <MULTI_VALUE_ARGS> <ARGN>)`
- `<PREFIX>` – string used as prefix for generated variables (e.g., `MYLIB_`).
- `<OPTIONS>` – list of boolean flags (present=true, absent=false).
- `<ONE_VALUE_ARGS>` – key and single argument
- `<MULTI_VALUE_ARGS>` – list of arguments that accept multiple values.
- `<ARGN>` – the raw argument list passed to the calling function/macro.

## Examples

### Using All args
```cmake
function(my_library name)
    # 1. Define what you expect
    set(options        INSTALL VERBOSE)
    set(oneValueArgs   VERSION OUTPUT_DIR)
    set(multiValueArgs SOURCES INCLUDE_DIRS DEPENDS)

    # 2. Parse — prefix ARG prevents collisions with CMake built-ins
    cmake_parse_arguments(
        ARG                  # prefix
        "${options}"
        "${oneValueArgs}"
        "${multiValueArgs}"
        ${ARGN}              # remaining args after 'name'
    )

    # 3. Use parsed values via ARG_<keyword>
    message(STATUS "Building library: ${name}")
    message(STATUS "  Version:     ${ARG_VERSION}")
    message(STATUS "  Output dir:  ${ARG_OUTPUT_DIR}")
    message(STATUS "  Install:     ${ARG_INSTALL}")   # TRUE or FALSE
    message(STATUS "  Sources:     ${ARG_SOURCES}")   # list
    message(STATUS "  Includes:    ${ARG_INCLUDE_DIRS}")

    # Check for unexpected/unparsed args — good for catching typos
    if(ARG_UNPARSED_ARGUMENTS)
        message(WARNING "Unknown arguments: ${ARG_UNPARSED_ARGUMENTS}")
    endif()

    # Check required args manually (cmake_parse_arguments doesn't enforce them)
    if(NOT ARG_SOURCES)
        message(FATAL_ERROR "my_library() requires SOURCES")
    endif()

    add_library(${name} ${ARG_SOURCES})

    if(ARG_INCLUDE_DIRS)
        target_include_directories(${name} PUBLIC ${ARG_INCLUDE_DIRS})
    endif()

    if(ARG_DEPENDS)
        target_link_libraries(${name} PUBLIC ${ARG_DEPENDS})
    endif()

    if(ARG_VERBOSE)
        message(STATUS "Verbose mode enabled for ${name}")
    endif()

    if(ARG_INSTALL)
        install(TARGETS ${name} DESTINATION lib)
    endif()
endfunction()
```

Calling the above function:
```cmake
my_library(mylib
    VERSION     1.2.3
    OUTPUT_DIR  ${CMAKE_BINARY_DIR}/out
    INSTALL                          # flag — just present, no value
    VERBOSE
    SOURCES
        src/foo.cpp
        src/bar.cpp
    INCLUDE_DIRS
        include/
        third_party/include/
    DEPENDS
        OpenSSL::SSL
        fmt::fmt
)
```

### Using options
```cmake
# Define a function that builds a library with optional behaviors
function(add_my_library TARGET_NAME)

    # cmake_parse_arguments(PREFIX OPTIONS ONE_VALUE_KEYWORDS MULTI_VALUE_KEYWORDS args)
    cmake_parse_arguments(
        ARG                          # Prefix for parsed variables
        "STATIC;ENABLE_WARNINGS;INSTALL"  # Options (boolean flags)
        "OUTPUT_DIR"                 # Single-value keywords
        "SOURCES;INCLUDE_DIRS"       # Multi-value keywords
        ${ARGN}                      # All remaining arguments passed to the function
    )

    # --- Access the parsed OPTION values ---
    # Each OPTION becomes ARG_<OPTION_NAME> and is either TRUE or FALSE

    if(ARG_STATIC)
        set(LIB_TYPE STATIC)
    else()
        set(LIB_TYPE SHARED)
    endif()

    add_library(${TARGET_NAME} ${LIB_TYPE} ${ARG_SOURCES})

    if(ARG_INCLUDE_DIRS)
        target_include_directories(${TARGET_NAME} PUBLIC ${ARG_INCLUDE_DIRS})
    endif()

    if(ARG_ENABLE_WARNINGS)
        message(STATUS "[${TARGET_NAME}] Compiler warnings ENABLED")
        target_compile_options(${TARGET_NAME} PRIVATE -Wall -Wextra)
    endif()

    if(ARG_OUTPUT_DIR)
        set_target_properties(${TARGET_NAME} PROPERTIES
            LIBRARY_OUTPUT_DIRECTORY ${ARG_OUTPUT_DIR}
            ARCHIVE_OUTPUT_DIRECTORY ${ARG_OUTPUT_DIR}
        )
    endif()

    if(ARG_INSTALL)
        message(STATUS "[${TARGET_NAME}] Will be installed")
        install(TARGETS ${TARGET_NAME} DESTINATION lib)
    endif()

endfunction()


# --- Calling the function ---

# With STATIC and ENABLE_WARNINGS options set (flags present = TRUE)
add_my_library(mylib_full
    STATIC                          # <-- Option flag: ARG_STATIC = TRUE
    ENABLE_WARNINGS                 # <-- Option flag: ARG_ENABLE_WARNINGS = TRUE
    INSTALL                         # <-- Option flag: ARG_INSTALL = TRUE
    SOURCES src/foo.cpp src/bar.cpp
    INCLUDE_DIRS include/ third_party/include/
    OUTPUT_DIR ${CMAKE_BINARY_DIR}/lib
)

# Without any options (all option flags default to FALSE / empty)
add_my_library(mylib_minimal
    SOURCES src/foo.cpp
)
```

## Flashcards
󰠗 What variables are created by `cmake_parse_arguments` when the prefix is `FOO_`? ;; `FOO_OPTIONS`, `FOO_ONE_VALUE_ARGS`, `FOO_MULTI_VALUE_ARGS`, `FOO_UNPARSED_ARGUMENTS`, plus a variable for each listed argument name prefixed with `FOO_`.
