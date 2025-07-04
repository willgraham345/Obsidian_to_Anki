---
tags: archive_deprecated/Varex
---
You need to throw on a 
`git submodule update --init`

This updates the repos

Glass = Hardware
- Kind of like device drivers for panels

Get to know the hardware guys
- They've been here a while, and they're smart. 


PAL = Physical access layer
- Allows you to talk to the glass

The API we have that lets our customers use 


VSP2 API 
CRAPI = Customer receptor API
- Generic thing that will pass all commands through from the client PC into the CRAPI that can be transferred over to the detector side. 
- CRAPI on detector as well as the client
Gerrit is their code review software
Function generators
- Can be driven by external sync
- High and Low can be used in final test to set framerates in fluor
	- 30 frames/sec
	- 60 frames/sec
- Ted did a bunch of stuff to them (he was good at embedded electronics)
- Old days were Makefiles, Project files. Now they're CMake.

Integrate = collect charge
Read out = get information 

Dark images
- You see the artefacts of the manufacturing process that happen 
	- TFTs don't get quite as hot due to suction cups that are placed on during the manufacturing process
	- Looks like ripples and gray
	- Salt & pepper
	- These are treated as flat noise
- Offset corrections fix this
	- Subtract from the dark image and all you have left is the signal
	- They need positive values for their pixels

