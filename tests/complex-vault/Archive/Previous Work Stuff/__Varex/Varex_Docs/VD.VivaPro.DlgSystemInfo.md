---
company: Varex
---
# DlgSystemInfo
- Description:
	- Declared in `dlgProductInfo.h`
	- Defined in `dlgProductInfo.cpp`

## Members
### Q_OBJECT
### `public`
#### `ctor -> void`
- Pointer to parent widget

### `private`
#### Methods
##### `initializeSoftwareInfo`
Overview:
- Grabs varex icon, title and build. 
Operations:
1. 

##### `initializeCurrents()`
Overview:
- Creates two `QLabel` pointer arrys
- Starts grabbing things
Operations:
1. 

#### Fields
##### isConnected
##### `TAB_TYPE`
- Enum class (software, detector, temperatures, voltages, currents are all potential values)