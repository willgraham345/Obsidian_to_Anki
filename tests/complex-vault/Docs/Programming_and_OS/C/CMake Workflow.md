---
summary: "CMake's build process. 5 Steps include: Configuration -> Generation -> Compilation -> Linking -> Installation (optional)"
type: note/process
headings:
  - "[[#Concepts of Note]]"
  - "[[#Diagrams]]"
  - "[[#Examples]]"
  - "[[#Workflows]]"
functions:
  - "[[CMake gtest_discover_tests]]"
processes:
  - "[[CMake Workflow 1 Configuration]]"
  - "[[CMake Workflow 2 Generation]]"
  - "[[CMake Workflow 3 Compilation]]"
  - "[[CMake Workflow#Building Tests]]"
  - "[[CMake Workflow#Calling outside executables]]"
  - "[[CMake Workflow#General process]]"
  - "[[CMake Workflow#Making dependency graphs]]"
  - "[[Cpp GoogleTest Building with CMake]]"
same:
  - "[[Cpp Build Pipeline]]"
similar:
  - "[[GNU make]]"
  - "[[Visual Studio Projects and Solutions]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, January 30th 2026, 11:49:32 am
diagrams:
  - "[[build-process.webp]]"
  - "[[cmake-build.webp]]"
item_of:
  - "[[CMake]]"
items:
  - "[[CMake Adding CMake Helper Functions]]"
  - "[[CMake Adding Library Examples]]"
  - "[[Cmake Build Tree]]"
  - "[[Cmake Source Tree]]"
template: "[[base_note_template]]"
template-version: 1.0.1
process_of:
  - "[[CMake]]"
  - "[[Cpp Build Pipeline]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
### Source File Dependencies

CMake generates dependency files for each source file in a porject.

- A `main.cpp` will have a generated `main.cpp.d` file saved in the `build/` folder hierarchy.

For C/C++ source files, CMake will scan each file for `#include` statements and add these to the list of dependencies for that file. The generated configuration files for the build system will include those dependencies in its build rules.

- Allows the build system to optimize compilation steps.
  ![[cmake-dependency.webp | 300]]

### Processes
##### CMake Main Workflow
 start:
1. [[CMake Workflow 1 Configuration]]
2. [[CMake Workflow 2 Generation]]
3. [[CMake Workflow 3 Compilation]]
 end:

##### Building Tests
 start:
1. [[Cpp gtest Invoking Tests]]
 end:

##### Making dependency graphs
 start:
1. [[CMake GraphViz]]
 end:

##### Calling outside executables
 start:
1. [[CMake Calling Outside Executables]]
 end:

## Diagrams
### Modern build system vs CMake Build System

![[build-process.webp | 700]]
![[cmake-build.webp | 700]]

