---
summary:
type: note/configuration
headings: ["[[#Usage]]"]
configuration_of: ["[[CMake CLI commands]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, January 15th 2026, 2:52:10 pm
tags: [tools/cmake]
template: "[[base_note_template]]"
template-version: 1.0.1
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
The https://cmake.org/cmake/help/latest/manual/cmake.1.html#manual:cmake(1)

## Usage


### Build fresh source of software code in build directory (typical usage)
```shell
cd some_software-1.4.2
$ mkdir build
$ cd build
$ cmake .. -DCMAKE_INSTALL_PREFIX=/opt/the/prefix
$ cmake --build .
$ cmake --build . --target install
```
- *ALWAYS* recommended to build in a separate directory, and enables building a single source with multiple toolchains. 

  `mkdir build` ;;; Create a new directory called `build` for storing build files.
  `cd build` ;;; Change directory to the `build` folder.
  `cmake .. -DCMAKE_INSTALL_PREFIX=/opt/the/prefix` ;;; Configure the project, setting the installation prefix to /opt/the/prefix
  `cmake --build .` ;;; Build the project using the generated build files in the current directory
  `cmake --build . --target install` ;;; Build the project and then install the specified target (in this case, the install target).
  `cmake [<options>] <path-to-existing-build>` ;;; Builds the project with the specified options

### Command line environment
CMake buildsystem can be invoked with Makefiles or Ninja
- Necessary to make sure that CMake can find the appropriate [[CMake build tool]], compiler, linker, and other tools as needed. 
- On Linux, the appropriate tools are often provided in system-wide locations and may be readily installed through the system package manager. 
- Visual Studio ships multiple command prompts and `vcvarsall.bat` scripts for setting correct environments and correct buildsystems
- Xcode has more than one version involved.
