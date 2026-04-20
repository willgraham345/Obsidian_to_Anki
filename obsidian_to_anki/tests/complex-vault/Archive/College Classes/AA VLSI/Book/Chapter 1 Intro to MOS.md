# MOS Transistors
Silicon is a 3d lattice. It's conductivity can be raised by introducing small amounts of impurities called "*dopants*". 
A MOS (metal-oxide-semiconductor) is created by superimposing several layers of conducting and insulating materials to form a sandwich-like structure. These are manufactured with chemical processing steps. 


Each transistor consists of a stack known as the gate (insulating layer of silicon dioxide a.k.a. glass), and the silicon wafer (a.k.a substrate, body, or bulk). Gates are now made from polycrystalline silicon. An nMOS transistor is built with a p-type body with regions of n-type semiconductor adjacent to the gate (source and drain). 
- a pMOS transistor is just the opposite, consisting of p-type source and drain regions with an n-type body. 

The gate is a control input. 
![[Pasted image 20230822144418.png]]
- The positive voltage is usually called $V_{DD}$ or $POWER$ and represents a logic 1 value in digital circuits. 
	- In popular logic families, $V_{DD}$ was set to 5V.

# CMOS Logic
## The Inverter
CMOS inverter is a NOT gate using one nMOS transistor and one pMOS transistor. 
 

The bar at the top is $V_{DD}$, and te

## CMOS Logic Gates
Two transistors in series are ON only if all the series transistors are ON. 
Two transistors in parallel are ON only if any of the parallel transistors are ON.


When we join a pull-up network to a pull-down network to form a logic gate, they will both attempt to exert a logic level at the output. 

- When both pull-up and pull-down are OFF, the high impedance or floating Z output state results. 
	- This matters for multiplexers, memory elements, and tristate bus drivers. 
	- The crowbarred (or contention) X level exists when pull-up and pull-down are simultaneously turned ON. Contention between the two networks results in an indeterminate output level and dissipates static power (usually unwanted)
	- ![[Pasted image 20230823113734.png]]
## Compound Gates
Performs a more complex logic function in a single state of logic, formed by using a combo of series and parallel switch structures. 


## Pass Transistors and Transmission Gates
*Strength* = how closely it approximates an ideal voltage source. 
- The stronger a signal, the more current it can source or sink. The power supplies are the strongest 1s and 0s.
An nMOS transistor is almost a perfect switch when passing a 0 and thus we say it passes a *strong* 0
- An nMOS transistor is imperfect at passing a 1. It's somewhat less than the $V_{DD}$ 

**Pass transistor** = When an nMOS or pMOS is used alone as an imperfect switch
- By combining an nMOS and a pMOS in parallel, we obtain a switch that turns on when a 1 is applied. 
- ![[Pasted image 20230823115416.png]]
Both control input and its complement are required by the transmission gate
- **Double rail** logic

In all examples so far, the inputs drive the gate terminals of nMOS transistors in the pull-down network, and pMOS transistors in the pull-up network. Thus, nMOS transistors only need to pass 0s and the pMOS transistors only need to pass 1s. This is considered a fully restored logic gate, and simplifies circuit design considerably. There is never a path through `ON` transistors from the 1 to the 0 supplies. 



A consequence of static CMOS gates is that they must be inverting. The nMOS pull-down network turns ON when the inputs are 1, leading to a 0 at the output. 

### Tristates
When the enable input EN is 1, the output Y is equal to the input A, just as in an ordinary buffer. 
A nonrestoring circuit: If the input is noisy or otherwise degraded, the output will receive the same noise. 
- When the output is driven from $V_{DD}$ or GND, it is a restoring logic gate. The tristate converter does not obey the conduction complements rule because it allows the output to float under certain input combinations. 
### Multiplexers
Key components in COS memory elements and data manipulation structures. 
- Chooses the output from among several inputs based on a select signal. 
- Two transmission gates can be tied together to form a compact 2-input multiplexer
- Transmission gates produce a nonrestoring multiplexer