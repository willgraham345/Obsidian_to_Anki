---
type: note
tags: note/VSCode
---
# Background
REALLY good guide on how to do this [here](https://code.visualstudio.com/docs/cpp/cmake-quickstart)

Workflow
Create --> Configure --> Build --> Debug
# Usage
1. Create CMakeLists.txt file
	1. Command `>Cmake: Quick Start`
	2. Enter project info, testing (if desired), 
	3. Library or executable. 
		1. Library will be a basic source and header file
		2. Executable will make... an executable
2. Create CMakePresets.json file
	1. `>Cmake: Quick Start`
		1. `Add a New Preset` and `Create from Compilers`
			1. Scans for kits on your computer and creates a list of compilers found on your system
	2. Select a compiler you want to use
	3. Enter a name for this preset.