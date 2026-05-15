---
type: meeting
company: Varex
tags: 
project: 
subproject:
---
# Links/People:
- [[Greg Gerber]]

# Todo:
- [ ] Change listview out for tabbed view
	- We want the listview for modules, but a table view if it's standard. 
		- Token:value more similar to XConfig
- [ ] Make two different token-value pages. Everything has at least one mode. 
	- Title it system area or something like that.w
		- Name the existing thing as mode

# Notes:
- Old school configs, the firmware knew where the offsets started. 
	- The firmware would say that it knew what registers were there
With modular confiugrations, they started doing 32bit offsets with 32bit registers. They'd have gaps because that's what the FPGA guys wanted
- There's an offset for all of them. 


Change

UDR are kind of like global registers for the module. 
- They have UDR offsets, and UDR registers. 
	- They apply to every mode. 
	- Lots of mode registers that start at the 256 offset. 
- These are virtual modes now...?
Mode register offset

We'll have to make sure that we're not messing up the modular. 