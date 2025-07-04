---
tags: note/ROS
type: note
---
# Background
Typical ROS program has the following operations:
1. Initialization
2. Create one or more ROS nodes
3. Process node callbacks
4. Shutdown

#### Initialization
Done by calling `init()` for a particular `Context`

#### Create nodes
Done by calling `create_node()` or instantiating a `Node` 

#### Processing Callbacks
Can be done by *spinning* on the node. The following functions can be used to process work that is waiting to be executed:
- `spin()`
- `spin_once()`
- `spin_until_future_complete()`
[[ROS2.rclpy.spin]]

#### Shutdown
When finished with your `Context`, the `shutdown()` function should be called. 


