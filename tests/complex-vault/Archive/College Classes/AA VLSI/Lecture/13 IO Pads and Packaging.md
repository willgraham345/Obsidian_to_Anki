Beginning of class notes
- A big problem in the industry occurs when you're trying to *implement* an RTL freeze
- An ECO is an engineering change order, which changes the module within an RTL freeze.
	- You usually need ~6 months to implement an RTL freeze without any changes. 
- Intel processors datasheets have thousands of pages of bug reports.

# IO Pads and Packaging
Everything we've done so far is regarding the core. We use verilog and use other tools to create a functional core.
- We're now starting to learn about full chip assembly


### Final Assembly
Our final project consists of a core and a pad ring (I/O ring)
- Core is the guts
- Pad ring (or pad frame) connects the guts to the outside world
	- Power delivery, protection, and interface are all included within the pad ring. 
	- Every single item needs to have guaranteed protection and power requirements satisfied. This quickly becomes a complicated problem.
Our chips must fit in a MOSIS Tiny Chip area
- 2mm x 2mm outside dimensions
It is critical to do a functional simulatino fo your whole chip, including the pads
- Make sure that you can drive the chip from external interface.

## Chip Core
Everything that is inside the pad ring
- Try to floorplan your core so that it's as small a rectangle as possible
- Make sure it fits in the frame you've chosen
- Make sure to connect `vdd` `gnd` and `clk` in the core
	- The core can be DRC and LVS checked
	- Can be simulated for functionality
	- This core is then routed to the pads. 

Once your core is complete, you need to connect it to the pad frame
- Re-do the functional simulation, but through the pads this time
- You should be able to re-use your testfixture
- Also a final DRC and LVS which includes the pads. 

What is the impedance of an oscilloscope probe?
- Probe capacitance is usually 10 pF capacitance

We need to have a huge amount of capacitors to drive the output capacitance

A brownout condition = Where voltage drops below where your voltage needs to be, so it becomes unstable
- Happens when there's a surge on demanded current
- Will cause a voltage drop across wires.
	- Moves from nominal voltage to below. 
	- Similar to when the light dims when the AC starts in your home. 
- IR drop
	- Make sure you minimize the resistance of your power delivery across your chip as much as possible. 
	- We'll try to have the same impedance on the power lines
 
 
 What is the goal of a pad?
- Connect the chip to the external world
	- By solder
	- Small gold wires?
Why can't we have big vias?
- Small vias and big vias will have incorrect etching
- We want the structures to act as identically as possible

#### Driving Large Capacitances
$t_{pHL} = \frac{C_L V_{swing} / 2}{I_{av}}$
- Transistor sizing
#### Using Cascaded Buffers
What is the value of *u*?
- 4
	- Fanout of 4 on any given stage
#### Designing Large Transistors and Cascaded Buffers
We'll take a transistor and and fold it into many different fingers
![[Pasted image 20231031150129.png]]
- Creating a bunch of smaller transistors creates one large transistor. 
- 


#### Bounding Pad Design
- A bunch of tiny little squares
![[Pasted image 20231031150258.png]]

#### Corner Pads
Why do we have a gap in the corner?
- We don't want heating.
The momentum of the electrons will try to bring the metal material with it. This would eventually migrate and eventually cut the pad. If we add the void it stops the movement.

### ESD and Analog Pads
What if we have a voltage that is higher than `vdd` or lower than `gnd`?
- Large voltages and currents can destroy gates and therefore destroy the 

Solve by creating two diodes connected to `Vdd` and `Gnd`. If our voltage goes above a threshold, it will start conducting and help manage ESD. Excess voltage will go through gnd or vdd.
- A small resistor in series creates a current limiter
	- We can only have so much current going through that line, and we can calculate the maximum amount of current going through the system. Prevents burning the wires from joule heating.

## Available Pads for this class ]
