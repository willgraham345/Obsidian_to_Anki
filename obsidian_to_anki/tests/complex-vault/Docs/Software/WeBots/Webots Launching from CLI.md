---
type: note
---
[Reference here](https://cyberbotics.com/doc/guide/starting-webots#command-line-arguments)


# Usage
```shell
webots [options] [worldfile]
```
## Options
```
 --help
    Display this help message and exit.

  --version
    Display version information and exit.

  --sysinfo
    Display information about the system and exit.

  --mode=<mode>
    Choose the startup mode, overriding application preferences. The <mode>
    argument must be either pause, realtime or fast.

  --no-rendering
    Disable rendering in the main 3D view.

  --fullscreen
    Start Webots in fullscreen.

  --minimize
    Minimize the Webots window on startup.

  --batch
    Prevent Webots from creating blocking pop-up windows.

  --clear-cache
    Clear the cache of Webots on startup.

  --stdout
    Redirect the stdout of the controllers to the terminal.

  --stderr
    Redirect the stderr of the controllers to the terminal.

  --port
    Change the TCP port used by Webots (default value is 1234).

  --stream[=<mode>]
    Start the Webots streaming server. The <mode> argument should be either
    x3d (default) or mjpeg.

  --extern-urls
    Print on stdout the URL of extern controllers that should be started.

  --heartbeat[=<time>]
    Print a dot (.) on stdout every second or <time> milliseconds if specified.

  --log-performance=<file>[,<steps>]
    Measure the performance of Webots and log it in the file specified in the
    <file> argument. The optional <steps> argument is an integer value that
    specifies how many steps are logged. If the --sysinfo option is used, the
    system information is prepended into the log file.

  convert
    Convert a PROTO file to a URDF, WBO, or WRL file.

Please report any bug to https://cyberbotics.com/bug
```

## Other Options
- `gui` **(bool):** If `False`, set the `--no-rendering`, `--stdout`, `--stderr` and `--minimize` flags. Default is `True`.
- `mode` **(string):** Set the `--mode` flag with the same value. Default is `'realtime'`.
- `stream` **(bool):** If `True`, set the `--stream` flag. Default is `False`.
- `port` **(integer):** Set the Webots instance port. Default is `1234`.
- `world` **(string):** Specifies the path to the world to be used. It can be a literal string or a [Substitution](https://github.com/ros2/launch/blob/2af92708bea1db2a6e15644053ef878fb990fedc/launch/launch/substitution.py), like in the [Examples](https://github.com/cyberbotics/webots_ros2/wiki/Examples) of this repository.
- `output` **(string):** (by default set to `'screen'`) and extra arguments will be used by the `init` function of [launch.actions.ExecuteProcess](https://github.com/ros2/launch/blob/2af92708bea1db2a6e15644053ef878fb990fedc/launch/launch/actions/execute_process.py).
- `ros2_supervisor` **(bool):** If `True`, spawns the `Ros2Supervisor` custom node that communicates with a Supervisor robot in the simulation. The `Ros2Supervisor` node is a special node interacting with the simulation. For example, it publishes the `/clock` topic of the simulation or permits to spawn robots from URDF files and PROTO strings.