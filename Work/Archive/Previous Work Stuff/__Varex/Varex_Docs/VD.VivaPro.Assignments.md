---
company: Varex
tags:
  - archive_deprecated/Varex
  - archive_deprecated/Varex/vivaPro
---
They want to make sure that the Linux stuff is working the same as on the Windows stuff. 
- VivaPro is a GUI for lots of the APIs found within the SDK. 
	- David Marshall is trying to work on fixing some CMake issues within VivaPro. 

There's an issue getting VivaPro into an SDK build. 
- We have a whole package that has the SDK build with VivaPro. 
	- VivaPro builds, but it isn't part of the package right now. 
- We have a VivaPro build on its own, and one within the SDK. 
	- We want to pick up the library version within the SDK version, and run it within Linux.
	- We want something in the `master` branch

On fpgit, search "vivapro" under My->Changes
- Grab one without a failure
- To integrate VivaPro into SDK is a challenge. 
- 

## Task 1
[Link to get Linux build](https://fpgit/#/c/23444/)
Fix build error in SDK 
Build 1708 on Jenkins (May 9 2024) for the Linux build
Build artefacts of the commit will tell you how the build went. 
- Select all files in zip and download everything. 
	- Pick the "Release" vivaPro release 

### `libvsb2dll/`
- Library that isn't default, and needs to be grabbed from the SDK
	- That's why we need the whole package so we can grab everything together. 
- We want to make sure whatever version we have is good. 
- Lots of people are working on this. 
	- Houses all the APIs that you see implemented within VivaPro
- He'll send me the library when he has a second
	- It's a linux library, and needs to be a `.tar` extension (linux version of `.zip`)


Windows side, everything is fine. 

The Linux side is the one that they are about to make things to work. So far, it compiles. 
- The only issues is that its difficult to run the whole thing in one place.  
- VivaPro build --> 

Play with the windows side to see what kinks I need to test. 
- I need to know all the features of the Windows side. 
	- Test everything on Linux to see what problems we have. 
		- Check features, files, storage, interaction, and all sorts of other stuff.
- At the same time, run it in Linux and start coding too. 
- I'll need to learn how to log within VivaPro. 

How does it know how to do an X-ray?
- There are different ways of telling a detector that the X-ray has started and that the X-ray is done. 
- Some OEMs do it through software, some do it thorough hardware

# Things to test
This entire thing is only for anlaysis guys. 

## Connection
- There are settings for the detector, and a detector setup process
	- Depends on name, URI, Library Full Path. 
	- He should be able 

## Acquisition Settings
- You can get get a raw image, and others. 

## Gain Calibration
- Does the background X-ray 

## Offset Correction

## Gain Calibration
To detect a bad pixel and gain values. 
- As long as it works on Windows, it should work on Linux. 
- Connection and acquisition are 

## Other things you can do
- Right clicking, every menu, ROI, everything should work the exact same on Linux as well as Windows. 
	- Shortcuts and other hotkeys should also be there. 

### ROI
- X, Y, ROI, EOI

### Pixel Compare Plot
Right click within screen
Compares one pixel for all frames. 
- Data we see here is the same 
- Make sure the file saved from this matches the Linux side of things. 


Make sure that all the data and analysis matches. 
- If it doesn't, go through the code to try and solve it. 

# Things to test round 2
## Saving Files
### `.seq` files
1. Save a `.seq` file as a bunch of different filetypes
2. Then, reopen the documents and make sure they all look and work correctly 
	1. Try to open and close them while looking at the same images grid patterns
For seq files, save as a bunch of different types
