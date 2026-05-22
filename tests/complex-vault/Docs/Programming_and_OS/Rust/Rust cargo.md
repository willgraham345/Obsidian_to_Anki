---
summary: Rust build system and package manager. This handles most of the intricacies and is typically what is used by developers the most.
type: note/tool
headings:
concepts:
  - "[[Rust cargo targets]]"
associations:
  - "[[Rust cargo toml]]"
  - "[[Rust rustc]]"
date created: Monday, March 31st 2025, 11:26:38 am
date modified: Monday, March 30th 2026, 4:46:17 pm
items:
  - "[[#Usage]]"
tags: [lang/build]
template:
template-version:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[Hello, Cargo! - The Rust Programming Language](https://doc.rust-lang.org/beta/book/ch01-03-hello-cargo.html#hello-cargo)

## Usage
  `cargo new --bin` ;;; Creates a new Cargo package rust with a binary target: `src/main.rs` 

  `cargo new --lib` ;;; Creates a new Cargo package with a library target `src/lib.rs`. 

  `cargo build` ;;; Builds the current project in rust 

  `cargo run` ;;; Runs the current test, will also build if not already built

  `cargo check` ;;; Checks your code to see if it can compile, but doesn't run an executable 

  `cargo init` ;;; Creates a new Cargo manifest in the current directory. Give a path as an argument to create in the directory. If there are typically-named Rust source files already in the directory, those will be used. If not, a sample `src/main.rs` will be created, or `src/lib.rs` if `--lib` is passed in

  `cargo add --path path` ;;; Add path dependencies `path` to a Cargo.toml manifest file.

  `cargo add --dev --path path` ;;; Add a development dependencies `path` to a Cargo.toml manifest file.

  `cargo add --build --path path` ;;; Add a build dependencies `path` to a Cargo.toml manifest file.

  `cargo add --target t` ;;; Add a path dependencies to a Cargo.toml manifest file.

  `cargo add --git url` ;;; Add git dependencies `url` to a Cargo.toml manifest file.


