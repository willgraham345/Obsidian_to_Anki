---
type: note
implementations:
  - "[[Cpp Class static members and methods]]"
  - "[[Cpp.memory.static_pointer_cast]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, November 22nd 2024, 3:44:22 pm
---
# Background
- Static variables exist for the "lifetime" of the translation unit it is defined in
	- If in a namespace scope, then it can't be accessed from any other translation unit. 
