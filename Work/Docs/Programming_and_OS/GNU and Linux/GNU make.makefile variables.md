---
type: note
---
# Background
Duplication is error-prone. Variables allow a text string to be defined once and substituted in multiple places later.


# Usage
Standard practice for every makefile to have a variable named `objects` (can also be `OBJECTS, objs, OBJS, obj`).
## Example
```
objects = main.o kbd.o command.o display.o \
          insert.o search.o files.o utils.o
```