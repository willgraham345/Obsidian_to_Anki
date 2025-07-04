---
type: note
up: ["[[Cpp Basics]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, November 22nd 2024, 4:07:41 pm
---
# Background
- A macro is a preprocessor directive that defines a symbolic name or expression, often with parameters, which is replaced by a specific piece of code before the program is compiled. 
- Often used to create reusable code snippets or defining constants
- For more information on how Preprocessor Directives can be used, see [[Cpp.include_and_forward_declaration]]

# Usage
| Directive       | Function                                                                           |
|-----------------|------------------------------------------------------------------------------------|
| `#include`      | Includes a header file in the program.                                            |
| `#define`       | Defines a macro.                                                                   |
| `#undef`        | Undefines a previously defined macro.                                             |
| `#ifdef`        | Checks if a macro is defined.                                                     |
| `#ifndef`       | Checks if a macro is not defined.                                                 |
| `#if`           | Tests a compile-time condition.                                                   |
| `#elif`         | Used with `#if` to provide an alternative condition.                               |
| `#else`         | Used with `#if` to provide an alternative condition if the previous condition fails.|
| `#endif`        | Ends conditional compilation.                                                      |
| `#error`        | Generates a compilation error message.                                             |
| `#pragma`       | Provides compiler-specific directives.                                             |
| `#line`         | Changes the line number and filename reported by the compiler.                     |
