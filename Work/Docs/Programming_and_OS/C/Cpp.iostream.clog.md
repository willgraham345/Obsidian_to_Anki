---
type: note
---
# Background
- Object of class [[Cpp ostream]] that represents the standard logging stream oriented to narrow characters (type `char`)
- Corresponds with [[Cpp iostream cerr]] to the C stream [[Cpp iostream cerr]]
- The standard logging stream is a destination of characters determined by the environment. 
	- The destination may be shared by more than one standard object ([[Cpp iostream cerr]] and [[Cpp cout]])
- An object of class [[Cpp ostream]] characters can be written using the insertion operator (`<<`) or as unformatted data
- By default, clog is synchronized with [[Cpp.stdio.stderr]]

# Usage