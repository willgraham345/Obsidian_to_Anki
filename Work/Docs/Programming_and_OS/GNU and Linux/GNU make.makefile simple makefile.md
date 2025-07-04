---
type: note
---
# Example
- All of the C filels include `defs.h`, but only those defining editing commands include `command.h`, and only low level files that change the editor buffer include `buffer.h`

```makefile
edit : main.o kbd.o command.o display.o \
       insert.o search.o files.o utils.o
        cc -o edit main.o kbd.o command.o display.o \
                   insert.o search.o files.o utils.o

main.o : main.c defs.h
        cc -c main.c
kbd.o : kbd.c defs.h command.h
        cc -c kbd.c
command.o : command.c defs.h command.h
        cc -c command.c
display.o : display.c defs.h buffer.h
        cc -c display.c
insert.o : insert.c defs.h buffer.h
        cc -c insert.c
search.o : search.c defs.h buffer.h
        cc -c search.c
files.o : files.c defs.h buffer.h command.h
        cc -c files.c
utils.o : utils.c defs.h
        cc -c utils.c
clean :
        rm edit main.o kbd.o command.o display.o \
           insert.o search.o files.o utils.o
```

## Example's Usage
To use this makefile to create the executable file called `edit` type:
```shell
make
```
To use this makefile to delete the executable file and all the object files from the directory, type:
```shell
make clean
```


## Things within the makefile
### Targets
`edit`
`main.o`
`kbd.o`
`clean`
- This isn't a file, but the name of an action. Since you normally do not want to carry out the actions in this rule, `clean` is not a prerequisite of any other rule. 
### Prerequisites
`main.c`
`defs.h`

### Recipes
`cc -c main.c`
`cc -c kbd.c`

Recipes say how to update the target file. A tab must come at the beginning of every line in the recipe to distinguish recipes from other lines in the makefile. 

