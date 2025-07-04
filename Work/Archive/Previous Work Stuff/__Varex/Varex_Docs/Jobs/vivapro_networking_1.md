---
company: Varex
tags:
  - archive_deprecated/Varex
  - archive_deprecated/Varex/vivaPro
---
##### Description:
Actual + Expected:
- Can't connect to the detector on windows/linux
![[Pasted.image.20240528135539.png| 750]]
	- Rebooted, tried to reset with the USB drivers with IT. 
	- Still unable to access this stuff. 
Reproduce:

##### System Overview:
![[networking.drawio.svg | 750]]
![[Pasted.image.20240528141523.png| 750]]
- Working sorta now :)
![[Pasted.image.20240528141841.png| 750]]
- Getting output from the `192.168.1.31` finally

##### Solution
Troubleshooting/Testing Steps Attempted:
Things Fixed:
- Drivers on my computer.
- USB passthrough on VirtualBox 
	- ![[Pasted.image.20240528142933.png| 300]]
- Wired settings on the VM
	- ASIX Ethernet on 
	- ![[Pasted.image.20240528143114.png| 300]]
	