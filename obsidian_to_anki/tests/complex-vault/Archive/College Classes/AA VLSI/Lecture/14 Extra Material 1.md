Previous years
- Covering specific modules and digital blocks
	- VGA
	- USB
- Q&A

Things to look up
- Bitstream = a sequency of bytes. This term is frequently used to describe the configuration data loaded into an FPGA
- PMU = platform management unit
	- A CPU to control an FPGA
- Hardware accelerator = A device that works with a processor to speed up a specific task
- Electromigration = movement of atoms based on the flow of current through a material
	- if 
- Redistribution Layer
	- RDL is an extra layer on an integrated circuit that makes I/O pads available in other locations of the chip, for better access to the pads where necessary. Makes chip to chip bonding simpler. Additional metal layer on top for pin arrangements.
		- This keeps protection as simple as possible.
- PGA = Pin Grid Array Packaging
	- Old school way of doing things
- LGA = Land grid array
	- New way of packaging CPUs today
- OSATs = outsourced semiconductor assembly and test
	- Handle packaging
	- 3rd party service that suppliers around the world offer which consists of semiconductor assembly, packaging and testing of ICs
		 - ASE, Amkor, Powertech, ChipMOS, and King Yuan are major players
	- They're in charge of the testing 
- DFM = Design for manufacturing
- DFT = Design for test
	- How do we make sure that our chip is going to work properly before we deliver it to a manufacturer. What can we do within our design to ease testing? Will this test take long? How can we shorten these tests to lower our margins?
		- This is the job of a test engineer
- SIMD = Single instruction multiple data
	- GPUs are very well suited for parallelism
	- AI is convolution based
- Dark silicon
	- Something that Apple is using. Turn on different parts of your chips to do different jobs
	- Apple leveraged space to use hardware accelerators
# What is packaging?
- Adaptation in size is what packaging is all about
	- The package is a fine-grained PCB
- The packaging is the means for adapting size between VLSI world and the PCB world 
	- The IO ring is much bigger than the actual VLSI chip. 
- Our IO is no longer required to be on the outside edge with a flip chip assembly
	- We quite often have IO's on the side anyways so we can have the IO ring arrangement 
	- We use 
## A flip chip assembly
- Top of silicon is flipped onto package substrate


In modern packages, you have a package in the package
- Multiple dies which are assembled within an interposer
	- An interposer is a piece of silicion that creates a redistribution layer
		- This could let you have two different tech nodes on the same package, and keep things more reliable
		- The more modular, the more reliable
		- You can also integrate multiple different companies together. 

Creating a package today is very similar to making a PCB today
- The rest is creating the right assembly housing
- It gets highly complex when you start doing something complicated, like A2D, high speed computing, and nearly everything else. 
- Package is also designed to allow for heat to dissipate and radiate away from the center
	- There's research for doing liquid cooling within the package. 


There's always interest in scaling things down:
- Parasitic capacitance down
- Power draw down (RC goes down)
- Wire lengths lower
- 


You can add a thermometer to a circuit by adding in a frequency generator
- $f = \alpha(Process, V, T)$
	- The process is a known PVT (Process, voltage, temperature) monitor
- Once we ahve this we can dispers PVT monitors