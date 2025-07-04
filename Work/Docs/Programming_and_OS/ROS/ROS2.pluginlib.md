---
tags: note/ROS
type: note
---
[ROS Wiki](https://wiki.ros.org/pluginlib)
# Background
- Provides tools for writing and dynamically loading plugins using the ROS build infrastructure
- These tools require plugin providers to register their plugins in the `package.xml` of their package
- Plugin = a dynamically loadable class that are loaded from a runtime library
	- i.e. shared object, dynamically linked library)