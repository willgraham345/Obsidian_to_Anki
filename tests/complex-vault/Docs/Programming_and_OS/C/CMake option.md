---
summary:
type: note/function
headings:
  - "[[#Concepts of Note]]"
  - "[[#Syntax]]"
  - "[[#Usage]]"
  - "[[#Workflows]]"
similar:
  - "[[CMake cmake_parse_arguments]]"
aliases: []
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Wednesday, March 11th 2026, 3:37:49 pm
function_of:
  - "[[CMake]]"
id: CMake option
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
used_by:
  - "[[CMake Cache]]"
  - "[[CMake CLI commands]]"
  - "[[CMake CLI Environment]]"
  - "[[CMake function]]"
uses:
  - "[[CMake cmake_parse_arguments]]"
---

# Summary
󰙎 CMake option ;;; Boolean cache entry that can be toggled by the user.

# Additional Background
- [`option()`](https://cmake.org/cmake/help/latest/command/option.html#command:option "option")

## Concepts of Note
- Provide a boolean option that the user can optionally select. This is set into the [[CMake Cache]]

## Syntax
 `option(VAR_TO_REF "helpString" ON)` ;;; Sets an optional variable `VAR_TO_REF` with a default value of `ON`. This optional variable can be set on the command line. `'helpString'` will be displayed when `cmake -LAH` is selected.

### Processes
 start:
1. Declare the option with `option(<var> "<help>" [value])` → adds `<var>` to the CMake cache.  
2. Users can change the value via `-D<var>=ON|OFF` on the command line or through a GUI.  
3. CMake scripts read the variable to decide which parts of the build to enable.
 end:

## Usage
- **Name**: `<variable>` (e.g., `ENABLE_FEATURE`)  
- **Type**: BOOL  
- **Default**: `[value]` (`ON` or `OFF`)  
- **Help Text**: `<help_text>` – shown in `cmake-gui` and `ccmake`.
 `option(ENABLE_FEATURE "Enable optional feature" OFF)` ;;; declares a boolean cache entry named `ENABLE_FEATURE` with a default of `OFF`.  
 `if(ENABLE_FEATURE)` ;;; conditionally compiles or links code when the option is `ON`.  
