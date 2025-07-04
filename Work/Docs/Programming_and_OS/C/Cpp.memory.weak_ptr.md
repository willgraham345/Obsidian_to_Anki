---
type: note/component
date created: Tuesday, October 8th 2024, 12:53:00 pm
date modified: Thursday, October 10th 2024, 11:15:49 am
---
(summary:: A smart pointer that holds non-owning reference to an object. Managed by a [[Cpp.memory.shared_ptr]], and must be converted to a shared_ptr in order to access the referenced object.)
[similar:: [[Cpp.memory.shared_ptr]] ]

[Why use std::weak\_ptr and what's the difference between this and std::shared\_ptr? : r/cpp\_questions](https://www.reddit.com/r/cpp_questions/comments/qxe9p5/why_use_stdweak_ptr_and_whats_the_difference/)
Can also be used to break reference cycles formed by objects managed by [[Cpp.memory.shared_ptr]]. 

# Usage
 [std weak_ptr - cppreference.com](https://en.cppreference.com/w/cpp/memory/weak_ptr)

## Ownership
- When an object needs to be accessed only if it exists, and if it may be deleted at any time by someone else, the `weak_ptr` is used to track the object, and it is converted to `std::shared_ptr` to acquire temporary ownership.
- The existence of a weak_ptr pointing at some memory will not stop a [[Cpp.memory.shared_ptr]] from deallocating and destroying the objects there.
- weak_ptr is aware of shared ptrs, but does not own the memory.
