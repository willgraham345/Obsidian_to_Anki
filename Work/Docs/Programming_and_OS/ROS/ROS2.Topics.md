---
tags: note/ROS
type: note
---
# Background
One of the three primary styles of interface provided by ROS 2. Topics should be used for continuous data streams, like sensor data, robot state, etc.
- ROS 2 is a strongly-typed anonymous publish/subscribe system. 

# Publish/Subscribe
Producers = publishers
Consumers = subscribers

Named so they can find each other. 

## Recording data
```shell
ros2 bag record
```
- Under the hood this creates a new subscriber to whatever topic you tell, without interrupting the flow of data to other parts of the system
# Anonymous
When a subscriber gets a piece of data, it doesn't generally know or care which publisher originally sent it. Subscribers and publishers can be swapped out with this architecture without affecting the rest of the system


# Strongly-typed
## Type enforced at various levels
If this is a ROS2 message
```
uint32 field1
string field2
```

The code will ensure that `field` is always an unsigned integer and that `field2` is always a string

## Semantics of each field
Semantics in each field are well defined. There is no automated mechanism to ensure this, but all core ROS types have strong semantics. 