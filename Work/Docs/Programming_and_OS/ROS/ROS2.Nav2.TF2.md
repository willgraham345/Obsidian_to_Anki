---
tags: note/ROS
type: note
---
# Background
Like many other packages, Nav2 requires transform tree of a robot to be published using the TF2 ROS package. 

A transform tree describes each robot. 

## Transforms in Nav2
Nav2 requires the following transforms to be published in ROS
1. `map` --> `odom`
2. `odom` --> `base_link` (usually published by odometry system, for more info see [[ROS2.odom]])
3. `base_link` --> `base_layer`
	1. `base_layer` represents the sensor base frames
		1. If there are multiple sensors, then a transform back to `base_layer` for each one is required

### `map` --> `odom`
- Usually provided by a different ROS package like [[ROS2.Nav2.amcl]]
- All ROS compliant SLAM and localization packages will provide you with this transformation automatically on launch
### `odom` --> `base_link`
- Usually published by odometry system using sensors such as wheel encoders. 
- Typically computed via sensor fusion using the `robot_localization` packaged
`base_footprint`. A virtual (non-physical) link which has no dimensions or collision areas. Its primary purpose is to enable various packages to determine the center of a robot projected to the ground. Nav2 uses this link to determine the center of a circular footprint used in its obstacle avoidance algorithms
- `base_link` --> `base_footprint`

### Other transforms
- What is covered in the rest of the notes in the [[ROS2 Nav2 First Time Robot Setup Guide]]
- Transformation tree is used by Nav2 to relate info from sensors or other frames of interest to the robot by the [[ROS2.Robot.State.Publisher]] and the URDF
	- In cases where there are more sensor coordinate frames on your platform, then a transform tree from `base_link` to each sensor coordinate frame needs to be published.
- Usually provided to Nav2 through the 
