---
tags: note/ROS
type: note
---
# Background
A participant in the ROS2 graph, which uses a client lbirary to communicate with other nodes. Nodes can communicate with other nodes within the same process, a different process, or on a different machine. 
- The unit of computation in a ROS graph. Each node should do one thing. 

Nodes can publish to named topics to deliver data to other nodes, or subscribe to named topics to get data from other nodes. They can also be a service client, or a service server. 
- Nodes can provide configurable parameters to change behavior during run-time.
Nodes are often complex combination of publishers, subscribers, service servers, service clients, action servers, and action clients, all at the same time. 



# Configuration of Nodes
## Launch File Options for Nodes
### Required Node Options
- `package` = `str` describing package to find node's source code
- `executable` = `str` describing the node's executable in the package xml
- `name` = `str` with node name
### Optional Node Options
- `namespace` = Launching the node within a namespace  e.g. `turtlesim1`
- `exect_name` = name of the process. Default is the same as `name`
- `parameters` = list of parameter files that are loaded for the node
	- e.g. `paremeters = "my_params.yaml"`
- `remappings` = Remapping node names
	- e.g. `remappings = [('/input/pose', '/turtlesim1/turtle1/pose1')]'`
- `arguments` = List of arguments to hand over to the node
	- e.g. `arguments = ['name', 'my_robot']`