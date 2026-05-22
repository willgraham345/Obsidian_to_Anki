---
title: "Buffer and Cache Memory in Linux"
source: "https://www.baeldung.com/linux/buffer-vs-cache-memory"
author:
  - "[[Written by: 											Robert Edward]]"
  - "[[Robert Edward]]"
published: 2022-03-06
created: 2025-12-04
description: "Learn about buffer memory and cache memory in Linux and the differences between them."
tags:
  - "clippings"
---
## 1\. Overview

In this tutorial, we’ll learn about buffer memory and cache memory and the differences between them. As we know, the use of Linux file system buffer and cache makes input and output (I/O) operations faster.

But, before we talk about the differences between buffer and cache, we need to understand what they are and how they operate.

## 2\. Buffer

Buffering is the process of preloading data into a reserved area of memory called buffer memory.

**Buffer memory is a temporary storage area in the main memory (RAM) that stores data transferring between two or more devices or between an application and a device.** Buffering compensates for the difference in transfer speeds between the sender and receiver of the data.

Systems automatically create buffers in the RAM whenever there are varying transmission speeds between applications or devices transferring data. The buffer accumulates the bytes of data received from the sender and serves it to the receiver when ready.

Buffers are useful when printing long documents. The system automatically creates a buffer and fills it with the document’s data so that it doesn’t have to wait for the printer before processing the next page.

**In computer networking, buffers are useful in data fragmentation and reassembly.** From the sender’s side, the system breaks down a large chunk of data into small packets and sends them over the network. On the receiver’s end, the system creates a buffer that collects the fragmented packets of data and reassembles them to their original format.

**Buffering supports copy semantics for an application’s input or output (IO).** Let’s assume an application has a buffer to write to the hard disk and that it executes the *write()* system call. If the application changes the buffer data before the system call returns, copy semantics offers a version of the data at the time of the last system call.

Buffers are executed in three capacities:

- bounded capacity: buffer memory size is limited, blocks senders if full
- unbounded capacity: buffer memory size is unlimited, accepts any amount of data from senders
- zero capacity: buffer memory size is zero, blocks all senders until the data is received

## 3\. Cache

Caching is the process of temporarily storing a copy of a given resource so that subsequent requests to the same resource are processed faster.

**Cache memory is a fast, static random access memory (SRAM) that a computer chip can access more efficiently than the standard dynamic random access memory (DRAM)**. It can exist in either RAM or a hard disk. Caching in RAM is referred to as memory caching, while caching in a hard disk is referred to as disk caching.

**Disk caching is advantageous because cached data in the hard disk isn’t lost if the system crashes. However, data access in disk caching is slower in comparison to memory caching.**

Disk cache sizes can range from 128 MB in normal hard disks to 1 GB in solid-state disks (SSDs).

Whenever a program requests data from the hard disk, the system first checks the cache memory. It only checks the hard disk if the requested data isn’t present in the cache memory. This greatly improves data processing because accessing it directly from the hard disk is slower.

Caches can support random access to large stores of information. Moreover, cache memory also uses complex algorithms that help to decide what data to keep or delete.

We can use the [*free*](https://www.baeldung.com/linux/free-command) command to check the sizes of the buffer memory and cache memory:

```bash
$ free -h
              total        used        free      shared  buff/cache   available
Mem:          7.6Gi       6.4Gi       170Mi       402Mi       1.1Gi       573Mi
Swap:         2.0Gi       589Mi       1.4Gi
```

We’re passing the *\-h* flag to display the results in a human-readable format. In this case, the total size of buffer memory and cache memory in the RAM is 1.1GB.

Cache memory may have a small size relative to RAM, but it has a significant effect on the general performance of the system.

## 4\. Key Differences Between Buffer and Cache

Let’s look at some of the key differences between buffer and cache:

| Buffer | Cache |
| --- | --- |
| Exists only in the RAM | Exists in either RAM or hard disk |
| Compensates for the difference in speed between two programs exchanging data | Quickens the access of data that is frequently requested |
| Stores the original data | Stores a copy of the original data |
| A normal temporary storage location in the RAM | A fast storage location in the RAM or hard disk |
| Made of dynamic RAM | Made of static RAM |

## 5\. Conclusion

In this article, we’ve learned about buffer memory and cache memory and some differences between them.

<video xmlns="http://www.w3.org/1999/xhtml"></video>