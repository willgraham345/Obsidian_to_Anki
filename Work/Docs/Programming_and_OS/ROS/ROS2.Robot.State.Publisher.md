---
tags: note/ROS
type: note
---
[Wiki Page](https://wiki.ros.org/robot_state_publisher)

# Background
- A package that publishes the state of a robot to the [[ROS2.tf2]] module
- Once the state is published, it is available to all components in the system that use [[ROS2.tf2]]
- This package can be used as a library as well as a ROS node. 
- All fixed transforms are future dated by 0.5s

# Usage/API
## Subscribed Topics
`joint_states`
- [[ROS2.Interfaces.JointState]]

## Parameters
`robot_description` (`urdf map`)
- URDF xml robot description. 
`tf_prefix(string)`
- Set the `tf` prefix for namespace-aware publishing of transforms
`publish_frequency` (`double`)
- default: 50Hz.
`ignore_timestamp` (`bool`)
- If true, ignore the publish_frequency and the timestamp of joint_states and publish a `tf` for each of the received joint_states. Default is "false".
`use_tf_static` (`bool`)
- Set whether to use the `/tf_static` latched static transform broadcaster. Default: true.
