---
tags: note/ROS
type: note
---
In your `launch.json`


```json
{
	// Use IntelliSense to learn about possible attributes.
	// Hover to view descriptions of existing attributes.
	// For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
	"version": "0.2.0",
	"configurations": [
			{
				"name": "ROS: Attach",
				"type": "ros",
				"request": "attach"
			},
			{
				"name": "ROS: Attach to Python",
				"type": "ros",
				"request": "attach",
				"runtime": "Python",
			},
			{ 
				// This works and fixes a bug I had with humble. See https://github.com/ms-iot/vscode-ros/issues/872
				"name": "Python Debugger: Current File with Arguments",
				"type": "debugpy",
				"request": "launch",
				"program": "${file}",
				"console": "integratedTerminal",
				"args": "${command:pickArgs}"
			},
		]
}
```