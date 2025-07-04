# Background
A combinational circuit that performs subtraction of two bits, one is minuend and the other is subtrahend taking into account the borrow of the previous adjacent lower minuend bit. 

3 inputs, 2 outputs
## Pros

## Cons



# I/O
## Inputs
- $A$
	- Minuend
- $B$
	- Subtrahend
- $B_{in}$
	- Previous borrow
## Outputs
- $D$
	- Difference
		- $D = (A ^\wedge B ) ^\wedge B_{in}$
- $B_{out}$
	- Output borrow
		- $B_{in} ( A ^\wedge B)' + A'B$
		- 





## Truth Table
![[Pasted image 20231027134226.jpg]]![[Pasted image 20231027135300.jpg]]