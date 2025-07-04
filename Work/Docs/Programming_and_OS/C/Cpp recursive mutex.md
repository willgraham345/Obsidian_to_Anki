---
summary: Synchronization primitive that can be used to protect shared data from being simultaneously accessed by multiple threads. More information on website
headings: ["[[#Methods of Note]]"]
type: note/class
aliases: []
class_of: ["[[Cpp std mutex (library)]]"]
date created: Friday, February 7th 2025, 12:53:55 pm
date modified: Tuesday, June 17th 2025, 11:36:11 am
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
##  Methods of Note
- A calling thread _owns_ a `recursive_mutex` for a period of time that starts when it successfully calls either [`lock`](https://en.cppreference.com/w/cpp/thread/recursive_mutex/lock "cpp/thread/recursive mutex/lock") or [`try_lock`](https://en.cppreference.com/w/cpp/thread/mutex/try_lock "cpp/thread/mutex/try lock"). During this period, the thread may make additional calls to [`lock`](https://en.cppreference.com/w/cpp/thread/recursive_mutex/lock "cpp/thread/recursive mutex/lock") or [`try_lock`](https://en.cppreference.com/w/cpp/thread/recursive_mutex/try_lock "cpp/thread/recursive mutex/try lock"). The period of ownership ends when the thread makes a matching number of calls to [`unlock`](https://en.cppreference.com/w/cpp/thread/recursive_mutex/unlock "cpp/thread/recursive mutex/unlock").
- When a thread owns a `recursive_mutex`, all other threads will block (for calls to [`lock`](https://en.cppreference.com/w/cpp/thread/recursive_mutex/lock "cpp/thread/recursive mutex/lock")) or receive a false return value (for [`try_lock`](https://en.cppreference.com/w/cpp/thread/recursive_mutex/try_lock "cpp/thread/recursive mutex/try lock")) if they attempt to claim ownership of the `recursive_mutex`.
- The maximum number of times that a `recursive_mutex` may be locked is unspecified, but after that number is reached, calls to [`lock`](https://en.cppreference.com/w/cpp/thread/recursive_mutex/lock "cpp/thread/recursive mutex/lock") will throw [std::system_error](https://en.cppreference.com/w/cpp/error/system_error "cpp/error/system error") and calls to [`try_lock`](https://en.cppreference.com/w/cpp/thread/mutex/try_lock "cpp/thread/mutex/try lock") will return false.
The behavior of a program is undefined if a `recursive_mutex` is destroyed while still owned by some thread. The