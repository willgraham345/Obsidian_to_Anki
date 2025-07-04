---
type: note
---
a mutually exclusive access around a shared state or resource. Often simply called a `lock`. A mutex is reentrant, which means a thread can take the mutex multiple times (as long as it gives it the same number of times). It also manipulates the priorities of the schedule. It should **NOT** be used in an ISR.


A token that is passed back and forth, more like a talking stick. Generally on or off, like a single-value semaphore. 