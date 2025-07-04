---
summary: Targets are the executables, libraries, and utilities built by CMake. Targets store their type  and keep track of general properties.
type: note/concept
down:
  - "[[CMake OUTPUT_NAME]]"
concepts:
  - "[[CMake Binary Targets]]"
  - "[[Cmake target link scopes]]"
functions:
  - "[[CMake add_custom_target]]"
  - "[[CMake get_target_property]]"
  - "[[CMake LINK_FLAGS]]"
  - "[[CMake set_target_properties]]"
  - "[[CMake target_sources]]"
  - "[[CMake.add_library]]"
  - "[[CMake.target_link_libraries]]"
implementations:
  - "[[CMake target_sources]]"
  - "[[CMake Targets Usage Requirements]]"
  - "[[CMake Types of Executables]]"
  - "[[CMake Types of Libraries]]"
  - "[[CMake.add_library]]"
  - "[[CMake.target_include_directories]]"
  - "[[CMake.target_link_libraries]]"
concept_of:
  - "[[CMake]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Monday, April 21st 2025, 12:04:40 pm
---
# Background
- Every [[CMake.add_library]], [[CMake add_custom_target]] command creates a target. 
- In addition to storing their type, targets also keep track of general properties. 
- Targets store a list of libraries that they link against, which are set by using the [[CMake.target_link_libraries]] command. 

## Executable options
By default, an executable will be a traditional console application that has a main entry point. One may specify `WIN32` option to request a WinMain entry point on Windows systems. 

## Specify include directories that are required when linking to a library
See [[CMake.target_include_directories# Specify include directories that are required when linking to a library]]