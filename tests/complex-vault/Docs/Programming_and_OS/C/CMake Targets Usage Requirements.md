---
summary: Usage requirements affect compilation of sources in the `<target>`, and are specified by properties defined on linked targets.
type: note/concept
headings:
implements:
  - "[[CMake target]]"
aliases: []
date created: Tuesday, October 15th 2024, 5:44:45 pm
date modified: Monday, February 23rd 2026, 11:27:54 am
keywords:
  - "[[CMake INTERFACE]]"
  - "[[CMake PRIVATE]]"
  - "[[CMake PUBLIC]]"
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
used_by:
---

# Summary
󰙎 Target Usage requirements ;; `PRIVATE`, `PUBLIC`, and `INTERFACE` control **how dependencies and properties propagate** between targets. You'll see them most often in commands like

# Additional Background


- [`target_compile_definitions()`](https://cmake.org/cmake/help/latest/command/target_compile_definitions.html#command:target_compile_definitions "target_compile_definitions")
- [`target_compile_options()`](https://cmake.org/cmake/help/latest/command/target_compile_options.html#command:target_compile_options "target_compile_options")
- [`target_include_directories()`](https://cmake.org/cmake/help/latest/command/target_include_directories.html#command:target_include_directories "target_include_directories")
- [`target_link_directories()`](https://cmake.org/cmake/help/latest/command/target_link_directories.html#command:target_link_directories "target_link_directories")
- [`target_link_options()`](https://cmake.org/cmake/help/latest/command/target_link_options.html#command:target_link_options "target_link_options")
- [`target_precompile_headers()`](https://cmake.org/cmake/help/latest/command/target_precompile_headers.html#command:target_precompile_headers "target_precompile_headers")
- [`target_sources()`](https://cmake.org/cmake/help/latest/command/target_sources.html#command:target_sources "target_sources")
