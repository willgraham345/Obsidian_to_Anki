---
type: note
---
# Background
`.so` = Shared objects. At link time, the object is verified against its API via the corresponding header file. The library isn't actually used until runtime, where it is needed.

- Dynamic libraries means that the `.so` can be replaced without requiring the base application to be recompiled. 
# Usage