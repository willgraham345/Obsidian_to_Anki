---
summary: A runtime environment, or a tool used to create+deploy+run applications. Components include a name and a container id.
type: note/system
components:
  - "[[Docker Container id]]"
  - "[[Docker Container name]]"
workflows:
  - "[[Docker Container defining start conditions]]"
  - "[[Docker Container devcontainer json]]"
  - "[[Docker Container Development features]]"
  - "[[Docker Container JSON Run]]"
  - "[[Docker Container cgroups resource control workflow]]"
similar:
  - "[[Docker Services]]"
prev:
  - "[[Docker Image]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, November 19th 2024, 1:44:21 pm
tags:
  - command/docker
---
# Background
- A thing that "contains" everything required to execute an application. Essentially a runtime environment *container*.
	- A tool used to create, deploy and run applications. They let us to package an app with all the parts it needs (libraries, frameworks, dependencies) and ship it all out as one package.
	- Continuous availability, using docker with tools like Kubernetes, is another reason for the popularity of containers. 
		- This enables multiple versions of your app container to be created at different times. Each container can be replaced on the fly. 
- Isolated environments in the host machine with ability to interact with each other and the host machine itself via defined methods (TCP/UDP)

## Components
Name
Container ID

# Usage
- [p] `docker stop $(docker ps -a -q)` = Stops all running docker containers = #command/docker 
<!--ID: 1751434091282-->
