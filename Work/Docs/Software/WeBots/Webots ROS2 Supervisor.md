---
type: note
---
ROS 2 Humble

# Background
The `Ros2Supervisor` node enhances the interface by creating additional services and topics to interact with the simulation
- Lets you record animations or spawn Webots nodes directly from the ROS 2 interface while the simulation is running.


## Ros2Supervisor Parts
1. Made of two parts: Webots Robot added to the simulation world
2. Ros2 node that connects to the Webots robot as an extern controller (similar way to your own robot plugin)
ROS2 node acts like a controller to call the supervisor API functions to control or interact with the simulation world. 


### Initialization
within the WebotsLauncher
```python
webots = WebotsLauncher(
    world=PathJoinSubstitution([package_dir, 'worlds', world]),
    mode=mode,
    ros2_supervisor=True
)
```
The `webots._supervisor` object must also be included in the `LaunchDescription` returned by the launch file like so:
```python
return LaunchDescription([
    webots,
    webots._supervisor,

    # This action will kill all nodes once the Webots simulation has exited
    launch.actions.RegisterEventHandler(
        event_handler=launch.event_handlers.OnProcessExit(
            target_action=webots,
            on_exit=[
                launch.actions.EmitEvent(event=launch.events.Shutdown())
            ],
        )
    )
])
```
# Capabilities
## Clock topic
The `Ros2Supervisor` node will get the time of the Webots simulation and publish it to `/clock` topic. 
- This means that it is mandatory to spawn `Ros2Supervisor` if other nodes have their `use_sim_time` parameter set to `true`
## Import a Webots node (Spawning)
We can spawn a node from strings through a service
- The service is named `/Ros2Supervisor/spawn_node_from_string` and is of type `webots_ros2_msgs/srv/SpawnNodeFromString`. The `SpawnNodeFromString` type expects a `data` string as input and returns a `success` boolean.

From the given string, the Supervisor node is getting the name of the imported node, and adding it to an intern list for potential later removal


The Node is imported using the `importMFNodeFromString(nodeString)`

### Example
```shell
ros2 service call /Ros2Supervisor/spawn_node_from_string webots_ros2_msgs/srv/SpawnNodeFromString "data: Robot { name \"imported_robot\" }"
```