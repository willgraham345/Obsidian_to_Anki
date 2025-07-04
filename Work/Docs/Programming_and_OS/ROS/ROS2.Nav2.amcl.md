---
tags: note/ROS
type: note
---
# Background
AMCL = adaptive monte carlo localization
[Package Wiki](https://wiki.ros.org/amcl)

## Subscribed Topics
`scan`
- (`sensor_msgs/LaserScan`)
`tf`
- (`tf/tfMessage`)
`initialpose`
- (`geometry_msgs/PoseWithCovarianceStamped`)
`map`
- (`nav_msgs/OccupancyGrid`)
	- When the `use_map_topic` parameter is set, amcl subscribes to this topic to retrieve the map used for laser-based localization
## Published Topics
`amcl_pose` 
- (`geometry_msgs/PoseWithCovarianceStamped`)
`particlecloud`
- (`geometry_msgs/PoseArray`)
`tf` 
- (`tf/tfMessage`)
- Publishes the transform from `odom` (which can be remapped via the `~odom_frame_id` parameter) to `map`.


![[Pasted.image.20240205155412.png]]