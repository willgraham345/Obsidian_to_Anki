---
type: note
---
# Backgrounbd
When makefiles are only created by implicit rules, an alternative style is possible with entries grouped by prerequisites instead of by their targets.
- This style is much more compact.

For example
```
objects = main.o kbd.o command.o display.o \
          insert.o search.o files.o utils.o

edit : $(objects)
        cc -o edit $(objects)

$(objects) : defs.h
kbd.o command.o files.o : command.h
display.o insert.o search.o files.o : buffer.h
```

- `defs.h` is given as a prerequisite of all the object files
- `command.h` and `buffer.h` are prerequisites of the specific object files listed for them. 