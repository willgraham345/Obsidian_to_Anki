---
type: person
company: University of Utah
title: 
location: 
email: 
aliases: 
date_last_spoken: 
follow_up:
---
# Social
Groups
Family
Friends
# Other
Meetings
```dataview
TABLE file.name as "Name", type as "Type"
	From [[]]
	SORT file.name DESC
	WHERE type = "meeting"
```
Updates
```dataview
TABLE file.name as "Name", type as "Type"
	From [[]]
	SORT file.name DESC
	WHERE type = "update_log"
```
Projects
```dataview
TABLE file.name as "Name", type as "Type"
	From [[]]
	SORT file.name DESC
	WHERE type = "project"
```

