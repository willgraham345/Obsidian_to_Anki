---
type: note
---
There is NAND and NOR flash memory
Non-volatile = doesn't require power to retain data
[NOR Flash Memory](https://www.techtarget.com/searchstorage/definition/NOR-flash-memory)

## NOR Memory
- Faster to read than NAND, but more expensive and takes longer to erase and write new data
- Characterized by fast random access times, which allow it to ready relatively small amounts of data from any address quickly. 
	- Capable of directly executing source code from memory, which makes this appropriate for use in bootloaders and firmware
	 - The first component is 
### Structure
- Parallel
### Requirements

### 

## NAND Memory
- NAND has a higher memory capacity than NOR, but is slower. 
- NAND memory devices are accessed serially, using the same eight pins to transmit control, address, and data information.
### Structure
- NAND can write to a single memory address, doing so eight bits (one byte) at a time.


| Category             | NAND                                               | NOR                                         |
| -------------------- | -------------------------------------------------- | ------------------------------------------- |
| Speed                | Slower                                             | Faster                                      |
| Price ($)            | Lower                                              | Higher                                      |
| Power Consumption    | Lower when turned on, higher when consistently run | Higher when turned on, lower when operating |
| Structure            | Serial                                             | Parallel                                    |
| Mainly used in:      | Data storage                                       | Code Execution                              |
| Algorithm strengthhs | Writes, erases, sequential reads                   | Random reads from memory                    | 

![[Pasted image 20231111143004.jpg]]