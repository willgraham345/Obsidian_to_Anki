---
company: Varex
type: note
---
# DlgSystemDevices
- Description:
	- Inherits from `QDialog` 

## ctor/dtor
### `DlgSystemDevices(QWidget *, bool)`
![[VD.VivaPro.DlgSystemDevices.png]]

### `~DlgSystemDevices(QWidget*, bool)`
## public
### Fields
`diskFreeNames: QVector`
`diskTotalBytes: QVector`
`diskFreeBytes: QVector`

### Member Functions
#### `initialize()`
Overview:
- Starts with the ui
Operations:
1. Does a bunch of stuff
2. Calls [[#`initAllMemoryInfo()`]]
3. Calls [[#`initAllDiskInfo()`]]

#### `initComPorts()`
#### `initNetworkIntrfaces()`
#### `initAllMemoryInfo()`
##### Windows
Overview:
- Gets total memory with `GetPhysicallyInstalledSystemMemory()`
	- That's a function defined by `sysinfoapi.h`
- All 
Operations:
1. `GetPhysicallyInstalledSystemMemory()`
2. `setMemItemText()`
3. `memset()`
4. `GlobalMemoryStatusEx`
5. `setMemItemText()`

##### Linux
Overview:
- Uses the `ui` pointer, which points at the ui
Operations:
1. creates `sysinfo` variable
2. Sets `setMemItemTest()` 

#### `initAllDiskInfo()`
Overview:
- Called by [[#`initialize()`]]
- Inits all disk info.
- Windows includes the winsock.h and iphlpapi.h files, along with MALLOC and FREE functions. 
- I think this thing doesn't check permissions on its files. 

##### Windows
Operations:
1. Pointer to a null terminated string that specifies a directory on the disk. 
2. Accepts any directory on a disk. 

##### Linux
Operations:
1. Looks for the `QStorageInfo` address, and the `QStorageInfo::mountedVolume()`. See 
	1. I don't think I can see inside of this thing. I know that It initializes 7 values inside of the `diskFreeNames`, `diskTotalBytes`, and `diskFreeBytes`. 
	2. Here's what it initializes:
	   ![[VD.VivaPro.DlgSystemDevices-1.png|350]]
		   `const QStorageInfo& storage : QStorageInfo::mountedVolumes()`
	3. Calls `setDiskInfo()` 

#### `initWinNetworkProperties()`
#### `setDiskInfo()`
Overview:
- Only has 1 implementation for both OS
- Sets info data for disk related widgets
	- Defined once for Linux as well as Windows
Operations:
1. Initializes a bunch of `QString` objects
2. Populates 3 pointer arrays `nameArray`, `capacityArray`, `freeArray`
	1. There are 3 things in each of them. 
References :`initAllDiskInfo()` for both Linux as well as Windows.

## private
### Fields
#### `ADAPTER_INFO`
name : `QString`
desc : `QString`
type : `QString`
macAddr : `QString`
ipAddr : `QString`
subnetMask : `QString`
flags : `QNetworkInterface::InterfaceFlags`
isWifi : `bool`
ipV4Protocol : `bool`
index : `int`

### Methods
`onOkButtonClicked()`
`processError()`
`onComboBoxPingActivated()`
`accept()`
`reject()`
