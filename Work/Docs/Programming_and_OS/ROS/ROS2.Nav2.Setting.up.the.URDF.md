---
tags: note/ROS
type: note
---
URDF = Unified Robot Description Fromat

We will also setup the robot state publisher and visualize our model in RVIZ
- We also will set up kinematic properties for simulation purposes

## URDF and the Robot State Publisher
One of the requirements for Nav2 is the transformation from `base_link` to the various sensors and reference frames. 
- Creating multiple publishers to handle all of these coordinate frame transformations may become tedious. Therefore, we will make use of the [[ROS2.Robot.State.Publisher]] to publish our transforms. 
- We will need to provide it with the correct URDF and it will automatically handle publishing the transforms. 
The URDF is an XML file representing a robot model. It will mainly be used to build transformation trees related to robot geometry but it also has other uses. 
- The URDF can be used to define physical properties and visualize transformations
- Can also handle XML Macros (Xacro) so we don't have to constantly redefine the URDF.

## Writing the URDF
### Example URDF
```xml
<?xml version="1.0"?>
<robot name="sam_bot" xmlns:xacro="http://ros.org/wiki/xacro">
  <!-- Define robot constants -->
  <xacro:property name="base_width" value="0.31"/>
  <xacro:property name="base_length" value="0.42"/>
  <xacro:property name="base_height" value="0.18"/>

  <xacro:property name="wheel_radius" value="0.10"/>
  <xacro:property name="wheel_width" value="0.04"/>
  <xacro:property name="wheel_ygap" value="0.025"/>
  <xacro:property name="wheel_zoff" value="0.05"/>
  <xacro:property name="wheel_xoff" value="0.12"/>

  <xacro:property name="caster_xoff" value="0.14"/>

  <!-- Robot Base -->
  <link name="base_link">
    <visual>
      <geometry>
        <box size="${base_length} ${base_width} ${base_height}"/>
      </geometry>
      <material name="Cyan">
        <color rgba="0 1.0 1.0 1.0"/>
      </material>
    </visual>
  </link>

  <!-- Robot Footprint -->
  <link name="base_footprint"/>

  <joint name="base_joint" type="fixed">
    <parent link="base_link"/>
    <child link="base_footprint"/>
    <origin xyz="0.0 0.0 ${-(wheel_radius+wheel_zoff)}" rpy="0 0 0"/>
  </joint>
</robot>
```
- `base_*` defines size of robot's main chassis
- `wheel_radius` and `wheel_width` define the shape of the robot's back wheels
- `wheel_ygap` adjusts the gap between the wheel and the chassis along the y-axis
- `wheel_zoff` and `wheel_xoff` position the back wheels along the z-axis and x-axis appropriately. 
- `caster_xoff` positions front caster along the x-axis
- `base_link` properties can be described with a variety of links
- `base_footprint` is a virtual non-physical link with no dimensions or collision areas. 



## Build and Launch
The following launch file will launch a robot publisher that uses the URDF to publish the transforms of the robot. The launch file will also launch RVIZ so we can visualize the robot. 
```python
import launch
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
import os

def generate_launch_description():
    pkg_share = launch_ros.substitutions.FindPackageShare(package='sam_bot_description').find('sam_bot_description')
    default_model_path = os.path.join(pkg_share, 'src/description/sam_bot_description.urdf')
    default_rviz_config_path = os.path.join(pkg_share, 'rviz/urdf_config.rviz')

    robot_state_publisher_node = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': Command(['xacro ', LaunchConfiguration('model')])}]
    )
    joint_state_publisher_node = launch_ros.actions.Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        arguments=[default_model_path],
        condition=launch.conditions.UnlessCondition(LaunchConfiguration('gui'))
    )
    joint_state_publisher_gui_node = launch_ros.actions.Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        condition=launch.conditions.IfCondition(LaunchConfiguration('gui'))
    )
    rviz_node = launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', LaunchConfiguration('rvizconfig')],
    )

    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(name='gui', default_value='True',
                                            description='Flag to enable joint_state_publisher_gui'),
        launch.actions.DeclareLaunchArgument(name='model', default_value=default_model_path,
                                            description='Absolute path to robot urdf file'),
        launch.actions.DeclareLaunchArgument(name='rvizconfig', default_value=default_rviz_config_path,
                                            description='Absolute path to rviz config file'),
        joint_state_publisher_node,
        joint_state_publisher_gui_node,
        robot_state_publisher_node,
        rviz_node
    ])
```




