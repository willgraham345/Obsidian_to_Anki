---
company: Varex
tags:
  - archive_deprecated/Varex
  - archive_deprecated/Varex/vivaPro
---
# Background
Configuration Items
Ubuntu 20.04
- User is `dev`, password `dev`
gcc
- 9.4.0
- stored in `/usr/bin/gcc`
gdb
- 9.1
- stored in `/usr/bin/gdb`
Source code
- Stored in `~/dev`
Qt
- 5.13.0
- Stored in `/home/dev`
qtBuildOnly


# Progress
## Building within QtCreator
Goal: Build Successfully
- Issues with not finding additional `src/` code
	- No `GL/gl.h` directory
- Build


### What Qt folder should look like:
dev@ubuntu:/opt/Qt/5.13.0$ ls  
5.13.0          Examples             MaintenanceTool      Tools  
components.xml  InstallationLog.txt  MaintenanceTool.dat  
dist            installer.dat        MaintenanceTool.ini  
Docs            Licenses             network.xml  

## Next Project
Writes binary files that the detectors can read
- Our detectors are so configurable through a config file that they use to do things. 
- They wrote a Qt-based configuration writer that isn't on winforms. 
	- It only does modular configs (newer products)
		- Z line
		- Gen 5 config
- DAQs are in there too
- They want to get rid of old versions in C#
	- They want to be able to open older config files in config creator, and have the same editability within the old school versions
- Config repository understands all of those options, and gets the information within there. 
	- The only ones that they have supported. 
	- They need to be able to provide support for old-school style support 

## Config Creator CMake STuff
`engineering/ConfigCreator`
Why don't we look at ConfigCreator CMake stuff
`engineering/ConfigCreator/CMakeLists.txt`

Could be a good model for the current project.