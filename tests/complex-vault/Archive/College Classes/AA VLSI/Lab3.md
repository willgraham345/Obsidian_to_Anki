#### What is CMOS technology? Briefly explains how it works.
- Complimentary metal oxide technology. The idea is to use both PMOS and NMOS technology to create logic functions. This enables both strong 0's and 1's to be passed along in logic gates. This provides higher noise immunity. 
#### For a transistor, what Ion and Io f f refer to? When measuring Ion and Io f f for an nmos transistor, what should be the values of VGS and VDS ?
- $I_{on}$ is the drain current at a voltage when the transistor is conducting, and $I_{off}$ is the drain current at a drain voltage. $I_{off}$ is the leakage current, which can often be idealized as zero when under manual analysis. 
- 
- $I_{OFF}$ is when $V_{gs}=0$ and $V_{ds} = V_{DD}$. 
- $I_{dsat}$ happens when $V_{gs} = V_{ds} = V_{DD}$.
	- In the long-channel model, $I_{off} = 0$, and $I_{on} = \frac{\beta}{2}(V_{DD} - V_t)$. 
- 
#### What is the function of a CMOS inverter? Draw its schematic.
- Flip digital logic. These can help to reduce footprint of circuits. 
- ![[Pasted image 20231002195630.png]]
	- Grabbed from book
#### Draw the Voltage Transfer Characteristic (VTC) and explain what is the switching point of a CMOS inverter.
- The VTC is a graph that shows the relationship between input and output voltages in a digital circuit. Can be used to measure the quality of a digital inverter. 
- ![[Pasted image 20231002200910.png]]![[Pasted image 20231002200910.png]]
- ![[Pasted image 20231002200934.png]]
- ![[Pasted image 20231002200944.png]]
#### When considering both input and output curves from a logic gate, how are the propagation delay, rising and falling time usually calculated?
- We usually apply a linear model, with inputs and outputs approximated as ramps. These are typically calculated as linear times, without worrying about first and second order characteristics. This can involve multiplying by 0.69 to approximate a first order system, or through multiplication of another approximating constant. 
#### What are the ff/tt/ss process corners in VLSI design? Why it is important to consider them when designing?
- Fast fast, typical typical, and slow slow. These are different manufacturing conditions and variations that can influence how well a circuit can be made. The idea is that you have a wide range of timing behind how well your circuit is likely to perform. You're essentially drawing a box around the performed of a circuit so it is guaranteed to work as designed. 
	- This lets us bin parts and make them more quickly. 