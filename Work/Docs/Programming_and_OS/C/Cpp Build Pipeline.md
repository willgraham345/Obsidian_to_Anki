---
type: note/workflow
same: ["[[CMake Workflow]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, January 3rd 2025, 9:51:05 am
workflow_of: ["[[Cpp]]"]
---
# Background

## Build Process
Preprocess
Compile
Link

![[Cpp.Build.Pipeline.png|225]]
![[Cpp.Build.Pipeline-1.png|250]]
![[Cpp.Build.Pipeline-2.png|603]]

## Projects with multiple source files
Steps 1-3 are performed independently on each source file to produce an object file (`.o`)
The linker then collects the source files and does the following:
- Scans the `.o` files for functions that are referenced but not present
- Scans archive (`.a`) files from the standard disk directories looking for those "unresolved" functions
- Combines the object files with parts from the archive files into an executable file. 

Each source file is an independent translation unit. 
- Means that any required `#include` statements, `#using` statements, class definitions, function prototypes, need to be present in each source file.
	- A `using` statement coded in one source file is not automatically available to your other source files.

# Usage