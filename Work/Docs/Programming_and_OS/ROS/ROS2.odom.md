---
tags: note/ROS
type: note
---
# Background
- A locally accurate estimate of a robot's pose and velocity based on its motion.
	- This data can be obtained from various sources (IMU, LIDAR, RADAR, VIO, and wheel encoders)
- A coordinate frame fixed frame relative to the robot's starting position. 
- The odom frame will drift over time, but it is a smooth transformation. This smoothness is important for certain controllers.
- The odom frame will interact with the map frame by receiving the map frame as its parent. 

- The `odom` frame and the transformation associated with it use a robot's odometry system to publish localization information that is continuous but becomes less accurate over time.
	- This information can still be used to navigate immediate vicinity.

- To obtain consistently accurate odometry information over time, the `map` frame provides globally accurate information that is used to correct the `odom` frame.



## Odom and Nav2
### Required Transform
As discussed in REP 105, the `odom` is connected to the rest of the system and Nav2 from `odom` --> `base_link`
- This transform is provided by a tf2 broadcaster, or frameworks like `robot_localization`
### Publishing of `nav_msgs/Odometry`
In addition to the required transform, Nav2 also requires the publishing of the `nav_msgs/Odometry` message because it provides velocity information about the robot. 

What is in 

# Usage
## Publishing Odometry Information 
```c
#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include <nav_msgs/Odometry.h>
int main(int argc, char** argv){
  ros::init(argc, argv, "odometry_publisher");
  ros::NodeHandle n;
  ros::Publisher odom_pub = n.advertise<nav_msgs::Odometry>("odom", 50);
  tf::TransformBroadcaster odom_broadcaster;
  double x = 0.0;
  double y = 0.0;
  double th = 0.0;
  double vx = 0.1;
  double vy = -0.1;
  double vth = 0.1;
  ros::Time current_time, last_time;
  current_time = ros::Time::now();
  last_time = ros::Time::now();
  ros::Rate r(1.0);
  while(n.ok()){
    ros::spinOnce();               // check for incoming messages
    current_time = ros::Time::now();
    //compute odometry in a typical way given the velocities of the robot
    double dt = (current_time - last_time).toSec();
    double delta_x = (vx * cos(th) - vy * sin(th)) * dt;
    double delta_y = (vx * sin(th) + vy * cos(th)) * dt;
    double delta_th = vth * dt;
    x += delta_x;
    y += delta_y;
    th += delta_th;
    //since all odometry is 6DOF we'll need a quaternion created from yaw
    geometry_msgs::Quaternion odom_quat = tf::createQuaternionMsgFromYaw(th);
    //first, we'll publish the transform over tf
    geometry_msgs::TransformStamped odom_trans;
    odom_trans.header.stamp = current_time;
    odom_trans.header.frame_id = "odom";
    odom_trans.child_frame_id = "base_link";
    odom_trans.transform.translation.x = x;
    odom_trans.transform.translation.y = y;
    odom_trans.transform.translation.z = 0.0;
    odom_trans.transform.rotation = odom_quat;
    //send the transform
    odom_broadcaster.sendTransform(odom_trans);
    //next, we'll publish the odometry message over ROS
    nav_msgs::Odometry odom;
    odom.header.stamp = current_time;
    odom.header.frame_id = "odom";
    //set the position
    odom.pose.pose.position.x = x;
    odom.pose.pose.position.y = y;
    odom.pose.pose.position.z = 0.0;
    odom.pose.pose.orientation = odom_quat;
    //set the velocity
    odom.child_frame_id = "base_link";
    odom.twist.twist.linear.x = vx;
    odom.twist.twist.linear.y = vy;
    odom.twist.twist.angular.z = vth;
    //publish the message
    odom_pub.publish(odom);
    last_time = current_time;
    r.sleep();
  }
}
```
## Example: Robot with Wheel Encoders
The goal in setting up odometry is:
1. To compute odometry information and publish the `nav_msgs/Odometry` message
2. `odom` --> `base_link` transform over ROS2

To calculate this, we'll need some sort of code that translates wheel encoder information to odometry info similar to the below snippet:
```python
linear = (right_wheel_est_vel + left_wheel_est_vel) / 2
angular = (right_wheel_est_vel - left_wheel_est_vel) / wheel_separation;
```
- Publishing this as an Odometry Message [Example](https://wiki.ros.org/navigation/Tutorials/RobotSetup/Odom/)

An alternative to manually publishing this information is through the [[ROS2 ros control]] framework. It contains various packages for real-time control of robots in ROS2. 
- Wheel encoders --> `diff_drive_controller`
	- Takes in the `geometry_msgs/Twist` messages published on `cmd_vel` topic, computes odometry information, and publishes `nav_msgs/Odometry` messages on `odom` topic. 

For other types of sensors, their respective ROS drivers should have documentation on how to publish odometry information. 


