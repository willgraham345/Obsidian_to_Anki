---
summary: "How the system is built and automated. Has 5 steps: Configuration -> Generation -> Compilation -> Linking -> Installation (optional)"
type: note/system
components:
  - "[[Cmake Build Tree]]"
  - "[[Cmake Source Tree]]"
workflows:
  - "[[CMake Workflow 1 Configuration]]"
  - "[[CMake Workflow 2 Generation]]"
  - "[[CMake Workflow 3 Compilation]]"
  - "[[Cpp GoogleTest Building with CMake]]"
same:
  - "[[Cpp Build Pipeline]]"
similar:
  - "[[GNU make]]"
  - "[[Visual Studio Projects and Solutions]]"
component_of:
  - "[[CMake]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, January 3rd 2025, 11:29:00 am
functions:
  - "[[CMake gtest_discover_tests]]"
workflow_of:
  - "[[CMake]]"
---

# CMake Buildsystems

## Modern build system vs CMake Build System

![[build-process.webp | 330]] ![[cmake-build.webp | 330]]

## Steps of the Build System

![[CMake Workflow.png | 500]]

```breadcrumbs
type: mermaid
fields: [workflows, concepts]
merge-fields: true
sort: basename asc
show-attributes: [field]
```

### Source File Dependencies

CMake generates dependency files for each source file in a porject.

- A `main.cpp` will have a generated `main.cpp.d` file saved in the `build/` folder hierarchy.

For C/C++ source files, CMake will scan each file for `#include` statements and add these to the list of dependencies for that file. The generated configuration files for the build system will include those dependencies in its build rules.

- Allows the build system to optimize compilation steps.
  ![[cmake-dependency.webp | 300]]

# Usage

For debugging, see
