---
summary: Build system generator specialized for speed. Has a bunch of tools, could be useful.
type: note/tool
headings:
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
same:
  - "[[CMake Workflow 2 Generation]]"
  - "[[GNU make]]"
inspiration:
  - "[[GNU make]]"
aliases: []
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, April 7th 2026, 5:27:58 pm
id: Cpp Ninja
items:
  - "[[Cpp Ninja Tools]]"
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
tool_of:
  - "[[CMake Workflow 2 Generation]]"
  - "[[CMake]]"
  - "[[Cpp]]"
uses:
  - "[[Clang]]"
---

# Summary
󰙎 Cpp Ninja ;;; Build system generator specialized for speed. A more modern alternative to [[GNU make]] when generating Cpp build files. Commonly paired with CMake.

# AdditionalBackground
## Concepts of Note
󰙎 Phony target ;;; A label that never corresponds to an actual file; always treated as out‑of‑date, useful for grouping commands (e.g., `clean`).
󰙎 Build graph ;;; directed acyclic graph of dependencies.
󰙎 Target ;;; output file produced by a rule.
󰙎 Rule ;;; command template that builds a target.
󰙎 Dependencies ;;; files or other targets that a rule requires.
- Parallel execution: Ninja schedules independent targets concurrently.
- Minimal syntax: simple, whitespace‑sensitive build file.
󰠗 Why does Ninja treat phony targets as always out‑of‑date? ;; Because they represent actions rather than files, ensuring the command runs whenever requested.
󰠗 When should you use a phony target? ;; For actions that don't produce a file, such as cleaning, testing, or code generation.

## Usage

 `ninja -t targets` ;;; Individual build outputs referenced by rules; can be files or phony.
 `ninja -t commands` ;; list all built‑in ninja commands.
 `ninja -t graph` ;; output the build dependency graph in DOT format.
 `ninja -t compdb` ;; emit a JSON compilation database for clang‑tools, useful for IDE tooling.

󰠗 How can Ninja’s `-t compdb` help CMake debugging? ;; It shows exact compile commands Ninja will run, letting you verify CMake‑generated flags.

[Tools manual](https://ninja-build.org/manual.html#_extra_tools)
