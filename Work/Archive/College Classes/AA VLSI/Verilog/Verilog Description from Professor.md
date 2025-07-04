# What is an HDL?
- An HDL (Hardware description language) can be thought of as a shorthand for describing digital hardware. 
- HDLs have specific ways of describing various classes of logic, called *idioms*. 
	- There are many ways to write HDL code whose behavior in simulation and synthesis differ. 

# Verilog History
## Verilog has a Split Personality
### Verilog is a HDL (hardware description language)
- Used to describe hardware elements, completely different than software development. Non-sequential.
### Testbench Creation Language
- Creates external test environment
	- Time & Voltage
	- Files & messages

# Quick Review Example
```verilog
Module name(args...);
	begin
		parameter ...; //define parameters
		input ...; //define inputs
		output ...; //define outputs
		wire ...; //internal wires
		reg ...; //internal regs, possibly output
	/// the parts of the module body are executed concurrently
	<continous assignments>
	<alwayss blocks>
endmodule
```

## Continuous Assignments to `wire` vars
- `assign variable = exp;`
	- Results in combinational logic
## Procedural assignment to `reg` vars
- Always inside procedural blocks (`always` blocks in particular for synthesis)
- blocking
	- `variable = exp;`
- non-blocking
	- `variable <= exp;`
- Can result in combinational or sequential logic. 

# Verilog Description Styles
## Structural
- Explicit structure of the circuit
- e.g. each logic gate instantiated and connected to others
## Behavioral
- Program describes input/output behavior of circuit
- Many structural implementations could have the same behavior
- e.g. different implementation of one Boolean function 
	- `y = a + b` is a description, but it doesn't provide description of how that happens

# Synthesis: Data Types
## Possible Values (`wire` and `reg`)
- `0`: Logic 0, false
- `1`: logic 1, true
- `Z`: High impedance
- `X`: Unknown
## Digital Hardware
- Domain of verilog
- Either `logic` (gates)
- Or `storage` (registers & latches)
- Verilog has two relevant data types
	- `wire`
	- `reg`
		- Latch contain information 
## Declarations
### Register Declarations
- `reg a;` 
	- Scalar register
- `reg[3:0] b` 
	- a 4-bit register
- `output g`; 
	- An output can be a reg
	- `reg g;`
- `output reg g; ` 
	- Verilog 2001 syntax
### Wire Declarations
- `wire d;`
	- A scalar wire
- `wire [3:0] e`
	- A 4-bit vector wire
- `output f`
	- An output can be a wire
### Parameters
- Used to define constants
``` verilog
parameter size = 16, foo = 8;
wire[size-1:0] bus; //defines a 16 bit bus
```