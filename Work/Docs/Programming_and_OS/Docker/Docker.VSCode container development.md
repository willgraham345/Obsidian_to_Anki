---
type: note
---
# Background
We would like to use a full-featured development environment. 
- A `devcontainer.json` file tells VS Code how to access (or create) a development container with a well-defined tool and runtime stack. 
	- This container can be used to: run an application, separate tools, libraries, or runtimes. 
- Workspace files are mounted from the local file system or copied or cloned into the container. 
- Extensions are installed and run within the container, where they have full access to the tools, platform, and file system. 
	- You can seamlessly switch your entire development environment just by connecting to a different container. 

![[Pasted image 20240403150756.png]]

Development inside of a container is the goal.

# Usage
## Quick start: Open an existing folder in a container
1. Start VS Code, run the **Dev Containers: Open Folder in Container...** command
2. Choose a **Dev Container Template** from a filterable list, or use an exiting Dockerfile or Docker Compose File. 

## Opening a Git repo in an isolated container volume
[Opening Git Repo in isolated container volume](https://code.visualstudio.com/docs/devcontainers/containers#_quick-start-open-a-git-repository-or-github-pr-in-an-isolated-container-volume)