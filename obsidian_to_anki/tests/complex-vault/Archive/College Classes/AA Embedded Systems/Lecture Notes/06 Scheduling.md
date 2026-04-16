# Prelab Work
## Book Reading
### 6.1
Not uncommonly, performance optimization is irrelevant by the time the product ships. When in doubt, use brute force.
#### 6.1.1 Performance Metrics
Capacity = a consistent measure of a service's size or amount of resources
Utilization = percent of capacity of a resource that is used for some given workload of request

A processor might be utilized 10% for the duration of some workload. 

Latency = delay between a change at the input to a system and the corresponding change at its output. 
Latency of a pipeline with stages A and B is greater than or equal to the sum of the latencies for each stage in the pipeline. 
Throughput = measure of the rate of useful work done by a service for some given workload of requests
- For a camera, we might care about how many frames per second the system can process
#### 6.1.2 Systems Approach to Designing for Performance
Diminishing returns often happen when engineers hyper-focus on one specific element of a process.

Iterative approach for designing for performance:
1. Measure the system to ﬁnd out whether or not a performance enhancement is needed. If performance is a problem, identify which aspect of performance (throughput or latency) is the problem. For multistage pipelines in which stages process requests concurrently, there is no direct relationship between latency and throughput, so improving latency and improving throughput might require different techniques.
2. Measure again, this time to identify the performance bottleneck. The bottleneck may not be in the place the designer expected and may shift from one design iteration to another.
3. Predict the impact of the proposed performance enhancement with a simple back-of-the-envelope model. (We introduce a few simple models in this chap- ter.) This prediction includes determining where the next bottleneck will be. A quick way to determine the next bottleneck is to unrealistically assume that the planned performance enhancement will remove the current bottleneck and result in a stage with zero latency and inﬁnite throughput. Under this assump- tion, determine the next bottleneck and calculate its performance.This calcula- tion will result in one of two conclusions:
	1. Removing the current bottleneck doesn’t improve system performance signiﬁcantly. In this case, stop iterating, and reconsider the whole design or revisit the requirements. Perhaps the designer can adjust the interfaces between stages with the goal of tolerating costly operations. We will discuss several approaches in the next sections.
	2. Removing the current bottleneck is likely to improve the system performance. In this case, focus attention on the bottleneck stage. Consider brute-force methods of relieving the bottleneck stage (e.g., add more memory). Taking advantage of the $\dfrac{d(technology)}{dt}$ may be less expensive than being clever. If brute-force methods won’t relieve the bottleneck, be smart. For example, try to exploit properties of the workload or ﬁnd better algorithms.
4. Measure the new implementation to verify that the change has the predicted impact. If not, revisit steps 1–3 and determine what went wrong.
5. Iterate. Repeat steps 1–5 until the performance meets the required level.

$AverageLatency = Frequency_{fast} \times Latency_{fast} \times Frequency_{slow} \times Latency_{slow}$

### 6.3 
## Zephyr Documentation
### Concepts
The scheduler determines which thread is allowed to execute at any point in time; this thread is known as the current thread
Reschedule points = various points when the scheduler is given an opportunity to change the identity of the current thread. 
- Examples
A thread sleeps when it voluntarily initiates an operation that transitions itself to a suspended or waiting state
### Scheduling Algorithm
When multiple ready threads of the same priority exist, the scheduler chooses the one that has been waiting the longest.
- earliest-deadline-first scheduling is available.
	- `k_thread_deadline_set()` is used to set a thread's deadline.
#### Options for deadline
- Simple linked-list ready queue ([`CONFIG_SCHED_DUMB`](https://docs.zephyrproject.org/2.7.5/reference/kconfig/CONFIG_SCHED_DUMB.html#std-kconfig-CONFIG_SCHED_DUMB))
    The scheduler ready queue will be implemented as a simple unordered list, with very fast constant time performance for single threads and very low code size. This implementation should be selected on systems with constrained code size that will never see more than a small number (3, maybe) of runnable threads in the queue at any given time. On most platforms (that are not otherwise using the red/black tree) this results in a savings of ~2k of code size.
- Red/black tree ready queue ([`CONFIG_SCHED_SCALABLE`](https://docs.zephyrproject.org/2.7.5/reference/kconfig/CONFIG_SCHED_SCALABLE.html#std-kconfig-CONFIG_SCHED_SCALABLE))
    The scheduler ready queue will be implemented as a red/black tree. This has rather slower constant-time insertion and removal overhead, and on most platforms (that are not otherwise using the red/black tree somewhere) requires an extra ~2kb of code. The resulting behavior will scale cleanly and quickly into the many thousands of threads.
    Use this for applications needing many concurrent runnable threads (> 20 or so). Most applications won’t need this ready queue implementation.
- Traditional multi-queue ready queue ([`CONFIG_SCHED_MULTIQ`](https://docs.zephyrproject.org/2.7.5/reference/kconfig/CONFIG_SCHED_MULTIQ.html#std-kconfig-CONFIG_SCHED_MULTIQ))
    When selected, the scheduler ready queue will be implemented as the classic/textbook array of lists, one per priority (max 32 priorities).
    This corresponds to the scheduler algorithm used in Zephyr versions prior to 1.12.
    It incurs only a tiny code size overhead vs. the “dumb” scheduler and runs in O(1) time in almost all circumstances with very low constant factor. But it requires a fairly large RAM budget to store those list heads, and the limited features make it incompatible with features like deadline scheduling that need to sort threads more finely, and SMP affinity which need to traverse the list of threads.
    Typical applications with small numbers of runnable threads probably want the DUMB scheduler.

### Cooperative Time Slicing
Once a thread becomes the current thread, it remains the current thread until it performs an action that makes it unready. If a cooperative thread performs lengthy computations, it may cause unacceptable delays in other threads of equal and higher priority threads.
![[Pasted image 20231016112025.png]]
A cooperative thread can voluntarily relinquish CPU to permit the CPU from time to time to permit other threads to execute. 
- Can be done by:
	- Calling [`k_yield()`](https://docs.zephyrproject.org/2.7.5/reference/kernel/threads/index.html#c.k_yield "k_yield") puts the thread at the back of the scheduler’s prioritized list of ready threads, and then invokes the scheduler. All ready threads whose priority is higher or equal to that of the yielding thread are then allowed to execute before the yielding thread is rescheduled. If no such ready threads exist, the scheduler immediately reschedules the yielding thread without context switching.
	- Calling [`k_sleep()`](https://docs.zephyrproject.org/2.7.5/reference/kernel/threads/index.html#c.k_sleep "k_sleep") makes the thread unready for a specified time period. Ready threads of _all_ priorities are then allowed to execute; however, there is no guarantee that threads whose priority is lower than that of the sleeping thread will actually be scheduled before the sleeping thread becomes ready once again.
### Preemtive Time Slicing
Once a preemtpive thread becomes the current thread, it remains the current thread until a higher priority thread becomes ready, or until the thread performs an action that makes it ready. 

![[Pasted image 20231016112031.png]]
- a preemtive thread can perform cooperative time slicing, or the scheduler's time slicing capability can be used to allow other threads of the same priority to execute.


## Prelab Questions
What are reschedule points?
- Any time a read status changes (ready and non-ready)
- If no one is running, ready
- If someone is running and marked unready?
	- Do we ever go back to the supervisor if the supervisor is not marked ready?
		- No, unless you are running preemptive slicing.
What is the difference between preemptive and cooperative slicing?
Give an example of a hard real-time requirement. What are the consequences of missing the deadline?
- An example of a hard real-time requirement could be anything controls related. In a drone, this would be the attitude controller making sure that the drone is pointed in a way that will keep it flying. If this deadline is missed and the drone becomes unstable, the entire system could be broken and jeopardized. 
Give an example of a soft real-time requirement. What are the consequences of missing the deadline?
- A soft real-time requirement might be an LED display for a system showing current values. While it might affect the latency for the user's awareness, the system isn't put in a risky state if these deadlines are missed. Streaming, VR, and videogames may feel like a hard deadline, but won't fundamentally risk the system. 
How could you use cooperative threads to implement mutually exclusion without the need for a kernel object, such as a semaphore.
- This can be done by calling `k_yield()` and `k_sleep()` at the end of the thread to ensure other threads have an opportunity to execute. There is no guarantee with `k_sleep()` that threads with lower priority will actually be scheduled before the sleeping thread becomes ready again.



# Ashton's Presentation
What causes issues with scheduling?
- Asymmetric or unbalanced nodes
- Additional higher level requirements over transmission of data
- Process limited
	- We could be bound by processing in addition to our network rate
	- What is our minimum bound?
- Latency is how long it takes us to take data in, and push data out
Soft deadline = an annoyance, but someone isn't harmed

Often we'll send a signal back to the producer to make sure that we get data in the correct time

When we're optimizing, we fix the problem child (it'll be obvious once you start going)
- Buffering between sections can cause problems
- Handling ethernet and packet routing can be tough

You can set the systick interrupt
- Default is once every 1 ms (1 kHz)
	- A preemtive thread cannot be interrupted before a systick happens.

What operations put a thread in an unready state?
- Sleep, timeout