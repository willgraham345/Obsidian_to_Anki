---
tags: [note/python]
type: note
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Wednesday, August 21st 2024, 7:14:08 pm
---

# Overview 
- Applications of python include: web programming, scripting, scientific computing, and AI.
- Python is an interpreted language which means that each line is executed as it is entered. Python also includes IDLE (integrated development environment) which includes tools for writing and debugging entire programs.
-  Everything in python is an object
-   Almost every object in python has attached functions, known as
    methods, that have access to the object's internal contents. They
    can be called using the syntax:
    -   obj.some_method(x, y, z)
    -   result = f(a, b, c, d=5, e='foo')
    -   Functions can take in both positional and keyword arguments.
- Versions of Python
	- Python 3.x is guaranteed to work in all future versions.

# Commenting
Single line:`#`
Multi-line: `''', or """`


# Good Practices
`if__name__ == "__main__
- This lets you test a function as a "main"


-   Every number, string, data structure, function, class, module, and so on exists in its own "box". Each object has an associated type and internal data. Even functions can be treated like any other object.

# Variables
Variables in Python
-   Variables in python are pass by reference
-   Most variables in python are mutable
Dynamic references, strong types
-   Object references in python have no type associated with them
    -   Variables are names for objects within a particular namespace;
    - the type information is stored in the object itself.
    -   Every object has a specific type (or class), and implicit
        conversions will occur only in certain obvious circumstances
        like float and int