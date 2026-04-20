---
summary: Build automation tool that reads a Makefile to determine stale targets and runs the minimal set of recipes to rebuild them.
type: note/tool
headings:
  - "[[#Concepts of Note]]"
  - "[[#Examples]]"
  - "[[#Usage]]"
down:
concepts:
  - "[[GNU make rules]]"
  - "[[GNU make variables]]"
same:
  - "[[Cpp Ninja]]"
similar:
  - "[[CMake Workflow]]"
inspired:
  - "[[Cpp Ninja]]"
ai_generated: true
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Tuesday, April 7th 2026, 5:32:03 pm
item_of:
  - "[[GNU]]"
tags: [tools/make]
template:
template-version:
tool_of:
  - "[[Cpp.build.tools.overview]]"
---

# Summary
󰙎 GNU make ;;; Build automation tool: reads a Makefile, determines stale targets by comparing timestamps, runs the minimal set of recipes to rebuild.

# Additional Background

- Language-agnostic — applies to any source→target transformation expressible as shell commands
- Only rebuilds what changed; compares modification timestamps to detect staleness
- Resolves correct build order automatically from prerequisite chains

## Concepts of Note


### [[GNU make rules]]

A rule tells make how to build a **target** from **prerequisites** by executing a **recipe**.

```makefile
target … : prerequisites …
        recipe line 1
        recipe line 2
```

󰙎 target ;;; File to create, or a phony action name (e.g. `clean`, `install`)
󰙎 prerequisites ;;; Files that must exist and be up-to-date before the recipe runs
󰙎 recipe ;;; Shell commands make executes; **every line must begin with a tab character**

A rule with no recipe causes make to fall back to an implicit rule.

### Variables

Define a string once, substitute everywhere with `$(VAR)`. Prevents repetition and drift.

```makefile
objects = main.o kbd.o command.o display.o \
          insert.o search.o files.o utils.o
```

󰙎 `objects` / `OBJECTS` / `objs` ;;; Conventional variable name for the object file list
- Expand with `$(objects)` — in both the prerequisite list and the recipe

#### Implicit Rules

make has built-in knowledge of common build patterns; omit a recipe to let make infer it.

󰙎 implicit rule ;;; Built-in pattern, e.g. `foo.c` → `foo.o` via `$(CC) -c foo.c`
- Rule chains: `.y` → `.c` → `.o` can resolve in a single invocation
- Override by writing an explicit recipe for the same target

### .PHONY Targets

Targets that name **actions**, not files. Prevents a real file named `clean` from shadowing the rule.

```makefile
.PHONY : clean
clean :
        -rm edit $(objects)
```

󰙎 `.PHONY` ;;; Declares targets as actions; make always runs them regardless of filesystem state
- `-` prefix on a recipe line: make continues past errors instead of aborting
- Keep `.PHONY` away from the top of the file — the first target becomes the default goal

### Processing Order

1. Reads the makefile in the current directory
2. Takes the **first non-`.`-prefixed target** as the default goal
3. Recursively resolves prerequisites depth-first before running any recipe
4. Ignores rules unreachable from the goal

## Usage



 `make` ;;; Build the default (first) target
 `make <target>` ;;; Build a specific named target
 `make -f <file>` ;;; Use a specific makefile path instead of `./Makefile`
 `make clean` ;;; Remove build artifacts via the `clean` phony target
 `make install` ;;; Copy built binaries to install prefix (default `/usr/local/bin`)
 `make all` ;;; Build all top-level targets the makefile knows about

Tab-complete available targets: type `make` then double-tab.

## Examples


Compact style — variables, grouped prerequisites, and implicit rules eliminate boilerplate:

```makefile
objects = main.o kbd.o command.o display.o \
          insert.o search.o files.o utils.o

edit : $(objects)
        cc -o edit $(objects)

# No recipes — implicit C compilation rule fills them in
$(objects) : defs.h
kbd.o command.o files.o : command.h
display.o insert.o search.o files.o : buffer.h

.PHONY : clean
clean :
        -rm edit $(objects)
```

- `make` → compiles any changed sources, links `edit`
- `make clean` → removes `edit` and all `.o` files; `-rm` tolerates missing files
