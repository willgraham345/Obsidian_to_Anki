---
tags: note/ROS
type: note
---
# Basic Idea
## Viewing Documentation
```bash
ros2 command --help
```

```bash
ros2 command verb -h
```

# Inspecting
| Inspection | Description | Flags |
| ---- | ---- | ---- |
| `ros2 action list -t` | Shows actions with their associated types |  |
| `ros2 interface list` | HUGELY useful tool that outlines all actions, messages, and services within thing |  |
| `ros2 interface proto <type>` | Output an interface prototype |  |
| `ros2 interface show <package_name/message_type>` | Gets info about a message type |  |
| `ros2 lifecycle set <node> <state>` | Sets the lifecycle state of a specific node. |  |
| `ros2 lifecycle transition <node>` | Transitions a node to its next lifecycle state. |  |
| `ros2 lifecycle info <node>` | Provides information about the node's lifecycle. |  |
| `ros2 lifecycle configure <node>` | Configures parameters for the lifecycle node. |  |
| `ros2 node list` | Returns a list of running nodes |  |
| `ros2 node info <node_name>` | Returns a list of subscribers, publishers, services, and actions (ROS graph connections) that interact with that node) |  |
| `ros2 topic list` | Returns a list of all topics running |  |
| `ros2 topic echo <topic_name>` | Listens to the given topic |  |
| `ros2 topic echo /topic_name` | Display messages published on a specific topic. |  |
| `ros2 topic hz /topic_name` | Show the publishing rate of a specific topic. |  |
| `ros2 topic pub /topic_name <msg_type>` | Publish a message on a specific topic. |  |
| `ros2 topic info /topic_name` | Display information about a specific topic. | `v` = verbose |
| `ros2 topic bw /topic_name` | Show the bandwidth used by a specific topic. |  |
| `ros2 topic find <msg_type>` | Find topics that publish a specific message type. |  |
| `ros2 node info` | Output info about a node | `-s` = enable ROS simulation time |
| `ros2 node list` | List all available nodes | `-a` = all, `c` display count only |
|  |  |  |
| `ros2 pkg executables <pkg_name>` | Returns a list of executables within the packge |  |
| `ros2 param dump <node_name>` | Inputs all parameters from a given node into a yaml file that can be loaded later |  |
| `ros2 param get <node_name> <parameter_list>` | Gets current value of a parameter |  |
| `ros2 param list` | Prints all parameters |  |
| `ros2 param load <noad_name> <parameter_file>` | Loads a yaml file (see `param dump` above) |  |


| Doctor | Description |
| --- | --- |
| `ros2 doctor` | Show potential issues within ROS2 |
| `ros2 doctor -r` | Output report of all checks |
| `ros2 doctor -rf` | Output report of failed checks only |
| `ros2 component -iw` | Include warnings as failed checks |

| tf2 Tools | |
| --- | --- |
| `ros2 run tf2_tools view_frames` | Generates a transform table for the current ros system |

#  Launching and Building
| Actions | Description |
| ---- | ---- |
| `ros2 action info <action_name>` | Output information about an action |
| `ros2 action list <action_name>` | Output a list of action names |
| `ros2 action send_goal <action_name>` | Send an action goal |
| `ros2 action show <action_name>` | Output the action definition |
| `ros2 launch <package_name> <launch_file_name>` | Launch a launch file directly from a package |
| `ros2 launch <package_name> <launch_file_name> -d` | Launch a launch file with a debug flag |


| Building | Description |
| ---- | ---- |
| `ros2 pkg create --build-type ament_cmake <package_name>` | Creates a Cpp package |
| `ros2 pkg create --build-type ament_python <package_name>` | Creates a python package |
| `colcon build` | Builds package |
| `colcon build --packages-select my_package` | Only builds `my_package` |
| `-r <old name>:=<new name>` | Remaps names within a node to a new name |
| `-r __node:=<new node name>` | Remaps name of the node itself |
| `-r __ns:=<new node namespace` | Remaps namespace of the node |


| Execution | Description |
| ---- | ---- |
| `ros2 run <package_name> <executable_name> --ros-args --params-file <file_name>` | Will load parameters at the start of a node |

| Recording                | Description                  |
| ------------------------ | ---------------------------- |
| `ros2 info <bag-name>`   | Output information of a bag  |
| `ros2 play <bag-name>`   | Plays a bag                  |
| `ros2 record <bag-name>` | Records a bag                |
| `ros2 record -a`         | Records everything (I think) |

## Transform Publishing

| Comand                                            | Options                                                                                                                                        | Descriptions                                           |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| `ros2 run tf2_ros static_transform_publisher`<br> | `--x x`<br>`--y y`<br>`--z z`<br>`--yaw yaw`<br>`--pitch pitch`<br>`--roll roll`<br>`--frame-id frame_id`<br>`--child-frame-id child_frame_id` | Launches a static transformer between two given frames |
|                                                   |                                                                                                                                                |                                                        |
