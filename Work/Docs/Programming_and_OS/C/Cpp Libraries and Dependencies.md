---
type: note/component
down: ["[[Cpp.Standard Library Descriptions]]"]
components: ["[[Cpp.Standard Library Descriptions]]"]
component_of: ["[[Cpp]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, January 3rd 2025, 9:50:28 am
---
# Background
Library = a collection of pre-compiled pieces of code that can be reused in a program.
- These can provide: classes, functions, data structures, routines, etc
- See [[CMake.add_library]] for how to add with CMake. 

## Shared libraries (Dynamic Library)
- One small executable, plus one or more libary files (`.dll` for windows, `.so` for Linux, `.dylib` on macOS)

### Examples
- [[Cpp.libraries.DLL]]

## Static Libraries
- One large executable
- A library that is merged into the actual program itself at build time for a single (larger) application containing the application code and library code. 
	- Final binary containing both main program and library exists as a single standalone binary file. 
	- Library MUST be present at compile time

### Examples
- [[Cpp.libraries.a]], All the code relating to this library is in this file, and it is linked directly into the program at compile time. 

## Header only Libraries
- May be the only option, if you're dealing with something that uses templates. 
- Advantages
	- Much simpler build process.
	- Don't need to worry about different platforms where the library might be used. 
	- You don't need to build the library, and you don't need to specify the compiled library during a the link step of the build. 
- Disadvantages
	- Bigger object files
	- Longer compilation
	- More tangled compilation
	- Harder to read as a 

## 
# Usage