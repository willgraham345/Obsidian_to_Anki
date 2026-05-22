---
type: update_log
date: 2024-07-17
week: 2024-W29
year: 2024
company: Varex
project: 
subproject: 
tags: 
status: closed
---

# Relevant Links
- 
# Message
I saw that my build 3 didn't pass yesterday, I'll double check on why that happened today. 

I've been trying to compile the changes we've made on my local VM. I've run into another issue when trying to build the vsp2.h file. Unfortunately, the build is showing that the vsp2.h file isn't found. 

Here's what I've done to try and fix it:
- I made sure I had the correct qtBuildOnly from your shared folder
- Output the path from the INCLUDEPATH variable
- Double checked that the directory containing the vsp2.h is at ~/qtBuildOnly/libvsp2mock 

I rechecked, and made sure that I have the correct qtBuildOnly from your shared folder. 