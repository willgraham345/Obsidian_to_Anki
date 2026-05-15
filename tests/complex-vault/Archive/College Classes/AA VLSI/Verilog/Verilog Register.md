# Background
- A reg (register) is a data object, which is holding the value from one procedural assignment to the next one and are used only in different functions and procedural blocks.
- A reg is a simple Verilog variable-type register and can't imply a physical register. In multi-bit registers, the data is stored in the form of unsigned numbers and sign extension is not used.
	- It does NOT synthesize. In System Verilog they created the `logic` data type to replace `reg`
## Example
```verilog 
reg c; // single 1-bit register variable
reg [5:0] gem; // a 6-bit vector;
reg [6:0] d, e; // two 7-bit variables
```

