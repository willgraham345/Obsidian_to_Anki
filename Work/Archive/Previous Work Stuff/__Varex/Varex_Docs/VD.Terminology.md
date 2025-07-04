---
company: Varex
tags: archive_deprecated/Varex
---
##### A

##### B

##### C
CT
- Computed tomography

##### D
Detector naming conventions
- *1616z* eth
	- Means its a 16cm x 16cm detector with an ethernet interface

| Detector Name   | Fluoro or Rad |
| --------------- | ------------- |
| 1616 z ethernet | Fluoro        |
| 2121 z exp      | Fluoro        |
| 3131 Cof        | Fluoro        |
| 4343 w \| Eth   | Rad           |
| 2530 C \| Eth   | Rad           |

##### E
ENG_BLD
- A type of branch naming scheme which is something that isn't quite an RC (release candidate), but has interesting features that a customer may be interested in exploring. ENG_BLD branches are not 1:1 with ENG_BLD labels, and the label is what matters. 

##### F
Fluoro
- Fluoro is short for fluoroscopy, which obtains moving images using several pulses of an X-ray beam to show internal organs and tissues.  
- Produce a live "video" format image, which can show movements inside the body. 
	- When done with contrast can highlight the inner lining of tubular organs in the body. 
##### G

##### H

##### I

##### J

##### K

##### L

##### M

##### N

##### O

##### P

##### Q

##### R
Radiography
- Radiography uses radiation to provide images of tissues, organs, bones, and vessels inside your body. 
	- An X-ray exposes you to a small dose of ionizing radiation to produce pictures of the inside of your body. 
RC
- Release candidate
- Each release candidate is labeled as an official build and handed to Software QA for final verification and validation.
	- Initial testing is automated
- Once a software product is released, they bump up the major/minor and start over with RC1. Kinda fun. 
ROI
- Region of interest
- Old Varex devices had a Region of Interest (ROI) in the config file for a specified mode. 
- VSP2 software interface includes added capabilities for OEMs to configure ROIs without requesting changes to the configuration file. 
- Shrinking ROI will not impact frame rate, but shrinking height of the ROI *will*. ROI changes will require new offset and gain calibrations. 

##### S
SDK
- Software development kit
- The tooele one is what lets teh customers operate their detectors. It's a product they sell along with the detectors, which the customer then uses to develop their end product. 

##### T
tether
- *might* be a way of sharing wifi from a phone to another device
- Can alternatively be attaching a device by wire to a data or power source
tooele
- Big ole software repo that they've been building forever. 
T01 vs T02
trigger

##### U

##### V
vtrigger
- Triggering the acquisition of an X-Ray by receiving X Ray within the panel. Instead of triggering a readout with the use of software, or an external signal, the X Ray itself triggers the readout. 

##### W

##### X

##### Y

##### Z
zlilz
- Name for a new line of detectors
	- Started as big z little z (large and small detectors of the same design) --> Zlilz --> zlilz
1616z
- 
