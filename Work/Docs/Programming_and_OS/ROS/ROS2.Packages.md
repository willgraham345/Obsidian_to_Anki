---
tags: note/ROS
type: note
---
# Background
What is a package?
- An independent unit inside your application (ROS 2 instance/system). This will have nodes inside of them, with associated drivers. 

Don’t forget to source the local file (. Install/local_setup.bash)
## File and Folder Structure in a Package
Files/folders that this will automatically create
- Cmake
	- Include (folder)
	- Src (folder)
		- Custom C++ nodes go here in the future
	- Package.xml
		- Dependencies listed here
	- CMakeLists.txt
		- Dependencies listed here
- Python
	- My_package
		- Custom python nodes go here in the future
	- Package.xml
		- Fields
			- Maintainer = your name and email
			- Description = package description
			- License = some kind of open source license (read about these before doing anything)
		- _depend
			- This is where you list dependencies REALLY important
		- Setup.py has the same description, maintainer and license fields. Version and name package_name must match exactly in both files
	- Resource
	- Setup.cfg
	- Setup.py
	- test
[Example ROS2 Packages](https://automaticaddison.com/organizing-files-and-folders-inside-a-ros-2-package/)

# Commands
|                                                            |                          |
| ---------------------------------------------------------- | ------------------------ |
| `ros2 pkg create --build-type ament_cmake <package_name>`  | Creates a Cpp package    |
| `ros2 pkg create --build-type ament_python <package_name>` | Creates a python package |
| `colcon build`                                             | Builds package           |
| `colcon build --packages-select my_package`                | Only builds `my_package`                         |
