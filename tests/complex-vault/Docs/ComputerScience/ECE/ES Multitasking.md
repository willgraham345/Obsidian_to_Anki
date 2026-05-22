---
type: note
---
- All reasons for executing multiple sequential programs at once involve timing. 
- ![[Pasted image 20230814145856.png]]
- We've discussed concurrency in a variety of contexts. This chapter will describe mechanisms that are implemented using low-level mechanisms and can provide infrastructure for realizing high-level mechanisms. 
	- These mid-level techniques are called **multitasking**,
- Thee designer constructs a model using a software tool that supports a model of computation. The model is then automatically or semi-automatically translated into a program that uses the mid-level or low-level mechanisms. That process is called **code generation** or **autocoding**
- Mechanisms in this chapter are typically provided by an operating system, a microkernel, or a library of procedures.
# Imperative Programs
- An imperative language is one that expresses a computation as a sequence of operations (C is an imperative language)
- **Observer pattern** = An `update` procedure changes the value of variable `x`. Observers (which are other programs or parts of the program) will be notified whenever `x` is changed by calling a `callback` procedure. 
	- i.e. the value of `x` might be displayed by an observer on the screen. Whenever the value changes, the observer needs to be notified so that it can update the display on the screen. 
- Using extended state machines, we can model the execution of certain simple C programs assuming the programs have a fixed and bounded number of variables. 
- **Linked Lists** = A data structure for storing a list of elements that varies in length during the execution of a program. Each element in the list contains a payload (the value of the element) and a pointer to the next element in the list (or a null pointer if the element is the last one). 
- Accurate models of C programs are often not finite state systems. 
# Threads
- **Threads** = imperative programs that run concurrently and share a memory space. They can access each others' variables. Threads exist in the form of interrupts on almost all microprocessors, even without any OS.
## Creating Threads
- **Pthreadss** or **POSIX threads** is an API wired into many modern operating systems. Defines a set of C programming language types, functions and constants. Standardized by IEEE in 1998 to unify variants of Unix. 
- In POSIX, a thread is defined by a C procedure and created by invoking the `pthread_create` procedure. 
- **start routine** = the procedure that the thread begins executing. 
	- May or may not return. It's quite common to see these not return in embedded applications. 
### Implementing Threads
- The core implementation of threads is a schedule that decides which thread to execute next when a processor is available to execute a thread. 
	- That decision can be based on **fairness**, where the principle is to give every thread an equal opportunity to run based on timing constraints or some other measure. 
		- These algorithms are discussed in Chapter 12.
- **Cooperative multitasking** = Does not interrupt a thread unless the thread itself calls a certain procedure or one of a certain set of procedures. 
	- May intervene whenever any OS system is invoked by the currently executing thread. 
	- Each thread has its own stack, and when the procedure call is made, the return address will be pushed onto the stack. 
- When a program is suspended, the scheduler makes a record of the stack pointer of the currently executing thread, and modifies the stack pointer to point to the stack of the selected thread. 
- **Starved** = When a program executes for a long time without making any operating system calls

# Processes and Message Passing
- **Processes** = Imperative programs with their own memory spaces. These programs cannot refer to each others' variables, and consequently they do not exhibit the same difficulties as threads. Communication between the programs must occur via mechanisms provided by the OS, microkernel, or a library. 
	- Implementation of processes generally requires an MMU (memory management unit). 
- **File System** = A way to create a body of data that is persistent in the sense that it outlives the process that creates it. One process can create data and write to a file, and another process can read from the same file. It is up to the implementation of the file system to ensure that the process reading the data does not read it before it was written. 
- **Message passing** = A flexible mechanism for communicating between processes. ne processes creates a chunk of data, deposits it in a controlled section of memory that is shared, and notifies the other process when that message is ready. 
	- Producer/consumer pattern
		- One thread produces a sequence of messages (a stream)
	- ![[Pasted image 20230816122928.png]]
		- Implementation of the same thing with `pthreads`
			- ![[Pasted image 20230816123107.png]]