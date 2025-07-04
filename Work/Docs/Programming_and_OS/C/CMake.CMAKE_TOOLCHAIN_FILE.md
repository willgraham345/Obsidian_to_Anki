---
type: note
---
# Background
 File containing cross-compiling data such as [`toolchains and sysroots`](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#manual:cmake-toolchains(7) "cmake-toolchains(7)").         

For more information on what should be in a toolchain file, see [[CMake cmake-toolchains]]
# Usage
[`CMAKE_TOOLCHAIN_FILE`](https://cmake.org/cmake/help/latest/variable/CMAKE_TOOLCHAIN_FILE.html#variable:CMAKE_TOOLCHAIN_FILE "CMAKE_TOOLCHAIN_FILE")
```shell
cmake --toolchain path/to/file
# or
cmake -DCMAKE_TOOLCHAIN_FILE=path/to/file
```
- The file will be loaded to set values for the compilers. 

## Another example
```shell
cmake -S . -B build/ -DCMAKE_TOOLCHAIN_FILE=toolchain-STM32F407.cmake
```
- Tells CMake to create something based on the current directory, build it in the `build/` directory, and points it towards the `toolchain-STM32F407.cmake` toolchain configuration file. 
	- This file will define variables for the target name and version. 