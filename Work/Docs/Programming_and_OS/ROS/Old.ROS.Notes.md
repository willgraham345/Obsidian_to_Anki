---
tags: note/ROS
type: note
---

ros2 interface show <msg type>
- Returns details of message, and specifically what the structure of data the message expects 

    

CMakeLists.txt

- Make file used to compile cpp node.
    

Debugging

- You can debug a ROS 2 node by looking at where it installed (look at setup.cfgfor python to find the directory). You can navigate to that directory and manually run the node. 
    

Launch

Creating a launch file

- Can be in python, xml, or yaml
    

- Python
    

- From launch import LaunchDescription
    
- From launch_ros.actions import Node
    

Launching and monitoring multiple nodes

Using substitutions

Using event handlers

Managing large projects

  

Parameters

Ros2 run <package_name> <executable_name>

- Launches an executable from a package
    

- Executables can be defined from the setup.py file, (or somewhere else for cpp)
    

ros2 param dump <node_name>

- Inputs all parameters into a yaml file that you can load later with:  
    ros2 param load <node_name> <parameter_file>
    

ros2 param get <node_name> <parameter_name>

- Gets current value of a parameter
    

ros2 param list

- Prints all parameters
    

  

Packages

What is a package?

- An independent unit inside your application (ROS 2 instance/system). This will have nodes inside of them, with associated drivers. 
    

CMake

ros2 pkg create --build-type ament_cmake <package_name>

Python package

ros2 pkg create --build-type ament_python <package_name>

  

After creating package, rebuild the workspace:

cd ~/ros2_ws

colcon build # orrr colcon build --packages-select my_package (only builds my_package now)

  

Don’t forget to source the local file (. Install/local_setup.bash)

  

Files/folders that this will automatically create

- Cmake
    

- Include (folder)
    
- Src (folder)
    

- Custom C++ nodes go here in the future
    

- Package.xml
    

- Dependencies listed here
    

- CMakeLists.txt
    

- Dependencies listed here
    

- Python
    

- My_package
    

- Custom python nodes go here in the future
    

- Package.xml
    

- Fields
    

- Maintainer = your name and email
    
- Description = package description
    
- License = some kind of open source license (read about these before doing anything)
    

- _depend
    

- This is where you list dependencies REALLY important
    

- Setup.py has the same description, maintainer and license fields. Version and name package_name must match exactly in both files
    

- Resource
    
- Setup.cfg
    
- Setup.py
    
- test
    

Package.xml

- Made with both cpp, and python libraries. 
    
- Edit this to decide what dependencies your library needs. 
    
- For cpp packages, you’ll need to add dependencies in both the CMakeLists.txt as well as the package.xml
    

Publishers

ros2 topic pub <topic_name> <msg_type> '<args>'

- Publishes data onto a topic directly from the command line
    

  

Import rclpy library

Import rclpy.node import Node

  

Publishers in python

- Class ClassName
    

Python Notes

- Remember, you can change python files to make them executables
    

Nodes

- Subprograms with the application, responsible for only one thing. They’re combined into a graph, and communicate with each other through topics, services, and parameters.
    
- They reduce code complexity, and are fault tolerant.
    
- These can also be written in Python or C++ 
    
- Common node methods:
    

- create_publisher: creates a publisher for a given topic with a given message type.
    
- create_subscription: creates a subscription to a given topic with a given message type.
    
- create_client: creates a client for a given service with a given request and response message type.
    
- create_service: creates a service for a given service with a given request and response message type.
    
- create_timer: creates a timer with a given duration and callback function.
    
- get_logger: returns a logger object for logging messages associated with the node.
    
- get_parameter: retrieves a parameter value from the parameter server.
    
- set_parameter: sets a parameter value on the parameter server.
    
- declare_parameter: declares a parameter with a default value and optional parameter descriptor.
    
- get_node_names: retrieves the names of all nodes on the ROS 2 network.
    
- get_topic_names_and_types: retrieves the names and message types of all topics on the ROS 2 network.
    
-   
    

Rosdep

- Rosdep is the dependency management tool that will work with ROS packages and external libraries. 
    

- Can be invoked when:
    

- Building a workspace adn needing appropriate dependencies to build the packages within
    
- Install packages (e.g. sudo apt install ros-galactic-demo-nodes-cpp) to check the dependencies needed for it to execute
    

- Checks package.xml files for “rosdep keys”, and cross-check that with teh rosdistro central index.
    

- Represented in the tags <depend>, <test_depend>, <exec_depend>, <build_depend>, and <build_export_depend>. They specify in what situation each of the dependencies are required in. 
    
- These dependencies are manually populated in the package.xml file by the package’s creators and should be an exhaustive list of any non-built in libraries and packages it requires.
    

- Initialize rosdep (initializes the tool and updates locally cached rosdistro index)
    

- Sudo rosdep init  
    Rosdep update
    

- Install dependencies
    

- Rosdep install –from-paths src -y –ignore-src
    

- – from-paths src specifies the path to check for package.xml field to resolve keys
    
- -y means to default yes to all prompts from the package manager to install without prompts
    
- –ignore-src means to ignore installing dependencies, even if a rosdep key exists, if the package itself is also in the workspace. 
    

- This is typically run over a workspace with many packages in a single call to install all dependencies. This would appear as the following, if the root of the workspace with directory “src” containing source code
    

Run

- Runs an executable from the local workspace, or the global ros installation w
    

ros2 run <package_name> <executable_name> --ros-args --params-file <file_name>

- Will load parameters at start of node
    

-   
    

Ros2 node list

- Return list of nodes
    

-   
    

Ros2 node info

- Returns list of subscribers, publishers, services, and actions (the ROS graph connections) that interact with that node
    

Services

ros2 service call <service_name> <service_type> <arguments>

- Calls a service, arguments are optional. (empty types don’t have arguments)
    

ros2 service list

- Lists all services
    
- ros2 service list -t
    

- Returns types alongside service names
    

ros2 service type <service_name>

- Returns type of service
    
- Types of service
    

- Empty: Service call sends no data when making a request and receives no data when receiving a response
    

-   
    

Topics

Ros2 topic echo <topic_name

- Publishes data to the command line
    

- Must be in YAML syntax
    

- I.e.  
    ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
    

- Once means publish message once then exit
    

- –rate HzInputInt
    

- Optional argument to publish at a rate
    

ros2 topic hz <topicname>

- Returns the frequency of how often it’s happening
    

Ros2 topic info

ros2 topic list

- Return list of topics currently active in the system
    
- ros2 topic list -t will return the same list of topics, this time with the topic type appended in brackets
    

  

Rqt

Rqt

- Launches rqt
    
- If nothing shows up, select Plugins>services>service caller from menu bar at the top
    
- Use refresh to ensure all services are available 
    

  

Remapping

- Lets you reassign default node properties, like node name, topic names, service names to custom values. 
    

- You can use this to change the thing being controlled
    

  
  

Nav2 Stuff

- Action servers
    

- A great way to control long-running tasks (like navigation)
    
- Can be found on nodes, rather than topics. 
    

- Lifecycle Nodes and Bond
    

- Unique to ROS2
    

- Nodes with machine transitions and tear
    

- Behavior Trees
    

- Tree structure of tasks to be completed
    
- Opposed to FSM (finite state machine) with dozens of states and hundreds of transitions
    

- Navigation Servers (configured with aliases for the task)
    

- Planner, Controller, Smoother
    

- Configured at runtime with names/aliases and types of algorithms to use.
    
- Types pluginlib names
    

- i.e. DWB controller used with name FollowPath, as it follows reference path. All parameters for DWB would then be placed in that namespace, e.g. FollowPath.<param>
    

- These three expose an action interface corresponding to its task
    
- For the behavior server, each of the behaviors alo contains their own name
    

- Planner
    

- Computes a path to complete some objective function
    
- Two examples are computing a path to a goal, or complete coverage
    
- Will have access to global environment representation and sensor data buffered into it
    

- Controllers
    

- Follow a globally computed path or complete a local task. 
    
- Will have access to local environment representation to attempt computer feasible control efforts for the base to follow.
    
- Can be written to:
    

- Follow a path
    
- Dock with a charging station using detectors in the odometric frame
    
- Board an elevator
    
- Interface with a tool
    

- Computes a valid control effort to follow the global plan. Many classes of controllers and local planners exist.
    

- Behaviors
    

- Deals with unknown or failure conditions of the system and autonomously handles them. 
    
- Can even notify someone via slack if the system is down
    

- Smoothers
    

- Criteria for optimal path
    
- Typically responsible for reducing ruggedness, as well as to increase distance from obstacles and high-cost areas.
    
- Have access to global environmental represenation
    
- General task is to receive a path and return an improved version
    

- Waypoint Following
    

- Basic feature, tells us how to use navigation to get to multiple destinations. 
    
- 2 schools of thought
    

- Dumb robot, smart centralized dispatcher
    

- Nav2_waypoint_follower is great for production grade in this case
    
- Waypoint follower is 1 unit of work. Waypoint following is just one step above navigation and below the system autonomy application
    

- Smart robot, dumb centralized dispatcher 
    

- Nav2_waypoint_follower is a nice sample, but you need waypoint following on the robot to carry more weight in making a robot solution. 
    

- You should use nav2_behavior_tree package to create custom application-level behavior tree using navigation to complete the task.
    

- There will soon be a Nav2_bt_waypoint_follower (might change name) that will allow you to create this application more easily.  
    

- State Estimation
    

- Within the navigation, there are two major transformations that need to be provided.
    

- Map to odom
    
- Odom to base_link
    

- You need to establish map -> odom -> base_link -> [sensor frames]
    
- TF2 are the time-variant transformation library  we use to represent and obtain time synchronized transformations. It’s the jbo of the global positioning system (GPS, SLAM, Motion Capture) to, at minimum, provide the map -> odom transformation. The odometry system should then provide the odom -> base-link transformation. The remainder of the transformations relative to the base_link should be static and defined in the URDF.
    
- Odometry
    

- The role of this system is to provide the odom -> base_link transformation
    
- The goal is to provide a smooth and continuous local frame based on robot motion. 
    
- Robot localization is used for this function
    

- Environmental Representation 
    

- Costmaps and Layers
    

- Current representation is a costmap, which is a 2D grid of cells containing a cost from unknown, free, occupied, or inflated cost
    

- Various layers are implemented as pluginlib plugins to buffer information into the costmap. It may be wise to process sensor data before inputting it into the costmap layer.
    
- Can be created to detect and track obstacles in the scene. These can alo be used to algorithmically change the underlying costmap based on some rule or heuristic.
    

- Costmap filters
    

- Basically annotations to designate keep out zones and speed requirements in marked areas. Provides an ability of marking areas on a map with additional features or behaviors.**