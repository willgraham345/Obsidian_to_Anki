---
tags: note/ROS
type: note
---
There's a great index of listed ros packages that can be used at [ROS Index](https://index.ros.org/repos/)

Good intro on installing from outside repositories: [Installing Packages](https://industrial-training-master.readthedocs.io/en/foxy/_source/session1/ros2/2-Installing-Existing-Packages.html#install-package-from-apt-repository)

# APT Installation
The general naming convention for ROS APT goes: `ros-<distro>-<package>`
- Underscores in package name are replaced with dashes
- Try pressing tab key while typing the package name


# Building from Source
## Example
Building a `fake_ar_publisher` repository into the directory

```zsh
cd ~/ros2_ws/src
git clone -b ros2 https://github.com/ros-industrial/fake_ar_publisher.git
```
- Needs to be installed within the `src/` for the package. Correct branch name is a thing to also look out for
- 
ros2 pkg prefix fake_ar_publisher


# Viewing Source Code
Source code for packages will be found in: 
```zsh
/opt/ros/<ROS_DISTRO/share/<pkg_name>
```