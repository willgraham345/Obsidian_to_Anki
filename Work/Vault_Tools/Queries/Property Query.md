---
type: vault_tool
---

Example,
- unique values of `type`
```
LIST
WHERE type
FLATTEN type
GROUP BY type
LIMIT 15
```

Editor
```dataview 
LIST
WHERE type
FLATTEN type
GROUP BY type
LIMIT 15
```