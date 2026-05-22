# MOSFET Fundamentals
## Questions at the beginning of class
- When we have some HDL, you can describe it using a behavioral or a structural description. Which is better?
	- If you have an exact topology of a circuit you want to implement, go to structural. 
	- If you want to let the tool have some freedom, give the tool a behavioral description. 
		- You will NEED a good constraint equation or description. 
- Latch inferences
	- When we aren't explicit with If/else statements (no default), it will infer that there is a latch. 

## Transistor Theory
- A transistor is a solid-state device used to amplify or switch electric signals. Electrons ($n$) or holes ($p$)
	- n-MOS: normally off
	- p-MOS: normally on
- $V_T$ = threshold voltage required to enter into inversion 
- P type substrate is the typical rule
	- This means that we have holes in our substrate
	- We really have 4 things to charge, because our substrate must also be charged. 
### Cutoff Operation Point
- $V_{GS} = 0$ 
- MOS cap is in accumulation 

#### Linear Operation Region
- $V_{GS} > V_T$
- Analog people LOVE this
	- People polarize their stuff somewhere in here, and then they want to navigate somewhere within these curves.
- $I_{DS}$ goes up when $V_{DS}$ goes up
- $I_{DS}$ goes up when $V_{GS}$ goes up
	- wider conductive channel
- 
#### Pinchoff Operation Region
- $V_{GS} > V_T$
- MOS cap is inverted presence of a conductive channel. 
- The drain potential $V_D$ induces a depletion region and charges drift towards the source
- For $V_{DS} = V_{GS} - V_T$, the channel is pinched off and the current reaches its maximum
#### Saturation Operation Region
- $V_{GS} > V_T$
- Where we like to play. It's the nice 0's and 1's found in digital stuff. 
- MOS cap is inverted, presence of a conductive channel. 
- $V_{DS} > V_{DSsat}$
	- drain depletion region expands, current level saturated


### p-type Transistor I-V
- All dopings and voltages are inverted for p-type
	- Source is the more positive terminal
- $\mu_p$ = Mobility, is determined by holes
	- Typically 2-3x lower than that of electrons $\mu_n$
	- Something we must characterize as a designer
- Thus, p-type must be wider to provide the same current
	- In CMOS technologies, usually assumed to be $\mu_n / \mu_p = 2$
- Any two conductors separated by an insulator have capacitance
	- MOS gate sits above the channel, and may partially overlap with source and drain. The gate capacitance can be approximated to $C_0 = WLC_{ox}$ assuming parallel plate capacitor. 
		- The bottom plate of the capacitor (the channel) depends on the mode of operation. 

