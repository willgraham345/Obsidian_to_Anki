---
summary: Synchronization primitive used to protect shared data from being accessed by multiple threads simultaneously. Steps include creation, locking, and unlocking.
type: note/class
headings:
  - "[[#Concepts of Note]]"
  - "[[#Media]]"
  - "[[#Usage]]"
similar:
associations:
  - "[[Cpp std lock_guard]]"
  - "[[Cpp std unique_lock]]"
class_of:
  - "[[Cpp std mutex (library)]]"
date created: Friday, February 7th 2025, 12:50:27 pm
date modified: Thursday, March 26th 2026, 2:23:49 pm
library_of:
  - "[[Cpp std]]"
tags: [lang/memory/threading/mutex]
template:
template-version:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note
A calling thread *owns* a mutex from the time it is successfully calls `lock` or `try_lock`

## Usage
  `a.lock()` ;;; Method that attempts to lock the mutex `a`. If another thread has already locked the mutex, this will block indefinitely. 



  `a.try_lock()` ;;; Attempts to lock the mutex `a`, immediately returns if the mutex is not available instead of indefinitely waiting.



  `a.unlock()` ;;; Unlocks the mutex `a` for other threads.

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
