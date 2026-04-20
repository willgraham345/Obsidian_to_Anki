---
summary: Targets are the executables, libraries, and utilities built by CMake. Targets store their type and keep track of general properties.
type: note/concept
headings:
  - "[[#Concepts of Note]]"
concepts:
  - "[[CMake properties]]"
  - "[[CMake visibility]]"
concept_of:
  - "[[CMake]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Wednesday, March 18th 2026, 8:16:52 pm
implementations:
  - "[[CMake add_library]]"
  - "[[CMake Libraries]]"
  - "[[CMake target_include_directories]]"
  - "[[CMake target_link_libraries]]"
  - "[[CMake target_sources]]"
  - "[[CMake Targets Usage Requirements]]"
  - "[[CMake visibility]]"
item_of:
  - "[[CMake]]"
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
uses:
  - "[[CMake add_custom_target]]"
  - "[[CMake configure_file]]"
  - "[[CMake get_target_property]]"
  - "[[CMake LINK_FLAGS]]"
  - "[[CMake OUTPUT_NAME]]"
  - "[[CMake set_target_properties]]"
  - "[[CMake target_compile_definitions]]"
  - "[[CMake target_link_libraries]]"
  - "[[CMake target_sources]]"
---

# Summary
󰙎 CMake target ;;; Targets are the executables, libraries, and utilities built by CMake. Targets store their type and keep track of general properties.

# Additional Background
## Concepts of Note

- Every [[CMake add_library]], [[CMake add_custom_target]] command creates a target. 
- In addition to storing their type, targets also keep track of general properties. 
- Targets store a list of libraries that they link against
	- Set by using the [[CMake target_link_libraries]] command. 

### Specify include directories that are required when linking to a library
See [[CMake target_include_directories# Specify include directories that are required when linking to a library]]

### Types of Targets
#### Binary (executable) targets
By default, an executable will be a traditional console application that has a main entry point. One may specify `WIN32` option to request a WinMain entry point on Windows systems. 
[[CMake Binary Targets]]

#### Library Targets
[[CMake Libraries]]
- ![[CMake Libraries#^836cee]]
- ![[CMake Libraries#^ece787]]

#### Target Visibility
[[CMake visibility]]

### How targets are used
Defined within [[CMake visibility#Target Visibility]]