---
type: note
---
1. Create package
2. Setup simulation world
3. In launch file, create a `WebotsController` node
	1. Needs to have the `robot_name` passed to it, along with a parameter of the `robot_description_path`
		1. This path is a URDF describing your plugin
			1. [[Webots Example URDF]]
		2. Your plugin is a custom class that will initialize a ros2 node, get all relevant devices connected to the robot, set up callbacks, and define the ros2 `step` function
4. Edit `my_robot_driver` plugin
	1. `webots_ros2_driver` subpackage creates a ROS2 interface for most sensors. Creating a custom plugin will extend this interface equivalent to a robot controller.
		1. You can use this to access the [Webots robot API](https://cyberbotics.com/doc/reference/robot?tab-language=python)
		2. The `MyRobotDriver` 