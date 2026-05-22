---
type: note
---
# Background

## Properties
A messaging queue has the following properties:
- Ring buffer
	- Data items that have been sent but not yet received
	- Aligned to an N-byte boundary (N = power of 2)
- Data item size
	- Measured in bytes
- Maximum quantity
	- Data items that can be queued in the ring buffer
## 
Must be initialized before it can be used.

A data item can be sent to a message queue by a thread or an ISR

A data item can be received from a message queue by a thread. The data item is copied to the area specified by the receiving thread. The size of this must equal the message queue's data item size. 
A message queue is a kernel object that implements a simple message queue, allowing threads and ISRs to asynchronously send and receive fixed-size data items.
## 