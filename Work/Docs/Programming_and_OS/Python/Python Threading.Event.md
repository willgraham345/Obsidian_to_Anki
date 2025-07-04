---
tags: note/python
type: note
---
# Background
One of the simplest mechanisms for communications between threads. One thread signals an event, and other threads wait for it. 

An event object manages an internal flag that can be set to true with the `set()` method, and reset to false with the `clear()` method. The `wait()` method blocks until the thread is true. 


# Usage

| Function/Method | Description |
| ---- | ---- |
| `Event()` | Instantiates a new event object. |
| `Event().wait(timeout)` | Blocks the thread until the internal thread is true. Blocked until another thread calls `.set()`, or until the optional timeout. |
| `Event().set()` | Sets the event, allowing other threads to use the computing. Lets other flags use the computing.   |
| `Event().clear()` | Opposite of `.set()`, makes the event unset. Threads waiting for it will block until it is set again. |
| `Event().is_set()` | Returns `True` if the event is set, `False` otherwise. |

Scenarios where you'd use `clear()`
1. Synchronization
2. Control flow
3. Resource management