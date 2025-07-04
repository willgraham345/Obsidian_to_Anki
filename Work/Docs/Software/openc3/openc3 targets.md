---
summary: Targets are the external pieces of hardware and/or software that COSMOS communicates with, described in `.txt` files. A target is anything that COSMOS can send commands to and receive telemetry from. target.txt defines the configuration file for individual targets.
type: note/concept
associations:
  - "[[openc3 command configuration]]"
  - "[[openc3 telemetry configuration]]"
concept_of:
  - "[[openc3 configuration]]"
date created: Thursday, October 24th 2024, 3:02:33 pm
date modified: Wednesday, March 26th 2025, 9:18:01 am
tags:
  - code/openc3/target_txt
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- Telemetry = Automatic transmission of data from a remote source to a central location. Often used to gather data from sensors to monitor/control a remote system.
- Commands = A one-time instruction that is sent to a computer or software to perform a specific task. 

## Media
[OpenC3 Target Keywords](https://docs.openc3.com/docs/configuration/target)


- [p] `TARGET` = Defines system target = #code/openc3/target_txt
<!--ID: 1751434089704-->

- [p] `LANGUAGE` = Specifies programming language = #code/openc3/target_txt
<!--ID: 1751434089708-->

- [p] `REQUIRE` = Lists dependencies = #code/openc3/target_txt
<!--ID: 1751434089712-->

- [p] `COMMAND` = Manage system commands = #code/openc3/target_txt
<!--ID: 1751434089716-->

- [p] `TELEMETRY` = Manage system telemetry = #code/openc3/target_txt
<!--ID: 1751434089720-->

- [p] `IGNORE_PARAMS` = Ignores specific parameters/files= #code/openc3/target_txt