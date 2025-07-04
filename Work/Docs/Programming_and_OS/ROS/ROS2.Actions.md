---
tags: note/ROS
type: note
---
# Background
Actions are different from topics in that there is a request and response, while topics send without confirmation.
- Defined within .action files
- Request, result, feedback
- An instance of an action is typically referred to as a goal

## Step by step
- Request is sent from an action client to an action server initiating a new goal
- Result is sent from an action server to an action client when a goal is done
- Feedback messages are periodically sent from an action server to an action client with updates about a goal
- An action definition is made of three messages separated by (- - -)
- Request, result, feedback

## C++ Action Server and Client
- Action servers send goal feedback and results to action clients
# Commands
|                         |                                    |
| ----------------------- | ---------------------------------- |
| `ros2 action info <action_name>`      | Output information about an action |
| `ros2 action list <action_name>`      | Output a list of action names      |
| `ros2 action send_goal <action_name>` | Send an action goal                |
| `ros2 action show <action_name>`      | Output the action definition       | 
## Examples
```bash
ros2 action send_goal <action_name> <goal_message> --ros-args -p <param_name>:=<param_value>

```

```bash
ros2 action send_goal /navigate_to_goal your_msgs/action/NavigateToGoal --args 'x:=2.0 y:=3.0' --ros-args -p timeout:=30.0

```



# Action Server vs Action Client
## Action Server
The entity that will accept the remote procedure request and perform some procedure on it. Responsible for sending out feedback as action progresses and should react to cancellation/preemption requests. 

## Action Client
Entity that will request remote server to perform a procedure on its behalf. 

There can be an arbitrary number of action clients using the same action
