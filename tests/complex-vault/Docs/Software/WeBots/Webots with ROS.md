---
type: note
---
There are two ways to use WeBots with ROS
1. Standard ROS controller
2. Custom ROS controller


## Standard ROS Controller
- Uses libCppController library
- During simulation, there can be multiple instances of robots or devices and other WeBots applications connected to the ROS network
	- Controller uses a specific syntax to declare its services or topics on the network

### Controller Syntax
`[robot_name_space]/[device_name]/[service/topic_name]`
- `[robot_name_space]`: ROS namespace to group services, topics and parameters
- `[device_name]`: shows you which device it refers to 
- `[service/topic_name]`: Identical or very close to Webots function it corresponds to
## Custom ROS Controller
- It is possible to implement a ROS node in C++ using the roscpp library
	- You'll need to setup a build configuration to handle both the catkin_make from ROS and the Makefile from Webots. 
- Generic solution is to use an extern controller and run the controller as a regular ROS node on the ROS side. 