---
tags: note/ROS
type: note
---
# Background
A collection of state estimation nodes, each of which is an implementation of a nonlinear state estimator for robots moving in 3D space

Contains two state estimation nodes:
- `ekf_localization_node`
- `ukf_localization_node`

Also provides a `navsat_transform_node` which aids in the integration of GPS data


# Features 
- Fusion of an arbitrary number of sensors. 
- Support for multiple ROS message types. All state estimation nodes in `robot_localization` can take in [[ROS2.Interfaces.Odometry]], [[ROS2 Interfaces Imu]], [[ROS2 Interfaces PoseWithCovarianceStamped]], or [[ROS2 Interfaces TwistWithCovarianceStamped]] messages
- If a given sensor message contains data that you don't want to include, the state estimation nodes in `robot_localization` allow you to exclude that data on a per-sensor basis. 
- Continuous estimation. Each state estimation node in `robot_localization` begins estimating the vehicle's state as soon as it receives a single measurement. 
# Installation
```shell
sudo apt install ros-<ros2-distro>-robot-localization
```

# Configuration
We specify the parameters of the `ekf_node` using a YAML file.
- Good practice is to create a `config` directory at root of project with a file named `ekf.yaml`
## Example config
```yaml
### ekf config file ###
ekf_filter_node:
    ros__parameters:
# The frequency, in Hz, at which the filter will output a position estimate. Note that the filter will not begin
# computation until it receives at least one message from one of theinputs. It will then run continuously at the
# frequency specified here, regardless of whether it receives more measurements. Defaults to 30 if unspecified.
        frequency: 30.0

# ekf_localization_node and ukf_localization_node both use a 3D omnidirectional motion model. If this parameter is
# set to true, no 3D information will be used in your state estimate. Use this if you are operating in a planar
# environment and want to ignore the effect of small variations in the ground plane that might otherwise be detected
# by, for example, an IMU. Defaults to false if unspecified.
        two_d_mode: false

# Whether to publish the acceleration state. Defaults to false if unspecified.
        publish_acceleration: true

# Whether to broadcast the transformation over the /tf topic. Defaultsto true if unspecified.
        publish_tf: true

# 1. Set the map_frame, odom_frame, and base_link frames to the appropriate frame names for your system.
#     1a. If your system does not have a map_frame, just remove it, and make sure "world_frame" is set to the value of odom_frame.
# 2. If you are fusing continuous position data such as wheel encoder odometry, visual odometry, or IMU data, set "world_frame"
#    to your odom_frame value. This is the default behavior for robot_localization's state estimation nodes.
# 3. If you are fusing global absolute position data that is subject to discrete jumps (e.g., GPS or position updates from landmark
#    observations) then:
#     3a. Set your "world_frame" to your map_frame value
#     3b. MAKE SURE something else is generating the odom->base_link transform. Note that this can even be another state estimation node
#         from robot_localization! However, that instance should *not* fuse the global data.
        map_frame: map              # Defaults to "map" if unspecified
        odom_frame: odom            # Defaults to "odom" if unspecified
        base_link_frame: base_link  # Defaults to "base_link" ifunspecified
        world_frame: odom           # Defaults to the value ofodom_frame if unspecified

        odom0: demo/odom
        odom0_config: [true,  true,  true,
                       false, false, false,
                       false, false, false,
                       false, false, true,
                       false, false, false]

        imu0: demo/imu
        imu0_config: [false, false, false,
                      true,  true,  true,
                      false, false, false,
                      false, false, false,
                      false, false, false]
```
