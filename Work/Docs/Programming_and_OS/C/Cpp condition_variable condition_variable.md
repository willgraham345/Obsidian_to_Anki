---
summary: Used with std::mutex to block one or more threads until another thread modifies a shared variable (the condition) and notifies the condition_variable.
type: note/class
similar:
  - "[[Cpp std mutex (library)]]"
class_of:
  - "[[Cpp condition_variable]]"
date created: Tuesday, November 26th 2024, 2:36:29 pm
date modified: Tuesday, November 26th 2024, 2:38:16 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`
The thread that intends to modify the shared variable must:
1. Acquire a [std::mutex](https://en.cppreference.com/w/cpp/thread/mutex "cpp/thread/mutex") (typically via [std::lock_guard](https://en.cppreference.com/w/cpp/thread/lock_guard "cpp/thread/lock guard")).
2. Modify the shared variable while the lock is owned.
3. Call [notify_one](https://en.cppreference.com/w/cpp/thread/condition_variable/notify_one "cpp/thread/condition variable/notify one") or [notify_all](https://en.cppreference.com/w/cpp/thread/condition_variable/notify_all "cpp/thread/condition variable/notify all") on the `std::condition_variable` (can be done after releasing the lock).

# Media
<iframe src="https://en.cppreference.com/w/cpp/thread/condition_variable" style="width: 100%; height: 1000px;"></iframe>