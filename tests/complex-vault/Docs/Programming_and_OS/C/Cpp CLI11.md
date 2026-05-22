---
summary: Header-only C++11 command-line parsing library. Drop in `CLI11.hpp`, create a `CLI::App`, attach options/flags/subcommands, call `CLI11_PARSE`.
type: note/library
headings:
  - "[[#Breadcrumbs]]"
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
classes:
  - "[[Cpp CLI App]]"
ai_generated: true
date created: Tuesday, June 24th 2025, 2:26:42 pm
date modified: Tuesday, April 14th 2026, 2:21:55 pm
tags: []
template:
template-version:
---

# Summary

`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

[Introduction · CLI11 Tutorial](https://cliutils.github.io/CLI11/book/)

## Concepts of Note

- 󰙎 Option ;;; Named arg with a value (`-f val` / `--file val`); bound to a C++ variable
- 󰙎 Flag ;;; Named arg with no value; sets a bool or increments an int counter
- 󰙎 Positional ;;; Unnamed arg matched by position; `add_option` name has no `-` prefix
- 󰙎 Subcommand ;;; Nested `CLI::App` enabling verb-style CLI (e.g. `git commit`)
- 󰙎 Validator ;;; Callable that checks or transforms a parsed value; chained via `->check()`

## Usage

### Setup

```cpp
#include "CLI/CLI.hpp"

int main(int argc, char** argv) {
    CLI::App app{"App description"};
    // attach options here
    CLI11_PARSE(app, argc, argv);  // handles --help, errors, and exit
}
```

 `CLI::App app{"desc"}` ;;; Root object; owns all options, flags, subcommands, and parse state
 `CLI11_PARSE(app, argc, argv)` ;;; Macro wrapping `app.parse()`; catches `ParseError` and exits cleanly

### Options

```cpp
std::string file;
int count = 0;

app.add_option("-f,--file", file, "Input file")->required()->check(CLI::ExistingFile);
app.add_option("-n,--count", count, "Repeat count")->default_val(1);
```

 `add_option(names, var, desc)` ;;; Bind named option to variable; type inferred from `var`; comma-separate short/long names
 `->required()` ;;; Abort with error if option absent
 `->default_val(v)` ;;; Set default, validates the value, shows in help
 `->envname("VAR")` ;;; Fall back to env var if flag not passed

### Flags

```cpp
bool verbose = false;
int verbosity = 0;

app.add_flag("-v,--verbose", verbose, "Enable verbose output");
app.add_flag("-V", verbosity, "Verbosity level");  // -V -V -V → verbosity == 3
```

 `add_flag(names, var, desc)` ;;; Bool var = set/unset; int var = increment per occurrence

### Positionals

```cpp
std::string input;
app.add_option("input", input, "Input file")->required();  // no '-' prefix = positional
```

### Subcommands

```cpp
auto* run = app.add_subcommand("run", "Run a job");
std::string mode;
run->add_option("--mode", mode, "Execution mode");

app.require_subcommand(1);
CLI11_PARSE(app, argc, argv);

if (*run) { /* subcommand was invoked */ }
```

 `app.add_subcommand(name, desc)` ;;; Returns `CLI::App*`; attach options to it directly
 `app.require_subcommand(N)` ;;; Require exactly N subcommands; `0` = optional
 `if (*sub)` ;;; True if that subcommand was used in this parse

### Multi-Value / Vectors

```cpp
std::vector<int> nums;
app.add_option("--nums", nums, "List");  // --nums 1 2 3  OR  --nums 1,2,3
```

 `->expected(N)` ;;; Exactly N values
 `->expected(Nmin, Nmax)` ;;; Between Nmin and Nmax values
 `->delimiter(',')` ;;; Split `1,2,3` on delimiter into separate values

### Validators

| Validator | Accepts |
|---|---|
| `CLI::ExistingFile` | Path that exists and is a file |
| `CLI::ExistingDirectory` | Path that exists and is a directory |
| `CLI::NonexistentPath` | Path that does not yet exist |
| `CLI::Range(min, max)` | Numeric value within \[min, max\] |
| `CLI::PositiveNumber` | Value > 0 |
| `CLI::Number` | Any numeric string |
| `CLI::Validator(fn, desc)` | Custom: `fn` takes `std::string&`, returns error string or `""` |

 `->check(V)` ;;; Validate; aborts parse on failure
 `->transform(V)` ;;; Validate and mutate the string in-place (e.g. map enum names to ints)

### Config Files

```cpp
app.set_config("--config", "config.ini", "Load config");
// INI format: key = value  (matches long option names)
```

See full modifier reference: [[Cpp CLI App]]

## Breadcrumbs

```breadcrumbs
type: mermaid
field-groups: [downs]
merge-fields: true
sort: field asc
show-attributes: [field]
```
