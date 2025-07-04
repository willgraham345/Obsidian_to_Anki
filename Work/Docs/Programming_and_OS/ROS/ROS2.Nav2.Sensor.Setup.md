---
tags: note/ROS
type: note
---
# Sensor Introduction
[[ROS2.Interfaces.Sensor.Msgs.Overview]] is provided to have easily common sensor interfaces.
- There are also radar_msgs and vision_msgs that have standard interfaces.
- radar_msgs defines radar-specific sensors with vision_msgs defining the messages used in computer vision


# Common Sensor Messages
[[ROS2.Interfaces.LaserScan]]
[[ROS2.Interfaces.PointCloud2]]
[[ROS2.Interfaces.Range]]


# Mapping and Localization
Now that we have a robot with its sensors set up, we can use the obtained sensor information to build a map of the environment to localize the robot on the map

The `slam_toolbox` is a set of tools and capabilities. 
- Officially supported SLAM libraries in Nav2. 

`nav2_amcl` can also have localization

Both of the above toolboxes use information from the laser scan to perceive the robot's environment. We need to make sure that they are subscribed to the correct topic that publishes the `sensor_msgs/LaserScan` message. 
- Can be configured by setting their `scan_topic` parameters to the topic that publishes taht message. 
- Convention to publish `sensor_msgs/LaserScan` messages to `/scan` topic


# Costmap 2D
The costmap 2D package makes use of sensor information to provide a representation of the robot's environment in the form of an occupancy grid
- The cells in the grid store cost values between 0-254 which denote a cost to travel through these zones
	- 0 means free, while 254 is lethally occupied
- Values in between these extremes are used by navigation algorithms
Implemented in the [[ROS2.Nav2.costmap_2d]]
- Consists of multiple layers, each of which has a certain function that contributes to a cell's overall cost. 
The layers are integrated into the costmap through a plugin interface and inflated

## Example nav2_costmap_2d
This one will use a configuration using lidar sensor information. We will set the obstacle and voxel layer to use the [[ROS2.Interfaces.LaserScan]] messages published to the [[ROS2.scan]] topic by the lidar sensor. 

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
### Description
We set parameters for two different costmaps
- `global_costmap`
	- Used for long-term planning
- `local_costmap`
	- Used for short-term planning and collision avoidance

Layers we use for our configuration are within the `plugins` parameter
- These values are set as a list of mapped layer names that also serve as namespaces for the layer parameters we set up defining the type of plugin to be loaded for that specific layer

For the static layer, we set `map_subscribe_transient_local` = `True`. This sets the QoS settings for the map topic

Another important parameter is the `map_topic` which defines the map topic to subscribe to. This defaults to `/map` when not defined


# Transforms 
`odom` --> `base_link` 
slam_toolbox: publishes the `map` --> `odom` transformation
- Messages published on the `map` topic will be used by the static layer of the `global_costmap`