---
type: project
project_id: 0
company: Varex
project: VivaPro
subproject: VivaPro_dev
tags: 
status: stalled
---
# Related Links:
# Updates/Notes:
## 2024-07-24 09:00
Opened the issue. Not sure on how I'm supposed to open the defect editor. I get weird blank things, and acquiring the image and defect map doesn't work. 

## 2024-07-24 10:00
Spent the last while familiarizing myself with the CPP libraries again, reorganized my own reference sheets

Started looking into the `DefectMapEditor` class/source code. It's complicated. 

## 2024-07-24 11:00
Started making [[VD.VivaPro.DefectMapEditor]], and the [[VD.VivaPro.ViewFrame]]. 
- [[VD.VivaPro.DefectMapEditor]] interacts with the GUI. I want to test how to Acquire the Image and Defect Map first. 
Looking through the code, and I don't know where to find a defect map file. 
When I click on the transmit tab, the editor does not return anything when I try to acquire the defectMap
There's a function that will transmit an empty defect map file to the detector. I think that's the thing to focus on. 

What's the difference between a defect map file and the defect map data?
- When I try to put the defect data onto the detector I don't have a response. Does that change according to different detectors?

There's another function that determines if there even is defectMap data at all. Called by a variety of different functions.
- Yep, this one is returning false, meaning that there is not any defectsmap data
	- Stack trace says that it was called by `onDefectMapEditorDownloadDefectAct`

## 2024-07-24 15:00
Fred messaged me saying I shouldn't worry about this one as much, and to focus on the other bugs. He said he'd take care of the Gerrit stuff.