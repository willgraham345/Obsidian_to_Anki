---
type: note
---
# Background
- Describes a large family of compilers for the C family, and is maintained as part of the LLVM project.
	- Strict adherence to C++ standards, modular design, and minimal modification to source code's structure during compilation
	- LLVM = a library that is used to construct, optimize and produce intermediate and/or binary machine code. It's a compiler famework, where you provide the "front-end (parser and lexer)" and the "back-end" (code that converts LLVM's representation to actual machine code).
	- ![[Pasted.image.20240606100507.png| 300]]
- Available under an open-source license (Apache License Version 2.0)
- Much faster, and uses much less memory when compared with GCC

Targets
- Generally has less targets than GCC
Support
- Has support from other build tools like [[CMake]] and [[Cpp Ninja]]

## How does it work? 
- Works like any other compiler, in 3 stages
	1. Front end used for parsing source code. Checks for errors, and builds a language-specific AST (abstract syntax tree) to work as its input code
	2. Optimizer for AST
	3. Back end, which generates the final code to be executed by the machine which can depend on the target
# Usage
## Installation
Really easy, just use [[Linux apt]]