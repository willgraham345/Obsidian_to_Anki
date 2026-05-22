---
type: note
---
# Background
- 3 parts to the Docker Engine
	- CLI
	- REST API
	- Docker Daemon

When we run a command (i.e. `docker container run`) the client sends a request through the REST API to the Docker Daemon which takes care of images, containers, and other resources. 

[Docs for cli](https://docs.docker.com/engine/reference/commandline/cli/)
- Only a handful are actually useful. 

# Usage