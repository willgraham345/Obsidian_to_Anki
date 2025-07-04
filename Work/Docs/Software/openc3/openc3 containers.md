---
summary: Containers in the openc3 stack.
headings: ["[[#Media]]"]
type: 
components: ["[[openc3 cosmos-cmd-tlm-api-1]]", "[[openc3 cosmos-init-1]]", "[[openc3 cosmos-script-runner-api1]]", "[[openc3 minio-1]]", "[[openc3 operator-1]]", "[[openc3 redis-1]]", "[[openc3 redis-ephemeral-1]]", "[[openc3 traefik-1]]"]
date created: Tuesday, April 15th 2025, 12:12:59 pm
date modified: Tuesday, April 15th 2025, 12:16:24 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
|Name|Description|
|---|---|
|cosmos-openc3-cosmos-init-1|Copies files to Minio and configures COSMOS then exits|
|cosmos-openc3-operator-1|Main COSMOS container that runs the interfaces and target microservices|
|cosmos-openc3-cosmos-cmd-tlm-api-1|Rails server that provides all the COSMOS API endpoints|
|cosmos-openc3-cosmos-script-runner-api-1|Rails server that provides the Script API endpoints|
|cosmos-openc3-redis-1|Serves the static target configuration|
|cosmos-openc3-redis-ephemeral-1|Serves the [streams](https://redis.io/docs/data-types/streams) containing the raw and decomutated data|
|cosmos-openc3-minio-1|Provides a S3 like bucket storage interface and also serves as a static webserver for the tool files|
|cosmos-openc3-traefik-1|Provides a reverse proxy and load balancer with routes to the COSMOS endpoints|
### Backend
[[openc3 redis-ephemeral-1]] = Contains all real-time data pushed into Redis streams
[[openc3 redis-1]] = Contains COSMOS configuration meant to persist
[[openc3 minio-1]] = High performance S3 compatible object store
## Media
[OpenC3 Key Concepts](https://docs.openc3.com/docs/getting-started/key-concepts)