---
type: note
---
### Distro: Humble

# [Creating the launch File](https://docs.ros.org/en/humble/Tutorials/Advanced/Simulators/Webots/Setting-Up-Simulation-Webots-Basic.html#create-the-launch-file)


```python
<plugin type="my_package.my_robot_driver.MyRobotDriver">
    <parameterName>someValue</parameterName>
</plugin>
```


If you had more robots in the simulation, you would have to run one instance of the robot driver node per robot. 
- `robot_name` parameter is used to define the name of the robot the driver should connect to. The `robot_description` parameter holds the path to the URDF file which refers to the `MyRobotDriver` plugin. You can see that the `WebotsController` node as the interface that connects your controller plugin to the target robot.
```python
my_robot_driver = WebotsController(
    robot_name='my_robot',
    parameters=[
        {'robot_description': robot_description_path},
    ]
)
```


## Example

```python
import os
import launch
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from webots_ros2_driver.webots_launcher import WebotsLauncher
from webots_ros2_driver.webots_controller import WebotsController


def generate_launch_description():
    package_dir = get_package_share_directory('my_package')
    robot_description_path = os.path.join(package_dir, 'resource', 'my_robot.urdf')

    webots = WebotsLauncher(
        world=os.path.join(package_dir, 'worlds', 'my_world.wbt')
    )

    my_robot_driver = WebotsController(
        robot_name='my_robot',
        parameters=[
            {'robot_description': robot_description_path},
        ]
    )

    return LaunchDescription([
        webots,
        my_robot_driver,
        launch.actions.RegisterEventHandler(
            event_handler=launch.event_handlers.OnProcessExit(
                target_action=webots,
                on_exit=[launch.actions.EmitEvent(event=launch.events.Shutdown())],
            )
        )
    ])
```