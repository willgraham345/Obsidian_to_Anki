---
tags: note/ROS
type: note
---
# Background
A group of messages and services common to robotics that are grouped together in [this repo](https://index.ros.org/p/sensor_msgs/)
- Covers a wide variety of topics, all of which are WIDELY used


## Different Messages
|**Message Type** |**Description** |
|---|---|
|BatteryState|Describes the power state of the battery.|
|CameraInfo|Meta information for a camera.|
|ChannelFloat32|Holds optional data associated with each point in a PointCloud message.|
|CompressedImage|A compressed image.|
|FluidPressure|Single pressure reading for fluids (air, water, etc) like atmospheric and barometric pressures.|
|Illuminance|Single photometric illuminance measurement.|
|Image|An uncompressed image.|
|Imu|Holds data from an IMU (Inertial Measurement Unit).|
|JointState|Holds data to describe the state of a set of torque controlled joints.|
|JoyFeedbackArray|An array of JoyFeedback messages.|
|JoyFeedback|Describes user feedback in a joystick, like an LED, rumble pad, or buzzer.|
|Joy|Reports the state of a joystick's axes and buttons.|
|LaserEcho|A submessage of MultiEchoLaserScan and is not intended to be used separately.|
|LaserScan|Single scan from a planar laser range-finder.|
|MagneticField|Measurement of the Magnetic Field vector at a specific location.|
|MultiDOFJointState|Representation of state for joints with multiple degrees of freedom, following the structure of JointState.|
|MultiEchoLaserScan|Single scan from a multi-echo planar laser range-finder.|
|NavSatFix|Navigation Satellite fix for any Global Navigation Satellite System.|
|NavSatStatus|Navigation Satellite fix status for any Global Navigation Satellite System.|
|PointCloud2|Holds a collection of N-dimensional points, which may contain additional information such as normals, intensity, etc.|
|PointCloud (Deprecated)|THIS MESSAGE IS DEPRECATED AS OF FOXY, use PointCloud2 instead.|
|PointField|Holds the description of one point entry in the PointCloud2 message format.|
|Range|Single range reading from an active ranger that emits energy and reports one range reading that is valid along an arc at the distance measured.|
|RegionOfInterest|Used to specify a region of interest within an image.|
|RelativeHumidity|A single reading from a relative humidity sensor.|
|Temperature|A single temperature reading.|
|TimeReference|Measurement from an external time source not actively synchronized with the system clock.|