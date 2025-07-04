---
company: Varex
tags:
  - archive_deprecated/Varex
  - archive_deprecated/Varex/config
  - archive_deprecated/Varex/config/parse
---
# Background
- Function call for reading in a configuration. 

### `public`
#### Methods
##### `config()`
Creates a new instance in memory, and is referenced all dang over. 

##### `isModular()`
- Returns `isModularConfig`
	- `isModularConfig` is defined in `ConfigBase.h`, and keeps track of the configuration they're using. See [[VD.ConfigBase]] for more info
	- The only time this variable is edited to true is within [[#`config()`]] method

### `private`
#### Methods
##### `parse(T &configData, uint32_t numBytes)`
Variables
- `configData` = input stream of configuration data
- `numBytes` = total number of bytes for data
Other Function/Class Calls
- [[VD.config.SystemToken]]
Exceptions
- `BaseException`
- `std::ifstream::failure`
	- `ResourceException`
- `std::exception`
![[VD.ConfigCreator.Parse.Calls2024-06-17.16.35.24.excalidraw]]

#### Fields
- Access:
	- Fields:
	- Methods:

# Usage