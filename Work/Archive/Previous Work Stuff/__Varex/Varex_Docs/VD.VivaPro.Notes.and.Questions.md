---
company: Varex
tags:
  - archive_deprecated/Varex
  - archive_deprecated/Varex/vivaPro
---
# Project Overview
Notes from Paul
1. We want to compile VivaPro within Linux, with proper execution within Linux. 
2. Test each of the features within Linux
	- Windows compile, and THEN a Linux compile. 
	- We need fluoro functionality and rad functionality
	- They have a DREAM machine that's in the lab for use with remote access. (ask about these)
		- They have a Gen6 hooked to this machine
		- When we get to the fluoro part of this, we'll need to get that set up

Talk with Fred
- There is a repo for VivaPro, and another for SDK
	- When they build SDK, it includes within the VivaPro build
		- The VivaPro needs the executable and the library
- Issues I'm fixing
	- Within the VivaPro repo

## Building
- Do I need to build within Jenkins, or can I build locally?
	- How do I do both?
		- Linux
		- Jenkins
	- Build from Git repo, 
```shell
git submodule update --init
```

### Two way to build it
1. Visual Studio (slow)
	1. `generate.bat`
	2. `build.bat`
2. QT (v5.13) (fast, and has a debugger)

#### Notes on QT
Build on Windows, debug within VM
Fred usually builds it in QT
Use QT Creator to launch, and open `vivaPro.pro` to open the project. 
Click build, 
- Click `compile output` to see how its compiling
- Fred has a local build on his C: drive that lets him compile through Windows. 
I have the wrong version of Qt which does not support visual studio 2019. I need to install 2017, but I should install Visual Studio 2017. 

### Debug build
He does the debug build here, and then builds onto linux. 

### Checking Version Number
Click VivaPro Menu : Help -> About
- Look at Version # Posted at top of screen

## New build notes
- `dependencies/`
	- For redistribution (for customers)
- `developer/`
	- Also for customer
- `lib/`
	- Where we put our `lib.vsp2` library
	- Internal creation, what we use for the testing. 
- `vivaPro`
	- Uses libraries within `lib/vsp2.so`
	- `plugins/`
		- Lots of `Qt`, we don't need to do anything
		- Created by `Qt`, and used by VivaPro executable. Needed by Qt, but we don't really need to worry about it. 
	- `qt.conf`
		- Do we even need it?
		- There is a `vivaPro.png` that is used to create the icon for the application (same with `vivaPro.desktop.desktop`)
			- Look into this, and making it into the icon for the app within linux (same with desktop)
		- Might be needed for use within the icon
- The only thing we need to change is the VivaPro executable
	- Build it, debug it, copy it. 
- `test/`
	- `update --init` adds all these files for us
	- Fred has that on his C: drive, which is why he commented out the last line in `vivaPro.pro`
		- There are configs that require us to build the correct versions of the configs. 

## Types of Detectors and types of images
rad: Still
- `.raw` files
Fluoro: "Live", similar to video
- `.seq` files

# Questions I Still have
- What is `pleora/eBus`? 
	- Why do I need it?
	- What version? [link to pleora]([Index of /tools/pleora/eBus](http://slfpbuildmstr/tools/pleora/eBus/))
- We've jumped around on versions quite a bit. Which one should I be focusing on?
- Which detector should I use?
- Why do I need the `sdk` and the `EBUS`? 
	- SDK
		- Do I need version 2419?
	- eBUS
		- Why is the `eBUS SDK` required?
		- What is the significance of everything on your personal folder?
- Again, what is the `libvsb2.dll`? 
	- You said I have it, I don't know what you mean by that. 
	- You mentioned it should go within the `lib/` directory in a Linux build. 
- Difference between `vivaPro` and `new_vivaPro_may20` in my VM?
	- `new_vivaPro_may20` is where we have executables
	- We get source code from vivaPro repo on git