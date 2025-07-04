---
tags: note/ROS
type: note
---
# Background
Colcon is a command line tool to improve workflow of building, testing, and using multiple software packages. Automates the process, handles ordering and sets up environment to use the packages
- All colcon tools start with the prefix `colcon` followed by a command and (likely) positional/optional arguments
- Not specific to ROS, can also be used to make other stuff
- All have the global options of:
```bash
--log-path <path> # Base path for all directories
--log-level <level> # Log level for console output, either by numeric or string value
```

# Commands
## Build

## Build with Output to the Terminal
```shell
colcon build --event-handlers console_direct+ --symlink-install
```