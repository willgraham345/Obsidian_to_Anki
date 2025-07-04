---
tags: note/ROS
type: note
---
Launch files may have arguments which affect their behavior. Substitutions can be used to provide more flexibility to affect this behavior with reusable launch files. 

Substitutions are variables that are only evaluated during execution of the launch description and can be used to acquire specific information like a launch configuration, an environment variable, or to evaluate an arbitrary python expression. 


	
## Parent launch file
```python
from launch_ros.substitutions import FindPackageShare

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution


def generate_launch_description():
    colors = {
        'background_r': '200'
    }

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('launch_tutorial'),
                    'launch',
                    'example_substitutions.launch.py'
                ])
            ]),
            launch_arguments={
                'turtlesim_ns': 'turtlesim2',
                'use_provided_red': 'True',
                'new_background_r': TextSubstitution(text=str(colors['background_r']))
            }.items()
        )
    ])
```
`FindPackageShare` substitution (code 1) is used to find the path to the `launch_tutorial` package.
- `PathJoinSubstitution` substitution is then used to join the path to that package path with the file `example_substitutions.launch.py` name (code 2). 

##### code 1
```python
PathJoinSubstitution([
    FindPackageShare('launch_tutorial'),
    'launch',
    'example_substitutions.launch.py'
])
```
##### code 2
```python
launch_arguments={
    'turtlesim_ns': 'turtlesim2',
    'use_provided_red': 'True',
    'new_background_r': TextSubstitution(text=str(colors['background_r']))
}.items()
```

## Substitutions Example Launch File
```python
from launch_ros.actions import Node

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, TimerAction
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, PythonExpression


def generate_launch_description():
    turtlesim_ns = LaunchConfiguration('turtlesim_ns')
    use_provided_red = LaunchConfiguration('use_provided_red')
    new_background_r = LaunchConfiguration('new_background_r')

    turtlesim_ns_launch_arg = DeclareLaunchArgument(
        'turtlesim_ns',
        default_value='turtlesim1'
    )
    use_provided_red_launch_arg = DeclareLaunchArgument(
        'use_provided_red',
        default_value='False'
    )
    new_background_r_launch_arg = DeclareLaunchArgument(
        'new_background_r',
        default_value='200'
    )

    turtlesim_node = Node(
        package='turtlesim',
        namespace=turtlesim_ns,
        executable='turtlesim_node',
        name='sim'
    )
    spawn_turtle = ExecuteProcess(
        cmd=[[
            'ros2 service call ',
            turtlesim_ns,
            '/spawn ',
            'turtlesim/srv/Spawn ',
            '"{x: 2, y: 2, theta: 0.2}"'
        ]],
        shell=True
    )
    change_background_r = ExecuteProcess(
        cmd=[[
            'ros2 param set ',
            turtlesim_ns,
            '/sim background_r ',
            '120'
        ]],
        shell=True
    )
    change_background_r_conditioned = ExecuteProcess(
        condition=IfCondition(
            PythonExpression([
                new_background_r,
                ' == 200',
                ' and ',
                use_provided_red
            ])
        ),
        cmd=[[
            'ros2 param set ',
            turtlesim_ns,
            '/sim background_r ',
            new_background_r
        ]],
        shell=True
    )

    return LaunchDescription([
        turtlesim_ns_launch_arg,
        use_provided_red_launch_arg,
        new_background_r_launch_arg,
        turtlesim_node,
        spawn_turtle,
        change_background_r,
        TimerAction(
            period=2.0,
            actions=[change_background_r_conditioned],
        )
    ])
```

`turtlesim_ns`, `use_provided_red`, and `new_background_r` launch configurations are defined. 
- They are used to store values of launch arguments in the above variables and pass them to the required actions. 

##### `DeclareLaunchArgument`
- Used to define the launch argument that it can be passed from the above launch file or from the console. 

## Modifying Launch Arguments
If you want to change the provided launch arguments, you can either update them in the `launch_arguments` dictionary in the `example_main.launch.py`, or launch the example `example_substitutions.launch.py` with the preferred arguments. 





Basically
`launch_webots_world_child.py`
`launch_webots_world_parent.py`
`launch_webots_spawn_child.py`




# General substitutions inside `launch.substitutions`
### EnvironmentVariable 
- Substitution that gets an environment variable value as a string, e.g.
`EnvironmentVariable('USER')`

### LaunchConfiguration
- Substitution that can access launch configuration variables
`LaunchConfiguration('use_sim_time', default=True)`

### PathJoinSubstitution
- Substitution to join paths, in a platform independent way
`PathJoinSubstitution([FindPackageShare("ur_description"), "rviz", "view_robot.rviz"])`

### PythonExpression 
- Substitution that can access contextual local variables. The expression may contain Substitutions, but must return something that can be converted to a string with str().
`PythonExpression([EnvironmentVariable('USER'), " == 'Alex'"])`
### TextSubstitution 
- Substitution that wraps a single string text.
`TextSubstitution(text='my_substitution_text')`
### ThisLaunchFile 
- Substitution that takes no arguments and returns the absolute path to the current launch file:
`ThisLaunchFile()`
### ThisLaunchFileDir 
- Substitution that takes no arguments and returns the absolute path to the directory of the current launch file:
1
`ThisLaunchFileDir()`
### FindExecutable
Substitution that tries to locate an executable on the PATH, e.g.:
1
`FindExecutable('executable_name')`
### LocalSubstitution
- Substitution that can access contextual local variables. e.g.:
`LocalSubstitution('event.reason')`
Command 
- Substitution that gets the output of a command as a string
`Command(command='linux_command')`
### AnonName 
- Generates an anonymous id based on name.
`AnonName('name_that_gets_an_anonymous_id')`
### NotSubstitution 
- Substitution that returns ‘not’ of the input boolean value
`NotSubstitution(PythonExpression('true')`