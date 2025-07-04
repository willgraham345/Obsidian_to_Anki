---
tags: note/ROS
type: note
---
# Background
- A framework for launch integration testing. Includes:
	- exit codes for all processes, checking shutdown, failing tests when a process dies unexpectedly, and stdout/stderr for all processes, cli used to launch the process
- How is this different from [[ROS2.launch_testing]]?
	- Not very nice output on launch_testing, this is much prettier. 

Notes from Quick start xample

## Testing Nodes
Writing test cases
- You can use fixtures and markers to parameterize your tests for different scenarios
- 

`launch_pytest` plugin will launch nodes found in the `launch_description` fixture, run the tests from the `test_read_stdout()` class, shut down launched nodes, and run statements after the yield statement in `test_read_stdout`