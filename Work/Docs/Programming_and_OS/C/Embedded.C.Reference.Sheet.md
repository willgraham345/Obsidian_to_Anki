---
type: note
---
# Overview of Embedded Systems

An embedded system is a piece of hardware that has software attached. This means they can be very flexible and efficient, but have a large development cost. Usually based on:
Sensor: Measures physical quantity and converts it to an electric signal.
A-D Converter:
[[Processor and ASICs]]: Processes data and transfers it to memory
D-A converter
Actuator: An actuator compares output from D-A converter to actual (expected) output stored in it and stores the approved output
Memory: Usually embeds ROM

# Definitions
- Can be found in: [[Computer Science Terminology]]
- **Application** = A program or set of programs designed to perform specific tasks or functions for end users. 
- **Cross compiler** = Type of compiler that runs on one platform (host platform), but generates executable code for a different platform (target platform). It compiles source code written for one architecture or operating system into machine code that can be executed on a different architecture or OS.
	- Terms:
		- Host = system on which cross-compiler runs, platform for development and compilation of source code 
		- Target = platform for which you want to generate executable code. Might be a different CPU architecture.
		- Use cases = Cross compilers are commonly used in scenarios where development is different from the platform that final executable will run. 
		- Configuration = setting up compiler tools like GCC
- **GCC** = GNU Compiler Collection, which is a collection of compilers and related tools used widely in software development which translates high-level programming (C, C++, Fortran) into machine code or intermediate code for different platforms and architectures. One of the most popular and widely used compiler suits. Main components include:
	- gcc: C compiler
	- g++: C++ compiler
	- gfortran: Fortran compiler
	- gcc and g++ with -ObjC flag: Objective-C Compiler
- **Program** = A series of instructions that cause a computer or a microcontroller to perform a particular task. Includes more than just instructions, with data and various memory addresses on which instructions are to perform their tasks.  
- **Startup Code** = Code that must be run on any microcontroller, usually given by the manufacturer. 
- **syscalls.c** = often a source file that contains low-level system call implementations used by the C runtime library (libc) or other higher-level functions in an embedded system or microcontroller environment. 
- **sysmem.c** = not a standard filename, but it could be a source file that deals with memory management or custom memory-related functions in a microcontroller project. The "sysmem.c" file might be used to implement memory allocation routines (e.g., malloc, free) or custom memory management strategies tailored to the specific microcontroller's memory architecture.
- **Thread** = The smallest unit of execution within a process. Each thread has its own program counter, stack, and local variables, but will share the memory space with other threads within the same process. Thread management and multithreading is handled by the operating system or a threading library. The level of control depends on the programming language and the platform used. 
	- Advantages: 
		- Improved responsiveness
		- Resource sharing
		- Utilization of multi-core processors, which can execute threads in parallel.

# Debugging
- You'll be able to debug different microcontrollers through manufacturer-defined paths which connect the processor to your PC (usually involving USB somehow).
- You may need to rewrite standard output functions (like `printf`) in `syscalls.c` and other places within your microcontroller. 
- Inside processors, you can have optional application-driven trace source that supports `printf `style debugging to trace operating system and application events, generating diagnostic system information.
## SWD
- Protocol for accessing ARM debug interface. Alternative to JTAG, and introduced to reduce pin number count
- 2Lines
	- SWDIO: bidirectional data line
	- SWCLK: clock driven by the host 
	- Optional pin: 
		- SWO: Serial Wire Output which is used for Single Wire Viewing
- By using SWD interface you should be able to program MCU's internal flash, you can access memory regions, add breakpoints, stop/run CPU. You can use the serial wire viewer for your printf statements for debugging. 
## JTAG
- Traditional mechanism for debug connections within the ARM7/9 family. With the Cortex-M family, ARM introduced the SWD Interface. 
- 4 lines
# Startup Code
- Must be run on any microcontroller, before anything else is run. 