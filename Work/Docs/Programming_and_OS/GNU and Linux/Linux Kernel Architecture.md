---
type: note
---
# Overview
![[Pasted image 20230811121608.png]]
- The core **Hardware** of any system (CPU, RAM, etc) cannot communicate with the users directly, and that is where the **Kernel** level of the Linux architecture comes into use. The Kernel basically helps us to contact the hardware, it helps us to provide our input into the hardware and receive the resultant output as well. Oh, wait! but how are we supposed to access the kernel? I don’t know where the kernel is! That is where the next level of Linux architecture comes in, **The Shell**. So, when the outer ring of **Users** wants to perform a command or run an **Application** in a Linux OS, the users are supposed to input their needs in The Shell, it in turn communicates with the kernel, and the kernel passes our input to the hardware. After the necessary processes are done, the resultant output is sent back to the kernel from the hardware and the kernel sends it back to the shell which is finally displayed as an output to the end-user!
## The Shell
Shell is part of the CLI Linux system
Shell doesn't work directly in a GUI environment.

## **Operations performed by a Kernel**

1. **Resource Management:** Decides which process gets the resource for operation.
2. **Memory Management:** Allocates system memory to the processes efficiently.
3. **Device Management:** Helps the processes to establish a connection with external devices like USB et cetera.
4. **System Calls:** Sometimes a process may not have enough permissions to access a resource, in such a situation system calls can be used to provide the necessary permissions to the processes. System calls can also be embedded in a shell script in order to avoid interrupts caused by denial of permissions.

