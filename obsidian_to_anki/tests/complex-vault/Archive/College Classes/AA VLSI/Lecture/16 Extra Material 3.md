System in package
- There are packaging technologies that put multiple active and non-active components directly mounted on the package substrate. This is then covered in resin. 
	- Very common for power-management components.
		- Large passives (capacitors) are needed for this stuff
Silicon chips assembled on a larger silicon substrate
- You can get really fine-grade wires like this
- The silicon substrate can be passive and/or/active

## 3d memory
3d Nand
- You make a pillar and stack the crap out of it
	- Can make super high-capacity flash stuff
		- Micron
Hybrid-memory cube (HBM)
- Stack multiple dies with 3 sillicon vias that connect all of them together. 
- Large density of DRAM


## Different Materials
Digital logic
- Silicon is easily the best
Other materials are better in different situations (i.e. thermal conduction bandgap, and other stuff). 
### Other hostile environments
Space has radiation that can interact with the atoms, elevating the atom energy levels. This can eject electrons, and switch the operating state of the transistor. Avoiding this is when different layout techniques are used. 
- We can either reduce this, or mitigate the switch after the fact
	- Triple modal redundancy (TMR)
		- Randomly, there will be bit flips. Because of that, I'll use 3 computers instead of one. When 2 are in agreement, I'll go with those. 
		- This can be implemented at a system level (3 computers), ALU, or even the latch level. Synchronization of this is a mess.
There are probability distributions of bitswitches per second at various speeds.
- This will also come with certain levels of resilience.
- Bitstream scrubbing is another algorithm happening. 
Space tech is usually FPGAs
- FPGAs enable you to build TMR to whatever level you want
There are even other applications that don't care about the radiation
# Memory
### SRAM
- Six capacitories or a latch
### DRAM
- 
### Flash Memory
The idea is to bury a charge within a gate
## Other Materials
- Much denser, but slower than flash
### Conductivity changes
## Magnetic Memories
### Changing orientation
Using nano-magnets
### Ferro-electric Memory
### Resistive Memory

# Differences between Synchronous and Asynchronous Resets
- More common to use Asynchronous resets
- From a synthesis perspective, it is a lot better to use a synchronous reset
	- It's direct, rather than needing to reset each of your flip flops

If your reset is HI, then it will 


Asynchronous resets
- 
Synchronous
- Assert, have a clock cycle, and then reset

# Generative AI
Cadence and synopsis aren't ready for open-source software
Open-soure EDA and open-source software is new


# Is it better to be a tool-user or a tool-maker with these FPGA/semiconductor companies?
- Tool-makers like algorithms
	- EDA is much smaller than the chip makers
- Tool-users like design
		- Intel, apple, Qualcomm, Apple, Google