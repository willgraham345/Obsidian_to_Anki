---
tags: note/ROS
type: note
---
# Background
- A class that encapsulates the lifecycle of [[ROS2 rclpy init]] and [[ROS2 rclpy shutdown]]
- Context objects should not be reused, and are finalized in their destructor
- Wraps the `rcl_context_t` type