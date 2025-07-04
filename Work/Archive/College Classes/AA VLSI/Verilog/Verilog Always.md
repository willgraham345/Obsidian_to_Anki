- Verilog behavior models contain procedural statements that control simulation, and manipulate variables to model hardware circuitry and data flow. 
- Each Verilog block always starts a separate activity flow. 
- Each Verilog `always` block repeats continuously throughout the duration of the simulation, executing the statements defined in its procedure. 

# Sequential vs Combinational Logic
Sequential
- Execution triggered based on a clock event (and frequently a reset event)
Combinational logic
- Execution trigered based on inputs to the logic (i.e. nets and variables on the right hand side of an assignment statement)

## Sequential Logic 
Synchronous
```verilog
always @(posedge clk)
	q <= d;
```
This describes an asynchronous reset (occurs without the clock)
```verilog
always @(posedge clk or negedge rst_n) 
	if (!rst_n) 
		q <= 1'b0; 
	else 
		q <= d;
```

## Combinational Logic 
- A physical implementation of a combinational circuit operates continuously, but 