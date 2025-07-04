---
summary: Every time docker successfully executes a `RUN` command, a new layer in the image filesystem is committed. You can use those layer ids as images to start a new container. You can see these if you set `DOCKER_BUILDKIT=0`.
type: note/workflow
headings:
  - "[[#Concepts of Note]]"
  - "[[#Examples]]"
date created: Tuesday, February 25th 2025, 12:57:06 pm
date modified: Tuesday, February 25th 2025, 1:00:20 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
Look for preceding docker image that was created, and exec into that
```shell
docker run --rm -it <id_last_working_layer> bash -il
```

## Examples
```
FROM busybox
RUN echo 'foo' > /tmp/foo.txt
RUN echo 'bar' >> /tmp/foo.txt
```

```
$ DOCKER_BUILDKIT=0 docker build -t so-26220957 .
Sending build context to Docker daemon 47.62 kB
Step 1/3 : FROM busybox
 ---> 00f017a8c2a6
Step 2/3 : RUN echo 'foo' > /tmp/foo.txt
 ---> Running in 4dbd01ebf27f
 ---> 044e1532c690
Removing intermediate container 4dbd01ebf27f
Step 3/3 : RUN echo 'bar' >> /tmp/foo.txt
 ---> Running in 74d81cb9d2b1
 ---> 5bd8172529c1
Removing intermediate container 74d81cb9d2b1
Successfully built 5bd8172529c1
```
Now start a container from various image commits....
```
$ docker run --rm 00f017a8c2a6 cat /tmp/foo.txt
cat: /tmp/foo.txt: No such file or directory

$ docker run --rm 044e1532c690 cat /tmp/foo.txt
foo

$ docker run --rm 5bd8172529c1 cat /tmp/foo.txt
foo
bar
```

Reproduce the error...