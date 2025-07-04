---
type: note
---
Here's a general overview of how a multi-core computer executes multiple threads in parallel:

1. Thread Creation: When a program starts execution, it can create multiple threads. Each thread represents a separate sequence of instructions that can be executed concurrently with other threads. These threads can perform different tasks or work on different parts of the program's workload.
2. Thread Scheduling: The operating system (or the thread scheduler) is responsible for managing the execution of threads on the available cores. It decides which threads to execute on which core and for how long. The thread scheduler aims to achieve efficient utilization of the available cores while ensuring fairness and responsiveness.
3. Core Assignment: The thread scheduler assigns threads to available cores based on scheduling algorithms and priorities. The goal is to distribute the workload evenly among the cores to make the best use of the available processing power.
4. Parallel Execution: Once threads are assigned to cores, each core starts executing the instructions of its assigned thread independently and in parallel with other cores. This allows the multiple threads to progress simultaneously.
5. Communication and Synchronization: In multithreaded applications, threads may need to communicate and share data with each other. Since the cores share the same memory space, threads can read and write data in shared memory locations. However, care must be taken to avoid data races and ensure proper synchronization to prevent conflicts and data corruption.
6. Completion and Joining: Threads can complete their tasks independently. Once a thread finishes its execution, it can return its results or signal the main program that it has completed its task. The main program can then wait for all threads to finish (if required) using thread joining mechanisms before proceeding further.

Note:
It's essential to design multithreaded applications carefully, considering issues like data sharing, synchronization, and load balancing to fully exploit the benefits of parallel execution.