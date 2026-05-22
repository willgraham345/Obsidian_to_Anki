---
summary:
type:
headings:
date created: Wednesday, September 25th 2024, 11:56:19 am
date modified: Thursday, January 8th 2026, 5:26:21 pm
template:
template-version:
---

```dataview 
LIST
FROM !"zz_Templates"
WHERE type
FLATTEN type
GROUP BY type
```