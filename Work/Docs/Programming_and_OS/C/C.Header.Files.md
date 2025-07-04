---
type: note
---
A header file is a file with a `.h` extension containing:
- C function declarations
- Macro definitions

The idea is that you can share this info between several source fields

Two types of header files:
- Files that the programmer writes
- Files that come along with your compiler

It is good practice to keep all these things within a header file
- Constants
- System-wide global variables
- Function prototypes 
	- `return_type function_name(parameter_list);`
	- Acts as a contract between the function definition and its callers, letting you define stuff later.