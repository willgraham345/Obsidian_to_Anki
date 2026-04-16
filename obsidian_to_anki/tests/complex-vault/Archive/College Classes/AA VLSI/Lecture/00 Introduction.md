P type vs N type
- P is positive (holes where electrons would be)
- N is negative (extra electrons)
- The first vacuum was let us amplify signals
	- Let us create the first computer (Electronic Numeral Integrator and Calculator)
		- 5000 additions per second
		- 150 kW
- Invention of the transistor is the next big invention
- Moving to silicon was the next big invention
- 1971 had the first microprocessor
- MOSFET has the giant advantage of scaling very gracefully over BJT
Moore's Law Limitations
- MOSFET physical limits
	- Leakage currrent
	- Quantum effect: ballistic transport, tunnel effects
	- Variability
- Economics' limits
	- Mask cost
	- Fab costs (ex: e-beam lithography)
- The big deal about a microprocessor is that it has an ARCHITECTURE
	- There are bit-widths and frequency

$P = \alpha f_c V_{DD}^2$ 
- Power and frequency relationship


# Verilog
HDL = hardware description language, you write out the description of a circuit
- Tool designed to describe a circuit
- NOT a programming language
	- You need to know what the underlying circuit IS
- The perk of that is you don't need to know everything about it

Verilog can also write test benches to verify your system
- Test benches are not designed to be physically limited

Describing an AND gate in verilog
- Module describes the boundary box of what you're trying to describe



The important parts of a verilog block is continuous assignments and always blocks
- continuous assignments is like connecting two wires together
``` verilog
assign variable = exp; //combinational logic

//procedural blocks (always blocsk in particular for synthesis)
variable = exp; //blocking
//holds the process until assignment is complete, and does things in sequential order (like reading a piece of C code)
// 

variable <= exp; //non-blocking. Can result in combinational or sequential logic.
// What will really happen is that there is a tool that will create a hardware block, which will then try to do things
```

## Two types of Descriptions in Verilog
### Structural
- Explicit structure of the gate
- e.g. each logic gate instantiated and connected to others
### Behavioral
- Program describes input/output behavior of circuit
- Many structural implementations could have same behavior
- e.g. Different implementations of one Boolean function