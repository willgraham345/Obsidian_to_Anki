---
type: note
---
# Background
Compiling a program is not the only thing you might want to write rules for. 

Makefiles commonly tell how to do a few other things besides compiling a program.
- i.e. how to delete all the object files so that the directory is `clean`

```
clean:
		rm edit $(objects)
```

# Usage

```
.PHONY : clean
clean :
        -rm edit $(objects)
```
- Prevents `make` from getting confused by an actual file called `clean` and causes it to continue in spite of errors from `rm`
- This should NOT be placed at the beginning of a makefile
- We want 