---
tags: note/ROS
type: note
---
# Background
- Single scan from a planar laser range-finder
- Basically an array of floats for a single sweep of the sensor representing the range measurement (in meters) with extra parameters for good understanding of the data
- Also tells us which TF frame the lidar is attached to, so the rest of the system is in space.
	- Common practice is to name the tf frame `laser_frame`
- Best practice to have LaserScan data uploaded to the [[ROS2.scan]] topic
## Packages that Use this
[[ROS2.slam.toolbox]]
[[ROS2.Nav2.amcl]]
[[ROS2.Nav2.costmap_2d]]

# Usage
[[ROS2.Interface.Std.Msgs.Header]]
- In `frame` `frame_id`, angles are measured around the positive Z axis (counterclockwise if Z is up) with zero angle being forward on the X axis
`float32 angle_min`
- Start angle of the scan `[rad]`
`float32 angle_max`
- End angle of the scan `[rad]`
`float32 angle_increment`
- Angular distance between measurements `[rad]`
`float32 time_increment`
- Time between measurements `[seconds]` - if your scanner is moving, this will be used in interpolating position of 3d points
`float32 scan_time`
- Time between scans
`float32 range_min`
- minimum range value `[m]`
`float32 range_max`        
- maximum range value `[m]`
`float32[] ranges` 
- range data `[m]`
	- (Note: values < range_min or > range_max should be discarded)
`float32[] intensities`
- intensity data [device-specific units]`
- If your device does not provide intensities, please leave the array empty.