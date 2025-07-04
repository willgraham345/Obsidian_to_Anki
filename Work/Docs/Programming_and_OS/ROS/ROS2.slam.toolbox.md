---
tags: note/ROS
type: note
---
# Background
[Source Code](https://github.com/SteveMacenski/slam_toolbox?tab=readme-ov-file)
Capabilities
- 2D SLAM for mobile robotics
- Life-long mapping
- Optimization-based localization built on the pose-graph
- Synchronous and asynchronous modes of mapping
- Kinetic map merging
- Plugin-based optimization solvers
- RVIZ plugin for interaction with the tools
- Graph manipulation tools in RVIZ

# API
See rviz plugin for an implementation of the use
Subscribed topics
`/scan` : [[ROS2.Interfaces.LaserScan]] 

| Subscribed Topics | Data Type | Description |
| ---- | ---- | ---- |
| `/scan` | [[ROS2.Interfaces.LaserScan]] | Input scan from laser to utilize |
| `/tf` | NA | Valid transform of your configured `odom_frame` to `base_frame` |

| Published Topics | Data Type | Description |
| ---- | ---- | ---- |
| `map` | [[ROS2 Occupancy Grid]] | Representation of the pose-graph at `map_update_interval` frequency |
| `pose` | [[ROS2 Interfaces PoseWithCovarianceStamped]] | Pose of the `base_frame` in the configured `map_frame` along with the covariance calculated from the scan match |

|Exposed Topic |Type|Description|
|---|---|---|
|`/slam_toolbox/clear_changes`|`slam_toolbox/Clear`|Clear all manual pose-graph manipulation changes pending|
|`/slam_toolbox/deserialize_map`|`slam_toolbox/DeserializePoseGraph`|Load a saved serialized pose-graph files from disk|
|`/slam_toolbox/dynamic_map`|`nav_msgs/OccupancyGrid`|Request the current state of the pose-graph as an occupancy grid|
|`/slam_toolbox/manual_loop_closure`|`slam_toolbox/LoopClosure`|Request the manual changes to the pose-graph pending to be processed|
|`/slam_toolbox/pause_new_measurements`|`slam_toolbox/Pause`|Pause processing of new incoming laser scans by the toolbox|
|`/slam_toolbox/save_map`|`slam_toolbox/SaveMap`|Save the map image file of the pose-graph that is useable for display or AMCL localization. It is a simple wrapper on `map_server/map_saver` but is useful.|
|`/slam_toolbox/serialize_map`|`slam_toolbox/SerializePoseGraph`|Save the map pose-graph and datathat is useable for continued mapping, slam_toolbox localization, offline manipulation, and more|
|`/slam_toolbox/toggle_interactive_mode`|`slam_toolbox/ToggleInteractive`|Toggling in and out of interactive mode, publishing interactive markers of the nodes and their positions to be updated in an application|
