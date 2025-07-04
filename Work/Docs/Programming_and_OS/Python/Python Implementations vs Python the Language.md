---
type: note
concept_of: ["[[Python Basics]]"]
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Thursday, February 6th 2025, 11:24:48 am
tags: [note/python]
---
# What is CPython?
The original python implementation that is downloaded from Python.org. It's called this to distinguish the implementation of the language engine from the Python *programming language*. 

You need to keep Python-the-language separate from whatever *runs* the Python code. 

## Compiler and PVM  
CPython happens to be implemented in C. CPython compiles your Python code into bytecode and interprets that bytecode in an evaluation loop. 

CPython has a compiler and a Python Virtual Machine (PVM). Compiler translates to byte code, and PVM executes the byte code. 

### Python Compiler
1. Tokenizes source code
2. Parses stream of tokens into abstract syntax tree (AST)
3. Transforms AST into control flow graph
4. Generates byte code based on the control flow graph

### PVM
Does garbage collection and managed memory

## Other implementations of Python
Jthon, IronPython, and PyPy are "other" implementations of Python. 
- Implemented in Java, C#, and RPython. 

## Does Python translate my Python code to C?
No, it instead runs an interpreter loop. 

# Cython?
A python project that translates Python-ish code to C. 

cython adds a few extensions to the python language and lets you compile your code to C extensions, code that plugs into the CPython interpreter. 