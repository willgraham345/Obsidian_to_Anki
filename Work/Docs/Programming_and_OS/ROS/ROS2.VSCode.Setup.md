---
tags: note/ROS
type: note
---
# Setup
[Official Extension Page](https://marketplace.visualstudio.com/items?itemName=ms-iot.vscode-ros#:~:text=The%20Visual%20Studio%20Code%20extension%20for%20ROS%20supports%20launch%20debugging,py%20for%20ROS2.)
[Github Repo for Extension](https://github.com/ms-iot/vscode-ros)
- Use this for the discussions
# Background/Misc
## Necessary Extensions
1. Install the Microsoft ROS extension, followed by a restart
	1. This should initiate the installation of Microsoft C/C++ and Microsoft Python
2. Install the C/C++ Extension Pack
	1. Provides Intellisense & C++ file navigation
	2. Will install CMake extension
### Other extensions
VSCode can also be used to develop remotely via SSH. You'd ned to install the Microsoft Remote SSH


Development on Docker
- VSCode can be used to develop on docker. You must install an extension called Microsoft De Containers
- You should also install the extension called Microsoft Dockerr, which allows you to work with containers and images
	- For more info, see [Attach to a running container](https://code.visualstudio.com/docs/devcontainers/attach-container)

## Sourcing ROS Dependencies
### For local development
#### Solution 1
You can source your ROS2 workspace in the same Debug console and try again
```shell
source install/setup.bash
```

#### Solution 2
You can modify the user .bashrc to source your ROS2 workspace whenever you attach VSCode to the container

#### Solution 3, for Docker Containers
If you do not want to run a command every time you start a debug session and you can't modify the .bashrc, you can use this approach

You want to execute a `source` command every time VSCode opens the container
- The VSCode DevContainer extension allows you to edit the JSon container configuration file, providing a field for this purpose. 


# Helpful Links
[Guide to VSCode with ROS2](https://picknik.ai/vscode/docker/ros2/2024/01/23/ROS2-and-VSCode.html)
[VSCode, Docker and ROS2](https://www.allisonthackston.com/articles/vscode-docker-ros2.html)