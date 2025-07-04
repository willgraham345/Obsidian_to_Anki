---
summary: List of arguments within docker that specify the way you'd like your containers to be run.
type: note/component
component_of: ["[[Docker Compose]]"]
date created: Wednesday, February 5th 2025, 1:33:23 pm
date modified: Monday, March 24th 2025, 6:10:47 pm
tags: [code/dockercompose]
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
- [p] `services` = List of all containers that should be started and run. Typically the first thing entered. = #code/dockercompose
<!--ID: 1751434091314-->

- [p] `extends` = Lets you share common config with different compose files. Define set of service options in one place, refer to it anywhere. Similar to `include` = #code/dockercompose = `file:` where you define the common configuration file
<!--ID: 1751434091319-->

- [p] `include` = Incorporate an entire other compose.yml file in your compose.yml file.  = #code/dockercompose = `path:` Where other config is
<!--ID: 1751434091323-->

      `depends_on:` Argument for a service defined in the new compose.yml. Give it the servcie defined in the old config.yml.