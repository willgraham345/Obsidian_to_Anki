Differential equation based on charging/dischargint of capacitances in a circuit is:

$I = C \frac{dV}{dt}$
- $I$ = current
- $V$ = voltage

Every real circuit has some capacitance, and transistors are no different
- There is diffusion capacitances between the drain and the body of each transistor between the source and the body of each transistor: $C_{db}$ and $C_{sb}$
- Gate capacitance $C_{gs}$

# RC Delay Model
- Approximate the nonlinear transistor I-V and C-V characteristics with:
	- Average resistance 
	- Average capacitance
	  over the switching range of the gate. 
- Does really well for delay estimation, despite being terrible for predicting analog behavior well
## Effective Resistance
$R_{eff} = \frac{V_{ds}}{I_{ds}}$
- R = effective resistance
- A unit nMOS transistor is defined to have effective resistance $R$
	- The size of the unit is arbitrary, but conventionally refers to a transistor with minimum length and minimum contacted diffusion width (i.e. 4/2 $\lambda$)
	- May also refer to the width of the nMOS transistor in a minimum-sized inverter in a standard cell library. 
- We'll use $2R$ in this book for simplicity. 
## Gate & Diffusion Capacitance
We define $C$ as the gate capacitance of a unit transistor of either flavor. 
- A transistor of $k$ times unit width has capacitance $kC$
- We assume a single average value, even though we know it is nonlinear. 
## Transient Response
- Applying the RC model to estimate the step response of the first-order system. The system has a transfer function of:
  
  $H(s) = \frac{1}{1 + sRC}$
  
  with a step response:
  $V_{out}(t) = V_{DD}\exp^{-t/\tau}$
  - $\tau = RC$

The propagation delay is the time when $V_{out}$ reaches $V_{DD} / 2$
- $t_{pd} = RC\ln2$
	- They can occasionally drop the $\ln$ term and write it as $t_{pd} = RC$, where $R = R'$
- the effective resistance $R$ is chosen to give the correct delay. 
- 
## Elmore Delay
We can generally represent circuits as an RC tree, (an RC circuit with no loops). 
- The root of the tree is the voltage source, and the leaves are the capacitors at the ends of branches. 
- Estimates the delay from a source switching to one of the leaf nodes changing as the sum over each node *i* of the capacitance $C_i$ on the node, multiplied by the effective resistance $R_{is}$ on the shared path from the source to the node and the leaf. 
$t_{pd} = \sum_{i}R_{is}C_i$  
- $i$ = each node
- $R_{is}$ = effective resistance

### Example
![[Pasted image 20231014165854.png]]
- Estimating the RC term here.
	- The circuit has a source with two nodes: $n_1, n_2$
- Elmore delay: $t_{pd} = R_1C_1 + (R_1 + R_2)C_2$


## Layout Dependence of Capacitance
- A good layout principle is to share diffusion nodes whenever possible to reduce the diffusion capacitance. 


# Linear Delay Model
## Normalized delay of a gate
Normalized delay of a gate can be expressed in units of $\tau$
$d = f + p$
- $p$ = parasitic delay when no load is attached
- $f$ = effort delay that depends on complexity and fanout of the gate
## Logical Effort
An inverter has a logical effort of 1. More complex gates have greater logical efforts, indicating that they take longer to drive a given fanout.
- A gate driving $h$ identical copies of itself is said to have a fanout.
- Indicates how much worse a gate is at producing output current as compared to an inverter.
$h = \dfrac{C_{out}}{C_{in}}$
- $C_{out}$ = capacitance of the external load being driven
- $C_{in}$ = Input capacitance of the gate

## Parasitic Delay
Delay of the gate when it drives zero load. Can be estimated with RC delay models.
- A good method for hand calculations is to count only diffusion capacitance on the output node.
$3RC = \tau$
## Delay in a Logic Gate
## Drive


# Logical Effort of Paths

## Delay in Multistage Logic Network
Logical effort is independent of size, while electrical effort depends on sizes. 

### Logical Effort
$G = \Pi g_i$
- $G$ = path logical effort
- $g_i$ = logical effort of *i*-th path
### Path Electrical Effort
Ratio of the output capacitance the path must drive, divided by the input capacitance presented by the path. 
$H = \dfrac{C_{out(path)}}{C_{in(path)}}$
- More convenient than defining path electrical effort
### Path Effort
$F = \Pi f_i = \Pi g_i h_i$
- Product of the stage efforts of each stage
- Recall that the stage effort of a single stage is $f = gh$