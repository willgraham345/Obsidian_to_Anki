---
type: note
---
# Background
Similar to a function in C or C++. Arguments can be passed in, and they become variables within the function. 

Standard variables like `ARGC`, `ARGV`, `ARGN`, `ARGV0`,  and `ARGV1` are supported

## Scope
Function calls have a dynamic scope. 
Within a function, you are in a new scope. All variables defined when the function was called remain defined, but changes to variables only exist within the function. 
# Usage