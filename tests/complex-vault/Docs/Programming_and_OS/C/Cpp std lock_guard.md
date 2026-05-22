---
summary: Mutex wrapper that provides a RAII (Resource acquisition is initialization) mechanism for owning a mutex for the duration of a scoped block.<br><br>When a lock_guard is created, it attempts to take ownership of the mutex it is given. When control leaves the scope in which the lock_guard object was created, the lock_guard is destroyed and the mutex is released.
type: note/class
headings:
  - "[[#Concepts of Note]]"
  - "[[#Media]]"
associations:
  - "[[Cpp std mutex]]"
class_of:
  - "[[Cpp std mutex (library)]]"
date created: Friday, February 14th 2025, 3:51:36 pm
date modified: Friday, February 14th 2025, 3:56:33 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- You need to give the `lock_guard` a variable name. 
- Acquires ownership of the given mutex `m`

## Usage
```cpp
// assume the mutex you want is mutex m
lock_guard (mutex_type& m);
```

## Media
[std::lock\_guard - cppreference.com](https://en.cppreference.com/w/cpp/thread/lock_guard)
<iframe src="https://en.cppreference.com/w/cpp/thread/lock_guard" style="width: 100%; height: 600px;"></iframe>