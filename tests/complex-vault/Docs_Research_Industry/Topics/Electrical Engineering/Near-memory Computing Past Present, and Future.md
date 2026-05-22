---
type: note
---
# Questions
## Abstract Summary
Memory hasn't been able to keep up with advances in processor technology from a  latency and energy consumption perspective. 

Dennard scaling = MOSFET scaling which states that as transistors get smaller, their power density stays constant. This didn't work, and stopped due to supply voltage limits.

Today's memory hierarchy usually consists of multiple levels of cache, the main memory, and storage. 

Traditional approach is to move data up to caches from the storage, and then to process it. NMC aims at processing close to where the data resides. Seeks to minimize the expensive data movements. 3-dimensional stacking is the true enabler of processing close to memory. Allows the stacking of logic and memory together using through-silicon via's TSVs that help to reduce memory access latency, power consumption, and provide higher bandwidth. 
## Motivation of Paper

## Methods
### NMC Classification Criteria in this paper
- Memory
- Processing
- Tool
	- Availability of tool infrastructure indicates maturity of the architecture
- Interoperability
	- Programming model, cache coherence, virtual memory, and efficient data mapping. 
- Application
	- Domain of the appication

### Programmable Unit Research
NDC
- Central multi-core in daisy-chain with multiple 3D stacked memories
[[TOP-PIM Throughput Oriented Programmable]]
- Architecture based on accelerated processing unit (APU). Each APU has a GPU and CPU on same silicon die, and are innterconnected with high-speed serial links with multiple 3d-stacked memory modules
AMC
- Active memory cube, built on HMC (Hbrid Memory Cube from Micron). Added several processing elements to vault of the HMC. Compiler support based on OpenMP for C/C++
PIM-enabled
- Compute-capable commands and specialized instruction to trigger NMC computation. NMC processors are composed of adders and SRAM operand buffer housed in logic layer of the HMC. 
Tesseract
- Graph processing applications. 
- One host processor, an HMC with multiple vaults
TOM
- host GPU interconnected to multiple 3d-saacked memories hat has a small light weight GPU cores. Develop a compiler framework that automatically identifies possible offloading candidates. 
Pattnaik
- NMC-assisted GPU architecture.
- Affinity prediction model decides where a given kernel should be executed. 
Mondorian
- Hardware and software co-design is needed to achieve efficiency for NMC systems.
- Current optimization of data-analytic algorithms heavily rely on RAM while NMC prefer sequential memory accesses to saturate huge bandwidth available. 
MCN
- Use a lightweight proocessor similar to Qualcomm snapdragon as NMC in the buffered DRAM DIMM
SSAM
- Use pin tool to characterize the arhcitectural behaviors of kNN (core of similarity search applications)
DNN-PIM
- Heterogenous NMC architecture for training deep neural network models
- Logic layer of 3D-stacked memory comprises programmable ARM cores and large fixed-function units (adders + multipliers)
- Extend OpenCL programming model to accomodate the NMC
Boroumand
- Evaluate NMC architectures for google workloads
- many google workloads spend a considerable amount of energy in data movement
- 2 NMC architectures
	- One based on CPU
	- Fixed-function accelerator on top of an HBM

### Fixed-function Unit
JAFAR
- embed an accelerator in a DRAM module to implement database select operations
IMPICA
- Accelerate pointer chasing operations with specialized units that decouple addresses generation from memory accesses in logic layer of 3D-stacked memory.
Vermij
- Sorting algorithm 
GraphPIM

### Reconfigurable Unit
Gokhale
- Place a data rearrangement engine (DRE) in logic layer of the HMC to accelerate data accesses while still performing computation on the host CPU
HRL
- HRL (heterogeneous reconfigurable logic)


### Discussion
## Context
NMC isn't new, and goes as far back as the 60s, but first appeared in the 90s. 
- Vector IRAM (VIRAM)

HMC = Microns Hybid Memory Cube
HBM = High Bandwidth Memory from AMD + Hynix
## Figures + Data Tables
![[Pasted image 20231206134611.png]]
![[Pasted image 20231206134553.png]]
![[Pasted image 20231206134830.png]]
## Interpretation
Majority of research have proposed homogenous processing unis near the memory 
- in-order cores
- GPUs
- FPGAs
- application specific acclerators
Majority of NMC proposals are targeted towards different types of data procoessing applications
- graph processing
- MapReduce
- Machine learning
- Database search

Logic layer 
## Future Work