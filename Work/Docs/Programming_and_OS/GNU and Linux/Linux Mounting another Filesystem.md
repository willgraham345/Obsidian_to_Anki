---
summary: All systems are arranged in a bit tree rooted at '/'. These files can be spread out and/or manually mounted using the mount command or the GUI interface.
type: note/workflow
date created: Monday, November 25th 2024, 1:03:48 pm
date modified: Tuesday, December 3rd 2024, 10:22:38 am
tags:
  - command/linux
workflow_of:
  - "[[Linux Filesystem Hierarchy]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`
[How to Mount File System in Linux | mount Command - GeeksforGeeks](https://www.geeksforgeeks.org/mount-command-in-linux-with-examples/)

# Usage
- [p] `cat /proc/filesystems` = View file system types Linux supports = #command/linux 
<!--ID: 1751434090855-->

- [p] `mount` = View currently mounted file systems on Linux = #command/linux 
<!--ID: 1751434090860-->

- [p] `mount -t <type> <device> <dir>` = Tells kernel to attach filesystem found at device to the dir= #command/linux = `-l` lists all filesystems mounted yet
<!--ID: 1751434090863-->

      `-h` display options for command
      `-V` display version info
      `-a` Mounts all devices described at `/etc/fstab`
      `-t` Type of filesystem device uses
      `-T` Describes an alternative fstab file
      `-r` Read-only mode mounted
- [p] `findmnt` = Explore mounted file systems in a tree structure = #command/linux = `-t` Use a filter
<!--ID: 1751434090867-->
