---
tags: note/ROS
type: note
---
#### Intellisense

When you open an existing ROS 2 Python project, IntelliSense does not find your ROS 2 Python modules or local package modules. To solve the issue, create a file settings.json with content matching roughly the following:

```
{
  "python.autoComplete.extraPaths": [
    "/opt/ros/humble/lib/python3.10/site-packages",
    "/opt/ros/humble/local/lib/python3.10/dist-packages",
    "/my_project/build/package1",
    "/my_project/build/package2"
  ],
  "python.analysis.extraPaths": [
    "/opt/ros/humble/lib/python3.10/site-packages",
    "/opt/ros/humble/local/lib/python3.10/dist-packages",
    "/my_project/build/package1",
    "/my_project/build/package2"
  ]
}
```

All Python dependencies are stored in the environment variable PYTHONPATH. Unfortunately, VSCode does not use it. To get the list of all libraries, source your project and type the following bash command

`IFS=:; for path in $PYTHONPATH; do echo "\"$path\","; done`