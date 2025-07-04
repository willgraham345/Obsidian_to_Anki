---
tags: note/ROS
type: note
---
| Name                          | ROS 1 command | ROS 2 command  | ROS2 Object         | Note |
| ----------------------------- | ------------- | -------------- | ------------------- | ---- |
| Launch Argument               | arg           | var            | LaunchConfiguration | [1]  |
| Anonymous ID Generation       | anon          | anon           | AnonName            |      |
| Environment Variable          | env           | env            | EnvironmentVariable |      |
| Optional Environment Variable | optenv        | env            | EnvironmentVariable | [2]  |
| Command Execution             |               | command        | Command             | [3]  |
| Current Directory             | dirname       | dirname        | ThisLaunchFileDir   |      |
| ROS Package Location          | find          |                |                     | [4]  |
| Current Launch File Path      |               | filename       | ThisLaunchFile      | [4]  |
| Executable Path               |               | find-exec      | FindExecutable      | [4]  |
| ROS Executable                |               | exec-in-pkg    | ExecutableInPackage | [4]  |
| ROS Package Share Path        |               | find-pkg-share | FindPackageShare    | [4]  |
| Expression Evaluation         | eval          | eval           | PythonExpression    | [5]  |


[1] Only one with inexplicable different command in ROS 1 and 2
[2] To use optenv in ROS 2, just add the default value to the command as the second argument.
[3] There is not a general way to load the results of an arbitrary command in ROS 1, but you can load the value into a ROS Parameter (See section 04 above)
[4] ROS 2 if much finickier about where files actually are. There is no general folder that covers everything, thus the find command doesn't make sense. Instead its split up into other commands.
[5] In ROS 1, eval cannot be used in YAML files.