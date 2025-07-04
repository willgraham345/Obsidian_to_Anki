---
status: closed
type: update_log
date: 2024-06-27
week: 2024-W26
year: "2024"
---
# Relevant Links
- [[Fred Zoghi]] 

# Message
Hi Fred! It's been a while since I checked in and I thought I'd give you an idea of what I've been up to.

First off, I was able to resize my virtual machine correctly from within the machine. I resized it earlier on the host machine, but the virtual machine wasn't picking it up. That has been taken care of and I have plenty of room to play around with. 

I've been able to more properly debug and I believe I have the beginnings of what's going wrong with [bug 3125](https://fpbugs/issues/31625). I've been getting segmentation errors and incorrect memory access while attempting to open the system devices. Within the class dlgSystemDevices the setDiskInfo method has returned errors. It doesn't fail on the first attempt, but rather on the 6th iteration. If I'm reading the git commits correctly, I believe you were able to get this section running within Windows. 

On Linux builds, there are different methods for setting the disk information. I'm trying to dig into these, and figure out which one is returning incorrectly. I'll send a more "official" email to you and Paul once I'm able to get further. 

Just to make sure, if this isn't what I should be working on, please let me know and I'll be happy to pivot!