---
company: Varex
tags: archive_deprecated/Varex
---
# Folder Structure
`docs/`
- Uses Doxygen
	- Doxygen will make nice lil graphs for you, and it's amazing. 
	- We use Javadoc as the format 
	- You'll get a build fail if you don't document the code. 
	- Can be run locally, or on Jenkins
- Documentation for the component that is not part of the overview
	- Summaries, diagrams, stuff like that. 
	- `mainpage.dox`
	- There are cool macros you can use within it. 
`doxygen/`
`inc/`
- Include statements you want other components to have access to
- When compiler goes through code, it keeps track of all the functions and variables. 
	- In C++, you can have two methods or two functions that have different parameters. The C++ compiler turns all the variables and encodes extra parameter set into the variable. 
	- `SymbolLookup.h` demangles the names back into English
	- `ErrorLookup.h`
		- APIs can turn error codes into strings
- I think its headers?
`src/`
- Where you put `.cpp` files
- You can put `.h` files here, but only if you don't intend for this to be included in something else. 
`test/`
- Where all the unit tests go
- These tests use GoogleTest for the testing platform, and typically use Doxygen-style comments for it. 