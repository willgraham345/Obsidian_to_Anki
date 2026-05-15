---
type: project
project_id: 0
tags: 
company: Varex
project: VivaPro
subproject: development
status: closed
---
# Related Links:
- [[Fred Zoghi]]

## Other Projects

# P8 VivaPro Currents Tab Not Showing Up Updates/Notes:
![[VD VivaPro TOC 2024-06-24 12.07.59.excalidraw]]
- Starting to debug VivaPro from Visual Studio
	- Started to document how VivaPro updates the current information.
	- Unable to connect to the detector, thinking I'll change the Windows firewall settings. 
For whatever reason, I can't connect back to the detector. No idea what's going on here. 
- Get connection to `192.168.2.11`, but not `192.168.2.31`
- I think trying out the network configure thing messed up the networking on my detector. 

## Differences between our Build and Main
```shell
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   build.sh
	modified:   generate.sh
	modified:   src/dlgFileInspectorSettings.h
	modified:   src/dlgVirtualModeMapper.cpp
	deleted:    test/config
	deleted:    test/exceptions
	deleted:    test/serial
	deleted:    test/utils
	modified:   vivaPro.pro

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	qtBuildOnly/
```
- I think the test dependencies are other repositories that we don't want to include in a build right here. 

## Working Debugger
Just came from working with Fred to get the debugger working. Starting to debug due to the different issues. 

Getting segmentation faults with the SIGSEGV signal name. 
- `DlSystemDevices::setDiskInfo()` is where the problem happens. 
	- `freeArray[index]->setText(strFree)`

I think there's not enough memory for the virtual machine to work. I'm going to try and resize the disk, and see if that helps. 

Figured out how to resize a virtual image using GParted

#### Segmentation Error
Still running into the same error as before. (see below)
![[P008 VivaPro Currents Tab Not Showing Up.png|550]]
- Error caused by accessing memory that does not belong to you. 
	- Helper mechanism to keep you from corrupting the memory. 
	- Ways to get it:
		- Dereference a null pointer
		- Writing to a portion of memory that was marked as read-only. 
		- Dangling pointer points to a thing that does not exist anymore. 
Iteration I'm getting to in the `dlgSystemDevices.cpp`: 6
- There are only 5 disks, so I'm not sure why it's reading an extra disk amount.

### 2024-06-28 15:00 
Having a tough time trying to get these Virtualbox USBs to recognize the detector again.

Restarting to try and get a fresh crack at solving the weird bug. 
- Either that fixed it, or everything else somehow started working all at once.

Got it figured out, added to [[VD.VivaPro.DlgSystemDevices#Linux]] with the picture of what is being initialized into the freeDisks stuff. 
- Updated Fred in:  [[2024-06-27 Fred - VivaPro]]

### 2024-07-01 09:00
Digging into the memory for the different 

#### Variables I'm looking at 
- `strName : String`
	- Values: `''`, `''`, `'/'`, ``
- `strCapacity : String`
	- Values: `"73 GB"`
- `strFree : String`
	- Values: `"48.59 GB"`
- `capacityArray : QLabel*[]: QObject`
- `freeArray : QLabelArray[]: QLabel: QObject`
- `nameArray : QLabelArray[]: QLabel: QObject`

Loop that's failing:
- Fails at `freeArray[index]->setText(strFree)`
	- This fails at 19042 in `qCustomPlot.cpp`
	- No idea why that's getting called. 
- When the `/run/user/125` is the variable that's being tested. 

I'm diving deep into the compiler, and I think there's some weird stuff going on with the freeArray. 

### 2024-07-01 13:00
Fred responded, saying that some of the detectors don't necessarily have currents on their tabs. I may have logged this bug incorrectly as I thought all of them had current sensors. 
- I'll check this on Windows later in the week if I can make some headway.

### 2024-07-01 14:00
- Fred said I should keep trying/working. 

#### Windows vs Linux processes
[[VD.VivaPro.DlgSystemDevices#`initAllMemoryInfo()`]]
- Windows has its own getter for physically installed memory
- How do I do the same in Linux?
	- Nothing official according to [this stack overflow thread](https://stackoverflow.com/questions/8122277/getting-memory-information-with-qt)
Working to get the linux equivalent, and figure out where people are going for windows app development. 

### 2024-07-02 09:00
Determined that the Linux system we're running is after 2.3.48, as the sysinfo looks like the seconds structure in [[Linux sysinfo#Different versions and structure]]

The sysinfo isn't really giving any helpful info as to why it would be failing. I need to double check on if I can decrease the incrementor on the originally failing loop and go from there. 

Went and looked at the file. Turns out the folder has inaccessible permissions that don't work with my stuff. 
- I don't think this is the case anymore. After inspection, many of the other running things have similar file permissions.

I tried to modify the Linux `initAllDiskInfo()` method, and it didn't fix anything.
- There's a [stack overflow thread](https://bbs.archlinux.org/viewtopic.php?id=217657) that says someone had issues when they included a matching header/source file pair in the build. When that was excluded, they didn't have issues. 
- [Qt Creator thread](https://bbs.archlinux.org/viewtopic.php?id=217657) that said something similar.} 


Need to send a new update for Fred...

write permissions for files causing issues:
- s_host_guest_share: `drwxrwx---`
- lock: `drwxrwxrwt `
- boot/efi: `drwx------`
write permissions for files that are not causing issues:
- run/user: `drwx------`

[[2024-07-02 Fred - Segmentation Faults]]

### 2024-07-02 11:00
Fred's suggestion was to remove the config thing if I still had issues.

I think I'm going to try and start developing within the `/src` window, as I believe it will let me do git diffs from my native Windows.
- Building is taking forever...

### 2024-07-02 13:00
- I ended up stopping the build process. Even after an hour, there just wasn't enough progress. 
- I'm trying to rebuild the vivapro directory, and it's giving me lots of errors with missing subfolders on the CMakeLists.txt. 
	- Not sure how to fix that. 
	- AAAA

I'm back on rebuilding and debugging similar to this timestamp: [[#2024-07-01 14 00]] 

### 2024-07-02 16:00
Sent Fred a bigger update, he said to just comment them out. Great to hear that after like 3 days on the same problem lol. 

Rebuilt with the Release version (rather than just the debug) and had the same issues. 

Instead of commenting all of the lines out, I put a subtract 2 in the iterator for line 255 of the `dlgSystemDevices.cpp`. 

Fred would also like me to look for issues rather than trying to fix any code/software. 


### 2024-07-08 09:00
Modifying the message
#### Message
This bug shouldn't be listed. I didn't realize that not all detectors necessarily have current tabs. The current tab is not shown in Windows. I believe I mischaracterized this bug. 