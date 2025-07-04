---
type: note/component
component_of:
  - "[[C stdio|Cpp stdio]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, November 26th 2024, 11:53:15 am
up:
  - "[[Docs/Programming_and_OS/C/Cpp stdio]]"
---
# Background
- Standard input stream, and the default source of data for most applications. In most systems, it is usually directed by default to the keyboard. 
- Can be used as an argument for any function that expects an input stream (`FILE*`) as one of its paramaters i.e. [[Cpp std stido fgets]], or [[Cpp.stdio.fscanf]]
- stdin can generally be redirected on most OS at the time of invoking the application

# Usage
## Redirect at invocation
```
myapplication < example.txt
```