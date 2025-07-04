---
summary: 
headings:
  - "[[#Usage]]"
type: note/library
component_of:
  - "[[Rust attributes]]"
date created: Tuesday, April 8th 2025, 11:08:25 am
date modified: Tuesday, April 29th 2025, 2:36:22 pm
tags:
  - code/rust/attributes/builtin
  - code/rust/attributes/codegen
  - code/rust/attributes/conditional
  - code/rust/attributes/debug
  - code/rust/attributes/derive
  - code/rust/attributes/diagnostics
  - code/rust/attributes/docs
  - code/rust/attributes/features
  - code/rust/attributes/ffi
  - code/rust/attributes/limits
  - code/rust/attributes/macros
  - code/rust/attributes/modules
  - code/rust/attributes/prelude
  - code/rust/attributes/runtime
  - code/rust/attributes/testing
  - code/rust/attributes/typesystem
components:
  - "[[Rust testing attributes]]"
  - "[[Rust derive attributes]]"
  - "[[Rust diagnostics attributes]]"
  - "[[Rust codegen attributes]]"
  - "[[Rust limits attributes]]"
  - "[[Rust type system attributes]]"
  - "[[Rust debugger attributes]]"
library_used_in:
  - "[[Rust attributes]]"
  - "[[Rust std]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- Conditional compilation
    - [`cfg`](https://doc.rust-lang.org/reference/conditional-compilation.html#the-cfg-attribute) — Controls conditional compilation.
    - [`cfg_attr`](https://doc.rust-lang.org/reference/conditional-compilation.html#the-cfg_attr-attribute) — Conditionally includes attributes.
- Testing
    - [`test`](https://doc.rust-lang.org/reference/attributes/testing.html#the-test-attribute) — Marks a function as a test.
    - [`ignore`](https://doc.rust-lang.org/reference/attributes/testing.html#the-ignore-attribute) — Disables a test function.
    - [`should_panic`](https://doc.rust-lang.org/reference/attributes/testing.html#the-should_panic-attribute) — Indicates a test should generate a panic.
- Derive
    - [`derive`](https://doc.rust-lang.org/reference/attributes/derive.html) — Automatic trait implementations.
    - [`automatically_derived`](https://doc.rust-lang.org/reference/attributes/derive.html#the-automatically_derived-attribute) — Marker for implementations created by `derive`.
- Macros
    - [`macro_export`](https://doc.rust-lang.org/reference/macros-by-example.html#path-based-scope) — Exports a `macro_rules` macro for cross-crate usage.
    - [`macro_use`](https://doc.rust-lang.org/reference/macros-by-example.html#the-macro_use-attribute) — Expands macro visibility, or imports macros from other crates.
    - [`proc_macro`](https://doc.rust-lang.org/reference/procedural-macros.html#function-like-procedural-macros) — Defines a function-like macro.
    - [`proc_macro_derive`](https://doc.rust-lang.org/reference/procedural-macros.html#derive-macros) — Defines a derive macro.
    - [`proc_macro_attribute`](https://doc.rust-lang.org/reference/procedural-macros.html#attribute-macros) — Defines an attribute macro.
- Diagnostics
    - [`allow`](https://doc.rust-lang.org/reference/attributes/diagnostics.html#lint-check-attributes), [`expect`](https://doc.rust-lang.org/reference/attributes/diagnostics.html#lint-check-attributes), [`warn`](https://doc.rust-lang.org/reference/attributes/diagnostics.html#lint-check-attributes), [`deny`](https://doc.rust-lang.org/reference/attributes/diagnostics.html#lint-check-attributes), [`forbid`](https://doc.rust-lang.org/reference/attributes/diagnostics.html#lint-check-attributes) — Alters the default lint level.
    - [`deprecated`](https://doc.rust-lang.org/reference/attributes/diagnostics.html#the-deprecated-attribute) — Generates deprecation notices.
    - [`must_use`](https://doc.rust-lang.org/reference/attributes/diagnostics.html#the-must_use-attribute) — Generates a lint for unused values.
    - [`diagnostic::on_unimplemented`](https://doc.rust-lang.org/reference/attributes/diagnostics.html#the-diagnosticon_unimplemented-attribute) — Hints the compiler to emit a certain error message if a trait is not implemented.
    - [`diagnostic::do_not_recommend`](https://doc.rust-lang.org/reference/attributes/diagnostics.html#the-diagnosticdo_not_recommend-attribute) — Hints the compiler to not show a certain trait impl in error messages.
- ABI, linking, symbols, and FFI
    - [`link`](https://doc.rust-lang.org/reference/items/external-blocks.html#the-link-attribute) — Specifies a native library to link with an `extern` block.
    - [`link_name`](https://doc.rust-lang.org/reference/items/external-blocks.html#the-link_name-attribute) — Specifies the name of the symbol for functions or statics in an `extern` block.
    - [`link_ordinal`](https://doc.rust-lang.org/reference/items/external-blocks.html#the-link_ordinal-attribute) — Specifies the ordinal of the symbol for functions or statics in an `extern` block.
    - [`no_link`](https://doc.rust-lang.org/reference/items/extern-crates.html#the-no_link-attribute) — Prevents linking an extern crate.
    - [`repr`](https://doc.rust-lang.org/reference/type-layout.html#representations) — Controls type layout.
    - [`crate_type`](https://doc.rust-lang.org/reference/linkage.html) — Specifies the type of crate (library, executable, etc.).
    - [`no_main`](https://doc.rust-lang.org/reference/crates-and-source-files.html#the-no_main-attribute) — Disables emitting the `main` symbol.
    - [`export_name`](https://doc.rust-lang.org/reference/abi.html#the-export_name-attribute) — Specifies the exported symbol name for a function or static.
    - [`link_section`](https://doc.rust-lang.org/reference/abi.html#the-link_section-attribute) — Specifies the section of an object file to use for a function or static.
    - [`no_mangle`](https://doc.rust-lang.org/reference/abi.html#the-no_mangle-attribute) — Disables symbol name encoding.
    - [`used`](https://doc.rust-lang.org/reference/abi.html#the-used-attribute) — Forces the compiler to keep a static item in the output object file.
    - [`crate_name`](https://doc.rust-lang.org/reference/crates-and-source-files.html#the-crate_name-attribute) — Specifies the crate name.
- Code generation
    - [`inline`](https://doc.rust-lang.org/reference/attributes/codegen.html#the-inline-attribute) — Hint to inline code.
    - [`cold`](https://doc.rust-lang.org/reference/attributes/codegen.html#the-cold-attribute) — Hint that a function is unlikely to be called.
    - [`no_builtins`](https://doc.rust-lang.org/reference/attributes/codegen.html#the-no_builtins-attribute) — Disables use of certain built-in functions.
    - [`target_feature`](https://doc.rust-lang.org/reference/attributes/codegen.html#the-target_feature-attribute) — Configure platform-specific code generation.
    - [`track_caller`](https://doc.rust-lang.org/reference/attributes/codegen.html#the-track_caller-attribute) — Pass the parent call location to `std::panic::Location::caller()`.
    - [`instruction_set`](https://doc.rust-lang.org/reference/attributes/codegen.html#the-instruction_set-attribute) — Specify the instruction set used to generate a functions code
- Documentation
    - `doc` — Specifies documentation. See [The Rustdoc Book](https://doc.rust-lang.org/rustdoc/the-doc-attribute.html) for more information. [Doc comments](https://doc.rust-lang.org/reference/comments.html#doc-comments) are transformed into `doc` attributes.
- Preludes
    - [`no_std`](https://doc.rust-lang.org/reference/names/preludes.html#the-no_std-attribute) — Removes std from the prelude.
    - [`no_implicit_prelude`](https://doc.rust-lang.org/reference/names/preludes.html#the-no_implicit_prelude-attribute) — Disables prelude lookups within a module.
- Modules
    - [`path`](https://doc.rust-lang.org/reference/items/modules.html#the-path-attribute) — Specifies the filename for a module.
- Limits
    - [`recursion_limit`](https://doc.rust-lang.org/reference/attributes/limits.html#the-recursion_limit-attribute) — Sets the maximum recursion limit for certain compile-time operations.
    - [`type_length_limit`](https://doc.rust-lang.org/reference/attributes/limits.html#the-type_length_limit-attribute) — Sets the maximum size of a polymorphic type.
- Runtime
    - [`panic_handler`](https://doc.rust-lang.org/reference/runtime.html#the-panic_handler-attribute) — Sets the function to handle panics.
    - [`global_allocator`](https://doc.rust-lang.org/reference/runtime.html#the-global_allocator-attribute) — Sets the global memory allocator.
    - [`windows_subsystem`](https://doc.rust-lang.org/reference/runtime.html#the-windows_subsystem-attribute) — Specifies the windows subsystem to link with.
- Features
    - `feature` — Used to enable unstable or experimental compiler features. See [The Unstable Book](https://doc.rust-lang.org/unstable-book/index.html) for features implemented in `rustc`.
- Type System
    - [`non_exhaustive`](https://doc.rust-lang.org/reference/attributes/type_system.html#the-non_exhaustive-attribute) — Indicate that a type will have more fields/variants added in future.
- Debugger
    - [`debugger_visualizer`](https://doc.rust-lang.org/reference/attributes/debugger.html#the-debugger_visualizer-attribute) — Embeds a file that specifies debugger output for a type.
    - [`collapse_debuginfo`](https://doc.rust-lang.org/reference/attributes/debugger.html#the-collapse_debuginfo-attribute) — Controls how macro invocations are encoded in debuginfo.
## Usage
- [p] `#[cfg(<conditional>)]` = Controls conditional compilation. [Conditional compilation - The Rust Reference](https://doc.rust-lang.org/nightly/reference/conditional-compilation.html#target_os)= #code/rust/attributes/builtin #code/rust/attributes/conditional = `target_os`  
<!--ID: 1751434090217-->

      `target_env`
      `test` Enabled when compiling test harness
      `panic` Set depending on the panic strategy
      `target_has_atomic` Set for each bit width that supports atomic loads, stores, and compare-and-swap operations
- [p] `#[cfg_attr]` = Conditionally includes attributes. = #code/rust/attributes/builtin #code/rust/attributes/conditional
<!--ID: 1751434090221-->

- [p] `#[test]` = Marks a function as a test. = #code/rust/attributes/builtin #code/rust/attributes/testing
<!--ID: 1751434090226-->

- [p] `#[ignore]` = Disables a test function. = #code/rust/attributes/builtin #code/rust/attributes/testing
<!--ID: 1751434090230-->

- [p] `#[should_panic]` = Indicates a test should generate a panic. = #code/rust/attributes/builtin #code/rust/attributes/testing
<!--ID: 1751434090234-->

- [p] `#[derive]` = Automatic trait implementations. = #code/rust/attributes/builtin #code/rust/attributes/derive
<!--ID: 1751434090239-->

- [p] `#[automatically_derived]` = Marker for implementations created by derive. = #code/rust/attributes/builtin #code/rust/attributes/derive
<!--ID: 1751434090243-->

- [p] `#[macro_export]` = Exports a macro_rules macro for cross-crate usage. = #code/rust/attributes/builtin #code/rust/attributes/macros
- [p] `#[macro_use]` = Expands macro visibility, or imports macros from other crates. = #code/rust/attributes/builtin #code/rust/attributes/macros
<!--ID: 1751434090249-->

- [p] `#[proc_macro]` = Defines a function-like macro. = #code/rust/attributes/builtin #code/rust/attributes/macros
<!--ID: 1751434382648-->

- [p] `#[proc_macro_derive]` = Defines a derive macro. = #code/rust/attributes/builtin #code/rust/attributes/macros
<!--ID: 1751434090254-->

- [p] `#[proc_macro_attribute]` = Defines an attribute macro. = #code/rust/attributes/builtin #code/rust/attributes/macros
<!--ID: 1751434382652-->

- [p] `#[allow, expect, warn, deny, forbid]` = Alters the default lint level. = #code/rust/attributes/builtin #code/rust/attributes/diagnostics
<!--ID: 1751434090261-->

- [p] `#[deprecated]` = Generates deprecation notices. = #code/rust/attributes/builtin #code/rust/attributes/diagnostics
<!--ID: 1751434090264-->

- [p] `#[must_use]` = Generates a lint for unused values. = #code/rust/attributes/builtin #code/rust/attributes/diagnostics
<!--ID: 1751434090268-->

- [p] `#[diagnostic::on_unimplemented]` = Hints the compiler to emit a certain error message if a trait is not implemented. = #code/rust/attributes/builtin #code/rust/attributes/diagnostics
<!--ID: 1751434090272-->

- [p] `#[diagnostic::do_not_recommend]` = Hints the compiler to not show a certain trait impl in error messages. = #code/rust/attributes/builtin #code/rust/attributes/diagnostics
<!--ID: 1751434090277-->

- [p] `#[link]` = Specifies a native library to link with an extern block. = #code/rust/attributes/builtin #code/rust/attributes/ffi
<!--ID: 1751434090281-->

- [p] `#[link_name]` = Specifies the name of the symbol for functions or statics in an extern block. = #code/rust/attributes/builtin #code/rust/attributes/ffi
<!--ID: 1751434090285-->

- [p] `#[link_ordinal]` = Specifies the ordinal of the symbol for functions or statics in an extern block. = #code/rust/attributes/builtin #code/rust/attributes/ffi
<!--ID: 1751434090289-->

- [p] `#[no_link]` = Prevents linking an extern crate. = #code/rust/attributes/builtin #code/rust/attributes/ffi
<!--ID: 1751434090293-->

- [p] `#[repr]` = Controls type layout. = #code/rust/attributes/builtin #code/rust/attributes/ffi
<!--ID: 1751434090298-->

- [p] `#[crate_type]` = Specifies the type of crate (library, executable, etc.). = #code/rust/attributes/builtin #code/rust/attributes/ffi
<!--ID: 1751434090302-->

- [p] `#[no_main]` = Disables emitting the main symbol. = #code/rust/attributes/builtin #code/rust/attributes/ffi
<!--ID: 1751434090307-->

- [p] `#[export_name]` = Specifies the exported symbol name for a function or static. = #code/rust/attributes/builtin #code/rust/attributes/ffi
<!--ID: 1751434090312-->

- [p] `#[link_section]` = Specifies the section of an object file to use for a function or static. = #code/rust/attributes/builtin #code/rust/attributes/ffi
<!--ID: 1751434090316-->

- [p] `#[no_mangle]` = Disables symbol name encoding. = #code/rust/attributes/builtin #code/rust/attributes/ffi
<!--ID: 1751434090320-->

- [p] `#[used]` = Forces the compiler to keep a static item in the output object file. = #code/rust/attributes/builtin #code/rust/attributes/ffi
<!--ID: 1751434090324-->

- [p] `#[crate_name]` = Specifies the crate name. = #code/rust/attributes/builtin #code/rust/attributes/ffi
<!--ID: 1751434090329-->

- [p] `#[inline]` = Hint to inline code. = #code/rust/attributes/builtin #code/rust/attributes/codegen
<!--ID: 1751434090333-->

- [p] `#[cold]` = Hint that a function is unlikely to be called. = #code/rust/attributes/builtin #code/rust/attributes/codegen
<!--ID: 1751434090337-->

- [p] `#[no_builtins]` = Disables use of certain built-in functions. = #code/rust/attributes/builtin #code/rust/attributes/codegen
<!--ID: 1751434090341-->

- [p] `#[target_feature]` = Configure platform-specific code generation. = #code/rust/attributes/builtin #code/rust/attributes/codegen
<!--ID: 1751434090345-->

- [p] `#[track_caller]` = Pass the parent call location to std::panic::Location::caller(). = #code/rust/attributes/builtin #code/rust/attributes/codegen
<!--ID: 1751434090349-->

- [p] `#[instruction_set]` = Specify the instruction set used to generate a function's code. = #code/rust/attributes/builtin #code/rust/attributes/codegen
<!--ID: 1751434090354-->

- [p] `#[doc]` = Specifies documentation. Doc comments are transformed into doc attributes. = #code/rust/attributes/builtin #code/rust/attributes/docs
<!--ID: 1751434090358-->

- [p] `#[no_std]` = Removes std from the prelude. = #code/rust/attributes/builtin #code/rust/attributes/prelude
<!--ID: 1751434090362-->

- [p] `#[no_implicit_prelude]` = Disables prelude lookups within a module. = #code/rust/attributes/builtin #code/rust/attributes/prelude
<!--ID: 1751434090367-->

- [p] `#[path]` = Specifies the filename for a module. = #code/rust/attributes/builtin #code/rust/attributes/modules
<!--ID: 1751434090372-->

- [p] `#[recursion_limit]` = Sets the maximum recursion limit for certain compile-time operations. = #code/rust/attributes/builtin #code/rust/attributes/limits
<!--ID: 1751434090378-->

- [p] `#[type_length_limit]` = Sets the maximum size of a polymorphic type. = #code/rust/attributes/builtin #code/rust/attributes/limits
<!--ID: 1751434090384-->

- [p] `#[panic_handler]` = Sets the function to handle panics. = #code/rust/attributes/builtin #code/rust/attributes/runtime
<!--ID: 1751434090389-->

- [p] `#[global_allocator]` = Sets the global memory allocator. = #code/rust/attributes/builtin #code/rust/attributes/runtime
<!--ID: 1751434090394-->

- [p] `#[windows_subsystem]` = Specifies the Windows subsystem to link with. = #code/rust/attributes/builtin #code/rust/attributes/runtime
<!--ID: 1751434090399-->

- [p] `#[feature]` = Used to enable unstable or experimental compiler features. = #code/rust/attributes/builtin #code/rust/attributes/features
<!--ID: 1751434090403-->

- [p] `#[non_exhaustive]` = Indicate that a type will have more fields/variants added in future. = #code/rust/attributes/builtin #code/rust/attributes/typesystem
<!--ID: 1751434090408-->

- [p] `#[debugger_visualizer]` = Embeds a file that specifies debugger output for a type. = #code/rust/attributes/builtin #code/rust/attributes/debug
<!--ID: 1751434090412-->

- [p] `#[collapse_debuginfo]` = Controls how macro invocations are encoded in debuginfo. = #code/rust/attributes/builtin #code/rust/attributes/debug
<!--ID: 1751434090416-->
