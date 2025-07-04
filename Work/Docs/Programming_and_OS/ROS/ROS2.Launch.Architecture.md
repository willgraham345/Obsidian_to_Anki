---
tags: note/ROS
type: note
---
# Background
launch is designed to provide features like:
- Describing actions
- generating events
- introspecting launch descrptions
- executing launch descriptions.

It also provides extension points so that the set of things core features operate upon, or integrate with, can be expanded with additional packages. 


## Launch Entities and Launch Description
The main object in a launch is: [:class:`launch.LaunchDescriptionEntity`](https://github.com/ros2/launch/blob/humble/launch/doc/source/architecture.rst#id1) from which other launch entities inherit their properties. 
- This class, and the classes derived from this class, say how the system should be launched, as well as how the launch should react to asynchronous events in the system during launch. 


## Actions
Actions let the user describe intentions, and the set of available actions can be extended to other packages. 

Actions may also have arguments, which affect their behavior. These arguments are where the [:class:`launch.Substitution`](https://github.com/ros2/launch/blob/humble/launch/doc/source/architecture.rst#id21)'s can be used to provide more flexibility

### Base Actions
| Action                                     | Description                                                                                                                                                                                                                                  |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `launch.actions.IncludeLaunchDescription`  | Includes another launch description as if it had been copy-pasted to the location of the include action.                                                                                                                                     |
| `launch.actions.SetLaunchConfiguration`    | Sets a `launch.LaunchConfiguration` to a specified value, creating it if it doesn't already exist. Launch configurations can be accessed by any action via a substitution, but are scoped by default.                                        |
| `launch.actions.DeclareLaunchArgument`     | Declares a launch description argument with a name, default value, and documentation. The argument is exposed via a command line option for a root launch description or as action configurations for the include launch description action. |
| `launch.actions.SetEnvironmentVariable`    | Sets an environment variable by name.                                                                                                                                                                                                        |
| `launch.actions.AppendEnvironmentVariable` | Sets an environment variable by name, appends to the existing value using a platform-specific separator, with options to prepend and specify a custom separator.                                                                             |
| `launch.actions.GroupAction`               | Helpful for scoping grouped actions for a designated group. Yields other actions and can be associated with conditionals. It can optionally scope the launch configurations.                                                                                                                             |
| `launch.actions.TimerAction`               | Yields other actions after a specified period of time has passed without being canceled.                                                                                                                                                     |
| `launch.actions.ExecuteProcess`            | Executes a process given its path and arguments, with options for working directory and environment variables.                                                                                                                               |
| `launch.actions.RegisterEventHandler`      | Registers a user-defined `launch.EventHandler` class to handle specific events.                                                                                                                                                              |
| `launch.actions.UnregisterEventHandler`    | Removes a previously registered event handler.                                                                                                                                                                                               |
| `launch.actions.EmitEvent`                 | Emits an `launch.Event` based class, triggering all registered event handlers that match it.                                                                                                                                                 |
| `launch.actions.LogInfo`                   | Logs a user-defined message to the logger. Variants like `LogWarn` may also exist.                                                                                                                                                           |
| `launch.actions.RaiseError`                | Stops execution of the launch system and provides a user-defined error message.                                                                                                                                                              |


## Substitutions
[[ROS2.Launch.Substitutions]]