---
type: note
---

# Storage Class Specifiers
A keyword used to define the scope, lifetime, and initial value of a variable declared within a program. The storage class indicates how memory is allocated and managed for the variable during the program's execution. 

## Auto
`auto`
- Default storage class
- Variables have local scope within the block they are defined, and are automatically destroyed when the block exits.
## Register
`register` 
- Used to suggest that a variable should be stored in a CPU for faster access. Only a hint to the compiler, and may not be followed
- Rarely used as modern compilers are typically better at optimizing register usage than developers
## Static
`static`
- Different meanings based on where it is used:
	- Static global variables
		- Specifies that the variable can only be defined by the current file. 
		- When used with global variables or functions at file scope, it restricts their visibility to the current translation unit (source file), and makes them inaccessible from other translation units. These variables and functions retain their value across different function calls.
	- Static functions
		- When used with local variables within a function, it changes their storage duration, making them retain their values across different function calls. The variable's scope remains local to the block it is defined in. 
- Great for a use in a global variable that is private to a function
## Extern
`extern`
- Used to declare a variable or a function that is defined in another translation unit (usually another source file). It provides a reference to the symbol without allocating storage for it in the current translation unit. 
- Tells C that the variable you're trying to modify exists in another translation. 
- Static variables CANNOT be externed
- Extern can be used during function call, when the function is defined outside the scope of the file
	- This is non compulsory, but optional. It's assumed. 
## Volatile
`volatile`
- Tells the C compiler that the value of the variable will change at unpredictable times during execution of the program, which prevents the compiler from performing certain optimizations (such as caching the value of the variable in a register and reading it repeatedly).


# ASCII Codes
- ASCII standard can encode 128 different character
- Can be encoded with the `char` data type