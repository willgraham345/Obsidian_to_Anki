---
type: note
---
ISA is where software meets hardware

ISA set components
- Operants: `int32, uint32, uint16, int8, uint8, float32, float64`
- Addressing modes: How do we access data (in regs, memory, etc)
- Operations: 4 major types
	- Operator functions (add, shift, xor, mul, etc)
	- Data movement (in regs, memory, etc)
	- Control transfer (branch, jump, call, return, etc)
	- Privileged and miscellaneous instructions (not part of the application)

ISA design considerations
- Simple target for compilers
- Support for OS and programming language features
- Support for important data types (floating-point, vectors)
- Code size
- Impact on execution efficiency (especially with pipelining)
- Backwards compatibility with legacy processors
- Provision for extensions

## N bit instruction set
What does an `n` bit instruction set mean?
- It means that data is n bits
	- Registers are n bits, addresses typically are n bits
	- MIPS that we study: 32-bit instruction set
	- RISC-V has 32 bits, 64 bits (and 128 bits)
- The size of each instruction in bits is independent
	- 64-bit RISC-V also uses 32 bit instruction size

## CISC vs RISC
### CISC
- Assembly programming -> HLL features as instructions
- Small number of registers (but memory is “fast) -> in-memory operands
- Code size must be small (transistors scarce) -> variable length instructions
- Backward compatibility -> complexity grows over time
### RISC
- Compilers -> simple instructions
- Large number of registers, memory much slower than processor -> load-store architecture
- Simple and fast decoding -> fixed length, fixed format


Instruction Classes
- Arithmetic and logic operations
- Execution template: fetch operands, perform op, store result
Instructions that move data
- Move data between registers, memory and I/O devices
Instructions that change control flow
- Redirect the control flow away from the next instruction 
- May be conditional or unconditional (including exceptions)

## Operators and their Instructions
Integer arithmetic (add, subtract, multiply, divide, remainder)

Relational
- < Set on less than 
- <= sle, sleu
- > sgt, sgtu
- >= see, sgeu
- == seq
- != sne

Branch

Instruction Operands - Registers
	- How many register-based operands should be specified?