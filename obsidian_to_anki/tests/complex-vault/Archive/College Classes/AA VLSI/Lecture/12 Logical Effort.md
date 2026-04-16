Goal: 
- Understand the rationale behind logic synthesizer and what the PnR tools are doing to optimize performance
- Under

You'll have a rules of four
- One gate can drive four other gates


How could we make an inverter faster?
- Make transistors bigger, so they can drive more current and drive more quickly. 
	- If we increase the size of our gates, we'll charge the output faster, but it takes longer to charge the input. 
- The performance of our circuit is influenced by our circuit sizing and schematic

## Sizing
- Important questions:
	- What is the best circuit topology for a function?
	- How many stages of logic give least delay

# General Situation Example
### Problem:
- You are the memory designer for an embedded automotive processor. You must design the decoder for a register file.

### Decoder specifications:
- 16 word register file
- Each word is 32 bits wide
- Each bit presents load of 3 unit-sized transistors
- True and complementary address inputs A\[3:0\]
- Each input may drive 10 unit-sized transistors

### You need to decide:
- How many stages to use?
- How large should each gate be?
- How fast can decoder operate?

## Delay in a Logic Gate
Express delays in process-independent unit

### $\tau$ Time Constant
Consider an inverter that is properly balanced
- pmos is x2, and nmos is x1 size
- If we draw a timing diagram between input $A$ and output $Y$
	- In this situation, $A$ is GND and can be approximated as an ideal step from GND to $V_{dd}$ at $t = t_0$, and $Y$ is close to $V_{DD}$
		- You'll have a 1st order discharge as $Y$ transitions to invert A
			- The delay is the period from which $Y$ goes from 90% of $V_{dd}$ to 10% above $A$ and GND is $\tau$
				- That value is equivalent to $\tau = 3RC$

- $\tau = 3RC$
	- R = Channel resistance of a minimally sized nmos transistor
	- C = gate capacitance of a minimally sized nmos transistor
		- 1C = gate of 1 minimum sized nmos
		- There are 3C because we'll have double the value on the pmos as the nmos.
		- We'll only have 1R because the the pull up or pull down network. Basically the resistance will only be seen from one or the other. 
	- $\tau$ = Fundamental delay of the technology
		- Basically the time constant associated with a minimal inverter that is unloaded.
			- We'll use this delay as a way to normalize all other delays

### Delay in the Logic Gate
- Terminology
	- $C_{in}$ = Capacitance that is connected to a given input (pin A of a 3-input NAND)
	- $C_{out}$ = Capacitance that is connected to the output pin
	- Only count one transistor in a series, count everything in a parallel

- Delay has two components, which are unit-less values of $\tau$
	- $d = f + p$
		- $d$ = delay
			- $d = \frac{t_d}{\tau}$ 
		- $f$ = effort delay (stage effort)
			- $f = gh$: Effort delay (stage effort)
				- $g$ = logical effort
					- Measures relative ability of gate to deliver current
						- $g =1$ for an inverter
						- Will be contained within the lib files.
					- $g = \dfrac{C_{in of CapOfGate}}{C_{In of InverterDrivingSameCurrent}}$
						- We say all loads are equal to one capacitive load
						- We can approximate a channel as a resistance (Ohm's law)
						- $R_{FirstOrderLogicGateResistance}$ = What is the equivalent resistance between one of the power rails and the output?
				- $h = \frac{C_{out}}{C_{in}}$ = electrical effort
					- Ratio of output to input capacitance
					- $1C$ = capacitance of a minimally sized nmos
						 - We only count the parasitic capacitance on the output, so ones in the middle of a series relationship we can treat as always loading. 
						 - We only add ones connected to the output
					- Sometimes called fanout
					 - Widths of the gates connected to the node
					- $C_{out}$ = 
			- Basically, the effort delay is measuring how capable the gate is, with the size of the load it will carry
		- $p$ = parasitic delay 
			- Represents delay of gate driving no load. The ratio between the output capacitance of a complex gate, and the capacitance of the input of the inverter.
			- Set by internal parasitic capacitance from the gate 
			- All transistors connected to the output $Y$ will contribute some parasitic capacitances
				- Each transistor will contribute one $C$
			- Parasitic capacitance for an inverter is always 1
### Delay Plots
- ![[Pasted image 20231005144537.png]]
	- The bigger the $h$ (electrical input), the longer the delay will get
		- It needs to have more time to charge the output
	- For a given capacitance, one will be more efficient at driving a code. 
### Computing Logical Effort
Logical effort is the ratio of the input capacitance of a gate to the input capacitance of
an inverter delivering the same output current.
- How do we know which is the stronger gate?

We find R to make sure that we're comparing C to an inverter driving the same current
- 

#### Examples
##### Minimally Sized Inverter
![[Pasted image 20231005145152.png]]
- We need to take this input, and compare it with an inverter (it is an inverter, so $g = 1$)

##### AND Gate
![[Pasted image 20231005145319.png]]
- What is the equivalent resistance of this gate?
	- What is the equivalent inverter driving this current?
- For the pull down network:
	- Each of the resistances has a doubled size, so it has twice as much current. This means that it has half the resistance, so it has $R = R_{nmoschannel} / 2$.
		- Therefore, we have $R_{pulldown} = 1R$
- Pull up network
	- We'll assume that it's going through a 1R 
		- Accurate timing information will be contained in lib files and within cadence. 
We now know that this equivalent resistance is $1R$, so it is equivalent to an inverter of minimal size. 
- g is not compared to the minimally sized inverter, but the g driving the same current. 


##### NOR

![[Pasted image 20231005150926.png]]
- 


## The $g$ parameter
For driving the same current (having the same effort on the output), we can now compare the difficulty of adding different components. 
- From above, we can see that a NAND gate is the most efficient in terms of logical effort. 
	- Our synthesizer will try to maximize performance
	- HW3 will cover this, and our exam will have this. 

### Logical Effort of Common Gates
![[Pasted image 20231005151731.png]]
- Performance-wise, a NAND gate drives better than NOR gate logic
- This is an issue, because arithmetic is formed using tables.
- General logic is NAND, arithmetic occurs in a synthetic.


We can do the same thing with the parasitic delay parameter
## $p$ parameter
- Look at the output $Y$, and see how many transistors are connected to it, and how much it could contribute to parasitic capacitance when it is driving no load. 
	- A function of the diffusion capacitance of the gate
	- The ratio between the output capacitance of a complex gate, and the capacitance of the input of the inverter
- Intrinsic to our gate, so there's no notion of what's connected to it from the input or the output. Accounts for how the internal capacitors need to charge to drive current. 

# Logical Effort on Skewed Gates
- Skewed gates favor one edge over another
	- Example: supposing rising output of inverter is the most critical. We'd downsize noncritical nMOS transistors.
- We're changing our ability to source current, meaning that our logical effort ($g$) will change
	- We'll then need to have two different $g$ variables for up and down
	- The nMOS is smaller than what it should be in a HI skew
![[Pasted image 20231019145737.png]]
- $g_u$ and $g_d$
# Multistage Logic Networks (a.k.a a Path)
- We'll generalize notions for paths.
- Paths use capital variables
### Path Logical Effort
$G = \Pi g_i$
- $C_{out} / C_{in}$ for the path
### Path Electrical Effort
$H = \dfrac{C_{out-path}}{C_{in-path}}$
### Path Effort
$F = \Pi f_i = \Pi g_i h_i$

Can we write $F = GH$?
- NO

## Branching Effort
- Accounts for branching between stages in path
- $b = \dfrac{C_{on path} + C_{off path} }{C_{on path}}$
- $B = \Pi b_i$
### Path Effort Delay
$D_F = \Sigma f_i$
### Path Parasitic Delay 
$P = \Sigma p_i$
### Path Delay 
$D = \Sigma d_i = D_F + P$
### Branching Effort
- Accounts for branching between stages in path
- Each logic gate's job is to charge itself and then the next stage. Makes a very nice boundary.
	- $C_{on path}$ only worries about the junction. 
	- Similar to the capacitance on a node
$b = \dfrac{C_{on path} + C_{off path}}{C_{on path}}$
$B = \Pi b_i$
$\Pi h_i = BH$

#### How do we calculate *B*?


## Designing Fast Circuits
Our goal is to design fast and efficient circuits. 
$D = \Sigma d_i = D_F + P$
- $D_F = \Sigma f_i$
- $F = \Pi f_i = \Pi g_i h_i$
	- Independent of gate size
### Optimizing a Logical Delay Path
Delay is smallest when each stage bears same effort
- We don't want beefy stages driving small ones. We want consistent and distributed stages.
- $\hat{f} = g_i h_i = F^{1/N}$
	- Where $\hat{f}$ = optimized $f_i$ for all $i$
- THUS, minimum delay of N stage path is:
	- $D = NF^{1/N} + P$
		- This is a **key** result of the logical effort methodology, and will enable us to find the fastest possible delay.
		- Doesn't require calculating gate sizes
			- We can define gate sizes on our way back.
#### We can size our gates to minimize path delay
How do we size our Gates for the least delay?
$\hat{f} = gh = g\dfrac{C_{out}}{C_{in}}$
Meaning that....
- $C_{{in}_i} = \dfrac{g_i C_{{out}_i}}{\hat{f}}$
- Working backwards, apply capacitance transformation to find input capacitance of each gate given load it drives
- Check work by verifying input cap spec is met.
# Examples
## 3-stage Path
Select gate sizes x and y for least delay from A to B
![[Pasted image 20231019151910.png]]

# Circuit Optimization
How many stages should a path use?
- Minimizing stages is not always fastest
### Example
Drive 64-bit datapath with unit inverter
##### Equations
- $D = NF^{1/N} + P$
-    $= N(64)^{1/N} + N$
#### Example conclusions
There is a stage number that is ideal for the given circuit

## Best Stage Effort Methodology
There exists an optimal effort to reach the best delays
Consider adding inverters to the end of path:
- $D = NF^{1/N} + \Sigma^{n_1}_{i=1}p_i + N(-n_1)p_{inv}$ 
- Finding the optimum: $\frac{\partial D}{\partial  N} = -F^{1/N} lnF^{1/N} + F{1/N} + p_inv = 0$
- The best stage effort is:
	- $\rho = F^{1/N}$
	- $p_{inv} + \rho(1-ln\rho)$
		- Has no closed-form solution
	- Neglecting parasitics ($p_{inv} = 0$), we find that $\rho = 2.718 e$
	- For $p_{inv}$ = 1, solve numerically and we get $\rho = 3.59$
- We get a magic number of 4 for a stage effort, and why fanout 4 (FO4) gates are representative of the performance of a technology
## Sensitivity Analysis on Best Stage Effort
- How sensitive is delay to using exactly the best number of stages
- ![[Pasted image 20231024150628.png]]
	- We can be a bit sloppy

# Method of Logical Effort
We first need to know how we are going to implement something. From there, we can extract the path effort. 
1. Compute path effort
	- $F = GBH$
2. Estimate best number of stages
	- $N = \log_4F$
3. Sketch path with N stages
4. Estimate least delay
	- $D = NF^{1/N} + P$
5. Determine best stage effort
	- $\hat{f} = F^{1/N}$
6. Find gate sizes
	- $C_{in_i} = \frac{g_iC_{out_i}}{\hat{f}}$



# Logical Effort Extraction 
Lib files will let us do the timing analysis, but a more precise estimate of a given logic gate of a given process node requires logical effort extraction
## From Docs
For a given logic gate, we'll have a normalized delay ($d$) related to an electrical effort ($h = C_{out} / C_{in}$)
- Lib files usually contain this information
	- 3 types of tables
- Pin Capacitance = $C_{in}$ of the logic gate
	- Input pin capacitance
- Intrinsic Delay = parasitic delay
	- There will be more and more complicated entries describing different transitions
		- e.g. AND gate with A and B as inputs. A is 1, B is 0. B transitions to 1, how does this affect the Y transitioning from 0 to 1?
- $K_{load}$ = $\frac{G}{C{in}}$
	- Doesn't directly give us logical effort $G$, but we can get it. 
	- Slope of Electrical Effort / Normalized Delay
![[Pasted image 20231026150426.png]]

## From Simulation
### Characterization conditions
- For fast circuits, a balanced stage effort of 4 is usually optimum
	- Slope of $4\tau$ (4 times the delay of an inverter)
- Representative circuit: Shape input and properly load the DUT
	- The second load stage is used to account for $C_{gd}$ that is Miller-multiplied when $e$ switches (there's a mirror effect)
	- ![[Pasted image 20231026151721.png]]
- Plot $t_{pd}$ vs $h$
	- Normalize by $\tau$
	- y intercept is parasitic delay
	- Slope is logical effort
	- ![[Pasted image 20231026151908.png]]
 - Delay fits straight line very well in any process as long as the input slope is consistent


# The Drive of a Gate
A standard cell library, the multiple versions of a gate are identified by the drive. 
The drive can be understood as the capability to drive a given load
- e.g. NAND2x1 and INVX1 ahve the same output current


# Summary and Limits of Logical Effort
Chicken and egg problem
- We need a path to compute $G$
- We don't know any number of stages without $G$

Logical effort is useful for thinking of delay in circuits
- Numeric logical effort characterizes gates
- NANDs are faster than NORs in CMOS
- Paths are fastest when effort delays are ~4
- Path delay is weakly sensitive to stages, sizes
- Using fewer stages doesn't mean faster paths
- Delay of path is about $log_4F FO4$ inverter delays
- Inverters and NAND2 best for driving large caps
Provides a language for discussing fast circuits
- Requires practice to master
- 



# Review on Logical Effort
Evaluating the performance of a circuit, based on its topology, looking at the tradeoffs in different categories.
- The relationship between $f$ and $p$ (effort delay, and parasitic delay)
	- The effort delay expresses the gate charging the external gate. Expresses the load of the external signal.
		- $f = gh$
			- $g$ = logical effort
				- How well the circuit can push the weight
				- $g = \dfrac{C_{FirstOrderLogicGateResistance}}{C_{InverterDrivingSameCurrent}}$
					- We say all loads are equal to one capacitive load
					- We can approximate a channel as a resistance (Ohm's law)
					- $R_{FirstOrderLogicGateResistance}$ = What is the equivalent resistance between one of the power rails and the output?
				- {channel_minimal_inverter}
					- divided by the equivalent inverter that drives the same amount of current
						- Look at the equivalent channel resistance as the gate $R_{channel}$
					- Minimally sized pmos has channel resistance of $R/2$
			- $h$ = electrical effort
				- How well the the thing can switch effort. The calisthenics to logical effort's weight lifting.
	- Parasitic delay is related to the layout. Delay component from no load, and the gate itself. 

## Ring Oscillator
Oscillates under conditions of clock delay


## REVIEW Number 2
- Our goal is to get to positive or zero slack so all timing constraints are met. 
	- What can we do if our timing isn't met (negative slack)?
		- Change clock (easy way)
		- Change timing constraints
		- Relax some of the area constraints
			- Changes architecture



## Review Number 3
- We can estimate delay of our circuit without knowing the sizing details
- For a path to have an optimum delay, we need to have every stage bear the same effort delay $\hat{f}$ 
	- We need $\hat{f}$ to be ~4
	- We need the same sizing across all stages
	- 




			- This is a requirement for gross margin on your product, but it makes a product that can't be sold a sellable product