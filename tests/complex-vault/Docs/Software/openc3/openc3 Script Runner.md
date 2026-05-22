---
summary: Script execution environment and script editor, letting you run Python/Ruby scripts to send commands and check telemetry from the COSMOS gui
type: note/tool
headings: ["[[#Workflows]]"]
concepts: ["[[openc3 script organization]]"]
date created: Tuesday, October 22nd 2024, 1:27:32 pm
date modified: Friday, December 12th 2025, 11:41:54 am
template:
template-version:
tool_of: ["[[openc3]]"]
uses: ["[[openc3 python API]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
### Processes
##### Running a script in script runner
 process_start:
1. `run_script.py` calls `RunningScript` class
2. `RunningScript` init process
3. Running script runs `exec()` on each line
 process_end:

