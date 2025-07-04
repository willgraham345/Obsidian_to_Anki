---
summary: Rust build system and package manager. This handles most of the intricacies and is typically what is used by developers the most.
type: note/tool
components:
  - "[[#Usage]]"
associations:
  - "[[Rust cargo toml]]"
  - "[[Rust rustc]]"
date created: Monday, March 31st 2025, 11:26:38 am
date modified: Monday, April 28th 2025, 11:15:11 am
tags:
  - command/rust/build-sys
concepts:
  - "[[Rust cargo targets]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[Hello, Cargo! - The Rust Programming Language](https://doc.rust-lang.org/beta/book/ch01-03-hello-cargo.html#hello-cargo)

## Usage
- [c] `cargo new` = Creates a new Cargo package rust = #command/rust/build-sys = `--bin` Create a package with a binary target `src/main.rs`
<!--ID: 1751434090586-->

      `--lib` Create a package with a library target `src/lib.rs`
      ``
- [c] `cargo build` = Builds the current project in rust = #command/rust/build-sys
<!--ID: 1751434090590-->

- [c] `cargo run` = Runs the current test, will also build if not already built = #command/rust/build-sys
<!--ID: 1751434090594-->

- [c] `cargo check` = Checks your code to see if it can compile, but doesn't run an executable = #command/rust/build-sys
<!--ID: 1751434090598-->

- [c] `cargo init` = Creates a new Cargo manifest in the current directory. Give a path as an argument to create in the directory. If there are typically-named Rust suorce files already in the directory, those will be used. If not, a sample `src/main.rs` will be created, or `src/lib.rs` if `--lib` is passed in = #command/rust/build-sys = `--bin` Create a package with a binary target `src/main.rs`
<!--ID: 1751434090601-->

      `--lib` Create a package with a library target `src/lib.rs`
- [c] `cargo add` = Add dependencies to a Cargo.toml manifest file = #command/rust/build-sys = `--path` Specify path
<!--ID: 1751434090605-->

      `--git` Specify url
      `--dev` Add as a development dependency
      `--build` Add as a build dependency
      `--target` Add as a dependency to the given target platform