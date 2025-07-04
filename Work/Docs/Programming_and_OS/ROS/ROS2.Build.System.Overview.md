---
tags: note/ROS
type: note
---
They created a set of packages under moniker `ament`, so it didn't collide with `catkin`
- `ament` is to make it easier to develop and maintain ROS2 core packages

## Package overviews
### Python
```
src/
  py_launch_example/
    launch/
    package.xml
    py_launch_example/
    resource/
    setup.cfg
    setup.py
    test/
```
- `launch/`
	- For python files, the `_launch.py` suffix is recommended but not required

### C++
Only adjust the `CMakeLists.txt`
```
# Install launch files.
install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}/
)
```

## ament_package
[Source Code](https://github.com/ament/ament_package)
Provides templates for environment hooks

#### package.xml
- Package manifest file
- Marks the root of a package, has meta information
- Machine-readable XML described in: [REP 127](https://www.ros.org/reps/rep-0127.html) and [REP 140](https://www.ros.org/reps/rep-0140.html)
##### Features
- `<depend>`
	- Declares rosdep key or ROS package this package needs.
	- `<build_depend, <build_export_depend>` and `<exec_depend>` all in one
