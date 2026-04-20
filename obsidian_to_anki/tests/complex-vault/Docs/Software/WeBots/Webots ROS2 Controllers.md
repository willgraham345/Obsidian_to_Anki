---
type: note
---
`webots_ros2_driver` will automatically create a ROS 2 interface for most sensors. We can extend this interface with a custom plugin, equivalent to a robot controller. 
- We can use the Webots robot API to create your own topics and services to control a robot


Creating a custom class in python
```python
import rclpy
from geometry_msgs.msg import Twist

HALF_DISTANCE_BETWEEN_WHEELS = 0.045
WHEEL_RADIUS = 0.025

class MyRobotDriver:
    def init(self, webots_node, properties):
        self.__robot = webots_node.robot

        self.__left_motor = self.__robot.getDevice('left wheel motor')
        self.__right_motor = self.__robot.getDevice('right wheel motor')

        self.__left_motor.setPosition(float('inf'))
        self.__left_motor.setVelocity(0)

        self.__right_motor.setPosition(float('inf'))
        self.__right_motor.setVelocity(0)

        self.__target_twist = Twist()

        rclpy.init(args=None)
        self.__node = rclpy.create_node('my_robot_driver')
        self.__node.create_subscription(Twist, 'cmd_vel', self.__cmd_vel_callback, 1)

    def __cmd_vel_callback(self, twist):
        self.__target_twist = twist

    def step(self):
        rclpy.spin_once(self.__node, timeout_sec=0)

        forward_speed = self.__target_twist.linear.x
        angular_speed = self.__target_twist.angular.z

        command_motor_left = (forward_speed - angular_speed * HALF_DISTANCE_BETWEEN_WHEELS) / WHEEL_RADIUS
        command_motor_right = (forward_speed + angular_speed * HALF_DISTANCE_BETWEEN_WHEELS) / WHEEL_RADIUS

        self.__left_motor.setVelocity(command_motor_left)
        self.__right_motor.setVelocity(command_motor_right)
```
`MyRobotDriver` implements 3 methods
- `init(self, ...)`: ROS counterpart of the Python init constructor.
	- Takes two arguments
		- `webots_node`: reference to Webots instance
		- `properties`: dictionary created from the XML tags given in the URDF files. See more here: [[Webots URDF]]
The robot instance in the simulation `self.__robot` can be used to access the Webots robot API. 
- Then it gets two motor instances and initializes them with a target position and a target velocity. 
	- A ROS node is then created and a callback method is registered for a ROS topic named `\cmd_vel` that handles `Twist` messages
		- After that, we implement the `__cmd_vel_callback(self, twist)` callback private method that will be called for each `Twist` message received on the `/cmd_vel` topic and will save it in the `self.__target_twist` member variable. 

`step(self)` method is called every time step of the simulation. The call to `rclpy.spin_once()` is needed to keep the ROS node running smoothly. 
- At each step it will retrieve the desired `forward_speed` and `angular_speed` from `self.__target_twist`