---
tags: note/ROS
type: note
---
How does ROS 2 discovery happen?
1. When a node is started, it advertises it presence to other nodes in the same network with the same ROS domain (`ROS_DOMAIN_ID` environment variable). Nodes respond to the advertisement with information about themselves so that the appropriate connections can be made and the nodes can communicate. 
2. Nodes periodically advertise their presence so connections can be made with new-found entities
3. Nodes advertise to other nodes when they go offline.

Nodes will only establish connections with other nodes if they have compatible quality of service settings. 
