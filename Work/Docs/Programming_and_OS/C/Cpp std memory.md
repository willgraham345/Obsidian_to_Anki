---
summary: The cpp standard library covering high level memory management tools.
type: note/library
classes: ["[[Cpp.memory.allocater_arg_t]]", "[[Cpp.memory.allocator_traits]]", "[[Cpp.memory.auto_ptr_ref]]", "[[Cpp.memory.auto_ptr]]", "[[Cpp.memory.bad_weak_ptr]]", "[[Cpp.memory.default_delete]]", "[[Cpp.memory.enable_shared_from_this]]", "[[Cpp.memory.get_pointer_safety]]", "[[Cpp.memory.owner_less]]", "[[Cpp.memory.pointer_traits]]", "[[Cpp.memory.shared_ptr]]", "[[Cpp.memory.unique_ptr]]", "[[Cpp.memory.weak_ptr]]"]
functions: ["[[Cpp make_shared]]", "[[Cpp memory make_unique]]", "[[Cpp.memory.addressof]]", "[[Cpp.memory.align]]", "[[Cpp.memory.allocate_shared]]", "[[Cpp.memory.const_pointer_cast]]", "[[Cpp.memory.declare_no_pointers]]", "[[Cpp.memory.declare_reachable]]", "[[Cpp.memory.dynamic_pointer_cast]]", "[[Cpp.memory.get_deleter]]", "[[Cpp.memory.get_pointer_safety]]", "[[Cpp.memory.get_temporary_buffer]]", "[[Cpp.memory.return_temporary_buffer]]", "[[Cpp.memory.static_pointer_cast]]", "[[Cpp.memory.undeclare_no_pointers]]", "[[Cpp.memory.undeclare_reachable]]", "[[Cpp.memory.uninitialized_copy_n]]", "[[Cpp.memory.uninitialized_copy]]", "[[Cpp.memory.uninitialized_fill_n]]"]
date created: Tuesday, November 26th 2024, 2:22:53 pm
date modified: Friday, January 3rd 2025, 10:02:44 am
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

Issues with normal pointers
- Memory leaks = memory is allocated but never freed with delete
- Dangling pointers = pointer to de-allocated memory.
- Wild Pointers = Pointers that are declared and allocated in memory, but never initialized
- Data Inconsistency = When some data is stored in memory but is not updated in a consistent manner.
- Buffer Overflow = When a pointer is used to write a memory address that is outside of the allocated memory block. Leads to data corruption which hackers can attack.

|Pointer|Smart Pointer|
|---|---|
|A pointer is a variable that maintains a memory address as well as data type information about that memory location. A pointer is a variable that points to something in memory.|It’s a pointer-wrapping stack-allocated object. Smart pointers, in plain terms, are classes that wrap a pointer, or scoped pointers.|
|It is not destroyed in any form when it goes out of its scope|It destroys itself when it goes out of its scope|
|Pointers are not so efficient as they don’t support any other feature.|Smart pointers are more efficient as they have an additional feature of memory management.|
|They are very labor-centric/manual.|They are automatic/pre-programmed in nature.|

# Media
<iframe src="https://en.cppreference.com/w/cpp/header/memory" style="width: 100%; height: 600px;background-color:white;"></iframe>