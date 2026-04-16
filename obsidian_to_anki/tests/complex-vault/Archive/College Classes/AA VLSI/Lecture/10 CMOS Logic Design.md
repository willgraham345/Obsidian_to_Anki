# Review 
- DRC (design rule checker)
	- Ensures that chips are made with high quality, and ensures that chip can be created with a guaranteed yield. 
	- The DRC dictates different rules defining what can be done layer-to-layer
- Different Layout
	- We created a NAND gate to make the layout more compact
	- We have an n-well that is designed to be shared
	- We can combine sources and drains together to make multiple contacts
		- Creates multiple transistors in series
- PMOS biased to $V_{DD}$, NMOS substrate should be biased to $V_{SS}$ 
# CMOS Logic Design 

## Standard Cells
### NOT
Truth Table

| Potential | A   | Y   | Potential |
| --------- | --- | --- | --------- |
| $V_{SS}$  | 0   | 1   | $V_{dd}$  |
| $V_{dd}$  | 1   | 0   | $V_{ss}$          |

## NAND2

| State | A   | B   | Y   |
| ----- | --- | --- | --- |
| 1     | 0   | 0   | 1   |
| 2     | 0   | 1   | 1   |
| 3     | 1   | 0   | 1   |
| 4     | 1   | 1   | 0    |
How do we make this?
- The output will be zero, when A and B are equal to 1.
- We'll use two pMOS transistors on bottom in series
T
## Duality Principle
- If you switch the parallel and serial configuration of a NOR2 gate, you get a NAND2 gate. Same with vice versa. It has a strong implication that it means is that you really only care if you're creating a pull-up or a pull-down network. 

## Standard Cells Complex Gates
Canonical form AND-OR: $Y = (A * B ) + (C * D )$


## Pass Gate
| G   | Y   | Function       | Representation |
| --- | --- | -------------- | -------------- |
| 0   | Z   | High Impedance | Open Switch    |
| 1   | A   | Transmission   | Closed Switch               |
The pass gate can help us pass 0's with an nMOS, but you can't pass a 1 (you'll get a $-V_{DD} - V_{thn}$)


# Review from Last Lecture

## Pass Gate Logic Gate
- Rather than going between 0 and 1, you're controlling if the input is following the input, or in high impedance. 
	- It's a single transistor. If we want to propogate 1's or 0's, we end up with a problem, in that pass gates are able to propogate 0's, but unable to propogate 1's correctly. 
		- You'll have a $\Delta V$ as an output
			- This will limit switching speed. 
			- It will not affect much for the next gate, but the noise margins may end up failing if these are cascaded.
				- In the old days, they'd throw in a buffer with a noise margin. This isn't great, because it takes a ton of space. We don't do this anymore, because our voltages today are much lower. 
- Instead of using these, we now use transmission gates
	- We use a pMOS to pass the 1's, and an nMOS to pass the 0's
	- We put two transistors in parallel, with an inverter between them. It lets you transmit both 0's and 1's

## Multiplexor
| G   | Y   |
| --- | --- |
| 0   | A   |
| 1   | B   | 

- Pass A OR B
- You can use 2 transmission gates, which will also lower our transistor count
	- We go from 16 transistors to 6 when implementing transmission gates over nand gates. 
	- The NAND is much better for speed, but much worse for area. 


# Review
We can use a different path to use multiplexors
- Mask: MUX Blue is wires
- We must have a bulk tap within a given distance of a transistor source. 
	- To have a nice potential 


The blue signal G is an input. 


## Sequential Logic
### Combination Logic:
- Output depends on current inputs
### Sequential Logic
- Output depends on current and previous inputs
- Requires separating previous, current, future
- Called *state* or *tokens*
	- How do we create storage for sequential logic? (flip-flops)
- Examples: FSM, pipelines

## Flip-Flop
- Flip flops are made out of latches
	- Latches are not edge-triggered, they are level-triggered
		- Transparent if the control input is equal, and will keep its previous value otherwise
		- Similar to the water in a pipe once the pipe is closed. It just stays put. 
- D flip flop
	- Element to be edge triggered
	- Whenever there is a transition on the clock, you do something. 
	- The transition matters
### Operation of a Flip-Flop
- When clock goes up, the setup time begins. The flip
- The setup time is when the input must be stable before the edge of interest arises. 
	- The hold is the time in which the input must be stable after 
	- Basically, you need to have things stable before you trigger the latch (the setup time)
- It takes time for data to go through our circuits
- There's a lot of timing within EE 3700 regarding these calculations

### Implementing a Flip Flop
- You can play lots of different tricks with the timing of your cells to fit different margins. 