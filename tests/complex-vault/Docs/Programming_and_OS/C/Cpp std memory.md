---
summary: The cpp standard library covering high level memory management tools.
headings:
  - "[[#Concepts of Note]]"
type: note/library
functions:
  - "[[Cpp std memory addressof]]"
  - "[[Cpp std memory align]]"
  - "[[Cpp std memory allocate_shared]]"
  - "[[Cpp std memory const_pointer_cast]]"
  - "[[Cpp std memory declare_no_pointers]]"
  - "[[Cpp std memory declare_reachable]]"
  - "[[Cpp std memory dynamic_pointer_cast]]"
  - "[[Cpp std memory get_deleter]]"
  - "[[Cpp std memory get_pointer_safety]]"
  - "[[Cpp std memory get_temporary_buffer]]"
  - "[[Cpp std memory make_shared]]"
  - "[[Cpp std memory make_unique]]"
  - "[[Cpp std memory return_temporary_buffer]]"
  - "[[Cpp std memory static_pointer_cast]]"
  - "[[Cpp std memory undeclare_no_pointers]]"
  - "[[Cpp std memory undeclare_reachable]]"
  - "[[Cpp std memory uninitialized_copy_n]]"
  - "[[Cpp std memory uninitialized_copy]]"
  - "[[Cpp std memory uninitialized_fill_n]]"
classes:
  - "[[Cpp std memory allocater_arg_t]]"
  - "[[Cpp std memory allocator_traits]]"
  - "[[Cpp std memory auto_ptr_ref]]"
  - "[[Cpp std memory auto_ptr]]"
  - "[[Cpp std memory bad_weak_ptr]]"
  - "[[Cpp std memory default_delete]]"
  - "[[Cpp std memory enable_shared_from_this]]"
  - "[[Cpp std memory get_pointer_safety]]"
  - "[[Cpp std memory owner_less]]"
  - "[[Cpp std memory pointer_traits]]"
  - "[[Cpp std memory shared_ptr]]"
  - "[[Cpp std memory unique_ptr]]"
  - "[[Cpp std memory weak_ptr]]"
  - "[[Cpp std memory memory_order]]"
  - "[[Cpp fstream ifstream]]"
date created: Tuesday, November 26th 2024, 2:22:53 pm
date modified: Thursday, October 2nd 2025, 1:12:44 pm
library_of:
  - "[[Cpp Memory]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
[Standard library header \<memory\> - cppreference.com](https://en.cppreference.com/w/cpp/header/memory)

Issues with normal pointers
- Memory leaks = memory is allocated but never freed with delete
- Dangling pointers = pointer to de-allocated memory.
- Wild Pointers = Pointers that are declared and allocated in memory, but never initialized
- Data Inconsistency = When some data is stored in memory but is not updated in a consistent manner.
- Buffer Overflow = When a pointer is used to write a memory address that is outside of the allocated memory block. Leads to data corruption which hackers can attack.


