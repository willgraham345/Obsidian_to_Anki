---
company: Varex
tags: archive_deprecated/Varex
---
# Background
Provides logging for the rest of the architecture
- Must be initialized before it can be used
	- Initialization is provided by an implementation of the `LogSettingsInterface` which is passed to the logging initialization call. 
	- Initialization only needs to happen once for the entire system. Future calls to `Vlog::initLogging()` will be ignored. 

Logging information for me is stored in:
`"C:\Users\wi994269\AppData\Local\Varex\logs\dlllogfile.txt"`
- The `LogSettings.txt` should be in that same folder. 

## Git History
![[Pasted.image.20240529145742.png| 750]]

# Usage
