We will discuss the characteristics of the MOS in more detail. 

The MOS is a majority-carrier device. 
- In an nMOS transistor, the majority carriers are electrons
- In a pMOS transistor, the majority carriers are holes. 

Accumulation mode
- When a negative voltage is applied to the gate, so there is a negative charge on the gate. 
Depletion 


# Long-Channel I-V Characteristics
Relates current and voltage for an nMOS transistor in each of its regions
- The long-channel model assumes that the current through an OFF transistor is 0. When a transistor turns ON, the gate attracts carriers (electrons) to form a channel. The electrons drift from source to drain at a rate proportional to the electric field between these regions. 
- Therefore, we can compute currents if we know the amount of charge in the channel and the rate at which it moves. 
$I_{ds}$ = current between source and drain

## On and off currents
$I_{on} = I_{dsat} = I_{ds}$ =ON current
- When $V_{gs} = V_{ds} = V_{DD}$
$I_{off}$ = OFF current
- When $V_{gs}$= 0, and $V_{ds} = V_{DD}$
### Within long-channel model
- $I_{off} = 0$
- Cutoff:
	- $I_{ds} = 0$
	- Conditions:
		- $V_{gs} < V_t$
- Linear
	- $I_{ds} = \beta(V_{GT} - V_{ds} / 2 ) V_{ds}$
	- Conditions:
		- $V_{ds} < V_{dsat}$
- Saturation
	- $I_{ds} = \frac{\beta}{2} V^2_{GT}$
	- Conditions:
		- $V_{ds} > V_{dsat}$


## Regions of Operation for a MOS transistor
- Cutoff or subthreshold region
- Linear Region
- Saturation region

# C-V Characteristics
Each terminal of a MOS transistor has a capacitance to the other terminals. In general, these are nonlinear and voltage dependent (C-V). 
- Can be approximated as simple capacitors when their behavior is averaged across the switching voltages of a logic gate. 
- Presents simple models of each capacitance suitable for estimating delay and power consumption of transistors. 
## 2.3.1 Simple MOS Capacitance Models
$C_g = C_{ox}WL$ 
- Approximate the gate capacitance as terminating at the source, and call the capacitance $C_{gs}$

Most transistors used in logic are of minimum manufacturable length, because this results in the greatest speed and the lowest dynamic power consumption. 

In addition to the gate, the source and drain also have capacitances. These capacitances are not fundamental to operation of the device, but do impact circuit performance and hence are called *parasitic* capacitors. 
- Arise from the p-n junctions between source or drain and are called diffusion capacitance $C_{sb}$ and $C_{db}$. 

## 2.3.2 Detailed MOS Gate Capacitance Model
The MOS gate sits above the channel and may partially overlap the source and drain diffusion areas. The gate capacitance has two components:
- Intrinsic capacitance $C_{gs}$ 
- Overlap capacitance $C_{gol}$ (to the source and drain)


# 2.4 Nonideal I-V Effects
The long-channel I-V model neglects many effects. This chapter goes into it much more. 
## 2.4.1 Mobility Degradation and Velocity Saturation
When strong lateral or vertical fields are applied, the long-channel model breaks down. 

Mobility Degradation: Strong fields hamper progress
- 
Velocity degradation: The faster you go, the more often you collide. 

## 2.4.2 Channel Length Modulation
Ideally, $I_{ds}$ is independent of $V_{ds}$ for a transistor in saturation, making the transistor a perfect current source. 
$V_A$ (early voltage) is proportional to channel length. This can be modulated and can reduce the gain of amplifiers. 

## Threshold Voltage Effects
### Body Effect
Body is an implicit 4th element. 
### Drain-Induced Barrier Lowering
The drain voltage $V_{ds}$ creates an electric field that affects the threshold voltage. (DIBL = drain-induced barrier lowering)
### Short Channel effect
Threshold voltage typically increases with channel length. When small $L$ is introduced, the depletion regions extend into a significant portion of the channel. This is the *short channel effect* or *$V_t$ rolloff*
## Leakage
When transistors are OFF, they still leak small amounts of current. Leakage mechanisms include subthreshold conduction between source and gate. 

Gate leakage is a quantum-mechanical effect caused by tunneling through the extremely thin gate dielectric
### Subthreshold Leakage
The long-channel transistor I-V model assumes current only flows from source to drain when $V_{gs} > V_t$
- In real transistors, current does not abruptly cut off below the threshold, but rather drops off exponentially. 
- When the gate falls off 



# DC Transfer Characteristics
## Static CMOS Inverter DC Characteristics
|      | Cutoff             | Linear                       | Saturated                    |
| ---- | ------------------ | ---------------------------- | ---------------------------- |
| nMOS | $V_{gsn} < V_{tn}$ | $V_{gsn} > V_{tn}$           | $V_{gsn} > V_{tn}$           |
|      | $V_{in} < V_{tn}$  | $V_{in} > V_{tn}$            | $V_{in} > V_{tn}$            |
|      |                    | $V_{dsn} < V_{gsn} - V_{tn}$ | $V_{dsn} > V_{gsn} - V_{tn}$ |
|      |                    |                              |                              |
|      |                    |                              |                              |



### CMOS Inverter Operation

| Region | Condition                                              | p-device  | n-device  | Output                 |
| ------ | ------------------------------------------------------ | --------- | --------- | ---------------------- |
| A      | $0 <= V_{in} < V_{tn}$                                 | linear    | saturated | $V_{out} = V_{DD}$     |
| B      | $V_{tn} <= V_{in} < V_{DD} / 2$                        | linear    | saturated | $V_{out} > V_{DD} / 2$ |
| C      | $V_{in}  = V_{DD} / 2$                                 | saturated | saturated | $V_{out}$ drops sharply |
| D      | $V_{DD} / 2 < V_{in} <= V_{DD} - \lvert V_{tp} \rvert$ | saturated | linear    | $V_{out} < V_{DD}/2$      |
| E      | $V_{in} > V_{DD} - \lvert V_{tp} \rvert$               | cutoff    | linear    | $V_{out} = 0$                       |
