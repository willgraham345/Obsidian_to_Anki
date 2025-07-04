---
tags: note/ROS
type: note
---
`base_link` = coordinate frame rigidly attached to robot base. Can be attached to base in any arbitrary position or orientation.
`odom` = World-fixed coordinate frame
- Typically computed based on odometry source (wheel odometry, visual, or IMU)
`map` = world fixed frame, with z axis pointing upwards