# Big Picture
- How do we navigate through abstraction layers? How can we keep in mind the giant picture?
- Computer aided design (CAD)

### Standard Cell Based Design
- Standardized ways of designing boolean logic gates. 
- 2 sets of parameters
	- Functionality (AND, OR, NAND2, etc)
	- Drive (small gate, or big gate for bigger current)
- The power of standard cells is that they can be stacked onto $V_{DD}$ and $GND$ rails. 
	- The algorithmic complexity for blocks is much simpler than handling a variety of polygons.
## Cell Design Tools
- Cell design toolflow, working with what's already been made.
- What we've done so far
- How do we build the standard cells? 
	- We take a schematic, simulate to make sure it's working. Once we've made our schematic, we build it with layouts.
- Start with a schematic editor
	- SPICE is a differential equation solver
- Tools we use
	- LVS = layout versus schematic
	- DRC = design rule checker
		- Makes sure that what you make can actually be manufactured at a lab.
	- PEX = Parasitic extraction
		- A bunch of mini executables
		- Captures parasitic we weren't capturing with our model with layout connection. 
			- Layout introduces parasitics. 
- Simulator we use:
	- Spice will take the things we design using the tools above, and make sure it works in a non-ideal world
- Standard cells are standardized formats, but will vary from manufacturer to manufacturer
	- Different libraries have different advantages. 
- Data files
	- GBSII
		- Actual database, that will contain all the polygons for our creation. Production-ready file with the polygons. 
			- REALLY ugly
		- Too large to use in many abstracted designs. 
	- LEF
		- Abstracted view of the layout (GBSII)
		- Basically only the layout of the standard cells
		- Tells you how to connect to other gates
	- LIB
		- All timing and power information for the cell. 
		- Lookup table of timing rather than a full simulation
			- Now we can evaluate the delay of a very complex task very quickly. 
	- Our toolchains will always require these files
## Semi-custom flows
- We make something custom, but only using standard cells.
### Workflow
1. Design phase (Modelsim, etc, 3710)
2. RTL
3. Front-end Logic Synthesis (Genius /DC)
	1. Creates a net list of logic gates
	2. Move from a behavioral representation to a structural netlist
4. Back-end PnR (Innovus/ICC2)
	1. Place and Round
	2. How do you assemble these things
#### Notes About Workflow`
- Front end logic synthesis only works on netlists
- Back end 

#### Traditional Logic Synthesis Flow (covered in lab5)
1. RTL
2. Unified Logic Optimizer
3. Technology Mapper
4. Logic Gates

#### Traditional PnR flow (covered in lab6)
1. Floorplanning
2. Placement
	1. Trying to minimize area, maximize performance with what you already have
3. Clock Tree Synthesis
	1. We want the clock to be touching everything, all at the same time
	2. We'll be routing our clock to hit everything with the same delay between all of them. We'd like to minimize skew and latency
	3. Very complex problem
4. Routing
	1. Connecting standard cell inputs/outputs together. 



# Review
- Abstraction enables automation
	- Working through abstraction, layer by layer
	- Toolflows we use
		- Semi-custom Flow
			- Working with standard flows
		- Full custom design flow
	- 

# New Stuff
## HDL Description
- Finite State machine outline in HDL.
