---
type: note
---
The linker is a crucial step in compiling, where compiled object files and libraries are combined to generate the final executable or shared object. The linker resolves dependencies and symbols among the different object files and libraries. 


# Components of a Linker
## Object files
- Compiled machine code generated from source code (`.c` files) and other object files 
## Libraries
- Libraries are collections of precompiled functions and code that can be reused across multiple programs. There are two types of libraries: static libraries (.a files) and dynamic/shared libraries (.so or .dll files). Static libraries are linked directly into the executable at compile time, while dynamic libraries are linked at runtime. You need to specify the libraries used by your program as linker arguments. For example:
	- `gcc main.o -lm`
		- In this case, `-lm` specifies the math library (libm), which provides mathematical functions like `sqrt`, `sin`, etc.
## Entry Point
- The entry point is the starting address in the code where the program execution begins. In C programs, the entry point is typically the `main` function. The linker needs to know the address of the entry point to start executing the program.
## Output File
- You need to specify the name of the output file (executable or shared object) that the linker should generate. This is usually done using the `-o` option. For example:
- `gcc main.o -o my_program`
## Library Directories
- If you have custom libraries installed in non-standard locations, you may need to specify the directories where the linker should search for libraries using the `-L` option.
## Library Dependencies
- Sometimes, libraries depend on other libraries. You may need to specify additional libraries that are required by the libraries you are linking with, using the `-l` option
## Linker Scripts
- 1. For advanced use cases, you may use linker scripts to control the layout of the output file, define memory regions, etc. Linker scripts are specified using the `-T` option.

# Example of Bash Script with an External Dependency
To add additional linking arguments, such as linking with an outside library, you can simply include the necessary linker flags when invoking the compiler. The order in which you specify the linking arguments matters, as the linker processes the arguments in the order they are given. If the script within your build depends on an outside library, you would specify the library after the object files and any other libraries it may depend on.

For example, let's say your build includes a script named "my_script.c" that depends on an external library "my_external_lib":

bashCopy code

```bash
gcc -o my_program main.c my_script.c -specs=rdimon.specs -lc -lrdimon -lmy_external_lib

```

In this command, we first specify the source files "main.c" and "my_script.c," and then we add the linker options "-specs=rdimon.specs -lc -lrdimon" to enable ARM semihosting. Finally, we add "-lmy_external_lib" to link with the "my_external_lib" library.

The linker will search for "my_external_lib" in the default library paths and any additional library directories specified using the "-L" option. If the library is found, it will be linked with your program. If the library is not found, you may encounter a linker error.

If the library is located in a non-standard directory, you can use the "-L" option to specify the directory where the linker should search for the library. For example:

bashCopy code

```bash
gcc -o my_program main.c my_script.c -specs=rdimon.specs -lc -lrdimon -L/path/to/libraries -lmy_external_lib`
```

Replace "/path/to/libraries" with the actual path to the directory containing "libmy_external_lib.a" (for static library) or "libmy_external_lib.so" (for shared library).

In summary, you can add additional linking arguments by including them on the command line when invoking the compiler. Ensure that you specify the necessary libraries in the correct order, and if needed, provide the paths to non-standard library directories using the "-L" option.