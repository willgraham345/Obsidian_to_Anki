---
type: cheatsheet
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Monday, December 2nd 2024, 6:35:15 pm
tags:
---
Most used
  `docker image ls` ;;; Lists all images = #tools/docker/build 
ID: 1751997629303



  `docker image rm <image>` ;;; Removes an image = #tools/docker 
ID: 1751997629308



  `docker image pull <image>` ;;; Pulls image from a docker registry = #tools/docker 
ID: 1751997629313



  `docker container ls` ;;; List running containers = #tools/docker = `-a` List all containers 
ID: 1751997629318



  `docker container rm <container>` ;;; Removes a container = #tools/docker = `-f` Force remove a container 
ID: 1751997629323



      Can be combined with `$(docker ps -qa)` to remove all currently-running processes
  `docker container stop <container>` ;;; Stops a container = #tools/docker 
  `sudo service docker start` ;;; Starts the docker engine from CLI = #tools/docker 


By section
  `docker image ls` ;;; List all images = #tools/docker 
  `docker pull <image>` ;;; Pull an image from Docker Hub = #tools/docker 
  `docker rmi <image>` ;;; Remove an image = #tools/docker 
  `docker build <path> | <URL>` ;;; Build an image from a Dockerfile = #tools/docker = `<path>` You can pass the relative/absolute path to a local directory for a build context. See [[Docker build context]] 
  `docker tag <image> <tag>` ;;; Tag an image with a name and optionally a tag = #tools/docker 

Docker hub commands
  `docker login` ;;; Log in to Docker Hub = #tools/docker 
  `docker logout` ;;; Log out from Docker Hub = #tools/docker 
  `docker search <image-name>` ;;; Search Docker Hub for images = #tools/docker 
  `docker push <image>` ;;; Push an image to Docker Hub = #tools/docker 
  `docker pull <image:tag>` ;;; Pull a specific version of an image from Docker Hub = #tools/docker 

General Commands
  `docker version` ;;; Show Docker version information = #tools/docker 
  `docker info` ;;; Display system-wide information about Docker = #tools/docker 
  `docker ps` ;;; List all running containers = #tools/docker = `-a` List even stopped containers 
  `docker start <container>` ;;; Start a stopped container = #tools/docker 
  `docker stop <container>` ;;; Stop a running container = #tools/docker 
  `docker system prune` ;;; Cleans up and frees all storage space unused by docker = #tools/docker  

Container commands:
  `docker run <image>` ;;; Run a command in a new container = #tools/docker = `-i` Keeps stdin open 
      `-t or --tty` Attaches a pseudo-tty to the container, connecting your terminal to the I/O streams of the container.
  `docker exec <container> <command>` ;;; Execute a command in a running container = #tools/docker = `-it` `sh` will let you run bash inside a container 
  `docker rm <container>` ;;; Remove a container = #tools/docker 
  `docker logs <container>` ;;; Fetch the logs of a container = #tools/docker 
  `docker inspect <container>` ;;; Display detailed information about a container = #tools/docker 
  `docker restart <container>` ;;; Restart a container = #tools/docker 
  `docker diff` ;;; Will show what has changed in a container = #tools/docker 
  `docker rm` ;;; Removes docker containers from = #tools/docker = `-f` Force remove 
      `$(docker ps -qa)` Remove all docker containers
  `docker volume rm` ;;; Remove volumes = #tools/docker =  `-f` Force 
ID: 1751997629327



      `$(docker volume ls -q)` Remove all docker volumes
  `docker cp [OPTIONS] CONTAINER:SRC_PATH DEST_PATH` ;;; Copy from the source path to the destination path. = #tools/docker = `-a` Archive mode (copy all uid/gid info) 
ID: 1751997629331



      `-L` Always follow symbol link in SRC_PATH
