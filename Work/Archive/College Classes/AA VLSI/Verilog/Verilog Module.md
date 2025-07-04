# Background
A module is a circuit that interacts with its outside through input and output ports. Complex circuits are built by composing bigger modules out of smaller modules and other pieces connected together. 
- A block of hardware with inputs and outputs
	- Modules can be described behaviorally, or structurally. 
## Behavior vs Structure
Behavior describe what a modules does
Structural describes how a module is built from simpler pieces. 


# Connecting Signals to Module Ports
## By position
```verilog
module_name instance_name ( wa, wb, wc ); //wa connects to first port, wb to second, wc to third
```
## By name
```verilog
module_name instance_name (.out(wc), .in1(wa), .in2(wb) ); //connects wc to out, wa to in1, wb to in2
//ordering is irrelevant
```


## Vectors to Ports
- Vector length of the port does not have to match the wire connecting to it, but this will cause zero-padding or truncation of the vector. 


## Examples
Logic Function
```verilog
module sillyfunction(input logic a, b, c,
output logic y);
assign y = ~a & ~b & ~c |
a & ~b & ~c |
a & ~b & c;
endmodule
```

32-bit Address
```verilog
module adder(input logic [31:0] a,
input logic [31:0] b,
output logic [31:0] y);
	assign y = a + b;
endmodule
```
