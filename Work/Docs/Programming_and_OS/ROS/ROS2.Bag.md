---
tags: note/ROS
type: note
---
# Background
Allows you to record/play topics to/from a rosbag


# Commands
|                          |                             |
| ------------------------ | --------------------------- |
| `ros2 info <bag-name>`   | Output information of a bag |
| `ros2 play <bag-name>`   | Plays a bag                 |
| `ros2 record <bag-name>` | Records a bag               |
| `ros2 record -a`         | Records everything (I think)                            |


## Converting to an MCAP file for Foxglove
```shell
mcap convert <ros2_db3.db3> <new_filename.mcap>
```