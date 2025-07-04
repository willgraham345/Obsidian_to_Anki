---
company: Varex
tags: archive_deprecated/Varex
---
# SettingsFileTests_SettingsFilePartialWildcard
- Description:
	- Logging with a partial logger name wildcard in Settings file.
	- Contains both a partial and global wildcard in the logger to Severity Map with different severity levels. 
		- The partial one should be matched.

## Process
![[VD.SettingsFilePartialWildcard.2024-06-13.16.22.50.excalidraw| 750]]
1. Creates `newSeverityMap` objects
		1. Has info/warn for different wildcards which reference 
		1. `["*"] = Vlog::Level::info`
		   `["SettingsFileTests.*] = Vlog::Level::warn`
	2. Create a test log settings file
		1. `format = "[%Y - %m - %d %T.%e%z][%L][***%n***][%v]"`
		2. `newSeverityMap`

### Call Graph
![[Pasted.image.20240613143303.png]]