---
tags: note/ROS
type: note
---
# Background
The costmap 2D package makes use of sensor information to provide a representation of the robot's environment in the form of an occupancy grid
- The cells in the grid store cost values between 0-254 which denote a cost to travel through these zones
	- 0 means free, while 254 is lethally occupied
- Values in between these extremes are used by navigation algorithms
Implemented in the [[ROS2.Nav2.costmap_2d]]
- Consists of multiple layers, each of which has a certain function that contributes to a cell's overall cost. 
**For more information on the 2D costmap, see [costmap_2d Ros1](http://wiki.ros.org/costmap_2d)**

#### Costmap 2d layers
Has plugin-based layers
- Static layer
	- `map` section of the costmap obtained from the messages published to `/map` like SLAM
- Obstacle layer
	- Objects detected by sensors that publish either or both the [[ROS2.Interfaces.LaserScan]] and [[ROS2.Interfaces.PointCloud2]]
- Voxel layer
	- Similar to obstacle layer, and can use [[ROS2.Interfaces.LaserScan]] and [[ROS2.Interfaces.PointCloud2]] information but handles 3d data instead
- Range layer
	- Allows for inclusion of information from sonar and infrared sensors
- Inflation layer
	- Represents the added cost values around lethal obstacles such that our robot avoids navigating into obstacles due to the robot's geometry. 
Layers are integrated through a plugin interface, and then inflated using a specified inflation radius, if the inflation layer is enabled


# Usage/Configuration
## Guide
[Costmap 2D Configuration Guide](https://navigation.ros.org/configuration/packages/configuring-costmaps.html)
[Costmap 2D Source Code](https://github.com/ros-planning/navigation2/tree/main/nav2_costmap_2d)

[Multiple Robot ROS2 Navigation](https://docs.omniverse.nvidia.com/isaacsim/latest/ros2_tutorials/tutorial_ros2_multi_navigation.html)


## Example SamBot Configuration
- Set both obstacle and voxel layer to use the LaserScan messages published to the /scan topic by the lidar sensor

### Configuring nav2_costmap_2d
```
global_costmap:
  global_costmap:
    ros__parameters:
      update_frequency: 1.0
      publish_frequency: 1.0
      global_frame: map
      robot_base_frame: base_link
      use_sim_time: True
      robot_radius: 0.22
      resolution: 0.05
      track_unknown_space: false
      rolling_window: false
      plugins: ["static_layer", "obstacle_layer", "inflation_layer"]
      static_layer:
        plugin: "nav2_costmap_2d::StaticLayer"
        map_subscribe_transient_local: True
      obstacle_layer:
        plugin: "nav2_costmap_2d::ObstacleLayer"
        enabled: True
        observation_sources: scan
        scan:
          topic: /scan
          max_obstacle_height: 2.0
          clearing: True
          marking: True
          data_type: "LaserScan"
          raytrace_max_range: 3.0
          raytrace_min_range: 0.0
          obstacle_max_range: 2.5
          obstacle_min_range: 0.0
      inflation_layer:
        plugin: "nav2_costmap_2d::InflationLayer"
        cost_scaling_factor: 3.0
        inflation_radius: 0.55
      always_send_full_costmap: True

local_costmap:
  local_costmap:
    ros__parameters:
      update_frequency: 5.0
      publish_frequency: 2.0
      global_frame: odom
      robot_base_frame: base_link
      use_sim_time: True
      rolling_window: true
      width: 3
      height: 3
      resolution: 0.05
      robot_radius: 0.22
      plugins: ["voxel_layer", "inflation_layer"]
      voxel_layer:
        plugin: "nav2_costmap_2d::VoxelLayer"
        enabled: True
        publish_voxel_map: True
        origin_z: 0.0
        z_resolution: 0.05
        z_voxels: 16
        max_obstacle_height: 2.0
        mark_threshold: 0
        observation_sources: scan
        scan:
          topic: /scan
          max_obstacle_height: 2.0
          clearing: True
          marking: True
          data_type: "LaserScan"
      inflation_layer:
        plugin: "nav2_costmap_2d::InflationLayer"
        cost_scaling_factor: 3.0
        inflation_radius: 0.55
      always_send_full_costmap: True
```