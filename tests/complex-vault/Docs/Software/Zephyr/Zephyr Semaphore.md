---
type: note
---
Semaphores are inter-context signaling mechanisms. There are many ways to use them. More like a flag, and used for more than just available and not available. 

Semaphores have a count, which represents the available resources. Typically, semaphores increment or decrement the count. Passing for p, V is release (dutch translation. In the Zephyr OS the operation is `take` and `give`. 

When a process wants access to the resources, it attempts to `take` the resource. If the count is zero, the process will need to wait until a resource is available. If the count is greater than zero, there are available resources, and the count is decremented. When the process is finished with the resource, it gives the resource back, decrementing the counter. 


Critical sections
- A critical section refers to a block of code that must be executed mutually exclusive with other execution contexts that share resources. Critical sections should be as small as possible.
	- While in the critical section, other execution is halted. 
	- Like interrupt handlers, staying in a critical section for too long can **starve** the system. 

Race conditions
- A scenario in which two threads have behavior that depends on the execution order of their code. If a thread can be preempted it can and will be preempted at any point, even in the middle of a line of C code. You should never rely on timing or chance for your code to work. 

Nice weird style trick
```C
k_sem_take(&semaphore, K_FOREVER);
{
	counter = counter + 1;
}
k_sem_give(&semaphore);
```
- Inside and outside of the context of the lock. This is the first class pattern in Python, using `with` blocks to provide a managed context for an open resource. 