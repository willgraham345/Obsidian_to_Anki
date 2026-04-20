Algorithmic State Machine: A flow chart for design of a digital circuit

- In digital systems, the binary information is divided into data and control information
- Control information gives various command signals that help perform various data operations
- Logic design of digital systems can be divided into:
	- Part responsible for design of the circuit that performs data processing operations
	- Part responsible for design of the control circuit which takes care of all operations and sequences
- Control sequence and data processing of digital system can be determined by a hardware algorithm. 
	- A flow chart is a traditional method for determining the sequence of procedural steps and decision paths for a hardware algorithm. 
# Elements

## State Box
![[Pasted image 20230922173643.png]]
- Represents a state
- Contains register transfer actions or output signals
- Customary to write only the name of the signal that has to be asserted in the given state
	- i.e. `z` instead of `z<=1`
	- It might be useful to write an action to be taken
		- e.g. `cout <= cout + 1`
## Decision Box
![[Pasted image 20230922173837.png]]
- Effect of the input on the control subsystem
- A given condition to be tested

## Condition Box
![[Pasted image 20230922173922.png]]
- A conditional output box
- Determines whether such outputs are generated is specified in the preceding decision box.

# ASM Chart Rules
- Transition is governed by a clock
- Transition occurs between ASM blocks
- For a given input combination, there is one unique exit path from the current ASM block
- Any closed loop in an ASM chart must include a state box