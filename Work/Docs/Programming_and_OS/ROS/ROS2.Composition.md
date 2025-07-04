---
tags: note/ROS
type: note
---
# Nodes vs Nodelets
In ROS 1 you can write your code as either a ROS node or as a ROS nodelet. ROS 1 nodes are compiled into executables.


# ROS2 Unified API
In ROS2 the recommended way of writing your node is similar to a nodelet, but called a `Component`. This makes it was to add common concepts to existing code like a life cycle [[ROS2.Lifecycle.aka.Managed.Notes]]


## Writing a Component
Since a component is only built into a shared library it doesn't have a `main` function. A component is commonly a subclass of `rclcpp::Node`. 
- It is not in control of the thread, and it shouldn't perform any long running or blocking tasks in its constructor. 
- It can use timers to get periodic notification. 
- It can create publishers, subscribers, servers, and clients. 

An important aspect of making such a class a component is that the class regiisters itself using macros from the package `rclcpp_components`. This makes the component discoverable when its library is being loaded into a running process - it acts as kind of an entry point. 

Additionally, once a component is created, it must be registered with the index to be discoverable by the tooling. 



## Using Components
The [composition package](https://github.com/ros2/demos/tree/galactic/composition) contains a couple of different approaches on how to use components. Common approaches are:
1. Start a ([generic container process](https://github.com/ros2/rclcpp/blob/galactic/rclcpp_components/src/component_container.cpp)) and call the ROS service [load_node](https://github.com/ros2/rcl_interfaces/blob/galactic/composition_interfaces/srv/LoadNode.srv) offered by the container. The ROS service will then load the component specified by the passed package name and library name and start executing it within the running process. Instead of calling the ROS service programmatically you can also use a [command line tool](https://github.com/ros2/ros2cli/tree/galactic/ros2component) to invoke the ROS service with the passed command line arguments
2. Create a [custom executable](https://github.com/ros2/demos/blob/galactic/composition/src/manual_composition.cpp) containing multiple nodes which are known at compile time. This approach requires that each component has a header file (which is not strictly needed for the first case).
3. Create a launch file and use `ros2 launch` to create a container process with multiple components loaded.
