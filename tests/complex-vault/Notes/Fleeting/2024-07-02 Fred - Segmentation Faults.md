---
status: closed
type: update_log
date: 2024-07-02
week: 2024-W27
year: 2024
company: Varex
project: 
subproject:
---
# Relevant Links
- [[Fred Zoghi]]
- [[P008 VivaPro Currents Tab Not Showing Up]]

# Message
I've been working on the segmentation faults for a while. Based on what I've been able to understand, I think there's some issues with the memory management, perhaps with some of the headers we included a got rid of to help with building. According to these articles: ---, there are cases where both an included header and source can lead to corrupted memory which is manifested in alternative locations. 

Other paths I've checked:
- I redid some of the QStorageInfo calls within the dlgSystemDevices.cpp to be in accordance with Qt's standards and their website. 
- I checked on the paths where the bug manifests. If I exclude those with a smaller numOfDisks incrementor, then the bug disappears.
	- I did further digging into the bug, and I found a few issues with the read/write permissions on the file causing issues. The thing that's weird is one of the files that works has the exact same read/write permissions as the disk causing the problem. 

I think I've hit a bit of a wall here. I'm going to try and look more into the headers we modified, hoping that the issues are somewhere in there.  