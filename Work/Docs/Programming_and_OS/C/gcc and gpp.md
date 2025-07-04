---
summary: 
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Monday, October 21st 2024, 3:54:52 pm
type: note
concepts:
  - "[[gcc search path]]"
---


[[gcc search path]]

https://www3.ntu.edu.sg/home/ehchua/programming/cpp/gcc_make.html

# Background
[About](https://gcc.gnu.org/)
- `g++` is a GNU c++ compiler invocation command used for preprocessing compilation, assembly and linking of source code to generate an executable file.
	- Started in the late 1980s
- General use compiler, associated with the GNU project. 
- Free and open-source with the GCC Runtime Library Exception

Targets
- Mainly Unix-like platforms, Windows support is provided through [[Cpp Cygwin]] or [[Cpp MinGW]] runtime libraries
	- Compiles with a variety of language extensions that is built upon some C++20 features.
Support
- Has support from other build tools like [[CMake Overview and Basics guide notes]] and [[Cpp Ninja]]
- Many IDEs including
	- VSCode, CLion, Qt Creator

- Default target executable file is `a.out` in the present working directory
