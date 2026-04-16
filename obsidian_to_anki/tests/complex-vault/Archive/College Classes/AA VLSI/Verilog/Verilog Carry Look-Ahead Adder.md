# Background
The drawback in a ripple carry adder is that it has carry propogation delay inducing slow computation. The $i$ block waits for the $i-1$ block to produce its carry.
- Adders are used in designs like multipliers and divisions. A CLA can be used to reduce propagation delay, by computing the carry signals in advanced based on input signals. 
## How it works
Broken up into two modules
- Partial Full Adder (PFA)
	- Generates  $S_i, P_i, G_i$ 
		- $G_i = A_i B_i$
		- $P_i = A_i ^\wedge B_i$
		- $S_i = A ^\wedge B_i ^\wedge C_i = P_i ^\wedge C_i$
- Carry look-ahead logic
	- Generates the carry-out bits
	- $C_1 = G_0 + P_0C_0$
	- $C_4 = G_3 + P_3G_2 + P_3P_2G_1 + P_3P_2P_1G_0 + P_3P_2P_1P_0C_0$

| A   | B   | Carry In | Description              |
| --- | --- | -------- | ------------------------ |
| 0   | 0   | 1        | Carry not propagated (0) |
| 0   | 1   | 1        | Carry is propagated (1)  |
| 1   | 0   | 1        | Carry is propagated (1)  |
| 1   | 1   | 1        | Carry is propagated (1)                         |

![[carry_look_ahead_adder.webp]]
## Pros
- Requires complex hardware to generate the carry based on input signals and complexity grows with increasing bits. 
## Cons
- Does not need to wait till the previous stage generates the carry. It can generate carry for each full adder simultaneously, hence it is faster compared to ripple carry adder
- Needs more hardware, so circuit is costlier
- Gets much more complicated for more than 4 bits. These are usually implemented as 4-bit modules




# Verilog Code
```verilog
module CarryLookAheadAdder(
  input [3:0]A, B, 
  input Cin,
  output [3:0] S,
  output Cout
);
  wire [3:0] Ci; // Carry intermediate for intermediate computation
  
  assign Ci[0] = Cin;
  assign Ci[1] = (A[0] & B[0]) | ((A[0]^B[0]) & Ci[0]);
  //assign Ci[2] = (A[1] & B[1]) | ((A[1]^B[1]) & Ci[1]); expands to
  assign Ci[2] = (A[1] & B[1]) | ((A[1]^B[1]) & ((A[0] & B[0]) | ((A[0]^B[0]) & Ci[0])));
  //assign Ci[3] = (A[2] & B[2]) | ((A[2]^B[2]) & Ci[2]); expands to
  assign Ci[3] = (A[2] & B[2]) | ((A[2]^B[2]) & ((A[1] & B[1]) | ((A[1]^B[1]) & ((A[0] & B[0]) | ((A[0]^B[0]) & Ci[0])))));
  //assign Cout  = (A[3] & B[3]) | ((A[3]^B[3]) & Ci[3]); expands to
  assign Cout  = (A[3] & B[3]) | ((A[3]^B[3]) & ((A[2] & B[2]) | ((A[2]^B[2]) & ((A[1] & B[1]) | ((A[1]^B[1]) & ((A[0] & B[0]) | ((A[0]^B[0]) & Ci[0])))))));

  assign S = A^B^Ci;
endmodule
```

```verilog
module TB;
  reg [3:0]A, B; 
  reg Cin;
  wire [3:0] S;
  wire Cout;
  wire[4:0] add;
  
  CarryLookAheadAdder cla(A, B, Cin, S, Cout);
  
  assign add = {Cout, S};
  initial begin
    $monitor("A = %b: B = %b, Cin = %b --> S = %b, Cout = %b, Addition = %0d", A, B, Cin, S, Cout, add);
    A = 1; B = 0; Cin = 0; #3;
    A = 2; B = 4; Cin = 1; #3;
    A = 4'hb; B = 4'h6; Cin = 0; #3;
    A = 5; B = 3; Cin = 1;
  end
endmodule


```