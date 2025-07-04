---
summary: Init system (the first daemon to start during booting and the last daemon to terminate during shutdown on Ubuntu) adopted by a variety of Linux distros. The root of the user space's process tree. Suite of basic building blocks for Linux, with a TON of components. Systemd's manages "units" which have a variety of types and capabilities. The type of each unit can be inferred by the suffix of the file (i.e. *.service).
headings: ["[[#Breadcrumbs]]", "[[#Concepts of Note]]", "[[#Diagrams]]"]
type: note/system
concepts: ["[[Linux systemd dropin configuration]]", "[[Linux systemd units]]"]
functions:
  [
    "[[Linux journalctl]]",
    "[[Linux systemctl]]",
    "[[Linux systemd-cgls]]",
    "[[Linux systemd-cgtop]]",
  ]
component_of: ["[[Linux]]"]
date created: Friday, September 13th 2024, 2:47:05 pm
date modified: Tuesday, June 10th 2025, 9:33:19 am
---

# Summary

`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

[Systemd Docs](https://systemd.io/)

## Concepts of Note

- Systemd is your first process
- When systemd dies, Linux dies?
- Your user0 process

## History and Alternatives

- Apparently [this](https://blog.darknedgy.net/technology/2020/05/02/0/) is a really good history of it, but I can't seem to access it on my work computer.
  ![[Linux systemd units#Types of Units/Best Practice]]

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
