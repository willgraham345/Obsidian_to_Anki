# Gate Primitives
## Background
Basic logic gates using one output and many inputs are used in Verilog. GATE uses one of the keywords and, nand, or, nor, xor, xnor for use in Verilog for N number of inputs and 1 output
## Example
```verilog
Example:  
   Module gate() 
   Wire ot0; 
   Wire ot1; 
   Wire ot2; 
   
   Reg in0,in1,in2,in3; 
   Not U1(ot0,in0); 
   Xor U2(ot1,in1,in2,in3); 
   And U3(ot2, in2,in3,in0)
```

## Going back to basics
```verilog
module and_gate(output out, input a, input b)
	assign out = a & b;
endmodule

module nor_gate(output out, input a, input b)
	assign out = ~(a | b);
endmodule
```
# Transmission Gate Primitives
## Background
- Includes both, buffers, and inverters.
- Single input, and one or more outputs. In the gate instantiation syntax, GATE stands for either the keyword `buf` or the `NOT` gate
## Example
```verilog
Example:  
   Module gate() 
   Wire out0; 
   Wire out1; 
   
   Reg in0,in1;
   Not U1(out0,in0); 
   Buf U2(out0,in0);
```

Not, buf, bufif0, bufif1, notif0, notif1

Not – n outout inverter

Buf – n output buffer

Bufifo – tristate buffer, active low enable

Bufif1 – tristate buffer, active high enable

Notifo – tristate inverter, active low enable

Notif1 – tristate inverter, active high enable