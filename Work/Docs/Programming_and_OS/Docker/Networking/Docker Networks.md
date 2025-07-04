---
summary: How docker containers connect/communicate with each other, and other non-Docker workloads.
type: note
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, November 21st 2024, 3:04:26 pm
tags: [command/docker]
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`
In compose files:
- [Networks top-level element](https://github.com/compose-spec/compose-spec/blob/main/spec.md#image)

# Background
- Container networking is the ability for Docker containers to connect/communicate with each other and/or non-Docker workloads.
- Containers have networking enabled by default. They only see networking interface with IP address, a gateway, a routing table, DNS services and other details details. 
- For information on how Docker manipulates `iptables`, see [Packet filtering and firewalls](https://docs.docker.com/network/packet-filtering-firewalls/)
- Allows you to specify virtual Docker networks. 
	- Network traffic from and to containers is routed through a Docker proxy. 
	- Allows different setups for networking between individual containers

## Host port vs Container port
Each [[Docker Container]] will have its own definable ports that are separate from the host's ports
![[Docker.Networking.png|500]]

# Usage
- [p] `docker network connect` = Connect a container to a network = #command/docker 
<!--ID: 1751434091135-->

- [p] `docker network create` = Create a network = #command/docker 
<!--ID: 1751434091139-->

- [p] `docker network disconnect` = Disconnect a container from a network = #command/docker 
<!--ID: 1751434091143-->

- [p] `docker network inspect` = Display detailed information on one or more networks= #command/docker 
- [p] `docker network ls` = List networks = #command/docker 
<!--ID: 1751434091147-->

- [p] `docker network prune` = Remove all unused networks= #command/docker 
- [p] `docker network rm` = Remove one or more networks = #command/docker = `$(docker network ls -q)` Stops/removes all unused networks.
<!--ID: 1751434091151-->
