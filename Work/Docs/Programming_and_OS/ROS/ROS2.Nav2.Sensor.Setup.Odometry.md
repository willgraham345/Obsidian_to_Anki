---
tags: note/ROS
type: note
---
# Odometry Intro
See [[ROS2.odom]]

# Simulating an Odometry System Using Gazebo
- We'll setup Gazebo and plugins required to make it work with ROS2

# Robot Localization Demo
`robot_localization` is used to provide a fused and locally accurate smooth odometry information from data provided by `N` odometry sensor inputs. 
- This information can be provided to the package through [[ROS2.Interfaces.Odometry]], [[ROS2 Interfaces Imu]], [[ROS2 Interfaces PoseWithCovarianceStamped]], [[ROS2 Interfaces TwistWithCovarianceStamped]] messages.

A usual robot setup consists of at least wheel encoders and IMU as its odometry sensor sources
When multiple sources are provided to `robot_localization`, it is able to fuse the odometry given by the sensors through state estimation nodes. 
- These nodes make use of an EKF or UKF

Fused sensor data is published by `robot_localization` package through the `odometry/filtered` and `accel/filtered`
- If enabled in its configuration, it can also publish the `odom` --> `base_link` transform on the `/tf` topic
