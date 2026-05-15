---
type: note
---
A thread is an execution context managed by the OS. The normal execution contexts for an embedded system running on bare metal are the main function execution and interrupt handlers. Threads have more in common with the main function than with interrupts, and typically run forever in a loop, and don't preempt the system in reaction to some event. 

In Zephyr, the structure that represents a thread is a `k_thread`


## Properties of a thread
Stack area 
- Region of memory used for the thread's stack. Size can be tailored to needs, and special macros exist to create and work with stack memory regions
Thread Control Block
- Kernel bookkeeping of the thread's metadata. Instance of type `k_thread`
Entry Point Function
- Invoked when the thread is started. Up to 3 argument values can be passed to the function. 
Scheduling Priority
- Instructs the kernel's scheduler how to allocate CPU time to the thread. 
Thread Options
- Allow the thread to receive special treatment by the kernel under specific circumstances
Start Delay
- Specifies how long the kernel should wait before starting the thread.
Execution mode
- Can either be supervisor or user mode. By default, threads run in supervisor mode and allow access to privileged CPU instructions, entire memory address space, and peripherals. Users threads have less privileges. 

## Lifecycle
A thread must be created before it can be used. 
- A start delay can be configured to start thread execution immediately. 
