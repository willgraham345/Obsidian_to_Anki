---
summary: A property is a key value pair attached to an object.
type: note/concept
headings:
functions:
  - "[[CMake set_property]]"
concept_of:
  - "[[CMake target]]"
  - "[[CMake]]"
date created: Thursday, October 17th 2024, 1:03:18 pm
date modified: Monday, March 2nd 2026, 4:21:24 pm
implementations:
  - "[[CMake set_property]]"
item_of:
  - "[[CMake]]"
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
uses:
  - "[[CMake OUTPUT_NAME]]"
---

# Summary
󰙎 CMake properties ;;; Key value pair attached to an object. These are often all caps letters defined within CMake somewhere.

# Additional Background
[cmake-properties(7) — CMake 3.31.0-rc2 Documentation](https://cmake.org/cmake/help/latest/manual/cmake-properties.7.html)
- Global Scope
- Directory scope
- Target Scope
- 

# Background
## Property Scope
- **GLOBAL**: Applies to the entire CMake project and is accessible anywhere in the project.
- **DIRECTORY**: Applies to a specific directory (and optionally its subdirectories) and affects targets, tests, and other entities in that directory.
- **TARGET**: Applies to individual targets like executables or libraries, affecting how they are built and linked.
- **SOURCE**: Applies to individual source files, influencing their specific compilation options or behaviors.
- **INSTALL**: Applies to installation rules, controlling how targets or files are installed.
- **TEST**: Applies to individual tests, defining how tests are executed or reported.
- **CACHE**: Applies to cache variables, modifying their behavior within the CMake cache (persisted settings between runs).
