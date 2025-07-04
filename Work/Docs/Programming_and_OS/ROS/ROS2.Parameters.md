---
tags: note/ROS
type: note
---
# Background
Parameters are configuration values for nodes. You can think of these as the node settings. Possible storage values are: integers, floats, booleans, strings, and lists. Each node in ROS2 maintains its own parmeters. 
- Parameters are addressed by: node name, node namespace, parameter name, and parameter namespace (parameter namespace is optional)

## Components of a Parameter
### Key
String
### Value
One of the following types: `bool`, `int64`, `float64`, `string`, `byte[]`, `bool[]`, `int64[]`, `float64[]` or `string[]`
### Descriptor
Default is empty, but can contain parameter descriptions, value ranges, type info, and additional constraints


## Declaring Parameters
By default, a node needs to declare all of the parameters that it will accept during its lifetime
See example below: [[ROS2.Parameters#Example Parameters within a class]]
- The node can also be instantiated with `allow_undeclared_parameters` to `true` which will allow parameters to be get and set on the node if they haven't been declared.

## Parameter Types
Attempts to change the type of a declared parameter at runtime will fail. 
If a parameter needs to be multiple types and the code using the parameter can handle it, this default behavior can be changed. 
- When the parameter is declared it should be declared using a `ParameterDescriptor` with the `dynamic_typing` member set to `true`


## Parameter callbacks
Can register two different types of callbacks and be informed when changes are happening to the parameters. Both are optional. 


## Interacting with Parameters


# Commands
|  |  |
| ---- | ---- |
| `ros2 param dump <node_name>` | Inputs all parameters into a yaml file that can be loaded later |
| `ros2 param get <node_name> <parameter_name>` | Gets current value of a parameter |
| `ros2 param list` | Print all parameters |
| `ros2 param load <node_name> <parameter_file>` | Loads a yaml file (see `param dump` above) |
| `ros2 run package_name executable_name --ros-args -p param_name:=param_value` | Pass a parameter to a node via the command line |


# Examples

## Example Parameters within a class
```python
import rclpy
import rclpy.node

class MinimalParam(rclpy.node.Node):
    def __init__(self):
        super().__init__('minimal_param_node')

        self.declare_parameter('my_parameter', 'world')

        self.timer = self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        my_param = self.get_parameter('my_parameter').get_parameter_value().string_value

        self.get_logger().info('Hello %s!' % my_param)

		# Set parameter back to default value to make sure that external changes go back to default
        my_new_param = rclpy.parameter.Parameter(
            'my_parameter',
            rclpy.Parameter.Type.STRING,
            'world'
        )
        all_new_parameters = [my_new_param]
        self.set_parameters(all_new_parameters)

def main():
    rclpy.init()
    node = MinimalParam()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
```
- The `my_param = self.get_parameter('my_parameter').get_parameter_value().string_value` grabs the value
- The `get_logger()` ensures the event is logged. 

## Changing via Launch File
```python
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='python_parameters',
            executable='minimal_param_node',
            name='custom_minimal_param_node',
            output='screen',
            emulate_tty=True,
            parameters=[
                {'my_parameter': 'earth'}
            ]
        )
    ])
```


