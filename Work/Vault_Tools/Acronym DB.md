---
type: vault_tool
date created: Tuesday, August 20th 2024, 4:30:06 pm
date modified: Thursday, October 3rd 2024, 11:52:10 am
---


```dataview
TABLE 
	WITHOUT ID 
	ack as "Acronym",
	meaning as "Meaning",
	[T.link, tags] as "Link/Tags" 
FROM ""
flatten file.tasks as T
flatten string(T.text) as txt
where T.status = "I"
flatten split(string(txt), "=")[0] as ack 
flatten split(string(txt), "=")[1] as meaning
where file.link != [[Checkboxes]] 
sort ack ASC

```

# Database
- [I] CCSDS = Acronym that says a global group of suggestions for something. 
- [I] CUI = [[Classifications.CUI]]
- [I] Spa = Space plugin-play architecture, built by the Air Force, we think we're the ones that have used it. 
- [I] LEO = Low earth orbit
- [I] RSO = Resident space object. 
- [I] NIR = Narrow IR
- [I] GPS = Global Positioning System
- [I] RPO = Rendezvous and proximity operations
- [I] EPS = Electrical power system, (can also be known as a PMU (power management unit))
- [I] GFE = Government furnished equipment.  
- [I] MDP = Mission data processor
- [I] CRTP = Curiously Recurring Template Pattern
- [I] SIL = Software in the loop
- [I] HIL = Hardware in the loop
- [I] PSIL = Payload Software in the loop
- [I] PSIL = Payload Software in the loop
- [I] C&T = Command and Telemetry Interface
- [I] OAP = Orbital Average Power
- [I] OBCS = On-board Computer System


- [I] AOS = Advanced Orbiting Systems
- [I] CAS = Central Address Service
- [I] CCSDS = Consultative Committee for Space Data Systems
- [I] FARM = Frame Acceptance and Reporting Mechanism
- [I] EPS = Electrical Power System
- [I] FSW = Flight Software
- [I] GPS = Global Positioning System
- [I] kbps = kilobits (103 bits) per second
- [I] LS = Lookup Service
- [I] Mbps = Megabits (106 bits) per second
- [I] SDL = Space Dynamics Laboratory
- [I] SOH = State of Health
- [I] SM-E = Ethernet Manager
- [I] SM-L = Local Manager
- [I] SPA = Space Plug-and Play Architecture
- [I] SSM = SPA Services Manager
- [I] TBD = To Be Determined
- [I] TC = Telecommand
- [I] UUID = Universally Unique Identifier
- [I] WBS = Work breakdown structure
- [I] HIP = Host interface power