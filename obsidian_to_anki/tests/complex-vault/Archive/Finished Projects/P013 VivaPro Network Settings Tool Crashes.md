---
type: project
project_id: 0
company: Varex
project: VivaPro
subproject: VivaPro_dev
tags: 
status: closed
---
# Related Links:
[Link to Issue](https://fpbugs/issues/31626)
[[]]

# Updates/Notes:
Goal: Try to build in Linux with the debugger. 

### 2024-07-16 15:00
Copied `qtBuildOnly` to the `/usr` directory
Cloning to the `qt_name_update` in my VM home directory

I've had some issues with building the library to test it. There's an issue with bringing the `vsp2.h` into the build. 
- 

### 2024-07-24 09:00
Starting to debut the connection. Need to see if I can get the network to interact nicely with the GUI. 

Getting this output from the VivaPro. I think the Network Settings tool is working just fine. 
![[P013 VivaPro Network Settings Tool Crashes.png|300]]
On closer inspection, I did see this:
![[P013 VivaPro Network Settings Tool Crashes-1.png|250]]

I think that bug may be ideal behavior. It lets the user know that there's been a problem with the communication and they need to reboot. 


I closed the issue, and am moving onto the next bug. 
