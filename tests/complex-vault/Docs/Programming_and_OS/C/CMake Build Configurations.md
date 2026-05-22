---
summary:
type: note/configuration
headings:
  - "[[#Concepts of Note]]"
  - "[[#Properties]]"
configuration_of:
  - "[[CMake cmake-toolchains]]"
  - "[[CMake Compiler Settings]]"
  - "[[CMake]]"
  - "[[CMake cmake-generators]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, January 15th 2026, 3:00:37 pm
template: "[[base_note_template]]"
template-version: 1.0.1
used_by:
  - "[[CMake Presets]]"
next:
  - "[[CMake Presets]]"
  - "[[CMake Workflow 1 Configuration]]"
configurations:
  - "[[CMake cmake_minimum_required]]"
variables:
  - "[[CMake Build Configurations#CMAKE_PREFIX_PATH: [[CMake CMAKE_PREFIX_PATH]]]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note


Build configs let projects be built in different ways for debug, optimized or any other sort of flag. CMake supports, by default:
- Debug: has most of the basic debug flags turned on
- Release: basic optimizations turned on. 
- MinSizeRel: Flags that produce the smallest object code, but not necessarily the fastest code. 
- RelWithDebInfo: Builds optimized build with debug info as well. 

CMake handles the configurations in slightly different ways depending on the generator being used. The conventions of the native build system are followed when possible.
- Configurations impact the build in different ways when using Makefiles versus using Visual Studio project files. 

### Visual Studio
- Supports Build Configurations.
- Within the IDE, you can select Debug and all sorts of other stuff. 
- The idea puts all binary files into directories with names of the active configuration. 
	- This brings extra complexity for projects that build programs need to be run as part of the build process from custom commands. 

### Makefile-based Generators
## Properties
### Variables
##### CMAKE_PREFIX_PATH: [[CMAKE_PREFIX_PATH]]