---
summary: "Smart pointer that retains ownership of an object through a pointer. Several `shared_ptr` objects may own the same object. The object is destroyed when either of the following happen: The last remaining `shared_ptr` is destroyed. The last remaining shared_ptr owning the object is assigned another pointer with the operator= or reset()"
date created: Tuesday, October 8th 2024, 12:59:59 pm
date modified: Tuesday, November 5th 2024, 5:01:49 pm
type: note/component
---

similar:: [[Cpp.memory.unique_ptr]]

<iframe src="https://www.reddit.com/r/cpp_questions/comments/qxe9p5/why_use_stdweak_ptr_and_whats_the_difference/" style="width: 85%; height: 600px;"></iframe>

# Usage
[std shared\_ptr - cppreference.com](https://en.cppreference.com/w/cpp/memory/shared_ptr)

## Race Conditions
If multiple threads access the same `shared_ptr` object without synchronization and any of those uses a non-`const` member function of shared_ptr then a data race will occur. Use std::atomic<shared_ptr>

## Cleanup
When the last `shared_ptr` is destroyed that one takes responsibility for cleaning up.

