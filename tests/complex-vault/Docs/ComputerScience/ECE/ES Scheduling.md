---
type: note
---
- When there are fewer processors than tasks (usually the case) or when the tasks must be performed at a particular time, a **scheduler must intervene**. 
- **Real-time systems** = collections of tasks where in addition to any ordering constraints imposed by the precedences between the tasks, there are also timing constraints. 
	- Typically, tasks have deadlines. 
	- Real-time programs can have all manner of timing constraints, not just deadlines
# Basics of Scheduling
## Scheduling Decisions
- **Scheduling decision** = a decision to execute a task, and has three parts
	- **assignment** = which processor should execute the task
	- **ordering** = in what order each processor should execute its tasks
	- **timing** the time at which each task executes
	- These decisions can be made at design time, or at run time (execution of the program)
- **Fully-static scheduler** = A scheduler that makes all decisions at design time. Typically does not need semaphores or locks, but can use timing to enforce mutual exclusion and precedence constraints.
- **Static order scheduler** = Performs task assignment and ordering at design time, but defers until run time the decision of when in physical time to execute a task. 
	- That decision may be affected by whether a mutual exclusion lock can be acquired, or whether precedence constraints have been satisfied. 
	- A task may block on a semaphore or a lock, in which case it blocks the entire sequence of tasks on that processor. A static order scheduler is often called an **off-line scheduler**
- **Static assignment scedulerr** = performs assignment at design time, and everything else at run time. Each processor is given a set of tasks to execute, and a run-time scheduler decides during execution what task to execute next
- **Fully dynamic scheduler** = Performs all decisions at run time. When a processor becomes available, the scheduler makes a decision at that point about what task to execute next on the processor, (both static and fully-dynamic schedulers are often called **on-line schedulers**).
- **Preemptive scheduler** = May make a scheduling decision during the execution of a task, assigning a new task to the same processor. A task may be in the middle of executing when the scheduler decides to stop that execution and begin the execution of another task. The interruption of the first task is called a preemption. 
## Task Models
- **Task model** = set of assumptions about the tasks that the scheduler makes about the structure of the program or tasks
	- Some schedulers assume that all tasks to be executed are known before scheduling begins, and other support arrival of tasks. 
	- Some schedulers support scenarios where each task $\tau \in T$ executes repeatedly, possibly forever, and possibly periodically.
- **Arrival of tasks** = Tasks become known to the scheduler as other tasks are being executed. 
- **Sporadic** = A task that repeats, with irregular timing, but there is a lower bound on time between task executions. 
- **Precedence Constraints** = A requirement that one execution precedes another. If execution $i$ must precede $j$, we can write $i < j$. $i$ and $j$ may be distinct executions of the same task, or executions of different tasks
- **Preconditions** = Conditions that must be satisfied before the task can execute. 
	- Availability for a lock can be a precondition
- **Enabled** = When preconditions are satisfied for a task, a task is said to be enabled.

### Terms in figure below
![[Pasted image 20230817132405.png]]
####  Task Executions
$\tau$

#### Release time 
$r_i$
a.k.a Arrival time
Earliest time at which a task is enabled
$s_i \geq r_i$ 
#### Start Time
$s_i$ 
Start Time at which execution actually starts
Required that:  $s_i \geq r_i$ 
#### Finish Time
$f_i$
Time at which the task completes execution
Required that: $f_i \geq s_i$ 
#### Response Time
$o_i$
$o_i = f_i - r_i$
Time that elapses between when the task is first enabled and when it completes execution

#### Execution Time
$e_i$ 
Total time that the task is actually executing. Does not include any time that the task may be blocked or preempted.
- Many schedulers assume that the task time is known and fixed, even though this is commonly untrue. 
- If the execution time is variable, it is common to assume that the worst-case execution time (WCET) is known.
#### Deadline
$d_i$
Time by which a task must be completed. 
- **Hard deadline** = A real physical constraint imposed by the application, where missing the deadline is considered an error.
- **Soft real-time scheduling** = scheduling when it's better to meat a deadline, but missing the deadline is not an error.
### Other Terms
A scheduler may use priority rather than (or in addition to) a deadline. This assumes each task is assigned a number called a priority, and the scheduler will always choose to execute he task with the highest priority. 

**Fixed priority** = A priority that remains constant over all the executions of a task
**Dynamic Priority** = allowed to change during execution. 

**preemptive priority-based scheduler** = a scheduler that supports arrivals of tasks and at all times is executing the enabled task with the highest priority
**non-preemptive priority-based scheduler** = A scheduler that uses priorities to determine which task to execute next after the current task execution completes, but never interrupts a task during execution to schedule another task

## Comparing Schedulers
**Feasible Schedule** = a schedule that accomplishes the goal to have all task executions meet their deadlines. $(f_i \leq d_i)$ 
**Optimal wrt feasibility** = a scheduler that yields a feasible schedule for any task set for which there is a feasible scheduler.


**Utilization** = The percentage of time that the processor spends executing tasks vs being idle

**Lateness** = A criterion used to compare schedulers, where the maximum lateness is defined for a set of task executions $T$ such that:
- $L_{max} = \underset{i\in T} {max}(f_i - d_i)$ 
- For a feasible schedule, this number is either zero or negative. 
- Maximum lateness can also be used to compare infeasible schedules. For soft real-time problems, this may be tolerable for this number to be positive, as long as it does not get too large.
**Total Completion Time (a.k.a. makespan)** = Performance goal rather than a real-time requirement. Defined by:
$M= \underset{i\in T}{max}f_i - \underset{i\in T}{min}r_i$ 
## Implementation of a Scheduler
- A run-time scheduler will typically implement tasks such as threads. Sometimes the scheduler assumes these threads complete in finite time, and sometimes it makes no such assumption. In either case, the scheduler is a procedure that gets invoked at certain times. For each simple, non-preemptive schedulers, the scheduling procedure may be invoked at each time when a task completes. 
- For preemptive schedulers, the scheduling procedure is invoked when any of several things occur:
	- A timer interrupt occurs, for example at a jiffy interval
	- An I/O interrupt occurs
	- An OS service is invoked
	- A task attempts to acquire a mutex
	- A task tests a semaphore
# Rate Monotonic Scheduling
Consider a scenario with $T = \{\tau_1, \tau_2, \cdots, \tau_n\}$ where the tasks execute periodically.
- We assume that each task $\tau_i$ must execute  in completion for once in each time interval $p_i$. 
	- $p_i$ = the period of the task
- Therefore, the deadline for the $j$-th execution of $\tau_i$ is $r_{i,1} + jp_i$ , where $r_{i,1}$ is the release time of the first execution. 
**RM (rate monotonic)** = Preemptive strategy optimal with respect to feasibility among fixed priority schedulers. It gives priority to a task with a smaller period.  

## An example:
- The simplest form of the problem has just two tasks $T = \{\tau_1, \tau_2 \}$ with execution times $e_1$ and $e_2$ and periods $p_1$ and $p_2$. Execution time of $e_2$ of task $\tau_2$ is longer than the period $p_1$ of task $\tau_1$. Thus, if these two tasks are not to execute on the same processor, it is clear that a non-preemptive scheduler will not yield a feasible schedule. If task $\tau_2$ must execute to completion without interruption, then task $\tau_1$ will miss some deadlines. 
- A preemptive schedule that follows the RM model will give $\tau_1$ higher priority because it's period is smaller. The schedule is feasible, whereas if $\tau_2$ had been given higher priority, then the schedule would not be feasible. 
- ![[Pasted image 20230817150114.png]]
	- This figure assumes that the time it takes to perform the preemption, called the **context switch time** is negligible. This is an assumption that is problematic in practice, as a context switch on processors with caches often causes substantial cache-related delays.
- It turns out that RM Schedulers cannot always achieve 100% utilization. In particular, RM Schedulers are constrained to have fixed priority.
	- This effect is bounded. If $\mu$ is less than or equal to a utilization bound given by:
		- $\mu \leq n(2^{1/n} -1 )$ 
			- Then the RM schedule is feasible. 
			- $n$ = number of tasks
	- As $n$ gets large, the utilization bound approaches $ln(2) \approx 0.693$ 
	- **This means that if a task set with any number of tasks does not attempt to use more than 69.3% of the available processor time, then the RM schedule will meet all deadlines**

# Earliest Deadline First
Given a finite set of non-repeating tasks with deadlines and no precedence constraints, a simple scheduling algorithm is earliest due date (EDD), also known as Jackson's algorithm. This minimizes the maximum lateness, compared to all other orderings of the tasks. 

- EDD is optimal with respect to feasibility, because it minimizes the maximum lateness.
- Does not support arrival of tasks, and hence does not support periodic or repeated execution of tasks. EDD is easily extended to support these yielding what is known as **EDF (earliest deadline first) (a.k.a. Horn's Algorithm)** 
	- A dynamic priority scheduling algorithm. If a task is repeatedly executed, it may be assigned a different priority on each execution. This can make it more complex to implement. 
- More expensive to implement than RM, but it generally has superior performance. RM is optimal wrt feasibility only among fixed priority schedulers. EDF is optimal wrt feasibility among dynamic priority schedulers. EDF also minimizes the maximum lateness. Any EDF schedule with less than 100% utilization can tolerate increases in execution times and/or reductions in periods and still be feasible. 

## EDF with Precedences
- EDF is optimal (it minimizes maximum lateness) for a task set without precedences. (basically, some tasks need to be executed before other tasks can be started)
- Given a finite set of tasks, precedences between them can be represented by a precedence graph. The EDF is not optimal if there are precedences. 
- Lawler's algorithm (LDF=Last Deadline First) solves this, choosing the last task to execute (the onewith no other dependencies), and then it works backward to choose the task.
	- LDF is optimal in minimizing maximum lateness, and is also optimal wrt feasibility. Does not support arrival of tasks.
	- A simple modification EDF* supports arrivals and minimizes the maximal lateness.

# Scheduling and Mutual Exclusion
Algorithms given so far are conceptually simple, but often have surprising side effects. This is especially true when tasks share resources and use mutual exclusion to guard access to those resources.
## Priority Inversion
In principle, a priority-based preemptive scheduler is executing at all times the high-priority enabled task. When using mutual exclusion, it is possible for a task to become blocked during execution. If the scheduling algorithm does not account for this possibility, serious problems can occur.
**Priority Inversion** = A scheduling anomaly where a high-priority task is blocked while unrelated lower-priority tasks are executing. 
## Priority Inheritance Protocol
- Solution to priority inversion
- When a task blocks attempting to acquire a lock, then the task that holds the lock inherits the priority of the blocked task. Thus, the task that holds the lock cannot be preempted by a task with lower priority than the one attempting to acquire the lock. 
- ![[Pasted image 20230817161007.png]]
## Priority Ceiling Protocol
- Priorities can interact with mutual exclusion locks in even more interesting ways. Priorities can be used to prevent certain kinds of deadlocks.
- **Priority ceiling protocol** = every lock or semaphore is assigned a priority ceiling equal to the priority of the highest-priority task that can lock it. A task $\tau$ can acquire a lock $a$ only if the task's priority is strictly higher than the priority ceilings of all locks currently held by other tasks. Intuitively, if we prevent task $\tau$ from acquiring lock $a$, then we ensure task $\tau$ will not hold lock $a$ while later trying to acquire other locks held by other tasks. 

# Multiprocessor Scheduling
- **Hu level scheduling** = An algorithm that assigns a priority to each task $\tau$ based on the **level**, which is the greatest sum of execution times of tasks on a path in the precedence graph from $\tau$ to another task with no dependents. Tasks with larger levels have higher priority thank tasks with smaller levels.
- **Critical Path** = Scheduling methods that emphasize the path through the precedence graph with the greatest total execution time. 
## Scheduling Anomalies
- **Priority inversion**
- **Deadlock** = The lower priority task starts first, and acquires lock $a$, then gets preempted by the higher priority task, which acquires lock $b$ and then blocks trying to acquire lock $a$. The lower priority task then blocks trying to acquire lock $b$, and no further progress is possible
	- ![[Pasted image 20230817161740.png]]
- **Richard's Anomalies**
	- Multiprocessor schedules are **non-montonic** (improvements in performance at a local level can result in degradations in performance at a global level)
	- **Brittle** = small changes can have big consequences
- If a task set with fixed priorities, execution times, and precedence constraints is scheduled on a fixed number of processors in accordance with the priorities, then increasing the number of processors, reducing execution times, or weakening precedence constraints can increase the schedule length. 