---
summary: A non-running container, built from a dockerfile or downloaded from Docker. Shows your computer how to create a container. Images are immutable and can't be changed after creation.
type: note/system
next: ["[[Docker Container]]"]
prev: ["[[Docker Dockerfile|Dockerfile]]"]
concept_of: ["[[Docker]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, September 12th 2025, 1:24:34 pm
tags: [tools/docker]
used_by: ["[[Docker Container]]", "[[Docker registry]]"]
uses: ["[[Docker Dockerfile|Dockerfile]]"]
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
  `docker image history IMAGE` ;;; Shows the history of an image = #tools/docker  
ID: 1751997629200



  `docker image import file|URL|- [REPOSITORY[:TAG]]` ;;; Import the contents from a tarbell to create a filesystem image = #tools/docker  
ID: 1751997629204



  `docker image inspect IMAGE [IMAGE...]` =Detailed info on one or more images ;;; #tools/docker 
  `docker image load IMAGE` ;;; Load an image or repo from a tar archive from a file or STDIN. = #tools/docker  
ID: 1751997629209



  `docker image prune` ;;; Remove all dangling images. = #tools/docker  
ID: 1751997629213


