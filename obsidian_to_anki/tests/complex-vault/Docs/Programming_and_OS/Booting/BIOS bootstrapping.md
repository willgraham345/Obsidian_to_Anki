---
type: note
---
# Background
- Loading the OS onto memory for operations is "bootstrapping" or booting. 
	- This is done with a bootloader program, which is typically BIOS. 
- chain loading = several bootstrapping stages, which change depending on what device we are working with. 

## BIOS process
The bootloader typically has multiple stages and uses chain loading to start. 

Stage 1 bootloader:
- Bootloader firmware is installed together with the BIOS in non-volatile memory. 
- Detects the boot device and moves to the next stage
MBR
- [[Docs/Programming_and_OS/Booting/BIOS Master Boot Record]]
VBR
- [[BIOS Volume Boot Record]]
IPL
- [[BIOS Initial Program Loader]]

# Usage