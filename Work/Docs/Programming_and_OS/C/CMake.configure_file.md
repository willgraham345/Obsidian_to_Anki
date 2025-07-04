---
type: note
---
# Background
[configure_file docs](https://cmake.org/cmake/help/latest/command/configure_file.html)
Copy a file to another location and modify its contents. 
- Copies an `<input>` file to an `<output>` file while performing transformations of input file content. 

## Transformations
Variables referenced in the input file and environment variables will be replaced with the current value of the variable, or the empty string if the variable is not defined. Read more in the [docs]((https://cmake.org/cmake/help/latest/command/configure_file.html#transformations)
# Usage
- [`configure_file()`](https://cmake.org/cmake/help/latest/command/configure_file.html#command:configure_file "configure_file")
```cmake
configure_file(TutorialConfig.h.in TutorialConfig.h)
```
## Syntax
```cmake
configure_file(<input> <output>
               [NO_SOURCE_PERMISSIONS | USE_SOURCE_PERMISSIONS |
                FILE_PERMISSIONS <permissions>...]
               [COPYONLY] [ESCAPE_QUOTES] [@ONLY]
               [NEWLINE_STYLE [UNIX|DOS|WIN32|LF|CRLF] ])
```
### Options
`<input>`
- Path to input file. Relative path treated with respect to [[CMake CMAKE_CURRENT_SOURCE_DIR]]. Path must be file, not a directory.
`<output>`
- Path to output file or directory. Relative path is treated with respect to value of [[CMake CMAKE_CURRENT_BINARY_DIR]]. If the path names an existing directory the output file placed in that directory with the same name as the new input file. 

`COPYONLY`
- Copy the file without replacing any variable references or other content. This option may not be used with `NEWLINE_STYLE`.
