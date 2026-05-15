---
summary: Mutual exclusion primitive useful for protecting shared data. Blocks threads waiting for the lock to be come available. Created using a `new` constructor. Each mutex has a type parameter representing the data that it protects. Data can only be accessed through the RAII guards returned from `lock` and `try_lock`.
headings: ["[[#Concepts of Note]]", "[[#Methods]]", "[[#Properties]]", "[[#Usage]]"]
type: note/class
methods: ["[[Rust std sync Mutex#`lock`]]", "[[Rust std sync Mutex#`try_lock`]]"]
date created: Tuesday, April 8th 2025, 12:09:10 pm
date modified: Thursday, November 6th 2025, 2:35:50 pm
item_of: ["[[Rust std sync]]", "[[Rust std]]"]
template:
template-version:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
  `let my_var ``=``Mutex::new(0)` ;;; Creates a mutex protecting an `i32` = #lang/data/sync/mutex 
ID: 1751997628067




󰙎  Poisoned mutex ;;; A mutex where the thread holding the lock panics. The mutex is then considered "poisoned" as it can indicate potential inconsistent data. = #lang/data/sync/mutex 
󰙎  Mutex guard ;;; The smart pointer returned by a `.lock()` call. Dereferences the type `T` (or `&mut T`) by allowing access to the protected data. Can be used to dereference using the `*` operator. = #lang/data/sync/mutex 
<!--ID: 1759154339813-->

### Poisoning
- A mutex is considered poisoned whenever a thread panics while holding the mutex. Once a mutex is poisoned, all other threads are unable to access the data by default as it is likely tainted.
- `lock` and `try_lock` return a `Result` indicating if a mutex is poisoned or not

## Usage

  `*mutex_guard` ;;; "Get past" a `MutexGuard` to modify/read the underlying datatype. #lang/data/sync/mutex 
  `my_mutex.lock()` ;;; Attempts to acquire lock, and will return a `Result<MutexGuard<T>, PoisonError<;mutexGuard<T>>>`. Success will return the guard, failure will return a poison. #lang/data/sync/mutex
  `my_mutex.try_lock()` ;;; Attempts to acquire lock without blocking, and will return a `Result<MutexGuard<T>,TryLockError>`. Success will return the guard, failure will return a poison. = #lang/data/sync/mutex 
<!--ID: 1759154339810-->

## Properties
### Methods
#### `lock`
#### `try_lock`
