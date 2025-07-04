---
tags: note/ROS
type: note
---
# Background
Holds data describing state of torque controlled joints

State of each joint is described by:
- position of the joint (rad or m)
- Velocity of the joint (rad/s or m/s)
- Effort applied to the joint (Nm or N)
Each joint is uniquely identified by its name, header specifies the time at which the joint states were recorded. 

This message consists of multiple arrays, one for each part of the joint state. 
The goal is to make each of the fields optional

All arrays in this message should have the same size, or be empty.


# Usage
[[ROS2.Interface.Std.Msgs.Header]] header  
[[ROS2 Interfaces Std Msg String]] name
[[ROS2 Interfaces Std Msg Float64]] position
[[ROS2 Interfaces Std Msg Float64]] velocity
[[ROS2 Interfaces Std Msg Float64]] effort