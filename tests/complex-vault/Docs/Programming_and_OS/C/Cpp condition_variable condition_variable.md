---
summary: Used with std::mutex to block one or more threads until another thread modifies a shared variable (the condition) and notifies the condition_variable.
type: note/class
headings:
similar:
  - "[[Cpp std mutex (library)]]"
class_of:
  - "[[Cpp condition_variable]]"
date created: Tuesday, November 26th 2024, 2:36:29 pm
date modified: Wednesday, March 25th 2026, 1:45:02 pm
tags: []
template:
template-version:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`
The thread that intends to modify the shared variable must:
1. Acquire a [std::mutex](https://en.cppreference.com/w/cpp/thread/mutex "cpp/thread/mutex") (typically via [std::lock_guard](https://en.cppreference.com/w/cpp/thread/lock_guard "cpp/thread/lock guard")).
2. Modify the shared variable while the lock is owned.
3. Call [notify_one](https://en.cppreference.com/w/cpp/thread/condition_variable/notify_one "cpp/thread/condition variable/notify one") or [notify_all](https://en.cppreference.com/w/cpp/thread/condition_variable/notify_all "cpp/thread/condition variable/notify all") on the `std::condition_variable` (can be done after releasing the lock).

# Additional Background

## Concepts of Note

### Spurious Wakeups
󰙎 spurious wakeup ;;; a thread waking from `wait()` without being notified — always use the predicate overload to guard against this

### Waiting Thread Protocol
The thread waiting on the condition must:
1. Acquire `std::unique_lock<std::mutex>` (not `lock_guard` — `wait()` must be able to atomically release and reacquire)
2. Call `cv.wait(lock, pred)` — releases lock and suspends atomically; reacquires lock on wakeup
3. Predicate re-evaluated on each wakeup; blocks again if false

## Properties

### Methods

##### wait
 `cv.wait(lk)` ;;; atomically releases `lk` and blocks; reacquires on notify — spurious wakeups possible
 `cv.wait(lk, pred)` ;;; equivalent to `while (!pred()) wait(lk);` — preferred; immune to spurious wakeups

##### wait_for / wait_until
 `cv.wait_for(lk, rel_time, pred)` ;;; blocks until `pred()` true or duration elapses; returns `pred()` result
 `cv.wait_until(lk, abs_time, pred)` ;;; blocks until `pred()` true or absolute time; returns `pred()` result

##### notify_one / notify_all
 `cv.notify_one()` ;;; unblocks one waiting thread (arbitrary selection)
 `cv.notify_all()` ;;; unblocks all waiting threads; use when multiple threads may proceed

## Usage

### Producer / Consumer Pattern
Notifier side:
 `{ std::lock_guard<std::mutex> lk(m); data_ready = true; } cv.notify_one();` ;;; set flag under lock, notify outside lock

Waiter side:
 `std::unique_lock<std::mutex> lk(m); cv.wait(lk, []{ return data_ready; });` ;;; blocks until `data_ready` true; predicate guards spurious wakeups

### condition_variable_any
󰙎 `std::condition_variable_any` ;;; variant accepting any `BasicLockable` (not only `std::unique_lock<std::mutex>`); slightly more overhead — see [[Cpp std concurrency support library]]

# Media
<iframe src="https://en.cppreference.com/w/cpp/thread/condition_variable" style="width: 100%; height: 1000px;"></iframe>