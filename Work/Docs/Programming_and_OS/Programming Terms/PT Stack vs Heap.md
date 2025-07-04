---
summary: Both are parts of the applications memory footprint in RAM, alongside machine code. Heap holds all global variables, allocated randomly by the programmer with fractured and "unsafe" memory. The stack is temporary memory allocation where data members are accessible only if the `method()` that contained them is currently running. The stack is linear, while the heap is hierarchical.
type: note/concept
concept_of:
  - "[[Cpp Runtime Allocation]]"
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Wednesday, January 8th 2025, 4:38:23 pm
headings:
  - "[[#Concepts of Note]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`
# Additional Background
## Concepts of Note
- [I] Call stack = part of the stack responsible for function and method control. Function calls add functions to the top of the stack, which return control to the caller of the function. `main()` (or its equivalent) is at the bottom of the stack. ^0eb195

### Stack
- Allocations done by compiler, sizes must be known at compile time. 
- Temporary memory allocation scheme where data members are accessible only if the `method()` that contained them is currently running
	- Stack memory allocation is considered safer as compared to heap memory allocation because data stored can only be accessed by the owner thread.
	- Less storage space than heap-memory
- Linear data structure
- Limited fixed size
- Keeps track of the call stack. 

### Heap
- All global variables are stored in heap
	- Every time we make an object, it creates it in heap-space and the referencing information is always stored in stack-memory.
- Use for anything that will outlive things on the [[#^0eb195|call stack]]
- Allocated randomly by programmer
- Not safe, seen by all threads (memory leak)
- Hierarchical data structure
- Less organized
	- Memory gets fragmented as blocks of memory is allocated and deallocated

## Example
### Only Heap
```cpp
int main()
{
// This memory for 10 integers
// is allocated on heap.
int *ptr = new int[10];
}
```

## Only Stack
```cpp
#include <iostream>
using namespace std;
int main()
{
	int a = 10; // stored in stack
	int* p = new int(); // allocate memory in heap
	*p = 10;
	delete (p);
	p = new int[4]; // array in heap allocation
	delete[] p;
	p = NULL; // free heap
	return 0;
}
```