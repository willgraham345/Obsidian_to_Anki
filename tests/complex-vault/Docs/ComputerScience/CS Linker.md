---
template: "[[base_note_template]]"
template-version: 1.0.2
type:
uses:
  - "[[Cpp object files]]"
  - "[[C Object Files]]"
implementations:
  - "[[Linux ld]]"
  - "[[C Linker]]"
headings:
  - "[[#Concepts of Note]]"
---

# Summary
󰙎 CS Linker ;;; Combines a number of object files and libraries to build an executable image”

Excerpt From
Real-Time Systems Development with RTEMS and Multicore Processors
Bloom, Gedare
This material may be protected by copyright.

The linker is a crucial step in compiling, where compiled object files and libraries are combined to generate the final executable or shared object. The linker resolves dependencies and symbols among the different object files and libraries. 

# Additional Background

## Concepts of Note
- [t] What three things define the behavior of the linker? What do they do? ;; Input and output (determines input files and live), Memory layout (describes memory), section and memory mapping (how input files are divided and organized into sections) 
- [I] Symbol resolution ;;; “associate symbol definitions with the corresponding references”
- [t] What in the gcc workflow designates the entry point in an executable? ;; The linker scripts mark it with a `ENTRY(<symbol>)`
- [I] Bare metal ;;; “When no loader is used—that is, the executable image is uploaded by means of an upload tool residing on the development host”
Linker scripts define the following:
- Which input files the linker will operate on, either object files or libraries. This is done by means of one or more INPUT() commands, which take input file names as arguments.
- The sequence in which they will be scanned by the linker, to perform symbol resolution and relocation. The sequence is implicitly established by the order in which input commands appear in the script and by the left-to-right order of their arguments.
- The special ways in which a specific file or group of files will be handled. For instance, the STARTUP() command labels a file as being a startup file rather than a normal object file.
- Where to look for libraries, when just the library name is given. This is accomplished by specifying one or more search paths by means of the SEARCH_DIR() command.
- Where the output—namely, the file that contains the executable image—will go, through the OUTPUT() command

The contents of each input object file are divided by the compiler (or the assembler) into several categories according to their characteristics, like:
• code (.text),
• initialized data (.data),
• uninitialized data (.bss).