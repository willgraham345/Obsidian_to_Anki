---
type: note
---

# Background
Dependent packages

# Background
- Software projects often require variables to be set on the command line when invoking CMake. Commonly used CMake variables are listed below:

# Usage
## Setting variables on the command line
CMake variables can be set when creating the initial build, or later on a subsequent invocation of cmake
### Set variable when creating initial build
```shell
mkdir build
$ cd build
$ cmake .. -G Ninja -DCMAKE_BUILD_TYPE=Debug
```
### Set variable on later build
```shell
cd build
$ cmake . -DCMAKE_BUILD_TYPE=Debug
```


### Setting Variables with `-D`
Can create or update (forced) a CMake `CACHE` entry. If `:<type>` portion is given 
```bash
cmake -DMY_CACHE_VAR="command line" -P cache.cmake
```
- The `-P` and `cache.cmake` direct the output to a script file. 
## Unset variables on command line
```shell
cd build
$ cmake . -UMyPackage_DIR
```