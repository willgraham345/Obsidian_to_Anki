---
type: note
---
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