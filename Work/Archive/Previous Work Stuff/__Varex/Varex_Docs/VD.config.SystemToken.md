---
company: Varex
tags:
  - archive_deprecated/Varex
  - archive_deprecated/Varex/config
---
# `SystemToken`
- Within `Config` namespace
- Description:
	- Provides id to values that follow
	- Some do not have values, and are only markers for parsing routines (i.e.`BEGIN_MODE`, `END_MODE`, `CONFIG_END_OF_FILE`)

## Members
### `public`
#### Methods
##### `Id2SysTok()`
##### `SysTok2Num`
##### `isValid(const uint32_t index)`
- To see if a system is valid for a system area.
- If not, it is either a valid Mode, Module  ModularMode, or Unknown
- Calls 

##### `fromString()`
##### `convert(id)`
##### `toString()`
#### Fields
##### `ID2SYSTOK : static const std::unordered_map<uint32_t, SystemToken::Name>`
- A static map for a system token in the parent class, and is the output from [[#`Id2SysTok()`]]
- 

##### `Name : enum class`
- Tons of different `enums`