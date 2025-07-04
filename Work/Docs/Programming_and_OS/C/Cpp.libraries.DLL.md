---
type: note
---
# Background
DLL = Dynamic link library
- A library that contains code and data that can be used by more than one program at the same time. By using a DLL, a program can be modularized into separate components. 
- Updates are easier to apply to each module without affecting other parts of the program
- Basically the same as a [[Cpp.libraries.so]], but rather than being included in the linking list at compile time, the library is loaded via `dlopen()`/`dlsym()` commands so library doesn't need to be present at build time for the program to compile. 

## Why use it?
- Much of the functionality within Windows OS is due to DLL. 
- Use of DLLs helps to promote a modularization of code, code reuse, efficient memory usage, and reduced disk space.
### Potential issues
- When a program uses a DLL, called dependencies may cause the program not to run. 
	- When a program uses a DLL, a dependency is created. If another program

## Example DLL Files
- ActivX Controls (`.ocx`)
- Control Panel (`.cpl`)
- Device driver (`.drv`)

## Types of DLLs
Load-time dynamic linking
- An application makes explicit calls to exported DLL functions like local functions. 
- To use this, provide a header (`.h`) file and an import library (`.lib`) file when you compile and link the application. 
	- The linker will provide the system with the information that is required to load the DLL and resolve the exported DLL function locations at load time. 
Run-time dynamic linking
- An application calls either the `LoadLibrary` function, or the `LoadLibraryEx` function to load DLL at runtime. 
	- After DLL is loaded, you get the `GetProcAddress` function to obtain the address of the exported DLL function you want to call. 
- When to use run-time dynamic linking:
	- Startup performance
	- Easy of use
	- Application logic
- You do NOT need to provide an import library file. 

# Usage