## Questions at the beginning of class
### How should we submit our homework
Explain how we do things, along with the understanding commented inside of the code.


## Recap from the Last Lecture
We talked about the art of making masks (layout)n
- Sequence, and process flow of manufacture is very important. 
- Masks are designed according to that sequence.
	- Active layer is what we use to define the transistor dimensions (source, drain, channel)
		- What we use to define the active device. 
- What makes us say something is a device?
	- Superposition of certain shapes in certain layouts
		- I *think* a transistor is contacts that connect the:
			- Gate
			- Source
			- Drain
			- Substrate
				- Has to be polarized all the time to avoid diode conduction. 
We want to polarize our substrates to voltages: $V_{DD}$ and $V_{SS}$
- nMos should be biased to ground
	- Substrate nature of a pMos is slightly p_doped. That p_doped substrate must be biased to ground
- pMOS should be biased to $V_{DD}$
	- Substrate of a pMOS is an n-well, so it's an n-doped well. This n-well must be biased to $V_{DD}$
	- n well should be connected to $V_{DD}$

![[Pasted image 20230919141501.png]]
- The big green region is n-well
	- Serves as a substrate for the pMOS. must be biased to $V_{DD}$


Different types of contacts
- Schottky contacts
	- Behaves like a diode, with non-linear characteristics
	- Have lower diodes than np-diodes (~0.3V)
	- Normal diodes (~0.7V)
- Ohmic Contacts
	- Much better for us (digital), and has lots of nice linear characteristics

# Design Rules
- Tell us what the fab can do, and ensuring that the manufacturing will be within the specifications.
	- There will be thousands of pages of rules.
### Defined the allowed geometry of the different layers
- Guidelines for making safe process masks
- Rules about the allowed sizes and shapes of a particular laer
- Rules about how different layers interact
### Ways to list Dimensions
- Absolute dimensions (i.e. microns)
- Scalable dimensions
	- Not used anymore, but used 20 years ago. Mentioned in textbook, but still commonly used in research papers
		- Things do not scale linearly anymore
	- Usually called "lambda" - half of the minimum drawn transistor channel length
	- Design in lambda units, then scale lambda for a particular process
## Layout rules Lambda stuff
- Passed because it is covered in our textbook
	- Routing tracks are defined as enough space to place wire and the required spacing to the next wire
	- If wire 4$\lambda$ and spacing 4$\lambda$ , routing track is 8$\lambda$
		- This pitch also leaves room to put a transistor between the wires
	- Area estimation formula
		- $A = t * 8 \lambda$
			- $t$ = number of metal tracks
## $\lambda$ Design Rules
- Routing tracks:
	- Defined as enough pace to place wire and the required spacing for the next wire
		- We have that because we respected rules for spacing two different transistors together. 
		- This matters because we are using standardized layout structures. We can find standard libraries with different numbers of cells. 
	- Defines how much area around your cell is allowed. 
		- Too little routing tracks means the design blows up
		- Too many tracks means wasted space
- If you make big lines, it means you're trying to get current through
	- If you have large current, you start having electromigration (momentum of electrons making particles move within the substrate) and other problems. 
		- Mesh deals with that. 
- Gate contacted pitch:
	- The minimum distance fro one transistor's gate to another's
	- The most important number in modern technologies

## Gate Layout and Stick Diagrams
- `ndiff` = n diffusion
- `pdiff` = p diffusion
- crossing `poly` is what makes a pMOS transistor?


## Transistor Sizing
- We want $L$ to be as small as possible
	- This lets us have faster transistors
	- Based on mobility $\beta$ 
- N-type transistors are around 3x better than P-type transistors in terms of $\beta$
	- Therefore, we make P-types twice as wide as N-types to start with 
- $L$ increases resistance. We can look at them as such
	- When we have transistors series
### Rule of thumb
Multiply each width by $n$ for a series stack of $n$ transistors
- i.e. Stack of 3 in series, each transistor should be 3x unit width size
- This is because series connections are like increasing the $L$ of the device
	- This will roughly equalize the current sourcing capability of pull-up and pull-down stacks in this gate