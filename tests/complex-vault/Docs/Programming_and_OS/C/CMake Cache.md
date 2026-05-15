---
summary: The "configuration" of CMake, which is written to a file called CMakeCache.txt
type: note/configuration
headings: ["[[#Concepts of Note]]"]
configuration_of: ["[[CMake]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, January 15th 2026, 3:18:54 pm
template: "[[base_note_template]]"
template-version: 1.0.1
used_by: ["[[CMake Build Configurations]]"]
uses: ["[[CMake option]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
The CMake cache can be thought of as a configuration file. 
- When CMake is run for the first time, it produces a `CMakeCache.txt` file in the top directory of the build tree. 
- The file is used to store global cache variables, whose values persist across multiple runs within a project build tree. 

Purposes
- Store users selections and choices ([[CMake option]] wouldn't need to be run again)
- Persistently store values between CMake runs. 
	- Typically system-dependent variables. 

Init args
- Arguments passed to CMake that set values before any scripts are run, which allow you to control build settings. 
- On the [[CMake CLI Environment]], these appear as `-D` arguments.

[More info on Caches](https://cmake.org/cmake/help/book/mastering-cmake/chapter/CMake%20Cache.html)

