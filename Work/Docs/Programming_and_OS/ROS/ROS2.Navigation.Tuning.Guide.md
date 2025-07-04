---
tags: note/ROS
type: note
---
# Background
Based on a [post from Kaiyu Zheng](https://kaiyuzheng.me/documents/navguide.pdf)

# 1. Velocity and Acceleration
DWA = dynamic-window approach
TEB = timed elastic band

Local planner takes messages in odometry messages (`odom` topic) and outputs velocity commands (`cmd_vel`). 
- Max/min velocity and acceleration are two basic parameters for the mobile base. 

## 1.1 To obtain maximum velocity
In ROS you can subscribe to the `odom` topic to obtain current odom info.  


$x$ velocity means the velocity in the direction parallel to robot's straight movement. Same as translational velocity. 

$y$ velocity is the velocity in the direction perpendicular to $x$ velocity movement. This can be thought of as strafing velocity.

# Global Planner
## Global Planners
To use the `move_base` node in navigation stack, we need to have a global planner and a local planner. There are three global planners that adhere to `nave_core:BaseGlobal` `Planner` interface:
- `carrot_planner`
- `navfn`
- `global_planner`
### carrot_planner
Simplest one. It checks if the given goal is an obstacle, and if so, picks an alternative goal close to the original, by moving back along the vector between the robot and the goal point. Eventually it passes this valid goal as a plan to the local planner or controller (internally). Does not do any global path planning. 

### navfn and global_planner
`navfn` uses Dijkstra's algorithm
`global_planner` uses a more flexible replacement with more options. 
- Support for `A*`, 
- Toggling quadratic approximation
- Toggling grid path

### Global Planner Parameters
`global_parameter` is generally what we want, so we'll take a look at the parameters

# AMCL
A ROS package that deals with robot localization. 
Each sample stores a position and orientation representing the robot's pose. Particles are all sampled randomly initially. When a robot moves, particles are resampled based on their current state as well as the robot's action using recursive Bayesian estimation. 

MCL maintains a motion model, and a measurement model. 
## Header in `LaserScan` messages
Messages published to the `scan` topic are of type `sensor_msgs/LaserScan` and have a header with dependent fields on the specific laser scanner you are using. 
## Parameters for measurement and motion models
- Parameters listed in the `amcl` package about tuning the laser scanner model (measurement) and odometry model (motion). 
	- A detailed discussion requires lots of understanding of the MCL algorithm. 
## Translation of the laser scanner
There is a `tf` transform from `laser_link` to `base_footprint` or `base_link` that indicates the pose of the laser scanner with respect to the robot base. If this transform is incorrect, it is very likely that the localization behaves strangely. 
- This is usually handled in `urdf` and `srdf` specification on your robot. If you are using a `rosbag` file, you may have to publish the transform yourself. 