---
type: note
---
Some IDE's will support directly viewing the memory within the target. This requires going through the datasheet of the target, and viewing where both program and SRAM data is stored. 
- You may need to edit the viewing type (i.e. signed integer, hexadecimal, binary) to see the correct representation of your data

# Different Types of Memory
## Non-volatile Memory
This is likely the instruction/program memory, where machine code will be stored within the `.elf` file
- In a 32-bit microcontroller
### ROM (Read Only Memory)
- MPROM = Mask Programmable ROM
- EPROM = Ultraviolet Erasable ROM
- EEPROM = Electrically Erasable Programmable ROM
### OTP (On time programmable)
### Flash
### FRAM (Ferroelectric ROM)
## Volatile Memory
- Data memory
	- May be in the memory/architecture section of the datasheet
- SRAM