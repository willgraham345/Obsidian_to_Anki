---
summary: The different types of CMake libraries. Typical usage has Static, shared, and modules.
date created: Tuesday, October 15th 2024, 5:41:16 pm
date modified: Tuesday, October 15th 2024, 5:42:26 pm
type: note/concept
implements:
  - "[[CMake target]]"
---

# Types of Library
## Normal Libraries
- `STATIC`: Archive of object files for use when linking other targets
- `SHARED`: Dynamic library that may be linked by other targets and loaded at runtime
- `MODULE`: Plugin that may not be linked by other targets, but may be dynamically loaded at runtime

## Optimized or Debug Libraries with a target
If you label a library with `debug` or `optimized`, then that library will only be linked in with the appropriate config type. 
```cmake
add_executable(foo foo.c)
target_link_libraries(foo debug libdebug optimized libopt)
```

## Object Libraries
- Large projects often organize their source files into groups, perhaps separate subdirectories, that each need different include directories and preprocessor definitions. 
- An Object Library is a collection of source files compiled into an object file which is not linked into a library file or made into an archive. 
	- Other targets created by [[CMake.add_library]] or [[CMake.add_executable]] may reference the objects using an expression of the form `$<TARGET_OBJECTS:name>` as a source, where `name` is the target crated by the [[CMake.add_library]] call. 
	See example of creating an object library 

## Source Files
- Source file structure is very similar to target. It stores the filename, extension, and a number of general properties related to a source file. Like targets, you can set and get properties using [[CMake set_source_files_properties]] and [[CMake get_source_file_properties]]

## Directories, tests, and properties
- In addition to targets and source files, you may find your self working with other objects like directories and tests. This usually means [[CMake set_directory_properties]] and [[CMake set_tests_properties]].