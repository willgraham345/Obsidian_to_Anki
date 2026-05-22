---
summary: OpenC3 COSMOS is a suite of apps that can be used to control a set of embedded systems. Can be anything from test equipment, development boards, to satellites. Lets you interact with a system (send commands, pull out data, view status) from the comfort of a web browser.
type: note/system
headings:
  - "[[#Breadcrumbs]]"
  - "[[#Concepts of Note]]"
  - "[[#Diagrams]]"
concepts:
  - "[[openc3 bridges]]"
  - "[[openc3 configuration]]"
  - "[[openc3 microservices]]"
date created: Tuesday, October 22nd 2024, 1:02:37 pm
date modified: Thursday, April 9th 2026, 4:49:56 pm
items:
  - "[[openc3 code generators]]"
  - "[[openc3 containers]]"
libraries:
  - "[[openc3 python API]]"
processes:
  - "[[openc3 guides]]"
tags: [tools/openc3, tools/openc3/plugin]
template:
template-version:
tools:
  - "[[openc3 Command Sender]]"
  - "[[openc3 Script Runner]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note
[OpenC3 Docs](https://docs.openc3.com/docs)

[OpenC3 Docs: Logging](https://docs.openc3.com/docs/guides/logging)
󰙎  Accessors ;;; Low level code which know how to read/write data into a buffer. The buffer data is then written out on an interface using protocols. Accessors handle serializations such as binary (CCSDS), JSON, CBOR, XML, HTML, Protocol Buffers, etc

󰙎  Message Log Files ;;; `.txt` files containing messages.

󰙎  Plugin ;;; What you write to extend COSMOS. Requires defining targets, interfaces, routers, tools, and microservices. ^c26f08
󰙎  Tool ;;; COSMOS application 

## Diagrams %% fold %% 
![[openc3.png | 800]]
