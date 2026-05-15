### Antenna Violations
During manufacturing, you are putting your wafer inside of a plasma with large electric field and free charges
- These charges may accumulate on metals, and serve as antennas and break down the oxide. 
- Antenna rules are there to ensure that you aren't accidentally destroying your transistors while producing your metal connections. Long metal wires trip these rules making sure you have smaller antenna. 
	- You can also remove this problem by adding a diode that will leak extra extra charges to the substrate to ground. 
		- Adding active devices to the substrate is the goal here. 

The entire industry is Tcl-based, but there are GUIs that work with the Tcl base. You'll be able to see these Tcl commands from the command line. 


### Tcl
The future is python, but the current setup is on Tcl scripting. 


### Software
- All software 
- The most advanced algorithmic derivations, graph theory, optimizations, but have the worst UI
- The business model is to sell underutilized and extremely expensive licenses. 
- fusion compiler
	- Can be hundreds of thousands and even millions in licensing fees
- There are export control rules on the software as well
	- Dual-use technologies: (an example is GPS chips, FPGA chips)
		- Can be used for both military and commerical uses
		- CCL 
		- You may or may not be able to do some of these things
		- These are with antennae, RF, radio, and nearly every other thing tech-related
	- This will also apply to individuals working within a company

## FPGA vs ASIC
### FPGA
Non-differentiated chips
- These have tiny bricks, which you configure with other bricks, to do some thing
Stem cells of digital electronics
- Standard cells are pre-differentiated
Can be reprogrammed to do something else
If you stay within low-enough volumes, you make a ton of money

### ASIC
- Designed and configured for some specific goal
- Highly specific silicon for whatever you're doing
	- Costs a TON
- AMD