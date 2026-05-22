---
summary: Finds a (usually external to project) package for use within CMake. Calls to this command can also be intercepted by dependency providers. This is typically less reliable than using a Config search.
type:
headings:
  - "[[#Concepts of Note]]"
  - "[[#Properties]]"
  - "[[#Usage]]"
variables:
  - "[[CMake find_package#<PackageName>_FIND_REGISTRY_VIEW]]"
  - "[[CMake find_package#CMAKE_FIND_PACKAGE_NAME]]"
similar:
  - "[[CMake FindPkgConfig]]"
date created: Monday, January 5th 2026, 12:01:43 pm
date modified: Monday, March 9th 2026, 10:40:30 am
tags: [lang/build/packages]
template: "[[base_note_template]]"
template-version: 1.0.2
used_by:
  - "[[CMake Calling Outside Executables]]"
  - "[[CMake modules]]"
uses:
  - "[[CMake CMAKE_MODULE_PATH]]"
  - "[[CMAKE_PREFIX_PATH]]"
---

# Summary
󰙎 CMake find_package ;;; Finds a (usually external to project) package for use within CMake. Calls to this command can also be intercepted by dependency providers. This is typically less reliable than using a Config search.

# Additional Background
[find\_package — CMake 4.2.1 Documentation](https://cmake.org/cmake/help/latest/command/find_package.html#config-mode-version-selection)

## Concepts of Note
- Where possible, projects should find packages using the basic signature.

### Search modes
󰙎 Module mode ;; CMake searches for a file called `Find<PackageName>.cmake`, looking first in [[CMake CMAKE_MODULE_PATH]], then among the [Find Modules](https://cmake.org/cmake/help/latest/manual/cmake-developer.7.html#find-modules). Some find modules provide limited (or no) support for versioning.
󰙎 Config mode ;; CMake searches for a file called `<lowercasePackageName>-config.cmake` or `<PackageName>Config.cmake`. In config mode, the command can be given a list of names to search for as package names. The locations where CMake searches for the config and version files is more complicated than Module mode. These are typically installed as part of the package, so these tend to be more reliable than module mode.

[Config Mode search Procedure](https://cmake.org/cmake/help/latest/command/find_package.html#search-procedure)

## Properties
### Variables
##### CMAKE_FIND_PACKAGE_NAME
- The `PackageName` which is searched for

##### \<PackageName\>\_FIND_REGISTRY_VIEW




## Usage
 `find_package(<PackageName> [<version>] [REQUIRED] [COMPONENTS <components>...])` ;;; Usage for `find_package()` in CMake.
