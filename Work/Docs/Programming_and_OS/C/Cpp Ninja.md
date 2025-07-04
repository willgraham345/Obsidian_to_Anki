---
summary: Build system generator specialized for speed. Has a bunch of tools, could be useful.
components: ["[[Cpp Ninja Tools]]"]
same: ["[[GNU make]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Wednesday, November 13th 2024, 10:43:49 am
type: note/system
---
# Background
Generator 
- Used for actual process of building apps similar to [[GNU make]]. 
- Focus on running as fast as possible with parallel builds. 
	- Intentionally kept minimal and focused on speed. 
- Commonly paired with [[CMake Overview and Basics guide notes]]

# Usage
Has some great tools that can be used by invoking `-t` flag.
<iframe src="https://ninja-build.org/manual.html#_extra_tools" style="width: 100%; height: 800px;"></iframe>
