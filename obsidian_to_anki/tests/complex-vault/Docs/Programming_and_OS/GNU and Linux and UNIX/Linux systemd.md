---
summary:
type: note/system
headings:
  - "[[#Breadcrumbs]]"
  - "[[#Concepts of Note]]"
  - "[[#Diagrams]]"
concepts:
  - "[[Linux systemd unit]]"
date created: Friday, September 13th 2024, 2:47:05 pm
date modified: Wednesday, April 8th 2026, 12:53:57 pm
images: "[[Linux systemd.png]]"
item_of:
  - "[[Linux]]"
items:
  - "[[Linux systemd unit]]"
  - "[[Linux systemd system conf]]"
libraries:
  - "[[C systemd sd-bus]]"
tags: []
template:
template-version:
tools:
  - "[[Linux journalctl]]"
  - "[[Linux systemctl]]"
  - "[[Linux systemd-analyze]]"
  - "[[Linux systemd-cgls]]"
  - "[[Linux systemd-cgtop]]"
used_by:
  - "[[CMake build tool]]"
  - "[[Linux boot]]"
uses:
  - "[[Linux fstab]]"
  - "[[Linux process error codes]]"
  - "[[UNIX XDG Base Directory]]"
---

# Summary

󰙎 systemd ;;; Init system (the first daemon to start during booting and the last daemon to terminate during shutdown on Ubuntu) adopted by a variety of Linux distros. The root of the user space's process tree. Suite of basic building blocks for Linux, with a TON of components. Systemd's manages "units" which have a variety of types and capabilities. The type of each unit can be inferred by the suffix of the file (i.e. service). This also provides a unified logging system that captures messages from the kernel, services, and user applications in one centralized, indexed log.

# Additional Background

[Systemd Docs](https://systemd.io/)

## Concepts of Note
[systemd - The Good Parts - YouTube](https://www.youtube.com/watch?v=r_haLf5mWhE&t=871s) 

- Systemd is your first process
- When systemd dies, Linux dies?
- Your user0 process

### History and Alternatives

- Apparently [this](https://blog.darknedgy.net/technology/2020/05/02/0/) is a really good history of it, but I can't seem to access it on my work computer.
- See [[Linux systemd unit#Types of Units/Best Practice]]

## Breadcrumbs

```breadcrumbs
type: mermaid
field-groups: [downs]
merge-fields: true
sort: field asc
show-attributes: [field]
```

## Diagrams

![[Linux systemd.png | 600]]
