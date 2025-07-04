---
type: note
---
# Background
The `#include` directive tells the preprocessor to inserrt the contents of another file into the source code at the point where the `#include` directive is found. 
- Include directives are typically used to include the C header files for C functions that are held outside of the current source file

# Syntax/Usage

```c
#include <header_file>
```
or
```c
#include "header_file"
```
- The difference between these two syntaxes is subtle but important. If a header file is included within <>, the preprocessor will search a predetermined directory path to locate the header file. If the header file is enclosed in "", the preprocessor will look for the header file in the same directory as the source file.

More info [here](https://stackoverflow.com/questions/21593/what-is-the-difference-between-include-filename-and-include-filename)
