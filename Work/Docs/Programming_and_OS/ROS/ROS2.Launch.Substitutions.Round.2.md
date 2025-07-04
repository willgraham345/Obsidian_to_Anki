---
tags: note/ROS
type: note
---
[Read Here](https://roboticscasual.com/tutorial-ros2-launch-files-all-you-need-to-know/#launch-substitutions)

## `EnvironmentVariable` Substitution
What is an `EnvironmentVariable`?
- A dynamic value that you can access inside the environment your process runs in
	- In the case below, it is the terminal from which you start the launch file. The `USER` field is defined by the system. 
```python
from launch import LaunchDescription
from launch.substitutions import EnvironmentVariable
from launch_ros.actions import Node
 
def generate_launch_description():
   return LaunchDescription([
      Node(
            package='turtlesim',
            executable='turtlesim_node',
            name=[EnvironmentVariable('USER'), '_turtlesim'],
      ),
   ])
```

