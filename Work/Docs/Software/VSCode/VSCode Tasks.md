---
type: note
tags: note/VSCode
---
# Background
- Tasks in VSCode can be configured to run scripts and start processes so they can be used within the software rather than exiting the application
	- Lots of tools exist for automatable tasks (linting, packaging, testing, deploying, and building). 
		- Some are build systems ([[GNU make]], [[Cpp.MSBuild]])
	- These tools are mostly run from the command line and automate jobs inside and outside of the inner software development loop. 
## Configuration
Stored within the `tasks.json` file in the `.vscode/` for a workspace. 
Extensions can also contribute tasks using a task provider. 

### Task auto-detection
VSCode auto-detects tasks for: 
- Gulp
- Grunt
- Jake
- npm

### Custom tasks
[[VSCode Custom Tasks]]


# Usage