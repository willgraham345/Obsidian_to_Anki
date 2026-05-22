---
summary: The file containing instructions on how a container should be built. A non-running container is known as an image.
type: note/system
headings:
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
functions:
  - "[[Docker Dockerfile RUN]]"
next:
  - "[[Docker Image]]"
aliases: [Dockerfile]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, April 2nd 2026, 11:08:08 am
item_of:
  - "[[Docker]]"
processes:
  - "[[Docker Dockerfile Debugging]]"
tags: [tools/docker/dockerfile]
template: "[[base_note_template]]"
template-version: 1.0.1
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

[Dockerfile reference | Docker Docs](https://docs.docker.com/reference/dockerfile/#run)

## Concepts of Note

###  Multi-stage
- Useful to anyone who has struggled to optimize Dockerfiles while keeping them easy to read and maintain
- You can use a previous stage as a new stage with [[Docker Dockerfile#`FROM`]]

### Basic outline
```dockerfile
FROM <image>:<tag>

RUN <install some dependencies>

CMD <command that is executed on `docker container run`>
```

## Usage

`CMD` or `ENTRYPOINT`
- Executed when the image is instantiated as container
- Executed at runtime
  `ADD` ;;; Add local or remote files and directories
  `ADD` ;;; Add local or remote files and directories.
  `ARG` ;;; Use build-time variables.
  `CMD` ;;; Specify default commands. There can only be one "CMD" instructions in a dockerfile. If you would like to run the same executable every time, then you should consider using `ENTRYPOINT`.
  `COPY` ;;; Copy files and directories.
  `ENTRYPOINT` ;;; Specify default executable.
  `ENV` ;;; Set environment variables.
  `EXPOSE` ;;; Describe which ports your application is listening on.
  `FROM` ;;; Create a new build stage from a base image.
  `HEALTHCHECK` ;;; Check a container's health on startup.
  `LABEL` ;;; Add metadata to an image.
  `MAINTAINER` ;;; Specify the author of an image.
  `ONBUILD` ;;; Specify instructions for when the image is used in a build.
  `SHELL` ;;; Set the default shell of an image.
  `STOPSIGNAL` ;;; Specify the system call signal for exiting a container.
  `USER` ;;; Set user and group ID.
  `VOLUME` ;;; Create volume mounts.
  `WORKDIR` ;;; Change working directory.
