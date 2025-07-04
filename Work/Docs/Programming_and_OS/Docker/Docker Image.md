---
summary: A non-running container, built from a dockerfile or downloaded from Docker. Shows your computer how to create a container. Images are immutable and can't be changed after creation.
next: ["[[Docker Container]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, October 31st 2024, 3:38:55 pm
tags: [command/docker]
type: note/system
---
`VIEW[**{summary}**][text(renderMarkdown)]`

[Docker Official Images](https://docs.docker.com/trusted-content/official-images/)

# Usage
## Where are images found?
Docker will search local images first, then move onto [Docker Hub](https://docs.docker.com/trusted-content/official-images/) if it can't find the desired image. 

## Image naming
Images *may* consist of 3 parts and a tag
```
registry/organization/image:tag
```

## Building Images
[[Docker Dockerfile]] determines how the image is built. 
```
docker build . -t <name>
```
- Will look for a file named "Dockerfile" and try to build it with the given name. 

Build an image from a dockerfile
```shell
docker image build
```

## Other Image Commands/Uses
- [p] `docker image history IMAGE` = Shows the history of an image = #command/docker 
<!--ID: 1751434091158-->

- [p] `docker image import file|URL|- [REPOSITORY[:TAG]]` = Import the contents from a tarbell to create a filesystem image = #command/docker 
<!--ID: 1751434091162-->

- [p] `docker image inspect IMAGE [IMAGE...]` =Detailed info on one or more images = #command/docker 
- [p] `docker image load IMAGE` = Load an image or repo from a tar archive from a file or STDIN. = #command/docker 
<!--ID: 1751434091166-->

- [p] `docker image prune` = Remove all dangling images. = #command/docker 
<!--ID: 1751434091170-->
