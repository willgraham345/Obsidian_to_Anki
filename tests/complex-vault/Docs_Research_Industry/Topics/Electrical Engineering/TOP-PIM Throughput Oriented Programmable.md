---
type: note
---
# Questions
## Abstract Summary
Moving computation closer to memory presents opportunities to reduce energy and data movement overheads. 
They're trying to use 3D die stacking to move memory-intesive computations closer to memory. 
- This approach can be commercially feasible
3D stacking provides:
- Increased bandwidth
- Throughput-oriented computing using programmable GPU compute units

They also produce methodology for rapid design space by predicting performance and energy of in-memory processors based on metrics obtained from execution. 

Early results show that PIM show moderate performance in return for significant energy efficiency improvements.
- viable PIM configurations are performance competitive with a representative mainstream GPU and even greater energy efficiency improvements. 
## Motivation of Paper
- Even with aggressive estimates on reducing DRAM's demands, sustaining memory may consume ridiculous amounts of energy. 

## Methods
You can stack memory on top of low-energy memory processors. These can be optimized for low-energy operation and reduce thermals. 
- The main compute processor isn't stringent to thermal constraints and can support compute-intensive code
- Energy-efficiency of GPUs enables GPU accelerated in-memory processing. 

What do they do:
- Explore GPU-accelerated architectures as in-memory processors
- Simulation methodology that automatically scales performance and power values
- Evaluate energy and performance impact of PIM in near-future technology nodes
## Context
3D die stacking
- 3D stacking allows multiple things to be combined, namely DRAM and logic dies to be coupled together. 
	- DRAM and logic die coupling
	- Interconnections within a die stack (TSV = through silicion via) enable higher bandwidth, lower latency, and lower energy communication across dies within a stack relative to 2D organizations
- Memory power
	- DLL/PLL
- GPU Architecture
	- At a high level, GPU architectures conssit of collections of simple ALUs operating under a single-instruction, multiple-thread model. 
	- Computing resources are grouped into compute units (CU).
		- Each CU is combined into four 16-wide SIMD units, a scalar unit, L1 cache and a shared scratchpad
			- DRAM memory is organized as a set of memory channels, each with an associated slice of the L2 cache. 
	- GPUs are highly multi-threaded, with each CU simultaneously running hundreds of threads
		- They can have ~10x the bandwidth over consumer CPUs. 
- Power + Thermal Considerations
	- in-memory processor and memory need to share the same path back to the heatsink. 
## Figures + Data Tables
## Interpretation
## Future Work