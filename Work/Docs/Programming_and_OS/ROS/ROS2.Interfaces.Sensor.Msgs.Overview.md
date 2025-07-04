---
tags: note/ROS
type: note
---
Common geometry messages are used to represent and exchange information. These messages are defined within the `geometry_msgs` package. 

## Data Types
|Data Type|Description|
|---|---|
|`Point`|Represents a 3D point with x, y, and z coordinates.|
|`Vector3`|Represents a 3D vector with x, y, and z components.|
|`Quaternion`|Represents a 3D orientation using quaternion notation.|
|`Pose`|Combines a `Point` and a `Quaternion` to represent 3D pose.|
|`Twist`|Describes linear and angular velocity using `Vector3`.|
|`Transform`|Represents a rigid-body transformation, often used in TF.|
|`Wrench`|Contains force and torque information using `Vector3`.|


