---
type: note
---
# Background
- Solution = a container to organize one or more related code projects, like a class library and a corresponding test project. 
- Project = One project produces one output (typically an executable or library (`dll`))
- If you are going to code three executables that uses related code, you'll create one solution and at least three projects

Project Explorer
- You'll see *filters* and folders in this.
	- Filters = Header files, Resource Files, Source Files
		- "virtual" folders for organizing source code. 

If you'd like to think of it like a tree, then this is what it'd look like:
```
.sln
   .vcproj
      .h
      .h
      .cpp
      .cpp
   .vcxproj
      .h
      .h
      .cpp
      .cpp
   .csproj
      .cs
```

## Configuration
Handled through the properties tab
- Testing, input/output directories, C++ language standard, and even the different build settings can be configured through this section. 
# Usage