---
summary: Sets a normal, cache, or environment variable to a given value.
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, October 15th 2024, 5:37:44 pm
type: note/function
---
# Background
- Sets a variable

# Usage
- [`set()`](https://cmake.org/cmake/help/latest/command/set.html#command:set "set")

## Set A Normal Variable
```cmake
set(<variable> <value>... [PARENT_SCOPE])
```
- Set or unset `<variable>` in the current function or directory scope. 
	- If at least one `<value>...` is given, set the variable to that value. 
- Note:
	- When evaluating `${VAR}` CMake first searches for a normal variable with that same name. If that doesn't exist, *then* CMake will search for a cache entry with that name. 
	- Unsetting a normal variable CAN expose a cache variable that was previously hidden. Keep t

### Options
[[CMake.PARENT_SCOPE]]

## Set a Cache Entry
```cmake
set(<variable> <value>... CACHE <type> <docstring> [FORCE])
```
- Sets the given cache `<variable>`. Type must be specified

### Cache Entry Type
- `BOOL`:  Boolean ON/OFF value.
- `FILEPATH`:  Path to a file on disk.
- `PATH`:  Path to a directory on disk.
- `STRING`:  A line of text.
- `INTERNAL`:  A line of text. cmake-gui(1) does not show internal entries. They may be used to store variables persistently across runs. Use of this type implies FORCE.

## Set Environment Variable
```cmake
set(ENV{<variable>} [<value>])
```
Sets an environment variable to the given. value. Subsequent calls of `$ENV{<variable>}` will return this new value.