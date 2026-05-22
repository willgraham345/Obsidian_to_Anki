---
summary: You can use the script runner to execute these scripts.
headings: ["[[#Concepts of Note]]", "[[#Media]]", "[[#Properties]]", "[[#Usage]]"]
type: note/library
functions: ["[[openc3 python API#load_utility]]"]
classes: ["[[openc3 Group]]", "[[openc3 Suite]]"]
concepts: ["[[openc3 script organization]]"]
date created: Wednesday, March 26th 2025, 9:41:38 am
date modified: Monday, December 8th 2025, 1:39:38 pm
library_of: ["[[openc3]]"]
tags: [tools/openc3/packets, tools/openc3/test]
template:
template-version:
used_by: ["[[openc3 configuration]]", "[[openc3 Script Runner]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- Components within this API
	- Retrieving user input
	- Providing info to user
	- Command interaction
	- Handling Telemetry
	- Packet data subscriptions
	- Delays
	- Limits
	- Plugins/packages
	- Targets
	- Interfaces
	- Routers
	- Script Runner Suites
	- Timelines
	- Metadata
	- Settings
	- Configuration

## Usage
  `id = subscribe_packets(packets)` ;;; Listen to one or more telem packets to arrive (unique ide returned used to retrieve data), and store it in variable `id`.
ID: 1751997630055


  `id = get_packets(id, block=nil, count=100)` ;;; Streams packet data from a previous subscription, stored in `id`.

### Checking
```python
# Note that for Python we need to pass globals() to be able to use COSMOS API methods like tlm()
elapsed = wait_check_expression("tlm('INST HEALTH_STATUS COLLECTS') > 5 and tlm('INST HEALTH_STATUS TEMP1') > 25.0", 10, 0.25, globals())
```

## Properties

### Functions
#### load_utility
- Goes through a weird process to perform imports within openc3 API.
- `traefik`->`script runner` ->`exec`->`stdout`
	- That then kicks back to `traefik`, which prints it to `stdout`

## Media
[OpenC3 Script Runner Tool](https://docs.openc3.com/docs/tools/script-runner)
[Scripting API Guide | OpenC3 Docs](https://docs.openc3.com/docs/guides/scripting-api)
