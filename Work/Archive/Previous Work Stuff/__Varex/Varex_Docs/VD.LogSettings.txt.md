---
company: Varex
tags: archive_deprecated/Varex
---
# Background
Library provides a `VlogSettingsFile` derived from `VlogSettingsInterface` that uses a file for logging settings. 

File is in JSON format, *however*, lines whose first non-whitespace character is `#` are treated as comments. 
- This file is re-read periodically so settings can be modified without restarting the software. 
	- Rereading may be slow if it's a large or complex file
### Parsing JSON
[3rdParty](https://github.com/nlohmann/json) is used to parse the JSON


# Usage