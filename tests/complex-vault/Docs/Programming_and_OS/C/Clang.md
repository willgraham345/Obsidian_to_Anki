---
summary: LLVM implementation of compilers for the C and Cpp lanaguages. Maintained as part of the LLVM project. Open source, typically has less targets than GCC with support from CMake and Cpp Ninja. Clang is the compiler, Clangd is the LSP.
headings:
  - "[[#Concepts of Note]]"
  - "[[#Diagrams]]"
  - "[[#Usage]]"
type: note/tool/build/compiler
implements:
  - "[[LLVM]]"
configurations:
  - "[[Clang .clang-tidy]]"
  - "[[Clangd .clang-format]]"
aliases: Clangd
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Wednesday, December 10th 2025, 9:25:37 am
images:
  - "[[LLVM Compiler Infrastructure.png]]"
template: "[[base_note_template]]"
template-version: 1.0.0
tool_of:
  - "[[Docs/Programming_and_OS/C/C]]"
  - "[[Cpp]]"
tools:
  - "[[Clangd clang-tidy]]"
used_by:
  - "[[CMake cmake-toolchains]]"
  - "[[CMake]]"
  - "[[Cpp Ninja]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- Describes a large family of compilers for the C family, and is maintained as part of the LLVM project.
	- Strict adherence to C++ standards, modular design, and minimal modification to source code's structure during compilation
	- LLVM = a library that is used to construct, optimize and produce intermediate and/or binary machine code. It's a compiler framework, where you provide the "front-end (parser and lexer)" and the "back-end" (code that converts LLVM's representation to actual machine code).
- Available under an open-source license (Apache License Version 2.0)
- Much faster, and uses much less memory when compared with GCC

- Has support from other build tools like [[CMake]] and [[Cpp Ninja]]

### How does it work? 
- Works like any other compiler, in 3 stages
	1. Front end used for parsing source code. Checks for errors, and builds a language-specific AST (abstract syntax tree) to work as its input code
	2. Optimizer for AST
	3. Back end, which generates the final code to be executed by the machine which can depend on the target

## Usage
### Installation
Really easy, just use [[Linux apt]]

## Diagrams
- ![[LLVM Compiler Infrastructure.png| 300]]