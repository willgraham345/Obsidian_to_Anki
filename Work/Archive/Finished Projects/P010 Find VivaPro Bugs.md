---
type: project
project_id: 0
company: Varex
project: VivaPro
subproject: testing
tags:
  - archive_deprecated/Varex/vivaPro
status: closed
---
# Related Links:
# P010 Find VivaPro Bugs Updates/Notes:
## 2024-07-02 16:00
### Not sure
1. Menu->Analysis isn't popping up with the VivaPro menu

### May relate to not having config
1. Offset calibration doesn't work. (screenshotted)
2. Gain calibration also doesn't work (screenshotted)
3. Acquire image
4. Getting configuration data didn't work.
5. Tools->Transmit Files
	1. Pops up with a "communication failed error Failed getting number of modes", but then advances to what I think is the correct menu/object
	   ![[P010 Find VivaPro Bugs.png|325]]
	   - Shows a dropdown for map types, but none for mode. 
	   - Clicking "Get Map File" and "Put Map File"
	   1. Put map file seems to work, or at least it pops up with a file explorer for looking for the files. Catches a file. 1
	   2. Similar story with the Config and User Files tag. The getters don't work, but the putters at least appear to be working. 