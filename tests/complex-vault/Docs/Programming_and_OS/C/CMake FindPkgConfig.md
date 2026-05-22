---
summary: A module for CMake, originally developed by FreeDesktop. Provides a few functions that load and configure modules.
type:
headings: ["[[#Properties]]", "[[#Usage]]"]
functions: ["[[CMake FindPkgConfig#pkg_check_modules()]]"]
variables: ["[[CMake FindPkgConfig#\\<XXX>\\_FOUND]]"]
similar: ["[[CMake find_package]]"]
date created: Monday, January 5th 2026, 12:44:09 pm
date modified: Thursday, January 8th 2026, 5:19:55 pm
template: "[[base_note_template]]"
template-version: 1.0.1
used_by: ["[[CMake modules]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Properties

### Variables
##### \<XXX>\_FOUND
### Functions
##### pkg_check_modules()
- Checks for all the given modules, setting a variety of result variables in the calling scope.
[FindPkgConfig — CMake 4.2.1 Documentation](https://cmake.org/cmake/help/latest/module/FindPkgConfig.html#command:pkg_check_modules)

## Usage
 `find_package(PkgConfig [<version>] [QUIET] [REQUIRED] [...])` ;; Basic usage of FindPkgConfig in Cmake
