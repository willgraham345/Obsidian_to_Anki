---
company: Varex
tags: archive_deprecated/Varex
---
# VlogSettingsInterface
`<interface>`
- Overview
	- Interface rules for logging setting
	- Implemented in [[VD.VlogSettingsFile]]

![[Pasted.image.20240514162952.png| 500 ]]

## Members
### Public Member Functions
- `getFormat() : virtual std::string`
	- Provides formatting string for log messages
	- Lots and lots of formatting flags here. Flags are preceded by a `%` sign. 
	- There's notes about a bug with the `s` formatter (source file and line number). All log entries contain source information info until this is fixed.
		- Example is `"foo.cpp:287"`
	- Don't override this method to use the default formatter. 
		- ❓Does that mean anything?