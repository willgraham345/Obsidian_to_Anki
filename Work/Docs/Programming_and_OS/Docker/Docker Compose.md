---
summary: A way of launching/managing multiple docker containers at once. This note has both the reference for usage as well as the reference for defining the compose files.
type: note/component
implements: ["[[Docker]]"]
concepts: ["[[Docker Compose File and Application]]"]
components: ["[[Docker Compose YAML Args]]"]
workflows: ["[[Docker Compose File Workflow]]"]
component_of: ["[[Docker]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Monday, February 24th 2025, 1:21:13 pm
tags: [command/docker, command/dockercompose]
---

# Summary

`VIEW[**{summary}**][text(renderMarkdown)]`
[Compose file reference | Docker Docs](https://docs.docker.com/reference/compose-file/) (use this or the [[Docker-compose Command DB]] for YAML inputs)
[docker compose CLI Reference](https://docs.docker.com/reference/cli/docker/compose/)
[history of compose](https://docs.docker.com/compose/intro/history/)
[Docker Compose Specification](https://github.com/compose-spec/compose-spec/blob/main/spec.md#image)

- File format for multi-container application.

# Breadcrumbs

```breadcrumbs
type: mermaid
depth: [0, 4]
field-groups: [downs]
merge-fields: true
sort: field asc
show-attributes: [field]
collapse: false
```

# CLI Usage

Services are defined within a compose file (typically `compose.yaml`) placed within the working directory

- These compose files can be merged using the
- [p] `docker compose` = Define and run multi-container applications within docker based on current directory = #command/dockercompose = `-f` Compose given configuration files.
<!--ID: 1751434091288-->

  `--profile` Specify a profile to enable
  `-p` Project name
- [p] `docker compose build` = Build or rebuild services = #command/dockercompose = `--pull` Always attempt to pull a newer version of the image
<!--ID: 1751434091292-->

  `--with-dependencies` Also build dependencies.
  `--no-cache` Do not use cache when building the image
- [p] `docker compose up` = Build (if necessary) and start services defined in your compose.yaml file within the project directory = #command/dockercompose = `-d` Detach mode (in background)
<!--ID: 1751434091296-->

  `-V` recreate anonymous volumes for services not defined.
  `--pull` Pull image before running (`always`,`missing`,`never`)
  `-`
- [p] `docker compose down` = Stops and removes running services = #command/dockercompose
<!--ID: 1751434091300-->

- [p] `docker compose logs` = Monitor the output of your running containers and debug issues. = #command/dockercompose
<!--ID: 1751434091304-->

- [p] `docker compose ps` = Displays running services = #command/dockercompose
<!--ID: 1751434091309-->

