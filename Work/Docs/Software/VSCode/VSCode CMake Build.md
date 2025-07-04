---
type: note
tags: note/VSCode
---
# Background
After you have configured your project, you can run a CMake build. 

## Default target
CMake persists a "default target" for the build process. The default target is "all" target (named `ALL_BUILD`) in some generators, which builds all of the targets that CMake has designated for a default build. 
- Modifying this within the view will present all known targets that CMake Tools can see, and the full path to the build result that will be generated. 

# Usage
## Starting a build
1. `CMake: Build`
2. `F7` key (default shortcut)
3. Select `Build` button in VSCode status bar. 
## cmake.buildDirectory
Results of any build are written to the `cmake.buildDirectory`
- Defaults to a subdirectory of the project directory
## Create a build Task
You can define a build task by running `Tasks: Configure Task`
- This creates a `${workspaceFolder}/.vscode/tasks.json` file. 
- You can modify `"targets"` with a single target or a list of targets that can be built. 
### Example custom build task
```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "type": "cmake",
            "label": "Sample CMake build task with single target",
            "command": "build",
            "targets": [
                "prj1"
            ],
            "group": "build",
            "problemMatcher": [],
            "detail": "Build task to build prj1"
        },
        {
            "type": "cmake",
            "label": "Sample CMake build task with multiple targets",
            "command": "build",
            "targets": [
                "prj1",
                "prj2"
            ],
            "group": "build",
            "problemMatcher": [],
            "detail": "Build task to build prj1 and prj2"
        }
    ]
}
```