---
type: note/component
concept_of: ["[[Networking]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Monday, December 2nd 2024, 11:37:08 am
---
# Background
- The IEEE standard for wireless LAN technology. Defines over-the-air communication without need for a physical cable. 
	- WLAN 802.11 standards also have security protocols . 
		- WEP = Wired Equivalent Privacy
			- Encrypts data sent over radio waves from end point to end point. 
		- WPA = Wi-Fi Protected Access.
			- Developed as an upgrade to WEP.
				- TKIP = Improved data encryption through temporary key integrity protocol. Scrambles the keys using a hashing algorithm. Has means for integrity-checking to ensure that keys have not been tampered with. 
			- EAP = Extensible authentication protocol. 

## WLAN Wireless Protocols

| **Specification**       | **Data Rate**                                                       | **Modulation Scheme**                                   | **Security** |
| ----------------------- | ------------------------------------------------------------------- | ------------------------------------------------------- | ------------ |
| 802.11                  | 1 or 2 Mbps in the 2.4 GHz band                                     | FHSS, DSSS                                              | WEP and WPA  |
| 802.11a                 | 54 Mbps in the 5 GHz band                                           | OFDM                                                    | WEP and WPA  |
| 802.11b/High Rate/Wi-Fi | 11 Mbps (with a fallback to 5.5, 2, and 1 Mbps) in the 2.4 GHz band | DSSS with CCK                                           | WEP and WPA  |
| 802.11g/Wi-Fi           | 54 Mbps in the 2.4 GHz band                                         | OFDM when above 20Mbps, DSSS with CCK when below 20Mbps | WEP and WPA  |

# Usage