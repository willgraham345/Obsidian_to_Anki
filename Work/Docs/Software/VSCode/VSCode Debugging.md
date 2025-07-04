---
summary: 
type: note/concept
concept_of:
  - "[[VSCode TOC]]"
date created: Tuesday, August 20th 2024, 2:05:35 pm
date modified: Thursday, February 13th 2025, 12:05:24 pm
components:
  - "[[VSCode Cpp Debugging]]"
---
# Background
- 

## Launch Configurations
- Configured through a `.vscode/launch.json`
- VSCode will detect your debug environment
- `Ctrl+Space` is really helpful for setting up debugger attributes. 

### Launch vs Attach
Launch = similar to a recipe on how to start the app in debug mode *before* VSCode attaches to it.
Attach = recipe on how to connect VSCode's debugger to an app or process that's already running.

## Breakpoints/Logpoints
- Helpful for stepping through functions

# Usage
## Launch.json attributes
### Mandatory Attributes
- `type` - the type of debugger to use for this launch configuration. Every installed debug extension introduces a type: `node` for the built-in Node debugger, for example, or `php` and `go` for the PHP and Go extensions.
- `request` - the request type of this launch configuration. Currently, `launch` and `attach` are supported.
- `name` - the reader-friendly name to appear in the Debug launch co

### Optional Attributes
- `presentation` - using the `order`, `group`, and `hidden` attributes in the `presentation` object, you can sort, group, and hide configurations and compounds in the Debug configuration dropdown and in the Debug quick pick.
- `preLaunchTask` - to launch a task before the start of a debug session, set this attribute to the label of a task specified in [tasks.json](https://code.visualstudio.com/docs/editor/tasks) (in the workspace's `.vscode` folder). Or, this can be set to `${defaultBuildTask}` to use your default build task.
- `postDebugTask` - to launch a task at the very end of a debug session, set this attribute to the name of a task specified in [tasks.json](https://code.visualstudio.com/docs/editor/tasks) (in the workspace's `.vscode` folder).
- `internalConsoleOptions` - this attribute controls the visibility of the Debug Console panel during a debugging session.
- `debugServer` - **for debug extension authors only**: this attribute allows you to connect to a specified port instead of launching the debug adapter.
- `serverReadyAction` - if you want to open a URL in a web browser whenever the program under debugging outputs a specific message to the debug console or integrated terminal. For details see section [Automatically open a URI when debugging a server program](https://code.visualstudio.com/docs/editor/debugging#_automatically-open-a-uri-when-debugging-a-server-program) below.