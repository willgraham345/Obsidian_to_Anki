---
tags: note/ROS
type: note
---
How to make tests discoverable

## Setup
- `setup.py` must have a dependency on `pytest` within the `setup(...)``
- Your test code needs to go in a folder titled `tests` in your package root dir.
- Any file that contains tests you want to run must have pattern `test_FOO.py` where `FOO` can be replaced with anything.
## Test Contents
You can write functions with the `test_` prefix and include whatever assert statements you'd like. 

## Special Commands
You can also specify arguments to the `pytest` 