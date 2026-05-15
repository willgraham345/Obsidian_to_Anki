Drawing the mask layers that will be used by fabrication people to make the devices
- Different from schematics
	- Schematics describe the LOGICAL connections
	- In layout you also describe the physical connections



## Example N-Type Transistor
Top view shows patterns that make up the transistor
- Diffused (active) mask is actually drawn as a solid rectangle
- Polysilicon mask goes on top of the active. 

## Layout basic ideas
-  you want transistors to be as small as possible, driving as much current as possible
	- You want L to be as small as possible, with W being whatever you need
- Masks cost in the $20M range
- Designing things in the 3 nanometer ranges

## General CMOS Cross Section
- Note that the general substrate is p-type
- The N-substrate for the P-transistor is in a "well"
	- There are lots of other layers
		- Thick SiO2 oxide ("field oxide")
		- Thin SiO2 oxide ("gate oxide")
		- Metal for interconnect
		- The thicker you're able to make these gates, the more you can limit quantum and leakage effects
		- The less resistive you can make this, the better off you'll be on packing in more and more transistors. 
	- Cutaway view
		- CMOS structure with both transistor types and a top-view structure 

# Layout Basics
- ![[Pasted image 20230914143055.png]]
- ![[Pasted image 20230914143103.png]]


Transistor: Where poly crosses active
- For N-type, nactive over the substrate (p substrate)
- For P-type, pactive inside an Nwell

There's really only one "active" mask
- Nselect and pselect layers define active types
- Our setup has separate nactive and pactive colors to help keep things straight. 
- Diffusion, poly, and metal all conduct
	- Resistances are very bad
		- Diffusion is worst, poly isn't too bad, metal is by far the best
- Contact cuts are needed to connect between layers


## Layout Subtlety
- We think of transistors as three terminal devices
	- Gate, source, drain
- They are really four-terminal devices
	- There's also a connection to the substrate
	- It's important to tie the substrate to a specific voltage
		- GND for P-substrate
		- VDD for N-well
			- Make sure PN-diodes from active to substrate and are reverse-biased
