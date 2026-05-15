---
summary: Python SDK for the Docker Engine API — manage containers, images, networks, and volumes programmatically.
type: note/library
headings:
up: "[[Python]]"
similar:
  - "[[Docker Container]]"
  - "[[Docker Image]]"
  - "[[Docker Networks]]"
  - "[[Docker Volume]]"
ai_generated: true
associations:
  - "[[Docker CLI basics]]"
  - "[[Docker.md]]"
date created: Tuesday, April 7th 2026, 12:00:00 pm
date modified: Tuesday, April 7th 2026, 11:23:06 am
library_of:
  - "[[Python]]"
tags: [programming/docker, programming/python]
template:
template-version:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
Install: `pip install docker`. Wraps the Docker Engine REST API over Unix socket or TCP.
Two client tiers: high-level (`DockerClient`) for typed resource objects; low-level (`APIClient`) for 1:1 REST endpoint mapping.

## Concepts of Note
󰙎 `DockerClient` ;;; High-level client — exposes resource collections (`containers`, `images`, `networks`, `volumes`) returning typed objects
󰙎 `APIClient` ;;; Low-level client — methods map 1:1 to Docker REST endpoints, returns raw dicts; use when high-level API lacks coverage
󰙎 resource object ;;; Typed Python object (`Container`, `Image`, `Network`, `Volume`) returned by collection methods; wraps `.attrs` dict and provides action methods
󰙎 collection ;;; Attribute on `DockerClient` (e.g. `client.containers`) grouping CRUD operations for a resource type
󰙎 `detach` ;;; Key behavioral split in `run()`: `True` → non-blocking, returns `Container`; `False` (default) → blocks, returns stdout `bytes`
󰙎 `stream` ;;; `True` on `logs()` / `build()` → returns byte-line generator instead of buffered output

## Usage

```python
import docker
client = docker.from_env()

# One-shot: run and capture stdout
output = client.containers.run("ubuntu:22.04", "echo hello", remove=True)

# Detached with streaming logs
c = client.containers.run("nginx", detach=True, ports={'80/tcp': 8080})
for line in c.logs(stream=True, follow=True):
    print(line.strip().decode())
c.stop()
c.remove()

# Build image from local Dockerfile
image, build_logs = client.images.build(path=".", tag="myapp:latest")

# Exec command inside running container
result = c.exec_run("ls /var/log")
print(result.output.decode())

# Create isolated network and attach container
net = client.networks.create("mynet", driver="bridge")
net.connect(c)
```

## Properties

### Client Connection
 `docker.from_env()` ;;; Connect via `DOCKER_HOST` / `DOCKER_TLS_VERIFY` env vars, or Unix socket default — preferred entry point
 `docker.DockerClient(base_url=...)` ;;; Explicit connection: `'tcp://10.0.0.1:2376'` or `'unix://var/run/docker.sock'`

### ContainerCollection
 `client.containers.run(image, cmd, **kw)` ;;; Create + start; key kwargs: `detach`, `auto_remove`, `ports`, `volumes`, `environment`, `network`
 `client.containers.get(id_or_name)` ;;; Returns `Container` by ID, name, or short ID
 `client.containers.list(all=False)` ;;; Returns `[Container]`; `all=True` includes stopped containers
 `client.containers.prune()` ;;; Remove all stopped containers; returns dict with reclaimed space

### Container
 `Container.start()` / `Container.stop(timeout)` / `Container.restart()` ;;; Lifecycle controls; `stop()` sends SIGTERM then SIGKILL after timeout
 `Container.remove(force=False)` ;;; Delete container; `force=True` removes running container
 `Container.logs(stream=False, follow=False)` ;;; Returns `bytes` or generator; use `stream=True, follow=True` to tail live output
 `Container.exec_run(cmd)` ;;; Run command inside container; returns `ExecResult` with `.exit_code` and `.output`
 `Container.wait()` ;;; Block until container exits; returns `{'StatusCode': int}`
 `Container.stats(stream=False)` ;;; CPU/memory/network usage; `stream=True` → stat dict generator
 `Container.reload()` ;;; Refresh `.attrs` from daemon
 `Container.attrs` ;;; Raw dict of container inspect data — equivalent to `docker inspect`

### ImageCollection
 `client.images.pull(repo, tag='latest')` ;;; Pull from registry; returns `Image`
 `client.images.build(path, tag, dockerfile)` ;;; Build from [[Docker Dockerfile]]; returns `(Image, log_generator)`
 `client.images.get(name)` ;;; Returns local `Image` by name or ID
 `client.images.list(filters={})` ;;; Returns `[Image]`; filter by `name`, `label`, `dangling`
 `client.images.prune(filters={})` ;;; Remove dangling (untagged) images

### Image
 `Image.tag(repo, tag)` ;;; Add a tag to the image
 `Image.save()` ;;; Returns generator of raw bytes (tar stream) — write with `open(f, 'wb')`
 `Image.attrs` ;;; Raw inspect data — equivalent to `docker image inspect`

### NetworkCollection & Network
 `client.networks.create(name, driver='bridge')` ;;; Common drivers: `bridge`, `overlay`, `host`, `none`; see [[Docker Networks]]
 `Network.connect(container)` / `Network.disconnect(container)` ;;; Attach or detach container at runtime
 `Network.remove()` ;;; Delete network; all containers must be disconnected first

### VolumeCollection & Volume
 `client.volumes.create(name, driver='local', driver_opts={})` ;;; Create named volume; mount via `volumes` kwarg on `run()`; see [[Docker Volume]]
 `client.volumes.get(name)` / `client.volumes.list()` ;;; Fetch single or all volumes
 `Volume.remove(force=False)` ;;; Delete volume; fails if in use unless `force=True`
