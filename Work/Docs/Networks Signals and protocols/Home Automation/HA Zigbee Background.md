---
type: note
---
# Background
Protocol designed for low power, wireless equipment. 
- Operates in 2.4 GHz radio range
- Zigbee lets devices turn their radio off while not transmitting
- Open standard

Has two devices:
- Zigbee coordinator (hub)
	- Responsible for initially starting the network and maintaining connection
	- Only one per network
	- Mains power
	- Really big point of failure. 
- Zigbee end device
- Zigbee router
	- Helps with mesh capability
	- Similar to a smart socket or smart switch. Can also send info to the coordinator, but can also route stuff to the coordinator as well. 
	- Mains power

Zigbee implements 128-bit end to end encryption
# Usage