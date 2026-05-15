---
type: note
---
Every thread requires its own stack buffer for the CPU to push context. 

## Kernel-only Stacks
If it is known that a thread will never run in user mode, or the stack is being used for special contexts like handling interrupts, it is best to define the stacks using the `K_KERNEL_STACK` macros

## Thread Stacks

## Thread Priorities
A thread's priority is an integer value, and can either be negative or non-negative. Numerically lower priorities takes precedence over numerically higher values. 

- The scheduler gives thread A of priority 4 higher priority over thread B of priority 7. C with a priority of -2 has higher priority than both thread A and B. 

- A _cooperative thread_ has a negative priority value. Once it becomes the current thread, a cooperative thread remains the current thread until it performs an action that makes it unready.
	- `- NUM_PRIORITIES` to -1
- A _preemptible thread_ has a non-negative priority value. Once it becomes the current thread, a preemptible thread may be supplanted at any time if a cooperative thread, or a preemptible thread of higher or equal priority, becomes ready.
	- 0 to `NUM_PRIORITIES`

### META-IRQ Priorities
There is a special subclass of cooperative priorities at the highest (numerically lowest) end of the priority space. These are scheduled according to their normal priority, but also have the ability to preempt all other threads, even if those threads are cooperative and/or have taken a scheduler lock.k 
- META-IRQ threads can still be interrupted by any hardware interrupt. 