---
summary: Cross-platform tool for managing a build process and a much more widely used tool when compared with GNU make. Abstracts the build process, and lets you define complex build processes in a common language.
type: note/system
concepts:
  - "[[CMake Install]]"
  - "[[CMake properties]]"
  - "[[CMake Variables]]"
  - "[[CMake target]]"
components:
  - "[[CMake.cmake-generators]]"
  - "[[CMake CPack]]"
workflows:
  - "[[CMake cmake-toolchains]]"
  - "[[CMake GraphViz]]"
  - "[[CMake Workflow]]"
aliases:
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Wednesday, December 18th 2024, 4:56:44 pm
tags:
---

CMake Tutorial Step I'm on](https://cmake.org/cmake/help/book/mastering-cmake/chapter/Getting%20Started.html)

```breadcrumbs
title: Breadcrumbs down
type: mermaid
field-groups: [downs]
merge-fields: true
sort: field asc
show-attributes: [field]
```

# Unsorted section...

- [[CMake.Modern.CMake.Best.Practice]]
- [[CMake.Template.Example]]
- [[CMake.Running.Other.Programs]]
- [[CMake.build.tool]]
  [[CMake.gui]]

# New Project

[[CMake.cmake.init]]
[[CMake.cmkr]]

# CMake

## CMake Overviews

### Most important overviews

- [[CMake Workflow]]
  - [[CMake cmake-toolchains]]
- [[CMake target]]
- [[CMake.Directory.Structure]]

### Semi-important overviews

- [[CMake.Running.CMake]]
  - [[CMake.Hello.World]]
- [[CMake.Installation.Options]]
- [[CMake.Language.Overview]]
- [[CMake.Cache]]

## Usage

[[CMake CLI commands]]

- [[CMake.Command.Line.Environment]]

### Build/Toolchain System

[[CMake.Invoking.the.Buildsystem]]

- [[CMake.cmake_minimum_required]]
- [[CMake.add_custom_command]]
  [[CMake.Presets]]

#### Build Variables

[[CMake.Build.Configurations]]

- [[CMake.CMAKE_CONFIGURATION_TYPES]]
- [[CMake CMAKE_CROSSCOMPILING]]
- [[CMake.CMAKE_PREFIX_PATH]]
- [[CMake.CMAKE_MODULE_PATH]]
- [[CMake.CMAKE_BUILD_TYPE]]
- [[CMake.CMAKE_INSTALL_PREFIX]]
- [[CMake.CMAKE_TOOLCHAIN_FILE]]
- [[CMake.BUILD_SHARED_LIBS]]
- [[CMake.CMAKE_EXPORT_COMPILE_COMMANDS]]
  [[CMake.cmake-generators]]
- [[CMake CMAKE_GENERATOR_PLATFORM]]

#### Compiler

[[CMake.Compiler.Settings]]

- [[CMake add_compile_options]]
- [[CMake add_compile_definitions]]
- [[CMake.CXX]]
- [[CMake LDFLAGS]]
- [[CMake CXXFLAGS]]
- [[CMake CFLAGS]]
- [[CMake CMAKE_CXX_CFLAGS]]
- [[CMake CMAKE_C_CFLAGS]]

##### Visual Studio

- [[CMake.CMAKE_CFG_INTDIR]]

#### Linker Options

- [[CMake.add_link_options]]

#### Toolchain

- [[CMake.toolchain.variables.and.properties]]
  - [[CMake.CMAKE_TOOLCHAIN_FILE]]
  - [[CMake CMAKE_SYSTEM_NAME]]
  - [[CMake CMAKE_SYSTEM_VERSION]]
  - [[CMake CMAKE_C_COMPILER]]
  - [[CMake CMAKE_CXX_COMPILER]]

### Flow control

#### Conditionals

- [[CMake.if]]
- [[CMake.option]]

#### Functions

- [[CMake.function]]
- [[CMake macro]]

#### Looping Constructs

- [[CMake.foreach]]
- [[CMake.while]]
- [[CMake break]]

### Targets

- [[CMake target]]
  - [[CMake ALIAS targets]]
- [[CMake add_custom_targets]]
- [[CMake set_target_properties]]
- [[CMake get_target_property]]
- [[CMake LINK_FLAGS]]
- [[CMake.file]]
- [[CMake.cmake_path]]
- [[CMake.configure_file]]

#### Executables

- [[CMake.add_executable]]
- [[CMake.target_compile_definitions]]

#### Libraries

- [[CMake.add_library]]
  - [[CMake.Adding.a.Library.Examples]]
- [[CMake.target_link_libraries]]
- [[CMake.add_subdirectory]]
  - [[CMake EXCLUDE_FROM_ALL]]
- [[CMake.include]]
- [[CMake.target_include_directories]]
- [[CMake set_directory_properties]]
- [[CMake set_tests_properties]]
- [[CMake add_test]]
- [[CMake.Adding.CMake.Helper.Functions]]

#### Source files

- [[CMake set_source_files_properties]]
- [[CMake get_source_file_properties]]

#### Misc

- [[CMake Install]]

### Miscelleaneous

#### Naming and Versioning

- [[CMake.CMAKE_CXX_STANDARD]]
- [[CMake.CMAKE_CXX_STANDARD_REQUIRED]]

##### Project

- [[CMake.project]]
  - [[CMake.PROJECT_SOURCE_DIR]]
  - [[CMake.PROJECT_BINARY_DIR]]
  - [[CMake PROJECT_IS_TOP_LEVEL]]
- [[CMake enable_language]]

#### Regular Expressions

- [[CMake.string]]

### Variables

[[CMake Variables]]

- [[CMake.set]]
  - [[CMake.PARENT_SCOPE]]
- [[CMake.unset]]
- [[CMake Transformations]]

### Visualizing/Debugging

[[CMake GraphViz]]
[[CMake.message]]
[[CMake.cmake_print_variables]]

## CMake Modules

[[CMake cmake-modules]]

### Find Modules

### Utility Modules

- [[CMake.ExternalProject]]
- [[CMake.FetchContent]]

# Including Other Packages

[[CMake GoogleTest Building]]

# Misc

[What's new in CMake (abbreviated version)](https://cliutils.gitlab.io/modern-cmake/chapters/intro/newcmake.html)
