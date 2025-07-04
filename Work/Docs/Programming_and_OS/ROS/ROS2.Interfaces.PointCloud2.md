---
tags: note/ROS
type: note
---
# Background
- Sometimes it is more convenient to deal with data as lots of points in 3D space
- Holds an N-dimensional points, containing info such as normals, intensity, etc.
	- Point data is stored in a binary blob, described by the contents in the `fields` array

# Usage
[[ROS2.Interface.Std.Msgs.Header]] header
	- Time of data acquisition and coordinate frame ID (for 3d points)
`uint32` height  
- If 2d unordered, height is 1
`uint32` width  
- Length of point cloud
[[Ros2 Interfaces PointField]]`[]` fields  
- Describes channels and layout in the binary data blob. 
`boolean` is_bigendian  
- Is this data bigendian?
`uint32` point_step  
- Length of a point in bytes
`uint32` row_step  
- Length of a row in bytes
`uint8`[]` data  
- Actual point data, size is (`row_step*height`)
`boolean` is_dense
- True if there are no invalid points