---
summary: You can use the script runner to execute these scripts.
headings: ["[[#Concepts of Note]]", "[[#Media]]", "[[#Usage]]"]
type: note/library
concepts: ["[[openc3 script organization]]"]
component_of: ["[[openc3]]"]
date created: Wednesday, March 26th 2025, 9:41:38 am
date modified: Wednesday, April 16th 2025, 3:46:20 pm
library_used_in: ["[[openc3 configuration]]"]
tags: [code/openc3/packets]
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
- [p] `id = subscribe_packets(packets)` = Listen to one or more telem packets to arrive (unique ide returned used to retrieve data) = #code/openc3/packets
<!--ID: 1751434089699-->

- [p] `id = get_packets(id, block=nil, count=100)` = Streams packet data from a previous subscription = #code/openc3/packets
<!--ID: 1751434382581-->


## Media
[OpenC3 Script Runner Tool](https://docs.openc3.com/docs/tools/script-runner)
[Scripting API Guide | OpenC3 Docs](https://docs.openc3.com/docs/guides/scripting-api)