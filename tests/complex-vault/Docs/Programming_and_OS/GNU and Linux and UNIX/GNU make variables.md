---
summary: Makefile variables — assignment forms, substitution syntax, automatic variables, and command-line overrides.
type: note/item
ai_generated: true
concept_of:
  - "[[GNU make]]"
tags:
  - tools/make
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Tuesday, April 7th 2026, 5:00:56 pm
---

# Summary
󰙎 GNU make variables ;;; Named text substitutions in Makefiles; define once, expand with `$(VAR)` everywhere.

# Concepts of Note

## Assignment Forms

- [I] `VAR = value` ;;; Recursive (lazy) — expanded each time `$(VAR)` is used; can reference variables not yet defined
- [I] `VAR := value` ;;; Simple (immediate) — expanded once at assignment time; safer for performance and predictability
- [I] `VAR ?= value` ;;; Conditional — sets `VAR` only if it is not already defined
- [I] `VAR += value` ;;; Append — adds to the existing value with a space separator

Prefer `:=` unless you need forward-reference behavior.

## Expansion

- [p] `$(VAR)` ;;; Standard expansion — works for single-character and multi-character names
- [p] `${VAR}` ;;; Alternative brace syntax — identical behavior to `$(VAR)`
- [p] `$(VAR:.old=.new)` ;;; Substitution reference — replaces `.old` suffix with `.new` in every word

## Automatic Variables

Set by make inside a recipe; refer to parts of the current rule. Read-only.

- [I] `$@` ;;; The target file name of the current rule
- [I] `$<` ;;; The first prerequisite
- [I] `$^` ;;; All prerequisites, space-separated, duplicates removed
- [I] `$*` ;;; The stem matched by a pattern rule (the `%` portion)
- [I] `$(@D)` / `$(@F)` ;;; Directory / file part of `$@`; same `D`/`F` modifier applies to other automatic vars

Example using automatic variables in a pattern rule:

```makefile
%.o : %.c
        $(CC) -c $(CFLAGS) $< -o $@
```

## Command-Line Override

Variables set on the command line take precedence over Makefile assignments.

- [p] `make CC=clang` ;;; Override `CC` for this invocation
- [p] `make CFLAGS="-O2 -Wall"` ;;; Pass flags without editing the Makefile
- Use `override VAR = value` in the Makefile to block command-line overrides for a specific variable

## Conventions

```makefile
objects = main.o kbd.o command.o display.o \
          insert.o search.o files.o utils.o
```

- [I] `objects` / `OBJECTS` / `objs` ;;; Conventional name for the object file list; reference as `$(objects)` in targets and recipes
- `CC`, `CXX`, `CFLAGS`, `CXXFLAGS`, `LDFLAGS` — standard implicit-rule variables; override these instead of editing recipes
