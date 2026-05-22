---
summary: A way of launching/managing multiple docker containers at once. This note has both the reference for usage as well as the reference for defining the compose files.
type: note/item
headings:
  - "[[#Breadcrumbs]]"
  - "[[#Usage]]"
implements:
  - "[[Docker]]"
concepts:
  - "[[Docker Compose File and Application]]"
processes:
  - "[[Docker Compose File Workflow]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, January 22nd 2026, 9:43:31 am
item_of:
  - "[[Docker]]"
items:
  - "[[Docker Compose spec]]"
tags:
  - tools/docker
  - tools/docker/compose
template:
template-version:
---

# Summary

`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

[Compose file reference | Docker Docs](https://docs.docker.com/reference/compose-file/) (use this or the [[Docker-compose Command DB]] for YAML inputs)
[docker compose CLI Reference](https://docs.docker.com/reference/cli/docker/compose/)
[history of compose](https://docs.docker.com/compose/intro/history/)
[Docker Compose Specification](https://github.com/compose-spec/compose-spec/blob/main/spec.md#image)

- File format for multi-container application.

## Breadcrumbs %% fold %%

```breadcrumbs
type: mermaid
depth: [0, 4]
field-groups: [downs]
merge-fields: true
sort: field asc
show-attributes: [field]
collapse: false
```

## Usage

Services are defined within a compose file (typically `compose.yaml`) placed within the working directory. Compose files can be merged using docker compose yaml.

  `docker compose` ;;; Define and run multi-container applications within docker based on current directory

  `docker compose build` ;;; Build or rebuild services, attempting to pull a newer version of the image.

  `docker compose build --no-cache` ;;; Build or rebuild services, and don't use the docker cache when building the image.

  `docker compose up -d` ;;; Build (if necessary) and start services defined in your compose.yaml file within the project directory, and disable printing output.

  `docker compose down` ;;; Stops and removes running services

  `docker compose logs` ;;; Monitor the output of your running containers and debug issues.

  `docker compose ps` ;;; Displays running services
