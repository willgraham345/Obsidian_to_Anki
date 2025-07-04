---
tags: note/ROS
type: note
---
# Background
A tool to check ROS2 setup and other potential issues such as network, package versions, rmw middleware

# Commands
| Doctor               | Description                         |
| -------------------- | ----------------------------------- |
| `ros2 doctor`        | Show potential issues within ROS2   |
| `ros2 doctor -r`     | Output report of all checks         |
| `ros2 doctor -rf`    | Output report of failed checks only |
| `ros2 component -iw` | Include warnings as failed checks                                    |
