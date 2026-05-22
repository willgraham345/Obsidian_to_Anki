---
summary: Makefile rules — explicit, pattern, static-pattern, and double-colon forms; order-only prerequisites.
type: note/concept
headings:
ai_generated: true
concept_of:
  - "[[GNU make]]"
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Tuesday, April 7th 2026, 5:32:57 pm
tags: [tools/make]
template:
template-version:
---

# Summary
󰙎 GNU make rules ;;; Define how make builds a target from prerequisites by executing a recipe; the fundamental unit of a Makefile.

# Additional Background
## Concepts of Note

### Explicit Rules

Direct mapping from target to prerequisites and recipe.

```makefile
target … : prerequisites …
        recipe
```

󰙎 target ;;; File to create, or a phony action name; first target in the file is the default goal
󰙎 prerequisites ;;; Files that must be up-to-date before the recipe runs; changes trigger a rebuild
󰙎 recipe ;;; Shell commands executed to build the target; **every line must begin with a tab**
- A rule with no recipe causes make to search for a matching implicit rule

### Pattern Rules

Apply one rule template to many targets by matching a stem with `%`.

```makefile
%.o : %.c
        $(CC) -c $(CFLAGS) $< -o $@
```

󰙎 `%` ;;; Wildcard stem that matches any non-empty string; same stem used in both target and prerequisite
󰙎 `$<` ;;; Automatic var — the first (matched) prerequisite
󰙎 `$@` ;;; Automatic var — the current target
- Pattern rules define implicit rules; make selects the best match when no explicit recipe exists

### Static Pattern Rules

Pattern rule applied to an **explicit, bounded list** of targets — safer than open-ended `%` patterns.

```makefile
$(objects) : %.o : %.c
        $(CC) -c $(CFLAGS) $< -o $@
```

- Syntax: `target-list : target-pattern : prerequisite-pattern`
- make raises an error if a target in the list doesn't match the pattern — catches typos early
- Prefer over a generic pattern rule when the target list is known

### Order-Only Prerequisites

Prerequisites that must be built first, but whose staleness does **not** trigger a rebuild of the target.

```makefile
output/%.o : %.c | output/
        $(CC) -c $< -o $@

output/ :
        mkdir -p output/
```

󰙎 `|` separator ;;; Prerequisites after `|` are order-only; never cause the target to be considered out-of-date
- Typical use: ensure a directory exists without rebuilding all targets when the directory timestamp changes

### Double-Colon Rules

Allow multiple independent rules for the same target; each runs if its own prerequisites are stale.

```makefile
important-target :: prereq-a
        recipe-a

important-target :: prereq-b
        recipe-b
```

󰙎 `::` ;;; Double-colon rule; runs independently per block, unlike single-colon which merges all prereqs
- Rare in practice; used when different actions suit different prerequisite sets
- Cannot mix `:` and `::` rules for the same target
