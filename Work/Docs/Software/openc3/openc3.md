---
summary: OpenC3 COSMOS is a suite of apps that can be used to control a set of embedded systems. Can be anything from test equipment, development boards, to satellites. Lets you interact with a system (send commands, pull out data, view status) from the comfort of a web browser.
headings: ["[[#Breadcrumbs]]", "[[#Concepts of Note]]"]
type: note/system
concepts: ["[[openc3 bridges]]", "[[openc3 configuration]]", "[[openc3 microservices]]", "[[openc3 terminology]]"]
components: ["[[openc3 code generators]]", "[[openc3 containers]]", "[[openc3 scripting API]]", "[[openc3 tools]]"]
workflows: ["[[openc3 script writing]]"]
date created: Tuesday, October 22nd 2024, 1:02:37 pm
date modified: Tuesday, June 3rd 2025, 4:47:54 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Breadcrumbs
```breadcrumbs
mermaid
field-groups: [downs]
merge-fields: true
sort: field asc
show-attributes: [field]
```

## Concepts of Note
[OpenC3 Docs](https://docs.openc3.com/docs)

[OpenC3 Docs: Logging](https://docs.openc3.com/docs/guides/logging)
![[openc3.png | 600]]
- [I] Target = An embedded system that the COSMOS commmand and telemetry server connects to using an interface. Basically, the thing you actually want to connect to = #term/openc3
- [I] Command = Packet of information telling a target to perform an action of some sort = #term/openc3
- [I] Telemetry packet = Packet of information providing status from a target = #term/openc3
- [I] Configuration files = Plain text config files used to define the command/telemetry packets, and configuring the cosmos apps. = #term/openc3
- [I] Interface = Defines the connection to a physical target. Typically ethernet connections using TCP/UDP but can also be serial. = #term/openc3
- [I] Accessors = Low level code which know how to read/write data into a buffer. The buffer data is then written out on an interface using protocols. Accessors handle serializations such as binary (CCSDS), JSON, CBOR, XML, HTML, Protocol Buffers, etc = #term/openc3

### Containerization
- Images (same as [[Docker Image]])
- Containers (same as [[Docker Container]])
- Environment file
	- Used along with docker compose to pass variables into runtime. `.env` file has key/value pairs that contain the version of COSMOS deployed, with usernames/passwords.
- Kubernetes
	- Manages containerized applications for easy management/discovery.
	- Helm charts

#### Front end
- Works on Vue.js,
- Single-spa
	- micro frontend framework acts as a top level router to render application requested.
- Astro UX

#### Back end
- Redis
	- Data store
- MinIO
	- High performance S3 compatible object store.
	- Hosts the COMSOS tool themselves and the log term files.
- Ruby on Rails
	- COSMOS API and Script runner are powered by this
	- Web application development framework written in Ruby.
