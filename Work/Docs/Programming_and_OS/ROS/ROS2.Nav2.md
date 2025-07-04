---
tags: note/ROS
type: note
---
# Useful Notes
[[ROS2 Nav2 First Time Robot Setup Guide]]

# Navigation Concepts
### Action Server
- Common way to control long-running tasks 
- Similar to a service server. A client will request some task to be completed. 
	- Allow us to call a long-running task in another process or thread and return a future to its result. 
- We can request feedback to clients
- Examples
	- A bulldozer is requested to move it's shovel up
		- A request may be an angle, a feedback may be the angle remaining to be moved. 
- Action servers are used to communicate with the highest level [[ROS2 Nav2 Behavior Tree]] with a `NavigateToPose` action message
## Lifecycle Nodes and Bond
- Lifecycle (or managed, more correctly) nodes are unique to ROS 2. These are nodes that contain state machine transitions for bringup and teardown of ROS 2 servers. Helps users structure their programs for debugging.
	- See more info [[ROS2.Lifecycle.aka.Managed.Notes]]
## Behavior Trees
- Nav2 uses a BehaviorTree CPP V3 as the behavior tree library. There are node plugins which can be constructed into a tree, inside the `BT Navigator`
	- Node plugins are loaded into BT. When XML of file is parsed, the registered names are associated. 
## State Estimation

## Environmental Representation
- The way the robot perceives the environment around it, and acts as the central localization for algorithms and data sources to combine info into one place. 
### Costmaps and Layers
- The current environmental representation is a costmap, a regular 2D grid of cells containing a cost from unknown, free, occupied, or inflated cost. 
- This map is searched to compute a global plan or sampled to compute local control efforts.
- Various costmap layers are implemented as [[ROS2.pluginlib]] plugins to buffer info into the costmap
### Costmap Filters
- A "filter mask"
	- Overlaid on a surface. The main goal here is to provide the ability of marking areas on maps with additional features or behavioral changes.
- A way to apply spatial-dependent behavioral changes into the Nav2 stack. 
- Examples
	- Keep out zones, speed limits, preferred lanes for robots in industrial environments and warehouses

# Standards
## Standard Units and Frame Orientation
Frames are defined using the right hand rule, with Z up and X forward, and units should be standard SI units
## Naming Conventions
Found [here](https://www.ros.org/reps/rep-0105.html)
`base_link`
- Coordinate frame attached to a fixed position on the robot, typically at its main chassis and rotational center
`odom`
- Fixed frame relative to the robot's starting position and is mainly used for locally-consistent representations of distances
`map`
- World fixed frame that is used for globally-consistent representations of distances