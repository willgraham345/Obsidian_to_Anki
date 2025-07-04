---
date created: Wednesday, September 25th 2024, 11:56:19 am
date modified: Wednesday, September 25th 2024, 12:10:30 pm
---

```dataview 
LIST
FROM !"zz_Templates"
WHERE type
FLATTEN type
GROUP BY type
LIMIT 15
```