---
summary: Runtime (dynamic) allocation should be used when the object will have a lifetime that is determined by the program logic rather than lexical scope. The `new` and `delete` operators are designed to support managed lifetimes. Another reason an be that the size of the object is determined at runtime. For simple cases (arrays, etc.) there are standard classes in the [[Cpp std vector]] which will handle this for you. Otherwise, you will have to manage this yourself.
type: note/concept
concepts: ["[[Cpp Heap]]", "[[PT Stack vs Heap]]"]
components: ["[[Cpp std stack]]"]
functions: ["[[Cpp delete]]", "[[Cpp new]]"]
date created: Friday, January 3rd 2025, 9:55:03 am
date modified: Friday, January 3rd 2025, 10:05:55 am
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Use cases
- Configuration that needs to be changed during run-time, so you avoid restarting an already-running container.
- Time cost of recompiling is too high, and you need to continue development at a faster pace.
- The binary size for your function/program/executable is too high.