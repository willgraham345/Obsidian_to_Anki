---
summary: How to expose the docker service within WSL to windows.
type: note/workflow
date created: Friday, January 10th 2025, 9:46:20 am
date modified: Friday, January 10th 2025, 9:51:30 am
workflow_of: ["[[Docker]]", "[[WSL]]"]
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

Edit systemd file and modify ExecStart line

Reload docker service

Visit http://localhost:2375/version, you should see a response.

Create/edit Windows environment variable `DOCKER_HOST` to value tcp://localhost:2375
- Done in the advanced system properties window.

You should be able to download and use docker on Windows.

## Gotchas
If systemd is not set up in your wsl, you'll need to edit the `/etc/wsl.conf` file to set systemd as the init system.
```
[network]
generateResolvConf = false

# this is what you need to add
[boot]
systemd= true
```


If you are getting "permissions error" when connecting to docker daemon socket, double check the permissions on `var/run/docker.sock` file. Turned out that something in the setup had changed the ownership to something else.