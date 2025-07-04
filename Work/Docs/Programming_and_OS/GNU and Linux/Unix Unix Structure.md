---
type: note
---
# Background
The Unix system is composed of several components that were originally packaged together. 

## Names/Filesystem Components
Kernel: Source code in `/usr/sys/` with several source subcomponents
- `conf`

Kernel – source code in `/usr/sys`, composed of several sub-components:
- `conf` – configuration and machine-dependent parts, including boot code
- `dev` – device drivers for control of hardware (and some pseudo-hardware)
- `sys` – operating system "kernel", handling memory management, process scheduling, system calls, etc.
- `h` – header files, defining key structures within the system and important system-specific invariables
Development environment – early versions of Unix contained a development environment sufficient to recreate the entire system from source code:
- `ed` – text editor, for creating source code files
- `cc` – C language compiler (first appeared in V3 Unix)
- `as` – machine-language assembler for the machine
- `ld` – linker, for combining object files
- `lib` – object-code libraries (installed in /lib or /usr/lib). libc, the system library with C run-time support, was the primary library, but there have always been additional libraries for things such as mathematical functions (libm) or database access. V7 Unix introduced the first version of the modern "Standard I/O" library stdio as part of the system library. Later implementations increased the number of libraries significantly.
- `make` – build manager (introduced in PWB/UNIX), for effectively automating the build process (See [[GNU make]])
- `include` – header files for software development, defining standard interfaces and system invariants
- Other languages – V7 Unix contained a Fortran-77 compiler, a programmable arbitrary-precision calculator (bc, dc), and the awk scripting language; later versions and implementations contain many other language compilers and toolsets. Early BSD releases included Pascal tools, and many modern Unix systems also include the GNU Compiler Collection as well as or instead of a proprietary compiler system.
- Other tools – including an object-code archive manager (ar), symbol-table lister (nm), compiler-development tools (e.g. lex & yacc), and debugging tools.
Documentation – Unix was one of the first operating systems to include all of its documentation online in machine-readable form.[25] The documentation included:
- `man` – manual pages for each command, library component, system call, header file, etc.
- `doc` – longer documents detailing major subsystems, such as the C language and troff

# Usage