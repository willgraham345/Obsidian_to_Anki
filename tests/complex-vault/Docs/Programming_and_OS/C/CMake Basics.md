---
summary:
type: note/concept
headings:
  - "[[#Concepts of Note]]"
  - "[[#Properties]]"
functions:
  - "[[CMake Basics#[[CMake if]]]]"
  - "[[CMake Basics#[[CMake set]]]]"
  - "[[CMake Basics#[[CMake target_link_libraries]]]]"
variables:
  - "[[CMake Basics#BUILD_SHARED_LIBS CMAKE BUILD_SHARED_LIBS]]"
  - "[[CMake Basics#CMAKE_BUILD_TYPE CMAKE_BUILD_TYPE]]"
  - "[[CMake Basics#CMAKE_INSTALL_PREFIX: [[CMAKE_INSTALL_PREFIX]]]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Wednesday, March 18th 2026, 8:11:57 pm
tags: []
template: "[[base_note_template]]"
template-version: 1.0.1
concept_of:
  - "[[CMake]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note


CMake takes one or more `CMakeLists` files as input and produces project files or Makefiles for use with a wide variety of native development tools. 
Typical process goes like this:
1. Project is defined in one or more CMakeLists files
2. CMake configures and generates the project
3. Users build project with their favorite development tool


Unless otherwise noted, you should always make a build directory and build from there. 
- Building in-source is possible, but you need to be careful. 

## Properties
### functions
##### [[CMake set]]
##### [[CMake target_link_libraries]]

##### [[CMake if]]

##### [[CMake project]]


### variables
##### CMAKE_BUILD_TYPE: [[CMAKE_BUILD_TYPE]]

##### CMAKE_INSTALL_PREFIX: [[CMAKE_INSTALL_PREFIX]]

##### BUILD_SHARED_LIBS: [[CMAKE BUILD_SHARED_LIBS]]