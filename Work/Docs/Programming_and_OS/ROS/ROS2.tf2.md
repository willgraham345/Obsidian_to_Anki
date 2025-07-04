---
type: note
tags:
  - note/ROS
---
# Background
tf2 is the transform library for ROS2, and maintains the relationships between cordinate frames in a tree structure
- Buffered in timem
- Lets user transform points between any two coordinate frames at a desired point in time. 

Tf2 *does* have some requirements around needing different transforms to be within a relatively similar time frame. Otherwise, tf2, may publish multiple tf2 trees which isn't super helpful. 
- [This thread](https://answers.ros.org/question/386260/tf_static-frames-not-available-in-lookup_transform/) details a workaround in python. 

# Usage
## tf2 has two different trees