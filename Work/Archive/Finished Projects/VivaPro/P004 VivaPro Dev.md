---
status: stalled
type: project
project_id: 0
tags: 
company: Varex
project: VivaPro
subproject: VivaPro_dev
---
# Relevant Links
People working on this with me
- [[Fred Zoghi]]
- [[Gonzalo Tello]]

Projects that came out of this:
- [[P008 VivaPro Currents Tab Not Showing Up]]
- [[P009 VivaPro Network Settings Tool]]
- [[P011 VivaPro Project File Doesn't Compile]]
Bug Screenshots
- [[vivapro-1.png]]
- [[vivapro-2.png]]
- [[vivapro-3.png]]
- [[vivapro-4.png]]
- [[vivapro-5.png]]
- [[vivapro-6.png]]
- [[vivapro-7.png]]
- [[vivapro-8.png]]
- [[vivapro-9.png]]

# Updates/Notes:
- Fred sent me a giant list to start working through in a word doc
- Enabled all the VivaPro firewall stuff
	- Gain calibration failed at this the last step:
	   ![[vivapro.png|350]]
		- Saved the transmission stuff in `Desktop/transmit`
- Seeing this image when launching VivaPro from Linux
  ![[vivapro-1.png|325]]
  - Got around it, acquiring images from Linux
  - Failing at the same spot in Linux
	  - ![[vivapro-2.png|375]]
Fred just messaged me saying that he's seeing different issues than me with the detector. I'm *guessing* that there was an error earlier in the Log Tests that I didn't fully catch. I'm hoping something incorrect  was written to the detector and I just didn't catch it.

Made a script to launch QTCreator within Linux. 

### Building in Linux
There are some issues with the build in Linux (see [[2024-06-25 Fred VivaPro-1.png]] and [[2024-06-25 Fred VivaPro.png]])
- From what I can tell, I think there may be some issues on the build targets with QT and a traditional Windows build. I may need to figure out how the debugging features within QT work when the build comes from a script (like in the `build.sh`, and `generate.sh` files)

#### Fred's Suggestions
VivaPro depends on the Config repo
- I can't use the `.pro` because I'd need to build the whole config file on my VM. Instead I can copy his `qtBuilOnly` folder directly into my home directory, and that will provide the necessary headers for my stuff to build. 

Fred said I may be missing environment variables, or at least the associated software/memory behind them. 

| Environment Variable | Exists?            |
| -------------------- | ------------------ |
| CMAKE_PREFIX_PATH    | :BoBxsCheckCircle: |
| LD_LIBRARY_PATH      | ⚠                  |
| LD_LIBRARY_PATH # 2  | ⚠                  |
I think I fixed an error within the LD_LIBRARY_PATH but I'm not 100% positive. 

New `LD_LIBRARY_PATH`: ![[P004 VivaPro Dev-2.png|425]]

New `CMAKE_PREFIX_PATH = ./:opt/Qt5.13.0/5.13.0/gcc_64/lib/cmake/Qt5`

#### Debugging
There is an error when we don't include the `autoversion.h` values. 
![[P004 VivaPro Dev-3.png|400]]
Did a bunch of edits to the `.pro` and realized I may not have the most updated version of the project. 

### Build Fixes
We need to rename a few of the files, so they have targets that match. Specifically:
- src/detectorAcquisitionRad.cpp
- dlgoptions.cpp
- src/viewFrameDisplayInterval.cpp
- test/qtBuildOnly/autoVersionQtBuildOnly.cpp
- ![[P004 VivaPro Dev-4.png]]
	- Left off here 

Added a few includes that Fred suggested, which brought us closer to the linking/compiling stage. 
- I think the thing that is failing is the moc_ somethign in there...

### Debugging again
#### Things we tried
Removed the libraries within the `.pro` file
- Led to an error with the `lirtualModeMapper::initialiaze()`
	- This had a ton of other errors too...
	- Undefined reference to other stuff. 

Keeping the libraries in gets a build all the way until:
- ![[P004 VivaPro Dev-5.png|1000]]
- Libraries and their origins:
	- `lAdvapi32`
		- May or may not be a Windows-specific dll library
		- [This stack overflow thread](https://stackoverflow.com/questions/14161656/what-would-be-the-equivalent-of-win32-api-in-linux) says that Qt may have an abstraction. 
	- `LDI32`
		- Might be a macro for TI products. [TI Thread](https://e2e.ti.com/support/processors-group/processors/f/processors-forum/354013/ldi32-pru-instruction)
	- `lHtmlhelp`
		- May be helpful for HTML scripts, but I'm still not positive. There are a few threads describing something like html to chm file conversion within linux [here](https://stackoverflow.com/questions/9174140/html-to-chm-file-under-linux)
		- `chm` are also proprietary files
	- `ldGdi32`
		- Couldn't find much
	- `liphlpapi`
		- This feels like it would be a Varex file. 
Modified the setup so we have 

##### Changes to the project file:
- unix/win32 conditionals
- Added $USER to the path on the `test/config/inc`

##### Current failures:
- Config isn't compiling for whatever reason. 

##### Attempts:
- We copied the qtBuildOnly into the vivapro directory and changed the 

##### Left off:
- ![[P004 VivaPro Dev-6.png|375]]

### Debugging again
1. Commented out lines in the dlgVirtualModeMapper.cpp
	- Commented out basically every function in the file. 
Had a successful build after commenting out a bunch of different stuff. I now have a fully-functional debugger. 


I'm going to start working on [[P008 VivaPro Currents Tab Not Showing Up]]

## Config 
- Ethernet 6 is what the USB->Ethernet is for. 
Windows

| Field                             | Value                   |                 |
| --------------------------------- | ----------------------- | --------------- |
| Ethernet USB port                 | 6                       |                 |
| Ethernet/USB IPv4 adapter address | `192.168.2.11`          | `255.255.255.0` |
| Detector IPv4                     | `192.168.2.31`          |                 |
| VivaPro Detector Setup            | `vrxnet://192.168.2.31` |                 |
|                                   |                         |                 |
Ubuntu

| Field                                    | Value          |
| ---------------------------------------- | -------------- |
| ASIX Ethernet Connected (not USB or PCI) | `192.168.2.11` |
| Detector IPv4                            | `192.168.2.31` |

ASIX need to be connected via USB