---
type: note
---
# Background
- Use `Ros2Supervisor` to import a URDF into WeBots. 
- A request has to be sent to the `Ros2Supervisor` node, done with the `URDFSpawner` process
- `webots_ros2_driver` has to be started after the URDF robot has been spawned. This is done by adding an `event_handler` on the URDFSpawner. 
[Ros2SupervisorNode](https://github.com/cyberbotics/webots_ros2/wiki/Tutorial-Ros2Supervisor-Node)

## Arguments
- `name` **(string):** Set the name of the robot in the simulation. It is required and has to be unique in the simulation.
- `urdf_path` **(string):** Set the path to the URDF file to convert. Has to be specified if `robot_description` is not specified.
- `robot_description` **(string):** Set the content of a URDF file to convert. Has to be specified if `urdf_path` is not specified.
- `translation` **(string):** Set the position of the robot when it will be spawned in the simulation.
- `rotation` **(string):** Set the rotation of the robot when it will be spawned in the simulation.
- `normal` **(bool):** If set, the normals are exported if present in the URDF definition. Default is `False`.
- `box_collision` **(bool):** If set, the bounding objects are approximated using boxes. Default is `False`.
- `init_pos` **(string):** Set the initial positions of your robot joints. Example: `init_pos='[1.2, 0.5, -1.5]'` would set the first 3 joints of your robot to the specified values, and leave the rest with their default value.
- `relative_path_prefix` **(string):** If `robot_description` is used, the relative paths in your URDF file will use this prefix. Example: `filename='head.obj'` with `relative_path_prefix='/home/user/myRobot/'` will become `filename='/home/user/myRobot/head.obj'`.


## Template
```python
import os
import pathlib
import launch
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.substitutions.path_join_substitution import PathJoinSubstitution
from launch_ros.actions import Node
from webots_ros2_driver.urdf_spawner import URDFSpawner, get_webots_driver_node
from webots_ros2_driver.webots_launcher import WebotsLauncher

def generate_launch_description():
    world = LaunchConfiguration('world')
    package_dir = get_package_share_directory("my_package")
    urdf_path = os.path.join(package_dir, 'resource', 'my_urdf_file.urdf')
    robot_description = pathlib.Path(urdf_path).read_text()

    # Define your URDF robots here
    # The name of an URDF robot has to match the WEBOTS_CONTROLLER_URL of the driver node
    # You can specify the URDF file to use with "urdf_path"
    spawn_URDF_robot = URDFSpawner(
        name='myRobot',
        urdf_path=urdf_path,
        translation='0 0 1',
        rotation='0 0 1 -1.5708',
    )

    # Driver nodes
    # When having multiple robot it is enough to specify the `additional_env` argument.
    # The `WEBOTS_CONTROLLER_URL` has to match the robot name in the world file.
    # You can check for more information at:
    # https://cyberbotics.com/doc/guide/running-extern-robot-controllers#single-simulation-and-multiple-extern-robot-controllers
    robot_driver = Node(
        package='webots_ros2_driver',
        executable='driver',
        output='screen',
        additional_env={'WEBOTS_CONTROLLER_URL': 'myRobot'},
        parameters=[
            {'robot_description': robot_description},
        ],
    )

    # The WebotsLauncher is a Webots custom action that allows you to start a Webots simulation instance.
    # It searches for the Webots installation in the path specified by the `WEBOTS_HOME` environment variable and default installation paths.
    # The Ros2Supervisor node is mandatory to spawn an URDF robot.
    # The accepted arguments are:
    # - `world` (str): Path to the world to launch.
    # - `gui` (bool): Whether to display GUI or not.
    # - `mode` (str): Can be `pause`, `realtime`, or `fast`.
    # - `ros2_supervisor` (bool): Spawn the `Ros2Supervisor` custom node that communicates with a Supervisor robot in the simulation.
    webots = WebotsLauncher(
        world=PathJoinSubstitution([package_dir, 'worlds', world]),
        ros2_supervisor=True
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'world',
            default_value='robotic_arms.wbt',
            description='Choose one of the world files from `/webots_ros2_universal_robot/worlds` directory'
        ),
        # Starts Webots
        webots,

        # Starts the Ros2Supervisor node created with the WebotsLauncher
        webots._supervisor,

        # Request the spawn of your URDF robot
        spawn_URDF_robot,

        # Launch the driver node once the URDF robot is spawned
        launch.actions.RegisterEventHandler(
            event_handler=launch.event_handlers.OnProcessIO(
                target_action=spawn_URDF_robot,
                on_stdout=lambda event: get_webots_driver_node(event, robot_driver),
            )
        ),

        # This action will kill all nodes once the Webots simulation has exited
        launch.actions.RegisterEventHandler(
            event_handler=launch.event_handlers.OnProcessExit(
                target_action=webots,
                on_exit=[launch.actions.EmitEvent(event=launch.events.Shutdown())],
            )
        )
    ])
```

