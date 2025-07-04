---
tags: note/ROS
type: note
---
# Background
## What is the `ROS_DOMAIN_ID`?
- The default middleware that ROS2 uses for communication is DDS.
	- The primary mechanism for having different logical networks share a physical network is known as the Domain ID. 
- ROS 2 nodes on the same domain can freely discover and send messages to each other, while ROS 2 nodes on different domains cannot.
- To avoid interference between different groups of computers running ROS 2 on the same network, a different ID should be set for each group
## Default Value
- Default `ROS_DOMAIN_ID=0`

## Choosing a domain ID
The domain ID is used by DDS to compute the UDP ports that will be used for discovery and communication
- [How the ports are computed](https://community.rti.com/content/forum-topic/statically-configure-firewall-let-omg-dds-traffic-through)
- UDP is an unsigned 16-bit integer
	- Highest val is 65535

### Platform-specific constraints
- [See here](https://docs.ros.org/en/foxy/Concepts/About-Domain-ID.html#platform-specific-constraints)
### Participant Constraints