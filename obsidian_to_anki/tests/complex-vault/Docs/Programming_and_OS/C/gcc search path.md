---
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Monday, October 21st 2024, 3:55:12 pm
type: note
---
# Background
GCC will search for included files based on the type of include statement

## Search order of `#include "file"`
1. Directory of the current file
2. Preconfigured list of standard system directories
	1. In Linux, [[Linux.Root Directories#/usr/include]]

## `#include <file>`
3. Look only in the standard system directories
Exact list depends on the target system, how GCC is configured, and where it is installed. 
- You can find this by invoking it with the -v option
```cpp
cpp -v /dev/null -o /dev/null
```

## Additional Configuration
- You can add additional command line options to add additional directories to the search path. 
- i.e. `-Idir` which causes `dir` to be searched after the current directory (for the quote form of the directive) and ahead of the standard system directories. You can specify multiple `-I` options on the command line, in which case the directories are searched in left-to-right order.

## More info [here](https://gcc.gnu.org/onlinedocs/cpp/Search-Path.html)