---
tags: note/ROS
type: note
---
# Background
- Framework for launch integration testing. Provides exit codes of all processes, and stdout and stderr are available for all tests. 
- CLI used to launch processes 
- Some tests can run concurrently with the launch and can interact with the running process

## Quick Start Example
```sh
launch_test test/launch_testing/examples/good_proc_launch_test.py
```
- `launch_test` launches nodes in `generate_test_description`, run tests from the 
# Basics
1. `generate_test_description` function should return a `launch.LaunchDescription` object that launches the system to be tested. 
2. Launch description needs to include a `ReadyToTest` action to signal the test framework to start
	1. Typically fine to start the active tests immediately. 
	2. In older tests, a `ready_fun` is declared as an argument to `generate_test_description`, which should be plumbed into the launch description with an `OpaqueFunction`. This is fully replaced with `ReadyToTest`.
3. Active Tests
	1. Any classes that inherit from `unittest.TestCase` and not decorated with the `post_shutdown_test` descriptor will be run concurrently with the process under test
4. Post-Shutdown Tests
	1. Any classes that inherit `from unittest.TestCase` that are decorated with the `post_shutdown_test` descriptor will be run after the launched processes have been shut down. These tests have access to the exit codes and the stdout of all of the launched processes, as well as any data created as a side-effect of running the processes.