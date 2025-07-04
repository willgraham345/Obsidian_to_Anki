---
tags: note/ROS
type: note
---
The footprint outlines the robot's 2D shape when projected to the ground and is used by Nav2 to avoid collisions during planning. The algorithms involved in this task make sure that the robot does not collide with the obstacles in the costmap while it computes the robot's paths or plans. 

Set up using the `footprint` or `robot_radius` parameter of the global and costmap.

You can also configure a local costmap with `footprint` (polygon) for irregularly-shaped robots.