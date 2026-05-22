---
summary: List of arguments within docker that specify the way you'd like your containers to be run.
type: note/item
headings:
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
ai_generated: true
associations:
  - "[[Docker Dockerfile]]"
date created: Wednesday, February 5th 2025, 1:33:23 pm
date modified: Thursday, April 2nd 2026, 1:57:36 pm
item_of:
  - "[[Docker Compose]]"
tags: [tools/docker/compose]
template:
template-version:
---

# Summary

`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note

Usage is defined here: [Services \| Docker Docs](https://docs.docker.com/reference/compose-file/services/#environment)

## Usage

### Top-level keys

 `name` ;;; Project name; overridable via env `COMPOSE_PROJECT_NAME`
 `services` ;;; Map of service definitions (core of any compose file)
 `networks` ;;; Named networks shared across services
 `volumes` ;;; Named volumes shared across services
 `secrets` ;;; Secrets shared across services
 `configs` ;;; Config objects shared across services
 `include` ;;; Embed sub-project compose files; sub-key: `path:`
 `x-<name>` ;;; Extension field — define reusable YAML anchor, reference with `<<: *name`
 `version` ;;; **Deprecated** — ignored by spec, remove from files

### Service fields

 `image` ;;; Image to use (`repo/tag`, digest, or local ID)
 `build` ;;; Build config; string = context path, or object with `context`, `dockerfile`, `target`, `args`, `platforms`
 `command` ;;; Overrides Dockerfile `CMD`
 `entrypoint` ;;; Overrides Dockerfile `ENTRYPOINT`
 `environment` ;;; Env vars as map or `KEY=VAL` list
 `env_file` ;;; Load env vars from file(s)
 `ports` ;;; Publish ports; short: `[HOST_IP:][HOST_PORT:]CONTAINER[/PROTOCOL]`; long form: `target:`, `published:`, `protocol:` (`tcp`|`udp`), `mode:` (`host`|`ingress`)
 `expose` ;;; Expose ports to linked services only (not to host)
 `volumes` ;;; Mount paths or named volumes; short form: `VOL:CONTAINER_PATH[:ro|rw]`; long form: `type:` (`bind` | `volume` | `tmpfs` | `cluster` | `npipe` | `image`) + `source:`, `target:`, `read_only:`, `bind.propagation:`
 `networks` ;;; Networks to join; references top-level `networks` key
 `depends_on` ;;; Startup ordering; condition values: `service_started` | `service_healthy` | `service_completed_successfully`
 `healthcheck` ;;; Health check config: `test:` (`["NONE"]` | `["CMD", ...]` | `["CMD-SHELL", "..."]`), `interval:`, `timeout:`, `retries:`, `start_period:`, `start_interval:`
 `restart` ;;; Restart policy: `no` | `always` | `on-failure` | `unless-stopped`
 `deploy` ;;; Swarm deployment config: `replicas`, `resources`, `restart_policy`, `update_config`, `placement`
 `profiles` ;;; Service only started when named profile is active
 `extends` ;;; Inherit config from another service; requires `service:`, optional `file:`
 `logging` ;;; Log driver config: `driver:` (`json-file` | `syslog` | `journald` | `gelf` | `fluentd` | `awslogs` | `splunk` | `none`) + `options:`
 `ulimits` ;;; Override container ulimits (e.g., `nproc`, `nofile`)
 `cap_add` ;;; Add Linux capabilities (e.g., `NET_ADMIN`, `SYS_ADMIN`)
 `cap_drop` ;;; Drop Linux capabilities
 `devices` ;;; Host device mappings: `source:` + `target:` + `permissions:`
 `init` ;;; Run an init process that forwards signals and reaps zombie processes
 `privileged` ;;; Gives all capabilities to the container, and lifts limitations enforced by the device cgroup controller. The container can now do almost everything the host can do.
 `read_only` ;;; Mount container filesystem as read-only
 `user` ;;; Username or UID to run process as
 `working_dir` ;;; Working directory for `entrypoint`/`command`
 `stop_signal` ;;; Signal used to stop container (default: `SIGTERM`)
 `sysctls` ;;; Kernel params to set in container
 `tmpfs` ;;; Mount a tmpfs into container
 `extra_hosts` ;;; Add `/etc/hosts` hostname mappings
 `dns` ;;; Custom DNS servers for container
 `hostname` ;;; Custom hostname for container
 `ipc` ;;; IPC namespace: `host` | `service:[name]` | `shareable`
 `labels` ;;; Docker labels as map or `KEY=VAL` list
 `secrets` ;;; Grant service access to top-level secrets
 `configs` ;;; Grant service access to top-level configs
 `network_mode` ;;; Override network stack: `bridge` | `host` | `none` | `service:[name]` | `container:[name]`
 `scale` ;;; Number of container replicas for this service

### Network fields

 `driver` ;;; Network driver: `bridge` (default, single-host) | `host` (share host stack) | `overlay` (multi-host Swarm) | `none` (disable) | `macvlan` (assign MAC) | `ipvlan`
 `driver_opts` ;;; Driver-specific options as key/value pairs
 `ipam` ;;; Custom IP Address Management; `driver:` (`default`|`host`), `config:` list with `subnet:`, `gateway:`, `ip_range:`
 `external` ;;; Network exists outside Compose — not created/destroyed by it
 `internal` ;;; Isolate network from external connectivity
 `attachable` ;;; Allow standalone containers to attach to this network
 `enable_ipv4` ;;; Enable IPv4 on this network
 `enable_ipv6` ;;; Enable IPv6 on this network
 `labels` ;;; Metadata labels for the network
 `name` ;;; Custom name for the network (overrides generated name)

### Volume fields

 `driver` ;;; Volume driver: `local` (default); third-party plugins (e.g., `nfs`, `s3fs`, `rexray`)
 `driver_opts` ;;; Driver-specific options; e.g., for `local` NFS: `type: nfs`, `o: addr=...,rw`, `device: :/path`
 `external` ;;; Volume exists outside Compose — not created/destroyed by it
 `labels` ;;; Metadata labels for the volume
 `name` ;;; Custom name for the volume (overrides generated name)

### Env var interpolation

 `${VAR}` ;;; Substitute env variable `VAR`
 `${VAR:-default}` ;;; Use `default` if `VAR` unset or empty
 `${VAR-default}` ;;; Use `default` only if `VAR` is unset (not if empty)
