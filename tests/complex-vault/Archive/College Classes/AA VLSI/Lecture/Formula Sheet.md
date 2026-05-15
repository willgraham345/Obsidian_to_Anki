# MOSFET Basics
## Terminals
Source
Gate
Drain
Body or Substrate
- Body is usually connected to source, making it operate like a 3-terminal device
	- nMOS: n-type substrate
	- pMOS: p-type substrate
- Can influence characteristics of the transistor like:
	- Leakage power
Substrate
- The fourth terminal that biases the transistor into operation
	- Reducing leakage power

bulk = well

poly (gate)

diff

Metal



## Junctions in CMOS
| Parameter                | nMOS                                         | pMOS                                         |
| ------------------------ | -------------------------------------------- | -------------------------------------------- |
| Source + Drain Type      | n-type                                       | p-type                                       |
| Channel Type             | n-type                                       | p-type                                       |
| Gate type (poly)         | n+                                           | p+                                           |
| Substrate type           | p-type                                       | n-type                                             |
| Gate type (metal)        | Si conductive band                           | Si valence band                              |
| Well type                | p-type                                       | n-type                                       |
| Threshold voltage        | Positive (enhancement), negative (depletion) | Negative (enhancement), Positive (depletion) |
| Inversion Layer Carriers | Electrons                                    | Holes                                        |

## Voltage Notation Definitions
$V_G$ = Voltage on the gate
$V_T$ = Voltage required to enter into inversion 
$V_{GS}$ = Voltage between gate and source
- When $V_{GS} < V_{Th}$ but more negative in a PMOS transistor, a current will flow between the drain and the source
$V_{DS}$ = Voltage between drain and source
$V_{DD}$ = Positive supply voltage
$V_{dd}$ = drain positive supply
$V_{ss}$ = source negative voltage


## MOS Capacitor Regions (Partially formed transistor)
#### Accumulation
- $V_G < 0$
- Negative charge on gate brings positive charge to channel
#### Depletion
- $0<V_G<V_T$
- Positive charge pushes positive charges away from channel leaving a depletion region in channel
#### Inversion
- $V_T < V_G$
- Negative charges attracted to channel, with depletion area further in the channel

## nMOS Modes of Operation
- All voltages are inverted for p-type
	- Source is the more positive terminal
### Currents (Drain and Source)
##### ON Current
ON current = $I_{on} = I_{dsat} = I_{ds}$
- When $V_{gs} = V_{ds} = V_{DD}$
##### OFF current
$I_{off}$ = OFF current
- When $V_{gs}$= 0, and $V_{ds} = V_{DD}$
##### Leakage Current
$I_G$, when $V_{GS} = V_{DD}$
### Voltage Long Channel I-V Model
#### Cutoff 
 $V_{gs} < V_T$
 $I_{DS} = I_{OFF} = 0$
- MOS cap is not active, no conductive channel
- Current through transistor:
	- $I_{ds} = 0$
- Drain, source, and gate voltage relationship:
	- N/A
#### Linear 
$V_T < V_{GS}$
$V_{DS} < V_{DSsat}$
$V_{DSsat} = V_{GS} - V_T$
$I_{DS} = \beta(V_{GS}-V_T - \dfrac{V_{DS}}{2})V_{DS}$
 - Conductive channel, MOS capacitor is inverted, the current is still rising linearly with the voltage across gate to source
##### Pinchoff Operation Region (When $V_{DSsat}$ is reached)
$V_{DS} = V_{DSsat} = V_{GS} - V_T$
- MOS capacitor is inverted with a conductive channel. The drain potential $V_D$ induces a depletion region and changes drift toward the source. 
#### Saturation  
$V_T < V_{GS}$
$V_{ds} > V_{dsat}$
$I_{DS} = \dfrac{\beta}{2}(V_{GS} - V_T)^2$
- $I_{DS} = \frac{\beta}{2} V^2_{GT}$


## C-V Characteristics
The gate can be viewed as a capacitor
- $C_G = C_{ox}WL$
When the transistor is on, the channel extends from the source. 
- We often approximate the gate capacitance as terminating at the source
- $C_{GS}$



# Electrical Components
## Basic Gates
## Logic
#### Inverter
- A NOT gate
- Transistors: 
	- 1 nMOS, 1 pMOS
## Data Storage
## Organization
#### Multiplexor
#### Tristate
- When the enable input is 1, the output is similar to an ordinary buffer


# Delay
## Delay in a Logic Gate
### $\tau$ Time Constant
$\tau = 3RC$
- R = channel resistance of minimally sized nmos
- C = gate capacitance of minimally sized nmos
- $\tau$ = fundamental delay of the technology
### Delay in the Logic gate
$d = f + p$
- $d$ = delay = $\dfrac{t_d}{\tau}$
- $f$ = effort delay (stage effort) = $gh$
	- $g$ = logical effort
		- Relative ability of a gate to deliver current, compared to a minimally sized inverter
		- $g = 1$ for an inverter (contained in the lib files)
	- $h = \dfrac{C_{out}}{C_{in}}$ = electrical effort (fanout)
		- Ratio of output to input capacitance
		- The bigger the electrical input, the longer the delay. It needs more time to charge everything.
- $p$ = parasitic delay
	- Represents delay of gate driving no load. Internal parasitic capacitance. 
## RC Delay Model
- Approximates the nonlinear I-V and C-V with average resistance and average capacitance.
### Effective Resistance
$R_{eff} = \frac{V_{ds}}{I_{ds}}$
- R = effective resistance
- A unit nMOS transistor is defined to have effective resistance $R$
	- The size of the unit is arbitrary, but conventionally refers to a transistor with minimum length and minimum contacted diffusion width (i.e. 4/2 $\lambda$)
	- May also refer to the width of the nMOS transistor in a minimum-sized inverter in a standard cell library. 
- We'll use $2R$ in this book for simplicity. 
### Transient Response
- Applying the RC model to estimate the step response of the first-order system.
- Step response of $V_{out}(t) = V_{DD}e^{-t / \tau}$

# Layout
N-wells and P-wells
- Create the source and the drain in a MOSFET. The wells are created with the opposite polarity of the substrate. 
General substrate is P-type. 
- The n-substrate for the p-transistor is in a "well"
	- To put an NMOS in a p-type substrate, you need to add surrounding n-type substrate. That's input as a well. 
## Layer Types
### Metal3
### Metal2
### Metal1
### Contact, Via1, Via2
### Polysilicon (Poly)
### Nselect, Pselect
Define active types
Our setup has separate nactive and pactive colors to keep things straight
### Nactive, Pactive
### Nwell

## What defines a transistor
A transistor is when poly crosses active
### nMOS
- nactive over the p-type substrate
### pMOS
- pactive inside an nwell
# Virtuoso
- nmos2v and pmos2v are transistors we should use for the rest of the class.

# Skewed Gates
HI-skew favor rising output (small nMOS)
LO-skew favor falling output (small pMOS)


# Design Flow Notes
High level description = RTL code 
Logic synthesis = Transforming RTL into gate-level description, also within an HDL
- Done by mapping HDL code onto a library of standard cells. Will also optimize. 
- Logic equivalence check = LEC, done to make sure there aren't any logical changes during the synthesis
Design constraints force our synthesis to actually make the circuit 
- Lets us put clock uncertainty, jitter, slew rate within the synthesis and within the circuit. 
- Forces the circuit to consider incomplete and non-ideal circuits.
PnR = place and Rout = gate level netlist after DFT
- GDSII = a binary file format representing planar geometric shapes, text labels, and other info. Shows the integrated circuit layout artwork. 
- GDSII is the layout file, the stuff on virtuoso. 


# Industry Notes
The semiconductor industry is ruled by: 
- Tlc scripting
	- Version controllable
- Linux
- Command lines
# Terminology
- BCD = Binary Coded decimal, assigning a four-digit binary code for each digit 0 through 0 in a decimal base 10 number
- Diffusion node = A point where two or more transistors are connected in a way that allows the flow of electrical charge. Typically, this refers to the connection of the drain and source terminals of multiple transistors.
- Octal = base-8 number system, uses the digits 0 to 7
- Word = a unit of data of a defined bit length that can be addressed and moved between storage and the computer processor
# Symbols and Suffix
## Symbol
[Symbol List](https://www.electronicshub.org/symbols/)
## Suffix Guide
- $E, e$ = Emitter
- $B, b$ = Base
- $C, c$ = CollectorSS
- $J, j$ = a generic semiconductor device terminal
- $A, a$ = Anode
- $K, k$ = Kathode
- $G, g$ = Gate
- $X, x$ = a generic node in a circuit
- $M, m$ = Maximum
- $Min, min$ = Minimum
- $(AV)$ = Average