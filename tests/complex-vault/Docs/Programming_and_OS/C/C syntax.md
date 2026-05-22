---
type: note/system
tags:
  - programming/c/syntax
date created: Wednesday, March 18th 2026, 12:00:00 pm
date modified: Wednesday, March 18th 2026, 12:00:00 pm
items:
  - "[[c_datatypes]]"
  - "[[c_operators]]"
  - "[[c_control_flow]]"
  - "[[c_functions]]"
  - "[[c_pointers]]"
  - "[[c_arrays]]"
  - "[[c_structs_unions_enums]]"
  - "[[c_preprocessor]]"
  - "[[c_storage_classes]]"
  - "[[c_type_qualifiers]]"
  - "[[c_scope_and_linkage]]"
similar:
  - "[[C.Memory.in.a.C.Program.Overview]]"
  - "[[C.Storage_Class_Specifiers]]"
  - "[[C.Filestructure]]"
  - "[[C.Input]]"
  - "[[C.Output]]"
  - "[[C.Threads]]"
  - "[[C.Mutex]]"
  - "[[C.Optimization]]"
up:
  - "[[Programming_and_OS Hub]]"
---

# Summary
󰙎 C syntax ;;; Hub for all C language syntax categories — types, operators, control flow, functions, pointers, aggregates, preprocessor, and storage.

# Additional Background
C (C89/C90 through C23) is a small, portable systems language. Its syntax is the direct ancestor of C++, Java, and others. This hub indexes the primary syntax topics; each item note covers one category in depth.

## Concepts of Note

| Category | One-liner | Note |
|---|---|---|
| Data Types | Primitives, aggregates, typedef, fixed-width integers | [[c_datatypes]] |
| Operators | Arithmetic, relational, bitwise, logical, assignment, comma, ternary | [[c_operators]] |
| Control Flow | `if`/`else`, `switch`, `for`, `while`, `do-while`, `goto`, `break`, `continue` | [[c_control_flow]] |
| Functions | Declaration, definition, prototypes, variadic (`stdarg.h`), recursion | [[c_functions]] |
| Pointers | Address-of, dereference, pointer arithmetic, `void*`, function pointers | [[c_pointers]] |
| Arrays | 1-D/multi-D, VLAs (C99), array-pointer decay | [[c_arrays]] |
| Structs / Unions / Enums | Aggregate layout, bit-fields, tagged unions, named enum constants | [[c_structs_unions_enums]] |
| Preprocessor | `#define`, `#include`, `#ifdef`/`#ifndef`, `#pragma`, token stringification | [[c_preprocessor]] |
| Storage Classes | `auto`, `static`, `extern`, `register` — controls lifetime and linkage | [[c_storage_classes]] |
| Type Qualifiers | `const`, `volatile`, `restrict` (C99), `_Atomic` (C11) | [[c_type_qualifiers]] |
| Scope & Linkage | Block, file, function, prototype scope; internal vs. external linkage | [[c_scope_and_linkage]] |

## Usage

󰙎 translation unit ;;; a single `.c` file after preprocessing; the basic unit of compilation
󰙎 linkage ;;; determines whether an identifier in multiple translation units refers to the same object

## Flashcards

󰠗 What are the four C storage classes? ;; `auto`, `static`, `extern`, `register`
󰠗 Which C standard introduced `_Bool`, `//` comments, and VLAs? ;; C99
󰠗 What is pointer decay? ;; An array name in an expression converts to a pointer to its first element; size information is lost
󰠗 What does `volatile` prevent? ;; The compiler caching a variable in a register; forces every access to touch memory
󰠗 Which qualifier signals a pointer is the sole alias to its target, enabling aggressive optimization? ;; `restrict` (C99)
