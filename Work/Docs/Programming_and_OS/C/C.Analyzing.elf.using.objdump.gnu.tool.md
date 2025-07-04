---
type: note
---
# Objdump
## Background
- Analyzes an `.elf` file. Helpful for instruction-level debugging.
## Options
- `-d` = disassembles machine code back into C code for you to read.
- `-h` = shows section headers too

# Example
Analyze an `.elf` by running:
```bash
arm-non-eabi-objdump.exe -h exeName.elf
```
- `-h` flag will give you the section headers too
- Will give a `.list` file, which will show output of the objdump

IDE's may do also do the disassembly for you too, meaning that you can go back and forth between machine code and higher level C code. 


# Sections of an .elf file
## .text
- Contains all "codes" or all "instructions" of your program
## .rodata
- Contains all the 'Read-only data' of your program
## .data
- Contains all the 'data' of your program


# Runtime Order
- To see the startup file (`.s`, you can open the `Startup` folder within your build project)
	- The following steps are for the STM32 Discovery board. MAY be different with other microcontrollers. I don't know, just a heads up to make sure. 
## Steps
1. Reset of Processor
2. Processor Jumps to reset Handler
3. Copy `.data` from FLASH to SRAM
4. Zero out SRAM locations corresponding to `.bss` section size
5. Call `std.library` init function `__libc_init()`
6. Call `main()` of the user program
7. Nevere return from `main()`  back to reset handler