# Background
Digital logic circuit that performs binary subtraction of two single bit binary numbers. 

## Pros
Simple and easy to design
Low cost, easy integration
## Cons
Inefficient for multi-bit numbers
High propagation delay
## Applications
Calculators, alarm frameworks, automotive, security, computer frameworks. 

# I/O
## Inputs
- A
	- Single bit number
- B
	- Single bit number
## Outputs
 - DIFFERENCE
	 - Difference between two bits
	 - XOR of the two inputs
 - BORROW
	 - Indicates if borrowing was necessary during the subtraction
	- NOT of A and AND of inputs A and B

# Truth Table

| A   | B   | Diff | Borrow |
| --- | --- | ---- | ----- |
| 0   | 0   | 0    | 0     |
| 0   | 1   | 1    | 1     |
| 1   | 0   | 1    | 0     |
| 1   | 1   | 0    | 0     |

## SOP form 
Diff = 
Borrow = $\bar{A}B$



![[Pasted image 20231026145214.png]]
Can be implemented much better in with NAND and NOR gates [here](https://www.geeksforgeeks.org/half-adder-half-subtractor-using-nand-nor-gates/)