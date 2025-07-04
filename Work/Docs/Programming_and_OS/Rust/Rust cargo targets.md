---
summary: Cargo packages consist of targets, corresponding to source files which can be compiled into a crate. The list of targets can be configured in the cargo toml manifest, often inferred automatically by the directory layout of the source files.
headings:
  - "[[#Concepts of Note]]"
  - "[[#Syntax]]"
type: note/concept
aliases:
  - Rust build targets
associations:
  - "[[Rust cargo toml]]"
date created: Monday, April 28th 2025, 11:15:37 am
date modified: Monday, April 28th 2025, 11:27:10 am
concept_of:
  - "[[Rust cargo]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[Cargo Targets - The Cargo Book](https://doc.rust-lang.org/cargo/reference/cargo-targets.html#cargo-targets)

## Concepts of Note
### Library
- Source: `src/lib.rs`
- Can be used and linked by other libraries and executables
- A package an only have one library, default name is name of the package with dashes replaced by underscores.

### Binaries
- Source: `src/main.rs`
	- Can also be stored in the `src/bin/` directory
	- 
- Executable programs that can be run after compilation
- Default binary is the package name
- 

### Tests
- Unit tests
	- Marked with `#[test]` attribute, located wtihin library or binaries.
	- Have access to private APIs located within the target they are defined in.
- Integration tests
	- Separate executable binary, containing `#[test]` functions, linked to the project's library and has access to its *public* API.

### Examples
- Files located in `examples/` are examples of functionality
- After compiltion, they're placed in the `target/debug/examples` directory

## Syntax
```toml
[lib]
name = "foo"           # The name of the target.
path = "src/lib.rs"    # The source file of the target.
test = true            # Is tested by default.
doctest = true         # Documentation examples are tested by default.
bench = true           # Is benchmarked by default.
doc = true             # Is documented by default.
proc-macro = false     # Set to `true` for a proc-macro library.
harness = true         # Use libtest harness.
edition = "2015"       # The edition of the target.
crate-type = ["lib"]   # The crate types to generate.
required-features = [] # Features required to build this target (N/A for lib).
```
[Cargo Targets - The Cargo Book](https://doc.rust-lang.org/cargo/reference/cargo-targets.html#configuring-a-target)
