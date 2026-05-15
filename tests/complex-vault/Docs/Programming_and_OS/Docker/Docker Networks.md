---
summary: How docker containers connect/communicate with each other, and other non-Docker workloads.
type: note/item
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, November 21st 2024, 3:04:26 pm
tags:
  - tools/docker
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
  `docker network connect` ;;; Connect a container to a network = #tools/docker  
ID: 1751997629095



  `docker network create` ;;; Create a network = #tools/docker  
ID: 1751997629099



  `docker network disconnect` ;;; Disconnect a container from a network = #tools/docker  
ID: 1751997629104



  `docker network inspect` ;;; Display detailed information on one or more networks= #tools/docker 
  `docker network ls` ;;; List networks = #tools/docker  
ID: 1751997629109



  `docker network prune` ;;; Remove all unused networks= #tools/docker 
  `docker network rm` ;;; Remove one or more networks = #tools/docker = `$(docker network ls -q)` Stops/removes all unused networks. 
ID: 1751997629114


