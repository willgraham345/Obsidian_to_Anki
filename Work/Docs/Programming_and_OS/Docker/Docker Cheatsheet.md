---
type: cheatsheet
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Monday, December 2nd 2024, 6:35:15 pm
tags: [command/docker, note/docker]
---
Most used
- [p] `docker image ls` = Lists all images = #command/docker/build
<!--ID: 1751434091328-->

- [p] `docker image rm <image>` = Removes an image = #command/docker
<!--ID: 1751434091332-->

- [p] `docker image pull <image>` = Pulls image from a docker registry = #command/docker
<!--ID: 1751434091336-->

- [p] `docker container ls` = List running containers = #command/docker = `-a` List all containers
<!--ID: 1751434091340-->

- [p] `docker container rm <container>` = Removes a container = #command/docker = `-f` Force remove a container
<!--ID: 1751434091344-->

      Can be combined with `$(docker ps -qa)` to remove all currently-running processes
- [p] `docker container stop <container>` = Stops a container = #command/docker
- [p] `sudo service docker start` = Starts the docker engine from CLI = #command/docker


By section
- [p] `docker image ls` = List all images = #command/docker
- [p] `docker pull <image>` = Pull an image from Docker Hub = #command/docker
- [p] `docker rmi <image>` = Remove an image = #command/docker
- [p] `docker build <path> | <URL>` = Build an image from a Dockerfile = #command/docker = `<path>` You can pass the relative/absolute path to a local directory for a build context. See [[Docker build context]]
- [p] `docker tag <image> <tag>` = Tag an image with a name and optionally a tag = #command/docker

Docker hub commands
- [p] `docker login` = Log in to Docker Hub = #command/docker
- [p] `docker logout` = Log out from Docker Hub = #command/docker
- [p] `docker search <image-name>` = Search Docker Hub for images = #command/docker
- [p] `docker push <image>` = Push an image to Docker Hub = #command/docker
- [p] `docker pull <image:tag>` = Pull a specific version of an image from Docker Hub = #command/docker

General Commands
- [p] `docker version` = Show Docker version information = #command/docker
- [p] `docker info` = Display system-wide information about Docker = #command/docker
- [p] `docker ps` = List all running containers = #command/docker = `-a` List even stopped containers
- [p] `docker start <container>` = Start a stopped container = #command/docker
- [p] `docker stop <container>` = Stop a running container = #command/docker
- [p] `docker system prune` = Cleans up and frees all storage space unused by docker = #command/docker 

Container commands:
- [p] `docker run <image>` = Run a command in a new container = #command/docker = `-i` Keeps stdin open
      `-t or --tty` Attaches a pseudo-tty to the container, connecting your terminal to the I/O streams of the container.
- [p] `docker exec <container> <command>` = Execute a command in a running container = #command/docker = `-it` `sh` will let you run bash inside a container
- [p] `docker rm <container>` = Remove a container = #command/docker
- [p] `docker logs <container>` = Fetch the logs of a container = #command/docker
- [p] `docker inspect <container>` = Display detailed information about a container = #command/docker
- [p] `docker restart <container>` = Restart a container = #command/docker
- [p] `docker diff` = Will show what has changed in a container = #command/docker
- [p] `docker rm` = Removes docker containers from = #command/docker = `-f` Force remove
      `$(docker ps -qa)` Remove all docker containers
- [p] `docker volume rm` = Remove volumes = #command/docker =  `-f` Force
<!--ID: 1751434091348-->

      `$(docker volume ls -q)` Remove all docker volumes
- [p] `docker cp [OPTIONS] CONTAINER:SRC_PATH DEST_PATH` = Copy from the source path to the destination path. = #command/docker = `-a` Archive mode (copy all uid/gid info)
<!--ID: 1751434091352-->

      `-L` Always follow symbol link in SRC_PATH