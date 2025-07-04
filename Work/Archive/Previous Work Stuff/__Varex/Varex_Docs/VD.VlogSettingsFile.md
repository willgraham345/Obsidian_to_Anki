---
company: Varex
tags: archive_deprecated/Varex
---
# VlogSettingsFile
Overview
- Inherits [[#VlogSettingsInterface]]
- Usually shown as a `settings` object
- Description:

## Members
#### Public Member Functions
- `getSeverity() : Vlog::Level`
	- Provides logging severity, **IF** the loggerName exists in the Log settings file. Otherwise, the default severity level. 
	- ❓Are we hitting this? Are we getting another default file thing? 

#### Private Fields
- `severityNameToLevelMap` = unordered map linking Logging severity text to logging enumerated level
- `loggerSeverityMap` = current hash map linking
- `whiteSpaceChars` = set of chars considered white space in Log Settings File
- `lastLogSettingsFileModTime` = last time the log settings file was modified

#### All Methods
- `setExitMonitoringThreadFlag()`
- `ApplyLogFileSettings()`
- `extractJsonLevelData`
	- `convertTextSeverityLevelToEnum()`
	- `updateSeverityMap()`
- `openAndFilterLogSettingsFile()`
	- `isCommentOrEmptyLine()`
- `hasLogSettingsFileBeenModified()`
- `convertSettingsToJson()`
- `extractJsonReloadData()`
- `extractJsonFormatData()`
- `initSettingsToDefaultValues()`
- `extractJsonRotationData()`
![[Pasted.image.20240613161711.png| 700]]

#### Fields
- `LoggerSeverityMap : Vlog::Level`

