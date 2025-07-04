---
summary: 
date created: Wednesday, November 13th 2024, 9:45:34 am
date modified: Wednesday, November 13th 2024, 9:46:15 am
type: note/concept
---
`VIEW[**{summary}**][text(renderMarkdown)]`

# Binary Targets
- Defined with [[CMake.add_executable]] and [[CMake.add_library]] commands. 
	- Resulting files have the appropriate `PREFIX`, `SUFFIX` and extensions for the platform targeted. 
- Dependencies between binary targets are expressed with the [[CMake.target_link_libraries]] command
```cmake
add_library(archive archive.cpp zip.cpp lzma.cpp)
add_executable(zipapp zipapp.cpp)
target_link_libraries(zipapp archive)
```
- `archive` here is defined as a `STATIC` library
	- A static library is an archive containing objects compiled from `archive.cpp` `zip.cpp` and `lzma.cpp`.
- `zipapp` is defined as an executable formed by compiling and linking `zipapp.cpp`.
	- When linking the `zipapp` executable, the `archive` static library is linked in. 

## Binary Executables
[[CMake.add_custom_command]] can generate rules to be run at build time that can transparently use an EXECUTABLE target as a `COMMAND` executable. 

## Binary Library Types
### Normal Libraries
- By default, [[CMake.add_library]] defines a `STATIC` library, unless a type is specified. 
	- In context of the buildsystem, the type of a library doesn't really matter. Commands, dependency specification and other APIs work similarly regardless of the library type. 
	- The exception here is the `MODULE` library, because it is generally not linked to. It is a type which is loaded as a plugin using runtime techniques. If the library does not export any unmanaged symbols (Windows resource DLL, C++/CLI DLL), it is required that the library not be a `SHARED` library because CMake expects `SHARED` libraries to export at least one symbol.

#### Apple Frameworks
- I won't be using this lol. See [here](https://cmake.org/cmake/help/latest/manual/cmake-buildsystem.7.html#id21) if something wild happens

### Object Libraries
- Defines a non-archival collection of object files resulting from compiling the given source files. Object files collection may be used as source inputs to other targets by using the syntax:
```cmake
$<TARGET_OBJECT:name>`
```
- This is a generator expression that can be used to supply the `OBJECT` library content to other targets

### Target Properties
### Transitive Usage Requirements
## Build Configurations
## Pseudo Targets
### Target Properties
### Transitive Usage Requirements
## Build Configurations
## Pseudo Targets