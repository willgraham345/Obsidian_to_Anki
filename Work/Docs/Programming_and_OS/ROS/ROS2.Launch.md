---
tags: note/ROS
type: note
---
# Background
ROS2 systems typically consist of many different nodes across many different processes. The launch system was mad to help automate the running. 
- Configuration includes:
	- What programs to run
	- Where to run programs
	- What arguments to pass programs
	- ROS-specific conventions which make it easy to reuse components throughout the system by giving them each a different configuration

## Creating a launch file
Can be in python, XML, or yaml
- Python
	- From launch import LaunchDescription
	- From launch_ros.actions import Node
Launching and monitoring multiple nodes
Using substitutions
Using event handlers
Managing large projects

# Commands
| Launch                                | Description |
| ------------------------------------- | ----------- |
| `ros2 launch <package> <launch-file>` | Does exactly what it sounds like            |

# Launch Entities and Launch Descriptions
`:class:launch.LaunchDescriptionEntity`, from which other entities that are launched inherit. 
- The class, or the classes derived from this class, are responsible for capturing the system architect's intent for how the system should be launched and how it should respond to asynchronous events in the system during launch. 
- A launch description entity has its `:meth:launch.LaunchDescriptionEntity.visit` method called during launching. 

`:class:launch.LaunchDescription` class encapsulates the intent of the user as a list of discrete `:class:launch.Action`'s 

Launch descriptions, and the actions they contain, can have references to `:class:launch.Substitution` within them. 
- These substitutions are things that can be evaluated during launch and can be used to do various things like:
	- Get a launch configuration
	- Get an environment variable
	- Evaluate arbitrary python expressions

## Action Classes

## Passing CLI Arguments In A Launch File
```python
from launch_ros.actions import Node
 
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration
 
def generate_launch_description():
    new_background_r_value = LaunchConfiguration('new_background_r')
 
    new_background_r_launch_arg = DeclareLaunchArgument(
        'new_background_r',
        default_value='200'
    )
 
    turtlesim_node = Node(
        package='turtlesim',
        executable='turtlesim_node',
        name='sim'
    )
 
    change_background_r_conditioned = ExecuteProcess(
        cmd=[[
            'ros2 param set ',
            '/sim background_r ',
            new_background_r_value
        ]],
        shell=True
    )
 
    return LaunchDescription([
        new_background_r_launch_arg,
        turtlesim_node,
        change_background_r_conditioned
    ])
```

## Include Arguments From Another Launch File
```python
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource
 
def generate_launch_description():
    return LaunchDescription([
        IncludeLaunchDescription(
                PythonLaunchDescriptionSource([
                    FindPackageShare("gazebo_ros"), '/launch', '/gazebo.launch.py'])
            )
    ])
```

## Composing Multiple Nodes into a Single Process
[[Ros2.Launch.Composable.Nodes]]