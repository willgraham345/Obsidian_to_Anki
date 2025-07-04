---
type: note
---
# Background
## Basic CMake Usage
CMake takes one or more `CMakeLists` files as input and produces project files or Makefiles for use with a wide variety of native development tools. 
Typical process goes like this:
1. Project is defined in one or more CMakeLists files
2. CMake configures and generates the project
3. Users build project with their favorite development tool


Unless otherwise noted, you should always make a build directory and build from there. 
- Building in-source is possible, but you need to be careful. 
## Standard Options
- `-DCMAKE_BUILD_TYPE=` Pick from Release, RelWithDebInfo, Debug, or sometimes more.
- `-DCMAKE_INSTALL_PREFIX=` The location to install to. System install on UNIX would often be `/usr/local` (the default), user directories are often `~/.local`, or you can pick a folder.
- `-DBUILD_SHARED_LIBS=` You can set this `ON` or `OFF` to control the default for shared libraries (the author can pick one vs. the other explicitly instead of using the default, though)
- `-DBUILD_TESTING=` This is a common name for enabling tests, not all packages use it, though, sometimes with good reason.


## Hello World for CMake
[[]]