---
type: note/concept
up: ["[[Rust Basics]]"]
date created: Tuesday, August 20th 2024, 2:05:35 pm
date modified: Wednesday, January 8th 2025, 4:41:30 pm
---

Basic project layout, and common files and folders, as used by `cargo`. [↓](https://cheats.rs/#cargo "On this site, below.")

|Entry|Code|
|---|---|
|📁 `.cargo/`|**Project-local cargo configuration**, may contain **`config.toml`**. [🔗](https://doc.rust-lang.org/cargo/reference/config.html "Third-party site (mainly used in conjunction with other symbols).") 🝖|
|📁 `benches/`|Benchmarks for your crate, run via **`cargo bench`**, requires nightly by default. * 🚧|
|📁 `examples/`|Examples how to use your crate, they see your crate like external user would.|
|`my_example.rs`|Individual examples are run like **`cargo run --example my_example`**.|
|📁 `src/`|Actual source code for your project.|
|`main.rs`|Default entry point for applications, this is what **`cargo run`** uses.|
|`lib.rs`|Default entry point for libraries. This is where lookup for `my_crate::f()` starts.|
|📁 `src/bin/`|Place for additional binaries, even in library projects.|
|`extra.rs`|Additional binary, run with `cargo run --bin extra`.|
|📁 `tests/`|Integration tests go here, invoked via **`cargo test`**. Unit tests often stay in `src/` file.|
|`.rustfmt.toml`|In case you want to [**customize**](https://rust-lang.github.io/rustfmt/) how **`cargo fmt`** works.|
|`.clippy.toml`|Special configuration for certain [**clippy lints**](https://rust-lang.github.io/rust-clippy/master/index.html), utilized via **`cargo clippy`** 🝖|
|`build.rs`|**Pre-build script**, [🔗](https://doc.rust-lang.org/cargo/reference/build-scripts.html "Third-party site (mainly used in conjunction with other symbols).") useful when compiling C / FFI, …|
|`Cargo.toml`|Main **project manifest**, [🔗](https://doc.rust-lang.org/cargo/reference/manifest.html "Third-party site (mainly used in conjunction with other symbols).") Defines dependencies, artifacts …|
|`Cargo.lock`|For reproducible builds. Add to git for apps, consider not for libs. 💬 [🔗](https://blog.rust-lang.org/2023/08/29/committing-lockfiles.html "Third-party site (mainly used in conjunction with other symbols).") [🔗](https://old.reddit.com/r/rust/comments/164qfjm/change_in_guidance_on_committing_lockfiles_rust/jya8ouf/ "Third-party site (mainly used in conjunction with other symbols).")|
|`rust-toolchain.toml`|Define **toolchain override**[🔗](https://rust-lang.github.io/rustup/overrides.html "Third-party site (mainly used in conjunction with other symbols).") (channel, components, targets) for this project.|

* On stable consider [Criterion](https://github.com/bheisler/criterion.rs).