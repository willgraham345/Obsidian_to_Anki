---
summary: Synchronization primitive used to protect shared data from being accessed by multiple threads simultaneously. Steps include creation, locking, and unlocking.
headings: ["[[#Concepts of Note]]", "[[#Media]]", "[[#Usage]]"]
type: note/class
similar: 
associations: ["[[Cpp std lock_guard]]"]
class_of: ["[[Cpp std mutex (library)]]"]
date created: Friday, February 7th 2025, 12:50:27 pm
date modified: Tuesday, June 17th 2025, 12:53:53 pm
library_used_in: ["[[Cpp std]]"]
tags: [code/cpp/multithreading/mutex]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note
A calling thread *owns* a mutex from the time it is succesfully calls either `lock` or `try_lock`

## Usage
- [p] `<mutexName>.lock()` = Method that locks the mutex. If another thread has already locked the mutex, a call to lock will block until lock is acquired = #code/cpp/multithreading/mutex
<!--ID: 1751434091572-->

- [p] `<mutexName>.try_lock()` = Tries to lock the mutex, returns if the mutex is not available. = #code/cpp/multithreading/mutex 
<!--ID: 1751434091576-->

- [p] `<mutexName>.unlock()` = Unlocks the mutex = #code/cpp/multithreading/mutex 
<!--ID: 1751434091580-->


### Typical workflow:
```
std::mutex mut;

void threadFn(void* arg){
	// 1. Lock the resource
	mut.lock();
	// 2. Access the resource
	doStuff();
	// 3. Unlock the resource
	mut.unlock();
}
```

## Media
[std::mutex - cppreference.com](https://en.cppreference.com/w/cpp/thread/mutex)
