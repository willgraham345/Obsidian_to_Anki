---
type: note
---
# Background
Build configs let projects be built in different ways for debug, optimized or any other sort of flag. CMake supports, by default:
- Debug: has most of the basic debug flags turned on
- Release: basic optimizations turned on. 
- MinSizeRel: Flags that produce the smallest object code, but not necessarily the fastest code. 
- RelWithDebInfo: Builds optimized build with debug info as well. 

CMake handles the configurations in slightly different ways depending on the generator being used. The conventions of the native build system are followed when possible.
- Configurations impact the build in different ways when using Makefiles versus using Visual Studio project files. 
## Visual Studio
- Supports Build Configurations.
- Within the IDE, you can select Debug and all sorts of other stuff. 
- The idea puts all binary files into directories with names of the active configuration. 
	- This brings extra complexity for projects that build programs need to be run as part of the build process from custom commands. 
## Makefile-based Generators
# Usage
