---
type: note
---
Parts of the thread's life:

## Thread creation
- Kernel initializes the thread control blocks as well as one end of the stack portion. The remainder of the stack is uninitialized
- You can specify a delay by setting the start delay to something other than `K_NO_WAIT`

## Thread Termination
Once a thread starts it runs forever. However, it can synchronously end by returning from its entry point function.
- Termination = ending synchronously by return from entry point function

### Thread dependent on other threads
A thread may want to sleep until another thread terminates
- `k_thread_join()` API

## Thread Aborting
Threads can end asynchronously by aborting. 

A thread can be aborted by another thread (or by itself) by calling `k_thread_abort()`


## Thread Suspension
`k_thread_suspend()` can be used to suspend any thread, including the calling thread. 
`k_thread_resume()` will remove the suspension
