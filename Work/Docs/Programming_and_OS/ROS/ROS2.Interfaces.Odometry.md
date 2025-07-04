---
tags: note/ROS
type: note
---
# Background
- Represents the estimates of position and velocity in free space
- The `pose` in this message should be specified in the coordinate frame given by `header.frame_id`
- The `twist` in this message should be specified in the coordinate frame given by the `child_frame_id`

# Usage
[[ROS2.Interface.Std.Msgs.Header]]
- Includes the frame id of the pose parent
- Provides the timestamped data in a given coordinate frame
`string child_frame_id`
- Frame id the pose is pointing at. The twist is in this coordinate frame
[[ROS2 Interfaces PoseWithCovariance]]
- Estimate pose that is typically relative to a fixed world frame
- Position and orientation of robot relative to the frame specified in `header.frame_id`
[[ROS2 Interfaces TwistWithCovariance]]
- Estimated linear and angular velocity relative to `child_frame_id`


