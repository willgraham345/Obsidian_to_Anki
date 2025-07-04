---
summary: Mutual exclusion primitive useful for protecting shared data. Blocks threads waiting for the lock to be come available. Created using a `new` constructor. Each mutex has a type parameter representing the data that it protects. Data can only be accessed through the RAII guards returned from `lock` and `try_lock`.
headings: ["[[#Concepts of Note]]", "[[#Methods]]"]
type: note/class
methods: ["[[#`lock`]]", "[[#`try_lock`]]"]
date created: Tuesday, April 8th 2025, 12:09:10 pm
date modified: Thursday, May 22nd 2025, 10:18:00 am
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- [p] `let my_var = Mutex::new(0)` = Creates a mutex protecting an `i32` = #code/rust/sync/mutex
<!--ID: 1751434090185-->

- [p] `my_mutex.lock()` = Attempts to acquire lock, and will return a `Result<MutexGuard<T>, PoisonError<;mutexGuard<T>>>`. Success will return the guard, failure will return a poison
- [p] `my_mutex.try_lock()` = Attempts to acquire lock without blocking, and will return a `Result<MutexGuard<T>,TryLockError>`. Success will return the guard, failure will return a poison
- [I] Poisoned mutex = A mutex where the thread holding the lock panics. The mutex is then considered "poisoned" as it can indicate potential inconsistent data. 
- A `MutexGuard<'a, T>` is the smart pointer returned by `.lock()`. It dereferences to `T` (or `&mut T`) allowing access to the protected data. Holds the lock for a lifetime.lo

### Poisoning
- A mutex is considered poisoned whenever a thread panics while holding the mutex. Once a mutex is poisoned, all other threads are unable to access the data by default as it is likely tainted.
- `lock` and `try_lock` return a `Result` indicating if a mutex is poisoned or not

## Methods
### `lock`
### `try_lock`