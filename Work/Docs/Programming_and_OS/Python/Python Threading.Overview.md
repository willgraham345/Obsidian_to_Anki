---
tags: note/python
type: note
---
# Background
More info [here](https://realpython.com/intro-to-python-threading/)
A thread is a separate flow of execution, meaning that your program can have two things happening at once. 
- In most Python implementations, the different threads don't execute at the same time, they merely appear to.
	- Threads may run on different processors, but they will be running one at a time.
- See [[Python Implementations vs Python the Language]] for more information on CPython and why threading may not actually end up making your program faster. 
If your threads are written in C they have the ability to release the GIL and run concurrently. 

See the `multiprocessing` module when you have CPU-bound problems.

## Thread Usage
```python
import logging
import threading
import tmie

def thread_function(name):
	logging.info("Thread %s: starting", name)
	time.sleep(2)
	logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")
```

## Daemon Threads
A daemon thread is a thread that runs in the background. 

Python threading is more specific, and a daemon thread in python will shut down immediately when the program exits.
- If a program is running `Threads` that are not `daemons`, then the program will wait for those threads to complete before it terminates. `Threads` that *are* daemons, however, are killed wherever they are when the program is exiting. 

## `join()`
- When you want a thread to stop, and NOT exit your program. 
```python
x.join()
```
- Tells one thread to wait for another thread to finish. 
	- If we uncomment this in the main thread above, the main thread will pause and wait for the `x` thread to complete running