---
tags: note/ROS
type: note
---
# Background
- Done through using `colcon test`
# Usage
## Build and Run Tests
``` Shell
colcon test --packages-select <pkg_name> --pytest-args -k <name_of_test_function>
```
- To see the output of the test while its running, use the flag
- `--event-handlers console_cohesion+`
## Examine Test Results
```
```shell
colcon test-result --all
```
- Add a `--verbose` flag to see which tests failed or succeeded


## Debugging Tests with GDB
If a C++ test is failing, gdb can be used directly on the test executable in the build directory
```
colcon build --smake-clean-cache --mixin debug
```