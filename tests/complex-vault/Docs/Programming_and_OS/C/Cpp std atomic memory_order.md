---
summary: Class specifying how memory accesses (including non-atomic accesses) are to be ordered around an operation.
headings: ["[[#Concepts of Note]]"]
type: note/class/enum
date created: Thursday, October 2nd 2025, 1:14:23 pm
date modified: Thursday, October 2nd 2025, 1:17:49 pm
---

# Summary

`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note

### Constants
|Name|Meaning|
|---|---|
|`memory_order_relaxed`|Relaxed operation: there are no synchronization or ordering constraints imposed on other reads or writes, only this operation's atomicity is guaranteed (see [Relaxed ordering](https://en.cppreference.com/w/cpp/atomic/memory_order.html#Relaxed_ordering) below).|
|`memory_order_consume`  <br>(deprecated in C++26)|A load operation with this memory order performs a _consume operation_ on the affected memory location: no reads or writes in the current thread dependent on the value currently loaded can be reordered before this load. Writes to data-dependent variables in other threads that release the same atomic variable are visible in the current thread. On most platforms, this affects compiler optimizations only (see [Release-Consume ordering](https://en.cppreference.com/w/cpp/atomic/memory_order.html#Release-Consume_ordering) below).|
|`memory_order_acquire`|A load operation with this memory order performs the _acquire operation_ on the affected memory location: no reads or writes in the current thread can be reordered before this load. All writes in other threads that release the same atomic variable are visible in the current thread (see [Release-Acquire ordering](https://en.cppreference.com/w/cpp/atomic/memory_order.html#Release-Acquire_ordering) below).|
|`memory_order_release`|A store operation with this memory order performs the _release operation_: no reads or writes in the current thread can be reordered after this store. All writes in the current thread are visible in other threads that acquire the same atomic variable (see [Release-Acquire ordering](https://en.cppreference.com/w/cpp/atomic/memory_order.html#Release-Acquire_ordering) below) and writes that carry a dependency into the atomic variable become visible in other threads that consume the same atomic (see [Release-Consume ordering](https://en.cppreference.com/w/cpp/atomic/memory_order.html#Release-Consume_ordering) below).|
|`memory_order_acq_rel`|A read-modify-write operation with this memory order is both an _acquire operation_ and a _release operation_. No memory reads or writes in the current thread can be reordered before the load, nor after the store. All writes in other threads that release the same atomic variable are visible before the modification and the modification is visible in other threads that acquire the same atomic variable.|
|`memory_order_seq_cst`|A load operation with this memory order performs an _acquire operation_, a store performs a _release operation_, and read-modify-write performs both an _acquire operation_ and a _release operation_, plus a single total order exists in which all threads observe all modifications in the same order (see [Sequentially-consistent ordering](https://en.cppreference.com/w/cpp/atomic/memory_order.html#Sequentially-consistent_ordering) below).|
