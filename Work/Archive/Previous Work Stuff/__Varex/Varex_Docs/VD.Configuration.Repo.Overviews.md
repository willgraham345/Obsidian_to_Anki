---
company: Varex
tags:
  - archive_deprecated/Varex
  - archive_deprecated/Varex/config
---
# Background
Configuration for receptors is usually done through a binary file. The `config` repo is how we modify these files. Example configurations are found in the `configuration` reop
- Exceptions are: `.ini` and  `mod-info.ini` files which supplement some software settings that are not included in the configuration file. 

## History of the repos
In the past, the Configure application was able to add a new mode with pre-defined registers and dacs and other token-value paris. 
- Application had to be updated and distributed consistently for a particular receptor. 
- If you use the wrong version it could severely mis-configure the file and cause crashes. 
XConfigure
- Replaced all the Configure applications
[[VD.config.Module]]
[[VD.configuration]]

# Usage