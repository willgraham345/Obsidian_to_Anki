---
type: note
tags: []
---
# Questions
## Abstract Summary
- PIM = processing in memory
	- Covers a wide spectrum of computing capabilities in close proximity or even inside of the memory array. 
- NMP = Near-memory processing
- IMP = In-memory processing
- NVM = non-volatile memory

## Motivation of Paper
- We can't breach the memory wall (a.k.a. power wall). Processors work much better, and are being outpaced by big data

## Methods
- NMP:
	- HMC and FPGA achieved much better CPU and FPGA-based graph processors
	- High performance NMP OpenCL-based FPGA accelerator for deep learning
 - IMP
	 - Utilize dot-product capability of crossbar structure for faster matriix multiplication
		 - PRIME, ISAAC, and memristiviie boltzmann machine are examples
	 - Neuromorphic system, which exploits the analog nature of NVM array to implement synaptic network to mimic fuzzy logic of human brain
	 - AP (associative processor), aka a nonvolatile content-addressable memory (nv-CAM), or ternary content addressable memory (nv-TCAM) which supports associative search to locate data records by content rather than addres. 
	  - Reconfigurable architecture (RA) which includes nonvolatile FPGA and reconfigurable in-memory computing architecture
		  - AP and RA show promise
			  - These guys also did an RA paper

## Context
- Recent advances have happened with die-stacking tech
	- HMC = Hybrid Memory Cube
		 - Better RAM performance compared with traditional DDR DRAM
	- HBM = High Bandwidth Memory
	- BE = Bandwidth Engine
 - The last decade has seen large progress in emerging NVMs
	 - Insertion of this tech into existing computer structures is unrealistic
	 - Difficult to convince end-users to switch to a new technology when significant benefits aren't reached.

## Figures + Data Tables
## Interpretation
## Future Work
- Virtual memory support
- memory/cache coherence
- fault tolerance
- security + privacy
- thermal + power constraints
- compatibility with modern programming models


