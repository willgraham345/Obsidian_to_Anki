---
status: closed
type : update_log
date: 2024-06-25
week: 2024-W26
year: 2024
tags: [archive_deprecated/Varex/vivaPro]
---
# Relevant Links
- [[P004 VivaPro Dev]] 
- [[Gonzalo Tello]]
- [[Fred Zoghi]]

# Message
I'm trying to reproduce the errors you've been having, and I'm not having a ton of luck. 


Things I've tried:
- Windows:
	1. Changed the ethernet port 6 back to unconfigured. 
	- Pinging:
		- 192.168.1.31 ❌
		- 192.168.2.31 ❌
		- 192.168.2.31 ✅ (worked after I reconfigured the IP addresses)
	- VivaPro worked great too. Not sure what the problem was. 
- Ubuntu 
	1. Ping worked when I configured the ASIX Ethernet to the right address. 
	2. I have the wired IP address set to `192.168.2.11`, and ping works great on that address. HOWEVER, when I pull up the Wired settings, it says that the address is set to `192.168.2.31`. 
		1. Trying a restart here. Hoping that changes something. 
		2. PSYCH! I got everything working. Life is peachy. 




## Midday Update
Any chance that these errors look familiar to you? I think there is some issues with the sourcing in the project but I could be wrong. Here is the output:
![[2024-06-25 Fred VivaPro.png|400]]![[2024-06-25 Fred VivaPro-1.png|200]]

## Autoversion
Hey Fred! I was able to narrow it down to a few errors.

The first error comes in the build, where I get an error saying two object files can't be built. I can see this traceto a ui/ui/_dlgAbout.h file and a /ui/ui_dlgAcquisitionModeSettings.h. I googled the issue, and I found this link: https://stackoverflow.com/questions/4034392/makefile-error1. I'm honestly not sure what to try here. 

I was running out of ideas, so I tried to run qtmake (one of the options right next to building the project). From that, it said that I can't access the /moc, /obj, /rcc, or /ui directories. It also said that it failed to find the src/detectorAcquisition.cpp, srcdlgOptions.cpp, src/viewFrameDisplayInterval.cpp, and test/qtBuildOnly/autoVersionQtBuildOnly.cpp.

Does any of that have any significance for you? I'm not super familiar with the Qt build process, but I'll look into it until I hear back or find a better solution. 

I found another error which says that we need to have an "autoversion.h" header file. This error is popping up in the dlgAbout.cpp