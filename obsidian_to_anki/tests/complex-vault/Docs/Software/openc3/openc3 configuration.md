---
summary: Openc3 configuration is done through text files, which are then compiled into a gem for use in the cosmos containers. The gem file will contain all information regarding commands/telemetry in openc3
type: note/concept
headings:
  - "[[#Concepts of Note]]"
concepts:
  - "[[openc3 file format]]"
  - "[[openc3 plugins]]"
  - "[[openc3 protocols]]"
  - "[[openc3 router]]"
  - "[[openc3 tables]]"
  - "[[openc3 targets]]"
concept_of:
  - "[[openc3]]"
date created: Thursday, October 24th 2024, 2:50:07 pm
date modified: Friday, March 20th 2026, 9:44:06 am
items:
  - "[[openc3 command configuration]]"
  - "[[openc3 interfaces]]"
  - "[[openc3 plugins]]"
  - "[[openc3 telemetry configuration]]"
tags: [tools/openc3]
template:
template-version:
uses:
  - "[[openc3 python API]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[OpenC3 Docs](https://docs.openc3.com/docs/configuration)

## Concepts of Note
- plugin.txt config file required for any COSMOS plugin. Declares contents of the plugin and provides variable.
󰙎  Configuration files ;;; Plain `.txt` config files used to define the command/telemetry packets, and configuring the cosmos apps.
