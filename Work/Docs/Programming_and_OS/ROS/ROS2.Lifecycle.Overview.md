---
tags: note/ROS
type: note
---
# ROS2 Life Cycle
Allows roslaunch to ensure that all components have been instantiated correctly before allowing any component to begin executing its behavior. It will also allow nodes to be restarted or replaced on-line.

A manged node presents a known interface, executes according to a known life cycle state machine, and otherwise can be considered a black box. 
- Allows freedom to the node developer on how they provide the managed life cycle functionality, while also ensuring that any tools created for managing nodes can work with any compliant node.

See more here: [Node Lifecycle](https://design.ros2.org/articles/node_lifecycle.html)

## Lifecycle States
### Primary States:
- `Unconfigured`
- `Inactive`
- `Active`
- `Finalized`
Transition out of a primary state requires action from an external supervisory process, with an exception of an error being triggered in the `Active` state.

### Transition States
Intermediate during a requested transition
- `Configuring`
- `CleaningUp`
- `ShuttingDown`
- `Activating`
- `Deactivating`
- `ErrorProcessing`

### Transitions exposed to a Supervisor Process
- `create`
- `configure`
- `cleanup`
- `activate`
- `deactivate`
- `shutdown`
- `destroy`

## Various lifecycle related verbs
`get` get lifecycle state of one or more nodes
`list` output a list of available transitions
`nodes` output a list of nodes with lifecylce
`set` Trigger lifecycle state transition



## Images