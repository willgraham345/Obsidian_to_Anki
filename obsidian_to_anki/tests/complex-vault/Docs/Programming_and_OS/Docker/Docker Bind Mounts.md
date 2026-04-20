---
summary: Bind mounts have limited functionality compared with volumes. A file/directory on the host machine is mounted into a container. This file is referenced by its absolute path on the host machine. When you use a volume, a new directory is created within Docker's storage directory on the host machine, and Docker manages that directory's contents.
headings: ["[[#Media]]", "[[#Usage]]"]
type: note/concept
similar: ["[[Docker Volume]]"]
date created: Monday, December 2nd 2024, 4:45:37 pm
date modified: Friday, April 25th 2025, 4:02:45 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

`-v` or `--mount`
- Mount is more explicit and verbose.

## Media
[Bind mounts | Docker Docs](https://docs.docker.com/engine/storage/bind-mounts/#choose-the--v-or---mount-flag)
 - [Choose the -v or --mount flag](https://docs.docker.com/engine/storage/bind-mounts/#choose-the--v-or---mount-flag)
- [Differences between `-v` and `--mount` behavior](https://docs.docker.com/engine/storage/bind-mounts/#differences-between--v-and---mount-behavior)
- [Start a container with a bind mount](https://docs.docker.com/engine/storage/bind-mounts/#start-a-container-with-a-bind-mount)
- [Mount into a non-empty directory on the container](https://docs.docker.com/engine/storage/bind-mounts/#mount-into-a-non-empty-directory-on-the-container)
- [Use a read-only bind mount](https://docs.docker.com/engine/storage/bind-mounts/#use-a-read-only-bind-mount)
- [Recursive mounts](https://docs.docker.com/engine/storage/bind-mounts/#recursive-mounts)
- [Configure bind propagation](https://docs.docker.com/engine/storage/bind-mounts/#configure-bind-propagation)
- [Configure the selinux label](https://docs.docker.com/engine/storage/bind-mounts/#configure-the-selinux-label)
- [Use a bind mount with compose](https://docs.docker.com/engine/storage/bind-mounts/#use-a-bind-mount-with-compose)
- [Next steps](https://docs.docker.com/engine/storage/bind-mounts/#next-steps)

# Media