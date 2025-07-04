---
type: note
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Monday, December 2nd 2024, 12:05:59 pm
tags: [command/cmake, note/cmake]
---
# Background
The https://cmake.org/cmake/help/latest/manual/cmake.1.html#manual:cmake(1)

# Usage
## Build fresh source of software code in build directory (typical usage)
```shell
cd some_software-1.4.2
$ mkdir build
$ cd build
$ cmake .. -DCMAKE_INSTALL_PREFIX=/opt/the/prefix
$ cmake --build .
$ cmake --build . --target install
```
- *ALWAYS* recommended to build in a separate directory, and enables building a single source with multiple toolchains. 

- [p] `mkdir build` = Create a new directory called `build` for storing build files. #command/cmake
- [p] `cd build` = Change directory to the `build` folder. #command/cmake
- [p] `cmake .. -DCMAKE_INSTALL_PREFIX=/opt/the/prefix` = Configure the project, setting the installation prefix to /opt/the/prefix #command/cmake
- [p] `cmake --build .` = Build the project using the generated build files in the current directory #command/cmake
- [p] `cmake --build . --target install` = Build the project and then install the specified target (in this case, the install target). #command/cmake
- [p] `cmake [<options>] <path-to-existing-build>` = Builds the project with the specified options

## Command line environment
CMake buildsystem can be invoked with Makefiles or Ninja
- Necessary to make sure that CMake can find the appropriate [[CMake.build.tool]], compiler, linker, and other tools as needed. 
- On Linux, the appropriate tools are often provided in system-wide locations and may be readily installed through the system package manager. 
- Visual Studio ships multiple command prompts and `vcvarsall.bat` scripts for setting correct environments and correct buildsystems
- Xcode has more than one version involved.