---
type: note
---

# Background
![[Pasted image 20240317145941.jpg]]
Method Area
- All class level information like class name, immediate parent class name, methods and variable info. 
- There is only one method area per JVM and it is a shared resource
Heap Area
- Information of all objects is stored in the heap area
- There is also one Heap Area per JVM
- It is also a shared resource
Stack Area
- For every thread, JVM creates one run-time stack which is stored here.
- Every block of this stack is called activation record/stack frame which stores methods calls.
- All local variables of that method are stored in their corresponding frmae
- After a thread terminates, its run-time stack will be destroyed by JVM. 
- Not a shared resource
PC Registers
- Store address of current execution instruction of a thread
- Each thread has separate PC Registers
Native Method Stakcs
- For every thread, a separate native stack is created
- Stores native method information

Method area