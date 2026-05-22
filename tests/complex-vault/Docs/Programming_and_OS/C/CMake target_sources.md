---
summary: "Specifies sources to use when building a target and/or its dependents. The target needs to have been created before this. Scope is designated with: `PRIVATE`, `PUBLIC`, or  `INTERFACE`."
type: note/function
headings:
implements:
  - "[[CMake target]]"
  - "[[CMake visibility]]"
similar:
  - "[[CMake target_link_libraries]]"
prev:
  - "[[CMake add_custom_target]]"
  - "[[CMake add_executable]]"
  - "[[CMake add_library]]"
date created: Wednesday, October 16th 2024, 11:08:17 am
date modified: Wednesday, March 18th 2026, 8:41:31 pm
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
used_by:
  - "[[CMake target]]"
uses:
  - "[[CMake file_sets]]"
---

# Summary
󰙎 CMake target_sources ;; Tells cmake the sources to use with a target (and its dependents), and the visibility around that target.

# Additional Background
- [target\_sources — CMake 3.31.0-rc1 Documentation](https://cmake.org/cmake/help/latest/command/target_sources.html)
- Targets created by [[CMake add_custom_target]] can only use [[CMake PRIVATE]] scope
- See [[CMake file_sets]] for the FILE_SET form

## Syntax
```cmake
target_sources(<target>
  <INTERFACE|PUBLIC|PRIVATE> [items...]
  [FILE_SET <set> [TYPE <type>] [BASE_DIRS <dirs>...] [FILES <files>...]]...)
```

## Concepts of Note

󰙎 Visibility ;;; [[CMake visibility]] — [[CMake PRIVATE]] sources are consumed by the target only; [[CMake PUBLIC]] also propagate to dependents; [[CMake INTERFACE]] propagate without being consumed by the target itself.

󰙎 FILE_SET ;;; Structured attachment of headers or modules to a target; enables install-aware propagation. See [[CMake file_sets]].

󰙎 BASE_DIRS ;;; Root directory used to compute install-relative paths for headers declared in a file set.

󰙎 Transitive propagation ;;; Sources declared [[CMake PUBLIC]] or [[CMake INTERFACE]] flow to any target that links against this one.

## Examples

### Library
```cmake
add_library(mylib STATIC)
target_sources(mylib
  PRIVATE src/foo.cpp src/bar.cpp
  PUBLIC FILE_SET HEADERS FILES include/foo.h include/bar.h)
```
`PUBLIC FILE_SET HEADERS` exposes headers to consumers without adding them to the compilation unit list.

### Library with FILE_SET (explicit BASE_DIRS)
```cmake
add_library(mylib STATIC)
target_sources(mylib
  PRIVATE src/foo.cpp
  PUBLIC
    FILE_SET HEADERS
    BASE_DIRS include
    FILES include/mylib/foo.h include/mylib/bar.h)
```
`BASE_DIRS` scopes the install-relative path — consumers get `mylib/foo.h`, not the full source path.

### Executable
```cmake
add_executable(myapp)
target_sources(myapp
  PRIVATE src/main.cpp src/util.cpp)
```

### Custom Target
```cmake
add_custom_target(gen_code COMMAND my_codegen)
target_sources(gen_code PRIVATE generated/out.cpp)
```
[[CMake add_custom_target]] targets accept only [[CMake PRIVATE]] scope — [[CMake INTERFACE]] and [[CMake PUBLIC]] are not permitted.
