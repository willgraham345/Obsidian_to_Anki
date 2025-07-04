---
type: note
---
# Background
Zephyr kernel lies at the heart of every application

It's a low footprint, high performance, multi-threaded execution environment with a rich set of available features. 

The rest of the Zephyr ecosystem (device drivers, network stack, application specific code) uses the kernel's features to create a complete application. 

Applications requiring more memory (50 - 900 KB), multiple communication devices (Wi-Fi & Bluetooth Low Energy), complex multi-threading, can be developed using the Zephyr kernel. 


# Scheduling Interrupts, and Synchronization
[[Zephyr Thread]]
[[Zephyr Scheduling]]
[[Zephyr System Threads]]
[[Zephyr Workqueue Threads]]
[[Zephyr Zephyr Without Threads]]
[[Zephyr Interrupts]]
[[Zephyr Polling API]]
[[Zephyr Semaphores]]
[[Zephyr Mutexes]]
[[Zephyr Condition Variables]]
[[Zephyr Symmetric Multiprocessing]]

# Data Passing
|Object|Bidirectional?|Data structure|Data item size|Data Alignment|ISRs can receive?|ISRs can send?|Overrun handling|
|---|---|---|---|---|---|---|---|
|FIFO|No|Queue|Arbitrary [1]|4 B [2]|Yes [3]|Yes|N/A|
|LIFO|No|Queue|Arbitrary [1]|4 B [2]|Yes [3]|Yes|N/A|
|Stack|No|Array|Word|Word|Yes [3]|Yes|Undefined behavior|
|Message queue|No|Ring buffer|Power of two|Power of two|Yes [3]|Yes|Pend thread or return -errno|
|Mailbox|Yes|Queue|Arbitrary [1]|Arbitrary|No|No|N/A|
|Pipe|No|Ring buffer [4]|Arbitrary|Arbitrary|No|No|Pend thread or return -errno|