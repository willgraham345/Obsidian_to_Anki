# Verilog
Blocking vs non-blocking
- A standard programming language is always blocking

```verilog
module the_top (clk, rst, a, b, sel, result); input clk, rst; 
	input [3:0] a,b; 
	input [2:0] sel; output reg [3:0] result; 
	wire[3:0] sum, dif, alu; adder u0(a,b,sum); 
	subber u1(.subtrahend(a), .subtractor(b), .difference(dif)); 
	
	assign alu = {4{(sel == ‘b000)}} & sum 
		| {4{(sel == ‘b001)}} & dif; 
	always @(posedge clk or posedge rst) 
		if (rst) result <= ‘h0; 
		else result <= alu;

endmodule
```

Breakdown
This Verilog code appears to define a module called "the_top" that performs some arithmetic operations based on the values of inputs `a`, `b`, and `sel`, and produces the result in the `result` output. Let's break it down line-by-line
1. `module the_top (clk, rst, a, b, sel, result);`
    - This line defines a module named "the_top" with six ports: `clk`, `rst`, `a`, `b`, `sel`, and `result`.
2. `input clk, rst;`
    - Declares `clk` and `rst` as input signals.
3. `input [3:0] a, b;`
    - Declares `a` and `b` as 4-bit input signals.
4. `input [2:0] sel;`
    - Declares `sel` as a 3-bit input signal.
5. `output reg [3:0] result;`
    - Declares `result` as a 4-bit output register.
6. `wire [3:0] sum, dif, alu;`
    - Declares three 4-bit wires: `sum`, `dif`, and `alu`. These wires are used to hold intermediate values.
7. `adder u0(a, b, sum);`
    - Instantiates an "adder" module named `u0`, connecting inputs `a` and `b` to it, and outputting the result into `sum`.
8. `subber u1(.subtrahend(a), .subtractor(b), .difference(dif));`
    - Instantiates a "subber" module named `u1`, connecting inputs `a` and `b` as `.subtrahend` and `.subtractor`, respectively, and outputting the result into `dif`.
9. `assign alu = {4{(sel == ‘b000)}} & sum | {4{(sel == ‘b001)}} & dif;`
    - This line uses a conditional assignment to calculate the value of `alu`. It checks the value of `sel` and selects either `sum` or `dif` accordingly. If `sel` is 'b000', it selects `sum`, and if `sel` is 'b001', it selects `dif`.
10. `always @(posedge clk or posedge rst)`
    - This is a synchronous always block that triggers on the positive edge of the `clk` signal or the positive edge of the `rst` signal.
11. `if (rst) result <= ‘h0;`
    - If the `rst` signal is asserted (high), it sets the `result` register to all zeros ('h0).
12. `else result <= alu;`
    - If `rst` is not asserted, it assigns the value of `alu` to the `result` register.

In summary, this Verilog module performs either addition or subtraction based on the value of `sel` and produces the result on the `result` output. If the reset signal `rst` is asserted, it clears the result to zero. Otherwise, it computes the result based on the selected operation.
Always go with the verbal option, commenting as much as possible with verilog. 


## Priority vs Parallel Choice (if)
```verilog
module priority (a, b, c, d, sel, z);
	input a, b, c, d;
	input [3:0] sel;
	output z;
	reg z;
	always @(a or b or c or d or sel)
	begin
		z = 0;
		if (sel[0]) z = a;
		if (sel[1]) z = b; 
		if (sel[2]) z = c; 
		if (sel[3]) z = d;
	end
endmodule
```

What does this do?
- Every time the output value will output 
- Everything is blocking, and will have a notion of priority
	- The third bit has more priority and power than the rest
		- ![[Pasted image 20230831141737.png]]


```verilog
module priority (a, b, c, d, sel, z);
	input a, b, c, d;
	input [3:0] sel;
	output z;
	reg z;
	always @(a or b or c or d or sel)
	begin
		z = 0;
		if (sel[0]) z = a;
		else if (sel[1]) z = b; 
		else if (sel[2]) z = c; 
		else if (sel[3]) z = d;
	end
endmodule

```

- In this case:
	- There is no priority, the if/else creates a complex tree. 
		- We don't know what the alternative will be. We calculate the if/else, and move along. In the other one, it STOPS, and THEN moves on (i.e. blocking)
		- This is an example of parallel choices
			- ![[Pasted image 20230831141748.png]]


## Case Statements
- Multi-way decision on a single expression
```verilog
case ( <expresion> )
<expression>: <statement>
<expression>, <expression>: <statement>
<expression>: <statement>
default: <statement>
endcase
```

- Common with finite-state machines
```verilog
reg [1:0] sel;
reg [15:0] in0, in1, in2, in3, out;
case (sel)
	2’b00: out = in0;
	2’b01: out = in1;
	2’b10: out = in2;
	2’b11: out = in3;
endcase
```


### Case Example 2

```verilog
// simple counter next-state logic
// one-hot state encoding…
parameter [2:0] s0=3’h1, s1=3’h2, s2=3’h4; //
reg[2:0] state, next_state;
always @(input or state)
begin
	case (state)
		s0: if (input) next_state = s1;
			else next_state = s0;
		s1: next_state = s2;
		s2: next_state = s0;
	endcase
end
```

Behavior at 3 is undefined (we haven't told it what to do), so it creates a latch inference
### Latch Inference
- **Latch inference** = Incompletely specified if and case statements, which cause the synthesizer to infer latches

```verilog
always @(cond)
begin
	if(cond) data_out <= dat_in;
end
```
This infers a latch because it doesn't specify what to do when `cond = 0`
- Fix this by adding an `else` if you want combinational logic
- In a case, fix by including `default`


## Full vs Parallel
- Case statements: check each case in a sequence
	- A case statement is *full* if all possible outcomes are accounted for
	- A case statement is *parallel* if the stated alternatives are mutually exclusive
### Full and Parallel
```verilog
// full and parallel = combinational logic
module full-par (slct, a, b, c, d, out);
	input [1:0] slct;
	input a, b, c, d;
	output out;
	reg out; // optimized away in this example
	always @(slct or a or b or c or d)
		case (slct)
			2’b11 : out <= a;
			2’b10 : out <= b;
			2’b01 : out <= c;
			default : out <= d; // really 2’b00
		endcase
endmodule
```
- Creates a multiplexor
	- ![[Pasted image 20230831143149.png]]
### Not Full, but Parallel
```verilog
// a latch is synthesized because case is not full
module notfull-par (slct, a, b, c, d, out);
	input [1:0] slct;
	input a, b, c, d;
	output out;
	reg out; // NOT optimized away in this example
	always @(slct or a or b or c)
		case (slct)
			2’b11 : out <= a;
			2’b10 : out <= b;
			2’b01 : out <= c;
		endcase
endmodule
```
- Because this is not full, a latch is inferred:
	- Not fully defined, but it IS parallel
	- ![[Pasted image 20230831143305.png]]

### Parallel but not Full
```verilog
// because case is not parallel - priority encoding
// but it is still full, so no latch…
// this uses a casez which treats ? as don’t-care
module full-notpar (slct, a, b, c, out);
...
	always @(slct or a or b or c)
	casez (slct)
		2’b1? : out <= a;
		2’b?1 : out <= b;
		default : out <= c;
	endcase
endmodule
```
- 
- Full, but not parallel 
	- Not parallel
	- ![[Pasted image 20230831143426.png]]

### Not Parallel, Not Full

```verilog
// because case is not parallel - priority encoding
// because case is not full - latch is inferred
// uses a casez which treats ? as don’t-care
module full-notpar (slct, a, b, c, out);
...
	always @(slct or a or b or c)
		casez (slct)
			2’b1? : out <= a;
			2’b?1 : out <= b;
		endcase
endmodule
```
- ![[Pasted image 20230831144024.png]]


## FSM Description (finite state machine)
- There is a best way to describe FSMs (RTL design = resistor transistor level)
	- We do this because of timings
		- We want the clock to control the transfer of data between circuits
		- We have specific, and clear control of timing between register transfers. 
- How to do it:
	- Combinational block for next_state generation
	- A combinational block for output generation
	- A sequential block to store the current state
	- ![[Pasted image 20230831144328.png]]
		- Can be a Moore or a Mealy machine (doesn't really matter)
### Modeling State Machines
```verilog
module FSM (clk, in, out);
	input clk, in;
	output out;
	reg out;
	// state variables
	reg [1:0] state; //our register state variable
	// next state variable
	reg [1:0] next_state;
	always @posedge(clk) // state register
		state = next_state;
	always @(state or in); // next-state logic
		// compute next state and output logic
		// make sure every local variable has an assignment in this block
endmodule
```
- Every time clock kicks in, we put `next_state`, into `state`
	- ![[Pasted image 20230831144636.png]]
![[Pasted image 20230831144656.png]]



```verilog
module moore (clk, clr, insig, outsig);
	input clk, clr, insig;
	output outsig;
// define state encodings as parameters
	parameter [1:0] s0 = 2'b00,
	s1 = 2'b01,s2 = 2'b10, s3 = 2'b11;
// define reg vars for state register
// and next_state logic
	reg [1:0] state, next_state;
//define state register (with
//synchronous active-high clear)
	always @(posedge clk)
	begin
		if (clr) state = s0;
	else state = next_state;
	end
// define combinational logic for
// next_state
	always @(insig or state)
	begin
		case (state)
			s0: if (insig) next_state = s1;
				else next_state = s0;
			s1: if (insig) next_state = s2;
				else next_state = s1;
			s2: if (insig) next_state = s3;
				else next_state = s2;
			s3: if (insig) next_state = s1;
				else next_state = s0;
		endcase
	end
	// assign outsig as continuous assign
	assign outsig = ((state == s1) || (state == s3));
endmodule
```


## Unsupported for Synthesis
- Delay
- initial blocks
- repoeat
- wait
- fork
- event
- deassign
- force
- release
- Other:
	- You can't assign the same `reg` variable in more than one procedural block 
	  `always @(posedge a)
		  `out = in1;`
	  `always@(posedgeb)`
		  `out = in2`
	- Combinational Always Blocks
	- 

