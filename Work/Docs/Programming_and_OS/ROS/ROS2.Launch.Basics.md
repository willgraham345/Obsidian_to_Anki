---
tags: note/ROS
type: note
---
# Background
[Understanding Ros2 Launch Files](https://github.com/MetroRobots/rosetta_launch)
Launch files can start and stop different nodes, trigger and act on various events. 

How we can leverage nodes
- Nodes can be remapped for easier launching
- Substitutions = variables that are evaluated only during the execution of the launch description
	- Can be used in arguments to provide more flexibility when describing reusable launch files
	- `LaunchConfiguration`, environment variable, or 


## Substitutions
### Setting Parameters Directly
```python
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(name='does_machines',
             package='donatello',
             executable='donatello_node',
             parameters=[{'pizza': 'mushrooms',
                          'brothers': ['leo', 'mike', 'raph']}]),
    ])
```
### Load Parameters from a YAML
```python
from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    return LaunchDescription([
        Node(name='does_machines',
             package='donatello',
             executable='donatello_node',
             parameters=[PathJoinSubstitution(FindPackageShare('donatello'), 'config', 'params.yaml')]), # How to change parameters from a YAML
    ])
```
### Command Line Argument
```python
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('pizza_type', default_value='mushrooms'),
        Node(name='does_machines',
             package='donatello',
             executable='donatello_node',
             parameters=[{'pizza': LaunchConfiguration('pizza_type')}]),
    ])
```
- Argument declared using `DeclareLaunchArgument`
- Value can be used with the `LaunchConfiguration` object
- 