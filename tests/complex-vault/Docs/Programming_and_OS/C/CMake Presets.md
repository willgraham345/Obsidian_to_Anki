---
summary: Configured through the `CMakePresets.json` in the root directory. A way to commonly-configure projects. Allows users to specify common configure options and share them with others. CMake also supports files included with the `include` field.
type: note/configuration
headings:
prev: ["[[CMake Build Configurations]]"]
configuration_of: ["[[CMake]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, January 15th 2026, 2:59:24 pm
template: "[[base_note_template]]"
template-version: 1.0.0
uses: ["[[CMake Build Configurations]]", "[[CMake CLI Environment]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
See [[VSCode CMake Presets]]
Sharing settings in CMake is a mess. There are reasons to have settings configured (CI builds, other users) and other stuff.

## `CMakePresets.json` and `CMakeUserPresets.json`
- CMake makes use of two files in the projects root directory. 
- These files allow common configuration options to be shared with others, and supports files included with the `include` field. 
- Exactly the same format, and both are optional (if `--preset` is specified, you need at least one. )
- Do *not* track `CMakeUserPresets.json` in your git repo. 

[Usage](https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html)