# Background
The primary difference of a full-adder is that it can easily carry the current inputs as well as the output from the previous additions. 
Adds three inputs, and produces two outputs
- C-OUT is known as the majority 1's detector, whose output goes high when more than one input is high
Designed in such a manner that can take eight inputs together to create a byte-wide adder and cascade the carry bit from one adder to another. 
- We use a full adder because when a carry-in bit is available, another 1-bit adder used since a 1-bit half-adder does not take a carry-in bit. 
- A 1-bit full adder adds three operands and generates 2-bit results. 

More information [here](https://www.geeksforgeeks.org/full-adder-in-digital-logic/):

## Pros
- Flexible, and can be used to add multi-bit numbers by binding different full adders together
- Carry info
	- Has a convey input which permits it to perform expansion of multi-bit numbers and to chain different adders together
- Speed

## Cons
- More complex than a half adder, and requires more parts
- Propagation deferral




# I/O
## Inputs
- A
	- Single bit number
- B
	- Single bit number
- C-IN
	- input carry
## Outputs
 - SUM
	 - LSB of the result
 - C-Out
	 - MSB of the result



![[Pasted image 20231026145512.jpg]]