---
summary: Waits for a value to be set asynchronously. Provides a mechanism to access the result of asynchronous operations to the creator. When asynchronous operation is ready to send a result to the creator by modifying shared state.
headings: ["[[#Syntax]]"]
type: note/class
associations: ["[[Cpp std promise]]"]
class_of: ["[[Cpp std future (library)]]"]
date created: Thursday, January 16th 2025, 12:51:24 pm
date modified: Tuesday, April 8th 2025, 12:17:17 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Syntax
```cpp
//from a promise
std::promise<int> p;
std::future<int> f = p.get_future();
```