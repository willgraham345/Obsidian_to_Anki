---
summary: Program used for preprocessing, linking, assembling source code into executable files. Free and open source project. Used primarily on Unix-like platforms. This is generally supported via other programs.
headings: ["[[#Concepts of Note]]"]
type: note
concepts: ["[[gcc search path]]"]
similar: ["[[Clang]]", "[[LLVM]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Wednesday, December 10th 2025, 9:27:58 am
template: "[[base_note_template]]"
template-version: 1.0.0
---

# Summary
- [I] gcc ;;; A “compiler driver” used for preprocessing, linking, assembling source code into executable files. Free and open source project. Used primarily on Unix-like platforms. This is generally supported via other programs.

# Additional Background

[[gcc search path]]

https://www3.ntu.edu.sg/home/ehchua/programming/cpp/gcc_make.html

[GCC vs. Clang/LLVM: An In-Depth Comparison of C/C++ Compilers \| by Alibaba Tech \| Medium](https://alibabatech.medium.com/gcc-vs-clang-llvm-an-in-depth-comparison-of-c-c-compilers-899ede2be378)
## Concepts of Note

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

### Versions
#### gcc13