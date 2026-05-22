---
summary: The different types of CMake libraries. Typical usage has Static, shared, and modules.
type: note/concept
headings:
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
functions:
  - "[[CMake add_library]]"
implements:
  - "[[CMake visibility]]"
  - "[[CMake target]]"
"":
date created: Tuesday, October 15th 2024, 5:41:16 pm
date modified: Monday, March 2nd 2026, 4:19:11 pm
items:
  - "[[CMake Libraries Shared]]"
  - "[[CMake Libraries Static]]"
tags: []
template: "[[base_note_template]]"
template-version: 1.0.1
uses:
  - "[[CMake add_library]]"
  - "[[CMake add_subdirectory]]"
  - "[[CMake BUILD_SHARED_LIBS]]"
  - "[[CMake include]]"
  - "[[CMake target_include_directories]]"
  - "[[CMake target_link_libraries]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
### Library Terms
󰙎 Static librares ;;; Archives of object files, produced by the archiver. These may be dependencies for executables, shared libs, or module libs.  ^836cee

󰙎 Shared libraries ;;; Created by LINKING object files together. Linkers record references to shared libraries in consuming binaries. At runtime, a dynamic loader searches for referenced libraries on disk and loads their symbols. ^ece787

󰙎 Module libraries ;;; Binary that is created by linking object files together. May *not* be linked by other binaries as a dependency. Plugins that an app can dynamically load at runtime.

󰙎 Object Libraries ;;; Collections of object files created from compiled source files without archiving or linking.

## Usage
### Optimized or Debug Libraries with a target
If you label a library with `debug` or `optimized`, then that library will only be linked in with the appropriate config type. 
```cmake
add_executable(foo foo.c)
target_link_libraries(foo debug libdebug optimized libopt)
```

### Object Libraries
- Large projects often organize their source files into groups, perhaps separate subdirectories, that each need different include directories and preprocessor definitions. 
- An Object Library is a collection of source files compiled into an object file which is not linked into a library file or made into an archive. 
	- Other targets created by [[CMake add_library]] or [[CMake add_executable]] may reference the objects using an expression of the form `$<TARGET_OBJECTS:name>` as a source, where `name` is the target crated by the [[CMake add_library]] call. 
	See example of creating an object library 

### Source Files
- Source file structure is very similar to target. It stores the filename, extension, and a number of general properties related to a source file. Like targets, you can set and get properties using [[CMake set_source_files_properties]] and [[CMake get_source_file_properties]]

### Directories, tests, and properties
- In addition to targets and source files, you may find your self working with other objects like directories and tests. This usually means [[CMake set_directory_properties]] and [[CMake set_tests_properties]].