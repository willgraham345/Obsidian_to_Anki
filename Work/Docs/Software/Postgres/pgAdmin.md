---
summary: GUI tool that is useful for connecting to a live database.
type: note/system
associations: ["[[Postgres]]"]
date created: Wednesday, March 26th 2025, 3:39:02 pm
date modified: Thursday, July 3rd 2025, 1:51:23 pm
tags: []
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

Use 
 - [c] `docker inspect <database_name> -f "{{json .NetworkSettings.Networks }}"` = Finds docker networking ip for a PostgreSQL container (may work for other stuff too) = #command/docker/networking
 