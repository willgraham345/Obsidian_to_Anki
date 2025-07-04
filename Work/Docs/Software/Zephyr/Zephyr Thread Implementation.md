---
type: note
---
1. A thread is spawned by defining its stack area and its thread control block, and then calling [`k_thread_create()`](https://docs.zephyrproject.org/2.7.5/reference/kernel/threads/index.html#c.k_thread_create "k_thread_create"). This will return its thread id, which can be used to reference the thread.
2. The stack area must be defined using [`K_THREAD_STACK_DEFINE`](https://docs.zephyrproject.org/2.7.5/reference/kernel/threads/index.html#c.K_THREAD_STACK_DEFINE "K_THREAD_STACK_DEFINE") or [`K_KERNEL_STACK_DEFINE`](https://docs.zephyrproject.org/2.7.5/reference/kernel/threads/index.html#c.K_KERNEL_STACK_DEFINE "K_KERNEL_STACK_DEFINE") to ensure it is properly set up in memory.
	1. - The original requested stack size passed to `K_THREAD_STACK` or `K_KERNEL_STACK` family of stack instantiation macros.
	2. For a stack object defined with the `K_THREAD_STACK` family of macros, the return value of [`K_THREAD_STACK_SIZEOF()`](https://docs.zephyrproject.org/2.7.5/reference/kernel/threads/index.html#c.K_THREAD_STACK_SIZEOF "K_THREAD_STACK_SIZEOF") for that’ object.
	3. For a stack object defined with the `K_KERNEL_STACK` family of macros, the return value of [`K_KERNEL_STACK_SIZEOF()`](https://docs.zephyrproject.org/2.7.5/reference/kernel/threads/index.html#c.K_KERNEL_STACK_SIZEOF "K_KERNEL_STACK_SIZEOF") for that object.

## Spawning a thread immediately
```c
#define MY_STACK_SIZE 500
#define MY_PRIORITY 5

extern void my_entry_point(void *, void *, void *);

K_THREAD_STACK_DEFINE(my_stack_area, MY_STACK_SIZE);
struct k_thread my_thread_data;

k_tid_t my_tid = k_thread_create(&my_thread_data, my_stack_area,
                                 K_THREAD_STACK_SIZEOF(my_stack_area),
                                 my_entry_point,
                                 NULL, NULL, NULL,
                                 MY_PRIORITY, 0, K_NO_WAIT);
```