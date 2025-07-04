---
summary: The file containing instructions on how a container should be built. A non-running container is known as an image.
type: note/system
functions:
  - "[[Docker Dockerfile RUN]]"
next:
  - "[[Docker Image]]"
aliases:
  - Dockerfile
component_of:
  - "[[Docker]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, February 25th 2025, 12:20:11 pm
tags:
  - command/dockerfile
workflows:
  - "[[Docker Dockerfile Debugging]]"
---
[Dockerfile reference | Docker Docs](https://docs.docker.com/reference/dockerfile/#run)

## Types of Dockerfiles
Multi-stage
- Useful to anyone who has struggled to optimize Dockerfiles while keeping them easy to read and maintain
- You can use a previous stage as a new stage with [[Docker Dockerfile#`FROM`]]
Final Image
- 

## Basic outline
```dockerfile
FROM <image>:<tag>

RUN <install some dependencies>

CMD <command that is executed on `docker container run`>
```

# Usage
[Dockerfile reference | Docker Docs](https://docs.docker.com/reference/dockerfile/#run)

### `CMD` or `ENTRYPOINT`
- Executed when the image is instantiated as container
- Executed at runtime


- [p] `ADD` = Add local or remote files and directories = #command/dockerfile 
<!--ID: 1751434091175-->

- [p] `ADD` = Add local or remote files and directories. = #command/dockerfile 
<!--ID: 1751434382795-->

- [p] `ARG` = Use build-time variables. = #command/dockerfile
<!--ID: 1751434091180-->

- [p] `CMD` = Specify default commands. There can only be one "CMD" instructions in a dockerfile. If you would like to run the same executable every time, then you should consider using `ENTRYPOINT` = #command/dockerfile
<!--ID: 1751434091184-->

- [p] `COPY` = Copy files and directories. = #command/dockerfile
<!--ID: 1751434091187-->

- [p] `ENTRYPOINT` = Specify default executable. = #command/dockerfile
<!--ID: 1751434091190-->

- [p] `ENV` = Set environment variables. = #command/dockerfile
<!--ID: 1751434091194-->

- [p] `EXPOSE` = Describe which ports your application is listening on. = #command/dockerfile
<!--ID: 1751434091198-->

- [p] `FROM` = Create a new build stage from a base image. = #command/dockerfile
<!--ID: 1751434091201-->

- [p] `HEALTHCHECK` = Check a container's health on startup. = #command/dockerfile
<!--ID: 1751434091204-->

- [p] `LABEL` = Add metadata to an image. = #command/dockerfile
<!--ID: 1751434091209-->

- [p] `MAINTAINER` = Specify the author of an image. = #command/dockerfile
<!--ID: 1751434091213-->

- [p] `ONBUILD` = Specify instructions for when the image is used in a build. = #command/dockerfile
<!--ID: 1751434091218-->

      
- [p] `SHELL` = Set the default shell of an image. = #command/dockerfile
<!--ID: 1751434091223-->

- [p] `STOPSIGNAL` = Specify the system call signal for exiting a container. = #command/dockerfile
<!--ID: 1751434091228-->

- [p] `USER` = Set user and group ID. = #command/dockerfile
<!--ID: 1751434091233-->

- [p] `VOLUME` = Create volume mounts. = #command/dockerfile
<!--ID: 1751434091238-->

- [p] `WORKDIR` = Change working directory. = #command/dockerfile
<!--ID: 1751434091244-->


## Use previous stage as a new stage