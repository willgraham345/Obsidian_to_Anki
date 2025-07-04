---
type: note
---
# Types of Processors
In general-purpose computing, the variety of instruction set architectures today is limited with the Intel x86 architecture dominating everything.
- That is untrue with embedded systems who have a large number of embedded processor

ISA = Instruction set architecture
- Definition of the instructions that the processor can execute and certain structural constraints (like word size)
- x86 is an ISA
- An abstraction shared by many realizations, appearing in different chips, often made by different manufacturers. 
Processor realization or a chip
- A piece of silicon sold by a semiconductor vendor


## Types of Processors
### Microcontrollers
- Small computer on a single integrated circuit consisting of a relatively simple CPU combined with peripheral devices like memory, I/O devices, and timers. 
- The simplest microcontrollers operate on 8-bit words and are suitable for applications that require small amounts of memory and simple logic functions. 
	- Small energy, and often include a sleep mode
	- Can operate on a small battery for years
- Can become quite elaborate
#### Notable Architectures
- Intel 8051
	- A very popular and durable architecture is the Intel 8051, an 8-bit microcontroller developed in 1980. The 8051 ISA is supported by many vendors including Atmel, Infineon, Dallas Semiconductor, NXP, ST, Texas Instruments, and Cypress Semiconductor
- ARM instruction set
- Motorola Coldfire
- Hitachi H8
- MIPS
- PIC
#### PLCs
- Specialized microcontroller for industrial automation. 
- Originated as replacements for control circuits, and are typically designed for continuous operation in a hostile environment. 
- Often programmed in ladder logic

### DSP Processors
- Many embedded applications do quite a bit of signal processing. These all deal with large amounts of data, and typically involve sophisticated math operations on the data. 
- Processors designed to support numerically intensive signal processing applications are called **DSP processors** or DSPs for short.
- **Finite Impulse Response** is often used when programming these things. 
- Single-chip DSP microprocessors first appeared in the early 1980s. 
- Difficult to program compared to the RISC architectures, primarily because of a complex specialized instructions, a pipeline that is exposed to the programmer, and asymmetric memory architectures. 
- The formulas for FIR, grayscale images, filtering operations, and other stuff is given within the book
	- A tapped delay line is a structure related to an FIR filter where input values come in and are propagated down the delay line which taps after each delay element.
### Graphics Processors
- A GPU (Graphics processing unit) is a specialized processor made for performing the calculations for graphics rendering. Dominant providers today are Intel, NVIDIA, and AMD.
- Some embedded applications are a good match for GPU's. They're typically very power hungry

# Parallelism
### Parallelism vs Concurrency
- A program is said to be concurrent if different parts of the program **conceptually** execute simultaneously
- A program is set to be parallel if different parts of the program **physically** execute simultaneously
- Concurrency is central to embedded systems
- Non-concurrent programs specify a sequence of instructions to execute. A programming language that expresses a computation as a sequence of operations is called an *imperative* language. 
- Sequential execution of a concurrent program is done typically today by a multitasking operating system, which interleaves the execution of multiple tasks in a single sequential stream of instructions. 
	- This complicates the problem of ensuring that things occur at the *right time*. 
### Pipelining
- Most modern processors are pipelined. 
- Synchronous-reactive model of the behavior is shown below:
	- ![[Pasted image 20230810163508.png]]
	- *PC* = program counter, which provides the address to the instruction memory. The instruction memory provides encoded instructions, which in the figure are assumed to be 32 bits wide. 
		- In the fetch stage, the PC is incremented by 4 (bytes), to become the address of the next instruction, unless a conditional branch instruction is providing an entirely new address for the PC. 
	- The decode pipeline stage extracts register addresses from the 32-bit instruction and fetches the data in the specified registers from the register bank.
	- *ALU* = arithmetic logic unit
	- Portions of the pipeline between the latches operate in parallel. There are five instructions being executed, each at a different stage of execution. This is easily visualized with a **reservation table**. A, B, C, D, E are each a set of instructions.
		- ![[Pasted image 20230810164112.png]]
	- **pipeline hazards** caused by dashed lines in 8.2. 
- **data hazard** = a form of pipeline hazard. In cycle 5, E is being fetched while D reads from the register banks, C is using the ALU, while B isi reading from or writing to data memory, while A is writing results to the register bank. The write by A occurs in cycle 5, but the read by B occurs in cycle 3. Thus, the value B reads will not be the value that A writes. This is a data hazard.
#### Methods to Avoid Pipelining
##### Explicit Pipeline
- Pipeline hazard is simply documented, and the program (or compiler) must deal with it. 
	- In the example above, where B reads a register written by A, the compiler may insert three `no-op` instructions (which do nothing) between A and B to ensure that the write occurs before the read. These no-op instructions form a **pipeline bubble** which propagates down the pipeline. 
##### Interlocks
- The instruction decode hardware, upon encountering instruction B that reads a register written by A, will detect the hazard and delay the execution of B until A has compiled the writeback stage. The pipeline above would be delayed by three clock cycles to permit Aa to complete. This can be reduced to two cycles if slightly more complex forwarding logic is provided, which detects that A is writing the same location that B is reading, and directly provides the data rather than requiring the write to occur before the read. **Interlocks provide hardware that automatically inserts pipeline bubbles.**
##### Out-of-order execution
- Hardware is provided that detects a hazard, but instead of simply delaying execution of B, proceeds to fetch C, and if C does not read registers written by either A or B, and does not write registers read by B, then proceeds to execute C before B. Reduces the number of pipeline bubbles
	- This creates a **control hazard**.

#### Methods to deal with control hazards
##### Delay branch
- Documents that a branch will take some number of cycles after it is encountered, and leaves it up to the programmer or compiler to ensure that the instructions follow the conditional branch. 
##### Interlock
- Provides hardware to insert pipeline bubbles as needed, just as with data hazards
##### Speculative execution
- The most elaborate technique, where hardware estimates whether the branch is likely to be taken, and begins executing the instructions as it expects to execute. If the expectation is not met, then it undoes any side effects (like register writes) that the speculatively executed instructions caused.


Except for explicit pipelines and delayed branches, all of these techniques introduce variability in the timing of execution of an instruction sequence. 

### Instruction-Level Parallelism
- Parellelism can take two broad forms, multicore architectures, or **instruction-level parallelism** (ILP)
	- A processor with ILP can perform multiple independent operations in each instruction cycle. 
- There are four major forms of ILP
	- CISC instructions
	- Subword parallelism
	- Superscalar
	- VLIW
#### CISC Instructions
- CISC = Complex instruction set computer
- A processor with complex (and typically specialized instructions) is called a CISC machine
	- Different than RISC (reduced set instruction computers)
- These can get really esoteric, and they are extremely challenging for a compiler to make optimal use of an instruction set
	- DSP processors are often used with code libraries written and optimized in assembly language. 
	- They can have issues with achieving hard real-time scheduling. 
#### Subword Parallelism
- Many embedded applications operate on data types that are considerably smaller than the word size of the processor. 
	- Data types are typically 8-bit integers, meaning it would be wasteful to use a 64-bit ALU to process a single 8-bit number
- Some processors implement subword parallelism where a wide ALU is divided into narrower slices enabling simultaneous arithmetic or logical operations on smaller words
- Subword parallelism was introduced by Intel in the general purpose Pentium processor and was called MMX.
	- Instructions were dividing the 64-bit datapath into slices as small as 8 bits.
- A **Vector Processor** is one where the instruction set includes operations on multiple data elements simultaneously. 
#### Superscalar Processors
- Uses fairly conventional sequential instruction sets, but the hardware can simultaneously dispatch multiple instructions to distinct hardware units when it detects that such simultaneous dispatch will not change the behavior of the program. These processors even support out-of-order execution, where instructions later in the stream are executed before earlier instructions. This makes execution times extremely difficult to predict, and in the context of multitasking (interrupts and threads), may not even be repeatable. 
#### VLIW
- VLIW = very large instruction word
- VLIW architectures are used instead of superscalar in order to get more repeatable and predictable timing. These include multiple function units, like superscalar processors, but instead of dynamically determining which instructions can be executed simultaneously, each instruction specifies what each function unit should do in a particular cycle.
	- A VLIW instruction set combines multiple independent operations into a single instruction. Like superscalar architectures, these multiple operations are executed simultaneously on distinct hardware. 
	- The order and simultaneity of the execution is fixed in the program rather than being decided on-the-fly. It's up the compiler or programmer (working at assembly language level) to ensure that the simultaneous operations are indeed independent. 
- Texas Instruments c6000 family of processors have a VLIW instruction set. Included in this family are three subfamilies of processors, the c62x and c64x fixed-point processors and the c67x floating-point processors. These are designed for use in wireless infrastructure (cell base stations and adaptive antennas), telecommunications (voice over IP and video conferencing), and imaging applications (medical imaging, surveillance, machine vision or inspection, and radar).
- TriMedia processor family, from NXP, is aimed at digital tv. The strategy is to make it easier for a compiler to generate efficient code, reducing the need for assembly-level programming. 

### Multi-core Architectures
- A combination of several processors on a single chip. These have only recently come into general-purpose computing
- **Heterogeneous multicore** machines combine a variety of processor types on a single chip vs multiple instances of the same processor type
- In embedded applications, multicore architectures are very advantageous because real-time and safety-critical tasks can then have a dedicated processor. 
- It's common to use multi-level caches, where the second or higher level cache is shared among the cores. This sharing makes it difficult to isolate the real-time behavior of the programs on separate cores.
- A different type of multicore architecture uses one or more *soft cores* together with custom hardware on an FPGA (field-programmable gate array). FPGA's are chips with hardware that is programmable using design tools. 