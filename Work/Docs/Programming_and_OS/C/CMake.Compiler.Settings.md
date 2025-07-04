---
type: note
---
# Background
On some systems, you may have more than one compiler to choose from or your compiler may be located in a non-standard place. You need to specify to CMake where this is located. 
## Ways to specify compilers
1. The generator can specify the compiler
2. Environment variable setting
3. Cache entry

### Generator notes
- Some generators are tied to a specific compiler
	- Visual Studio 19 generators always use Visual Studio 19 compilers
	- For Makefile-based generators, CMake will try a list of usual compilers until it finds a working one. 

### Specifying a Compiler from the Command Line
See [[CMake CLI commands#Specify a Compiler]]