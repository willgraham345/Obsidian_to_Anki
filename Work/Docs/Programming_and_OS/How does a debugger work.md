---
type: note
---
# Background
![[1_554AE0054vtiRNfcqlOXLw.webp|300]]

[How does a debugger work?](https://stackoverflow.com/questions/216819/how-does-a-debugger-work)
- The user tells what process to attach to. This can be done by name or process ID. 
	- In windows, this is the `DebugActiveProcess` [[W Win32 DebugActiveProcess]]
	- In Linux, debugging begins with the 
- Once attached, the debugger will enter an event loop much like for any UI.
- Instead of events coming from the windowing system, the OS will generate events based on what happens in the process being debugged. 
	- In windows, this is the [[W Win32 WaitForDebugEvent]]
- The debugger is able to read/write the target process' virtual memory and adjust its memory values through APIs provided by the OS. There is an entire list of debugging functions for windows
- The debugger is able to use system information from symbol files to translate from addresses to variable names/locations in the source code. 

This process typically looks similar with other managed environments (Java, .NET) as the VM will provide the API rather than the OS. 

# Usage