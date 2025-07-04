---
type: note
tags:
  - note/ROS
---
# Background
There are multiple frameworks available for testing launch files within ROS2. Be aware that testing modules may or may not be available on your ROS2-specific machine. 
You can run tests from the CLI using the following arguments...
```bash
colcon test-result --all --verbose
```

See [[Python Pytest.Overview]] python-specific descriptions, and [[ROS2.launch_pytest]] for writing python tests within a ROS2 framework. To launch from CLI, see [[ROS2.Running.Tests.from.CLI]].

# Writing Basic Tests with Python
Uses the `ament_cmake_python` for making tests discoverable
- In the 
## Package Setup
### setup.py
Must test dependency on `pytest` within the call to `setup(...)`
```python
tests_require=['pytest']
```


## Test files and folders
Need to go in a folder called `tests` in the root of your package
Any file that contains tests that you want to run must have the pattern `test_FOO.py` where `FOO` can be anything
## Example Package Layout
awesome_ros_package/
  awesome_ros_package/
      __init__.py
      fozzie.py
  package.xml
  setup.cfg
  setup.py
  tests/
      test_init.py
      test_copyright.py
      test_fozzie.py
## Test Contents
- There are lots of resources on pytest, but in short, you can write functions with the `test_` prefix and include whatever assert statements you'd like
## Running Tests
## Special Commands
You can also specify arguments to pytest framework from CLI with the `--pytest-args` flag. 


# Testing Notes from Video
colcon test, launch_test + unittest

