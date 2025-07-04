# Background
A logic circuit that performs binary addition of two single-bit numbers
## Pros
Simple and fast
## Cons
Limited usefulness

## Applications
Arithmetic circuits, data handling, address unraveling, encoder and decoder circuits, multiplexers and demultiplexers, counters

# I/O
## Inputs
- A
	- Single bit number
- B
	- Single bit number
## Outputs
 - SUM
	 - LSB of the result
 - CARRY
	 - MSB of the result


# Truth Table

| A   | B   | Sum | Carry |
| --- | --- | --- | ----- |
| 0   | 0   | 0   | 0     |
| 0   |  1   |  1   |   0    |
| 1   |   0  |  1   |   0    |
| 1    |   1  | 0    | 1      |

SUM = $A (XOR) B$ = $A\bar{B} + \bar{A}B$
CARRY = $A(AND)B$ = $A*B$


# Image
![[Pasted image 20231026142807.png]]
Can be implemented much better in with NAND and NOR gates [here](https://www.geeksforgeeks.org/half-adder-half-subtractor-using-nand-nor-gates/)