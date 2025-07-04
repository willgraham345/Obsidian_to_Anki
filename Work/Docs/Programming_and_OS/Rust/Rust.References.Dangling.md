---
type: note
---
# Background
- In languages with pointers, it is easy to create a dangling pointer (a pointer that references a location in memory that may have been given to someone else)
	- In Rust, the compiler guarantees that references will never be dangling references. 
	- If you have a reference to some data, the compiler will ensure that the data will not go out of scope before the reference to the data does. 
