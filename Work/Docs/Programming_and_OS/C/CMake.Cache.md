---
type: note
---
# Background
The CMake cache can be thought of as a configuration file. 
- When CMake is run for the first time, it produces a `CMakeCache.txt` file in the top directory of the build tree. 
- The file is used to store global cache variables, whose values persist across multiple runs within a project build tree. 
## Purposes to the Cache
- Store users selections and choices ([[CMake.option]] wouldn't need to be run again)
- Persistently store values between CMake runs. 
	- Typically system-dependent variables. 
## Cache Initializer Arguments
- Arguments passed to CMake that set values before any scripts are run, which allow you to control build settings. 
- On the [[CMake.Command.Line.Environment]], these appear as `-D` arguments.

[More info on Caches](https://cmake.org/cmake/help/book/mastering-cmake/chapter/CMake%20Cache.html)
# Usage
- Don't directly edit the cache file. Cache files contain full paths.
