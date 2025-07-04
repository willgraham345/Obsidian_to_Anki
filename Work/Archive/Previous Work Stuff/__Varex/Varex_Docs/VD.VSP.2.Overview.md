---
company: Varex
tags: archive_deprecated/Varex
---
# Background
![[Pasted.image.20240509150238.jpg| 600]]
- VSP is an API adapter on the architecture overview
- Written in C# and C
- Tons of unit tests
## Acquisition
##### Fluoroscopy
Fluoroscopy detectors are designed to deliver images over Ethernet link or over Coax
`vsp_fluoro_acquisition_start()`
`vsp_fluoro_acquisition_stop()`
##### Radiography
Rad acquisition 
`vsp2_rad_acquisition_start`() - arm the detector for acquisition
`vsp2_rad_acquisition_trigger`() - software trigger to initiate integration
`vsp2_rad_acquisition_stop`() - disarms and returns the detector to idle
`VSP2Callback` - receives events during the acquisition cycle
There are some great Rad acquisition sequence diagrams in the documentation 
## Calibration files
There are 3 calibration files per mode: offset, gain, and defect. 
- Used for on-board corrections during image acquisition. 
- All files necessary for imaging reside on the detector except for the client library. 
- APIs can be used for offset and gain calculations. 
- `vsp2_get_map()`
		- Used to transfer calibration maps to and from the detector.
# Usage
Defined in chapter 15 of the document. 