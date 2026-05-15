A.k.a a Latch

Circuits that have two stable states that can store information. The circuit can be made to chagne state by signals applied to one or more control inputs and will output its state.


# D Flip-flop
- Known as the data or delay flip-flop
- Captures the value of D-input at a definite portion of the clock cycle (such as the rising edge of the clock). That captured value becomes the $Q$ output. At other times, $Q$ does not change. 
	- Can be viewed as a memory cell, a zero-order hold, or a delay line. 
## Symbol and Circuit Diagrams
![[Pasted image 20230922111816.png]] ![[Pasted image 20230922112146.png]]
## Truth Table
|Clock|$D$|$Q{next}$|
|---|---|---|
|Rising edge|0|0|
|Rising edge|1|1|
|Non-rising|$X$|$Q$|
## Clock
When a flip-flop sees a rising edge of the clock, it registers the data from the Input D to the Output Q. 
![[Pasted image 20231106160146.png]]