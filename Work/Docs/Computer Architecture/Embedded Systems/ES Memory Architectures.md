---
type: note
---
**Volatile** = if power is lost, memory is lost
- To achieve reasonable performance at reasonable cost, faster memories must be mixed with slower memories.
- Address space of a processor architecture is divided up to provide access to the various kinds of memory, to provide support for common programming models, and to designate addresses for interaction with devices other than memories, such as I/O devices
# Memory Technologies

## RAM (Random access memory)
- Memory where individual items can be written and read one at a time relatively quickly. 
- SRAM (static RAM) is faster than DRAM (dynamic RAM), but is also larger (silicon-wise). DRAM holds data for a short time, so each memory location must be refreshed. SRAM holds memory for as long as power is maintained. 
- Most embedded computer systems include SRAM. Many also include DRAM
	- DRAM refresh can introduce variability to the access times.
	- Manufacturers of DRAM will specify that each memory location must be refreshed, and number of locations must be refreshed together. 
## Non-volatile Memory
### ROM (read-only memory)
- a.k.a. mask rom
- Firmware means a program or constant data that never needs to change. It's firm, because it isn't as changeable as "sofftware"


# Memory Hierarchy
- Many processors use a memory hierarchy, which combines different memory technologies to increase overall memory capacity. Typically, a relatively small amount of on-chip SRAM ill be used with a larger amount of off-chip DRAM. These can be further combined with a third level, such as disk drives, which have large capacity, but lack random access and can be quite slow to read and write. 
	- An application programmer may not be aware that memory is fragmented across these technologies.
## Virtual Memory
- Makes the diverse technologies look to the programmer like a contiguous address space. The OS and/or the hardware provides address translation
	- Address translation = converting logical addresses in the address space to physical locations in one of the available memory technologies. 
	- TLB = Translation lookaside buffer, a piece of hardware that can speed up address translations. 
- This may require the designer to understand memory much better than a typical programmer, because you're concerned about how quickly data/addresses can be read.
## Memory Maps
- Memory map = defines how addresses get mapped to software, used by the proceessor. 
	- Total size of address space is constrained by address width of the processor. 
	- 32-bit processor can address $2^{32}$ locations, or 4 GBs assuming each address refers to one byte. 
- This architecture separates addresses used for program memory from those used for data memory. 
	- This enables memories to be accessed via separate busses, permitting instructions and data to be fetched simultaneously. Effectively doubles the memory bandwidth.
- **Harvard architecture** = Memory architecture that separates data memory from program memory. 
- **von Neumann architecture** = Stores program and data in the same memory. 
- ![[Pasted image 20230811125959.png]]
	- Each of these peripherals occupies some of the memory addresses by providing memory--mapped registers
- **Bit Banding** = Some of the unused addresses can be used to access individual bits rather than entire bytes or words in the memory and peripherals. This makes certain operations more efficient, since extra instructions to mask the desired bits become unnecessary.
## Register file 
- **Register File**= The most tightly integrated memory in a processor, which stores a word. The word size is a key property of the processor. The register file may be implemented directly using flip flops in the processor circuitry, or the registers may be collected into a single memory bank, typically using the same SRAM technology discussed above. 
	- The number of registers is usually small. AN ISA typically provides instructions that can provide one, two, or three registers. 
## Scratchpads and Caches
- Many embedded applications mix memory technologies. Some memories are accessed before others; we say that the former are "closer" to the processor than the latter. 
	- A close memory (SRAM) is typically used to store working data temporarily while the program operates on it. 
	- If the close memory has a distinct set of addresses and the program is responsible for moving data into it or out of it to the distant memory, then it is called a scratchpad
- Cache memory can present some difficulties with embedded systems because their timing behavior can vary substantially in ways that are difficult to predict. 
	- An architecture will typically support a much larger address space than what can be stored in the physical memory of the processor, with a virtual memory system used to present the programmer with the view of a contiguous memory space. 
- If the processor is equipped with a memory management unit (MMU), then programs reference logical addresses and the MMU translates these to physical addresses.
	- For example, using the memory map in Figure 9.1, a process might be allowed to use logical addresses 0x60000000 to 0x9FFFFFFF (area D in the figure), for a total of 1 GB of addressable data memory. The MMU may implement a cache that uses however much physical memory is present in area B. When the program provides a memory address, the MMU determines whether that location is cached in area B, and if it is, translates the address and completes the fetch. If it is not, then we have a cache miss, and the MMU handles fetching data from the secondary memory (in area D) into the cache (area B). If the location is also not present in area D, then the MMU triggers a page fault, which can result in software handling movement of data from disk into the memory. Thus, the program is given the illusion of a vast amount of memory, with the cost that memory access times become quite difficult to predict. It is not uncommon for memory access times to vary by a factor of 1000 or more, depending on how the logical addresses happen to be disbursed across the physical memories.
### Basic Cache Organization
- Suppose that each address in a memory system comprises $m$ bits, for a maximum of $M = 2^m$ unique addresses. 
	- A cache memory is organized as an array of $S = 2^s$ *cache sets*
		- Each cache set in turn comprises $E$ *cache lines*. A Cache line stores a single block of $B = 2^b$ bytes of data, along with **valid** and **tag** bits. The valid bit indicates whether the cache line stores meaningful information, while the tag (comprising $t = m - s - b$ bits uniquely identifies the block that is stored in the cache line.)
	- A cache can be characterized by the tuple $(m, S, E, B)$ 
		- The overall cache size $C$ is given as $C = S*E*B$ bytes
		- ![[Pasted image 20230811160746.png]]
### Direct-Mapped Caches
- A cache with exactly one line per set $(E = 1)$ is called a **direct-mapped cache**. For such a cache, given a word $w$ requested from memory, where $w$ is stored at an address $a$, there are three steps in determining whether $w$ is a cache hit or a miss:
1. **Set Selection**: The s bits encoding the set are extracted from address a and used as an index to select the corresponding cache set.
2. **Line Matching**: The next step is to check whether a copy of w is present in the unique cache line for this set. This is done by checking the valid and tag bits for that cache line. If the valid bit is set and the tag bits of the line match those of the address a, then the word is present in the line and we have a cache hit. If not, we have a cache miss.
3. **Word Selection**: Once the word is known to be present in the cache block, we use the b bits of the address a encoding the word’s position within the block to read that data word.
- On a cache miss, the word $w$ must be requested from the next level in the memory hierarchy. Once this block has been fetched, it will replace the block that currently occupies the cache line for $w$.
	- While a direct-mapped cache is simple to understand and to implement, it can suffer from conflict misses. A conflict miss occurs when words in two or more blocks that map to the same cache line are repeatedly accessed so that accesses to one block evict the other, resulting in a string of cache misses. Set-associative caches can help to resolve this problem.

### Set-associative Caches
- **Set-associative cache**: can store more than one cache line per set. If each set in a cache can store $E$ lines, where $1 , E , C / B$ , then the cache is called an E-way set-associative cache.
	- Associative comes from associative memory, which is a memory that is addressed by its contents. That is, each word in the memory is stored along with a unique key and is retrieved using the key rather than the physical address indicating where it is stored. An associative memory is also called a **content-addressable memory**
- For a set-associative cache, accessing a word $w$ ad address $a$ consists of the following steps
	1. Set Selection: This step is identical to a direct-mapped cache.
	2. Line Matching: This step is more complicated than for a direct-mapped cache because there could be multiple lines that w might lie in; i.e., the tag bits of a could match the tag bits of any of the lines in its cache set. Operationally, each set in a set-associative cache can be viewed as an associative memory, where the keys are the concatenation of the tag and valid bits, and the data values are the contents of the corresponding block.
	3. Word Selection: Once the cache line is matched, the word selection is performed just as for a direct-mapped cache.
- A common policy is **LRU** (Least recently used), in which the cache line whose most recent access occurred the furthest in the past is evicted. Another common policy is **FIFO**. 
- Good cache replacement policies are essential for good cache performance. 
	- Implementing these policies requires additional memory to remember the access order, with the amount of additional memory differing 
- **Fully-associative cache** A cache where $E = C/B$, i.e. there is only one set. For such a cache, line matching can be quite expensive for a large cache size because an associative memory is expensive. Fully-associative caches are typically only used for small caches, such as the TLB's mentioned earlier.
# Memory Addresses
- At minimum, a memory model defines a range of memory addresses to the program
- In C, these addresses are stored in `pointers`.
- In 32-bit architecture, memory addresses are 32-bit unsighed integers, capable of representing addresses 0 to $2^{32} - 1$, which is around four billion addresses
	- Each address refers to a byte (eight bits) in memory. 
	- The C `char` data type references a byte
		- `int` has at least two bytes
- Since memory addresses refer to a byte, when writing a program that directly manipulates memory addresses, there are two critical compatibility concerns:
	- **Alignment**
	- **Byte order**
		- The first byte may represent the eight low order bits of the int (a representation called little endian), or it may represent the eight high order bits of the int (a representation called big endian). 
		- Intel's x86 and ARM architectures by default use little-endian representation. IBM's PowerPC uses big endian. 
			- Some processors support both
## Stacks
- A stack is a region of memory that is dynamically allocated to the program in a last-in first out pattern (LIFO). 
- A **stack pointer** (typically a register) : contains the memory address on top of a stack. When an item is pushed onto the stack, the stack pointer is incremented and the item is stored at the new location referenced by the stack pointer. When an item is popped off the stack, the memory location referenced by the stack pointer is (typically) copied somewhere else (e.g., into a register) and the stack pointer is decremented.
- Stacks are typically used to implement procedure calls. 
	- Given a procedure call in C, for example, the compiler produces code that pushes onto the stack the location of the instruction to execute upon returning from the procedure, the current value of some or all of the machine registers, and the arguments to the procedure, and then sets the program counter equal to the location of the procedure code. 
- **Stack frame** = the data for a procedure which is pushed onto the stack
	- It can be disastrous if the stack pointer is incremented beyond the memory allocated for the stack. Such a **stack overflow** can result in overwriting memory that is being used for other purposes, leading to unpredictable results. Bounding the stack usage is an important goal. 
	- This becomes difficult with recursive programs, where a procedure calls itself. Embedded software designers often avoid using recursion to circumvent this difficulty. 

- An example of an error due to misuse or misunderstanding of the stack
```C
int* foo(int a) {
	int b;
	b = a * 10;
	return &b;
}
int main(void){
	int* c;
	c = foo(10);
	...
}
```
- The variable `b` is a lcoal variable, with its memory on the stack. When the procedure returns, the variable `c` will contain a pointer to a memory location *above the stack pointer*. 
	- The ocntents of that memory location will be overwritten when items are next pushed onto the stack. It is therefore incorrect for the procedure `foo` to return a pointer to `b`. By the time that pointer is de-referenced (i.e. if a line in `main` refers to `*c` after line 8), the memory location may contain something entirely different from what was assigned in `foo`. 
	- C provides no protection against such errors. 

## Memory Protection Units
- Many processors provide **memory protection** in hardware. Tasks are assigned their own address space, and if a task attempts to access memory outside its own address space, a **segmentation fault** or other exception results. This will typically result in termination of the offending application. 
## Dynamic Memory Allocation
- General-purpose software applications often have indeterminate requirements for memory, depending on parameters and/or user input. To support such applications, computer scientists have developed dynamic memory allocation schemes, where a program can at any time request that the operating system allocate additional memory. 
	- The memory is allocated from a data structure known as a **heap**, which facilitates keeping track of which portions of memory are in use by which application. Memory allocation occurs via an operating system call (such as `malloc` in C). When the program no longer need access to memory that has been so allocated, it deallocates the memory (by calling `free` in C).
- **Garbage collector** = A garbage collector is a task that runs either periodically or when memory gets tight that analyzes the data structures that a program has allocated and automatically frees any portions of memory that are no longer referenced within the program. When using a garbage collector, in principle, a programmer does not need to worry about explicitly freeing memory. 
	- With or without garbage collection, it is possible for a program to inadvertently accumulate memory that is never freed. This is known as a memory leak, and for embedded applications, which typically must continue to execute for a long time, it can be disastrous. The program will eventually fail when physical memory is exhausted.
- Another problem with memory allocation schemes is memory fragmentation, which occurs when a program chaotically allocates and deallocates memory in varying sizes. A fragmented memory has allocated and free memory chunks interspersed, and often the free memory chunks become too small to use. 
	- Defragmentation is required in this case.
- Defragmentation and garbage collection are both very problematic for real-time systems. Straightforward implementations of these tasks require all other executing tasks to be stopped while the defragmentation or garbage collection is performed. 
## Memory Model of C
- C programs store data on the stack, on the heap, and in memory locations fixed by the compiler. Consider the following C program:
```C
int a = 2;
void foo(int b, int* c) {
	...
}
int main(void) {
	int d;
	int* e;
	d = ...; //assign some value to d
	e = malloc(sizeInBytes); //Allocate memory for e.
	e* = ...; //Assign some value for e.
	foo(d, e);
	...
}
```
- In this program:
	- `a` is a global variable
		- The compiler will assign it a fixed memory location.
	- `b` and `c` are *parameters*
		- Allocated on the stack when the procedure `foo` is called. 
			- A compiler also could put them in registers rather than on the stack
	- `d` and `e` are *automatic variables* or *local variable*
	- Declared within the body of a procedure (in this case, `main`)
		- Compiler will allocate space on the stack for them
- When `foo` is called on line 11, the stack location for `b` will acquire a *copy* of the value of variable `d` assigned on line 8. This is an example of *pass by value*, where a parameter's value is copied onto the stack for use by the called procedure. 
- The data will be referred to by the pointer `e`, on the other hand, is stored in memory allocated on the heap, and is then passed by reference (the pointer to it, `e`, is passed by value). 
- The address is stored in the stack location for `c`. If `foo` includes an assignment to `*c`, then after `foo` returns, that value can be read by dereferencing `e`.
- The global variable `a` is assigned an initial value on line 1. There is a subtle pitfall here. The memory location storing `a` willbe initialized with value 2 *when the program is loaded*. ?This means that if the program is run a second time without reloading, then the initial value of `a` will not necessarily be 2. It's value will be whatever it was when the first invocation of the program ended. In most desktop OS, the program is reloaded on each run so this problem does not show up. In embedded systems, the program is not necessarily reloaded for each run. The program may be run from the beginning, for example, each time the system is reset. To guard against this problem, it is safer to initialize global variables in the body of `main`, rather than on the declaration line, as done above. 