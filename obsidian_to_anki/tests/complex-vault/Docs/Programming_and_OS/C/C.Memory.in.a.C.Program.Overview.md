---
type: note
---
# Overview
A typical memory representation of a C program consists of the following sections
![[Pasted image 20230808192910.png]]
## 1. Text segment (i.e. instructions)
- One of the sections of a program in an object file or in memory. As a memory region, a text segment may be placed below the heap or stack in order to prevent heaps and stack overflows from overwriting it. 
- Usually, the text segment is sharable so that only a single copy needs to be in memory for frequently executed programs, such as text editors, the C compiler, the shells, and so on. Also, the text segment is often read-only, to prevent a program from accidentally modifying its instructions.
## 2. Initialized data segment
- Initialized data segment, usually called simply the Data Segment. A data segment is a portion of the virtual address space of a program, which contains the global variables and static variables that are initialized by the programmer.  
- Note that, the data segment is not read-only, since the values of the variables can be altered at run time.  
- This segment can be further classified into the initialized read-only area and the initialized read-write area.  
- For instance, the global string defined by `char s[] = “hello world”` in C and a C statement like `int debug=1` outside the main (i.e. global) would be stored in the initialized read-write area. And a global C statement like `const char* string = “hello world”` makes the string literal `“hello world”` to be stored in the initialized read-only area and the character pointer variable string in the initialized read-write area.  
	- Ex: `static int i = 10` will be stored in the data segment and global `int i = 10` will also be stored in data segment
## 3. Uninitialized data segment
- Uninitialized data segment often called the “**bss**” segment, named after an ancient assembler operator that stood for “**block started by symbol**.” Data in this segment is initialized by the kernel to arithmetic 0 before the program starts executing uninitialized data starts at the end of the data segment and contains all global variables and static variables that are initialized to zero or do not have explicit initialization in source code.  
- For instance, a variable declared static `int i`; would be contained in the BSS segment. 
- For instance, a global variable declared `int j`; would be contained in the BSS segment.
## 4. Stack
- Happens on contiguous blocks of memory, 
- Allocation happens in the function call stack. The size of memory to be allocated is known to the compiler and whenever a function is called, its variables get memory allocated on the stack. Whenever the function call is over, the memory for the variables is de-allocated. This all happens using some predefined routines in the compiler. 
	- Only accessible by the memory 
- A programmer does not have to worry about memory allocation and de-allocation of stack variables. 
- This kind of memory allocation is also known as Temporary memory allocation because as soon as the method finishes its execution all the data belonging to that method flushes out from the stack automatically. This means any value stored in the stack memory scheme is accessible as long as the method hasn’t completed its execution and is currently in a running state.
### Stack Memory Example

```c
int main()
{
// All these variables get memory allocated on stack
int a;
int b[10];
int n = 20;
int c[n];
}
```
## 5. Heap

# Stack vs Heap
|Parameter|STACK|HEAP|
|---|---|---|
|Basic|Memory is allocated in a contiguous block.|Memory is allocated in any random order.|
|Allocation and De-allocation|Automatic by compiler instructions.|Manual by the programmer.|
|Cost|Less|More|
|Implementation|Easy|Hard|
|Access time|Faster|Slower|
|Main Issue|Shortage of memory|Memory fragmentation|
|Locality of reference|Excellent|Adequate|
|Safety|Thread safe, data stored can only be accessed by the owner|Not Thread safe, data stored visible to all threads|
|Flexibility|Fixed-size|Resizing is possible|
|Data type structure|Linear|Hierarchical|
|Preferred|Static memory allocation is preferred in an array.|Heap memory allocation is preferred in the linked list.|
|Size|Small than heap memory.|Larger than stack memory.|