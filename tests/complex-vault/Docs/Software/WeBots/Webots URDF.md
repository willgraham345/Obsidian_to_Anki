---
type: note
---
We need to create a URDF to declare the `MyRobotDriver`
- This allows the `webots_ros2_driver` ROS node to launch the plugin and connect it to the target robot.

## Sample URDF
```XML
<?xml version="1.0" ?>
<robot name="My robot">
    <webots>
        <plugin type="my_package.my_robot_driver.MyRobotDriver" />
    </webots>
</robot>
```
- Plugin does not take in any input parameter, but this can be achieved with a tag containing the parameter name.
```XML
<plugin type="my_package.my_robot_driver.MyRobotDriver">
    <parameterName>someValue</parameterName>
</plugin>
```

## Advanced URDF
`webots_ros2_driver` contains plugins to interface most of Webots devices with ROS 2 directly. These plugins can be loaded using the `<device>` tag in the URDF file of the robot. 
- `reference` attribute should match with the Webots device `name` parameter.
- List of all existing interfaces and corresponding parameters on the [device reference page](https://github.com/cyberbotics/webots_ros2/wiki/References-Devices)
### Generic Example of URDF
```xml
<?xml version="1.0" ?>
<robot name="RobotName">
    <webots>
        <device reference="referenceName" type="typeName">
            <ros>
                <!-- If `False`, disable the device. By default the device will be enabled. -->
                <enabled>False</enabled>

                <!-- Set the main topic name of the device. By default it will be `/robotName/referenceName`. -->
                <!-- If a device publishes several topics, the secondary topics names are relative to the main topic name. -->
                <!-- Example: if the main topic name is `my_robot/camera`, the secondary topic for the `camera_info` messages -->
                <!-- will be `my_robot/camera/camera_info`. -->
                <topicName>/new_topic_name</topicName>
                <!-- Set the update rate in Hz of the topic. By default the topic will be published at each simulation step. -->
                <updateRate>10</updateRate>
                <!-- If `True`, the device topics will constantly publish, which can slow down the simulation. -->
                <!-- By default the topics are publishing only if there is at least one subscriber for the corresponding topic. -->
                <alwaysOn>True</alwaysOn>
                <!-- Set the frame ID for message headers. By default the frame ID is `referenceName`. -->
                <frameName>new_frame_name</frameName>
            </ros>
        </device>
    </webots>
</robot>
```

- `reference` should match the name of the device in the robot
- `type` should match the type of device (can be found in each device in the next sections)
The `webots_ros2_driver` will parse the `<device>` tags referring to the DistanceSensor nodes and use standard parameters in the `<ros>` tags to enable sensors and their topics. 
