---
summary: 
headings:
  - "[[#Usage]]"
type: note/library
item_of:
  - "[[Rust attributes]]"
date created: Tuesday, April 8th 2025, 11:08:25 am
date modified: Tuesday, April 29th 2025, 2:36:22 pm
tags: 
items:
  - "[[Rust testing attributes]]"
  - "[[Rust derive attributes]]"
  - "[[Rust diagnostics attributes]]"
  - "[[Rust codegen attributes]]"
  - "[[Rust limits attributes]]"
  - "[[Rust type system attributes]]"
  - "[[Rust debugger attributes]]"
library_of:
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
  `#[cfg(<conditional>)]``=``target_os` ;;; Controls conditional compilation. [Conditional compilation - The Rust Reference](https://doc.rust-lang.org/nightly/reference/conditional-compilation.html#target_os) = #lang/meta/attributes/builtin #lang/meta/attributes/conditional 
ID: 1751997628113



      `target_env`
      `test` Enabled when compiling test harness
      `panic` Set depending on the panic strategy
      `target_has_atomic` Set for each bit width that supports atomic loads, stores, and compare-and-swap operations
  `#[cfg_attr]` ;;; Conditionally includes attributes. = #lang/meta/attributes/builtin #lang/meta/attributes/conditional 
ID: 1751997628118



  `#[test]` ;;; Marks a function as a test. = #lang/meta/attributes/builtin #lang/meta/attributes/testing 
ID: 1751997628123



  `#[ignore]` ;;; Disables a test function. = #lang/meta/attributes/builtin #lang/meta/attributes/testing 
ID: 1751997628128



  `#[should_panic]` ;;; Indicates a test should generate a panic. = #lang/meta/attributes/builtin #lang/meta/attributes/testing 
ID: 1751997628133



  `#[derive(Foo)]` ;;; Trait implementation for `Foo`, without manually writing the boilerplate. = #lang/meta/attributes/builtin #lang/meta/attributes/derive 
ID: 1751997628137



  `#[automatically_derived]` ;;; Attribute marker for implementations created by derive. = #lang/meta/attributes/builtin #lang/meta/attributes/derive 
ID: 1751997628142



  `#[macro_export]` ;;; Attribute marking something which exports a macro_rules macro for cross-crate usage. = #lang/meta/attributes/builtin #lang/meta/attributes/macros 


  `#[macro_use]` ;;; Attribute which expands macro visibility, or imports macros from other crates. = #lang/meta/attributes/builtin #lang/meta/attributes/macros 
ID: 1751997628148



  `#[proc_macro]` ;;; Attribute which defines a function-like macro. = #lang/meta/attributes/builtin #lang/meta/attributes/macros 


  `#[proc_macro_derive]` ;;; Attribute which defines a derive macro. = #lang/meta/attributes/builtin #lang/meta/attributes/macros 
ID: 1751997628154



  `#[proc_macro_attribute]` ;;; Attribute which defines an attribute macro. = #lang/meta/attributes/builtin #lang/meta/attributes/macros 


  `#[allow, expect, warn, deny, forbid]` ;;; Attribute which alters the default lint level, (includes all possible levels). = #lang/meta/attributes/builtin #lang/meta/attributes/diagnostics 
ID: 1751997628160



  `#[deprecated]` ;;; Attribute which generates deprecation notices. = #lang/meta/attributes/builtin #lang/meta/attributes/diagnostics 
ID: 1751997628164



  `#[must_use]` ;;; Attributes which generates a lint for unused values. = #lang/meta/attributes/builtin #lang/meta/attributes/diagnostics 
ID: 1751997628169



  `#[diagnostic::on_unimplemented]` ;;; Attribute which hints to the compiler to emit a certain error message if a trait is not implemented. = #lang/meta/attributes/builtin #lang/meta/attributes/diagnostics 
ID: 1751997628173



  `#[diagnostic::do_not_recommend]` ;;; Atteribute which hints the compiler to not show a certain trait impl in error messages. = #lang/meta/attributes/builtin #lang/meta/attributes/diagnostics 
ID: 1751997628177



  `#[link]` ;;; Attribute which specifies a native library to link with an extern block. = #lang/meta/attributes/builtin #lang/meta/attributes/ffi 
ID: 1751997628181



  `#[link_name]` ;;; Specifies the name of the symbol for functions or statics in an extern block. = #lang/meta/attributes/builtin #lang/meta/attributes/ffi 
ID: 1751997628185



  `#[link_ordinal]` ;;; Specifies the ordinal of the symbol for functions or statics in an extern block. = #lang/meta/attributes/builtin #lang/meta/attributes/ffi 
ID: 1751997628190



  `#[no_link]` ;;; Prevents linking an extern crate. = #lang/meta/attributes/builtin #lang/meta/attributes/ffi 
ID: 1751997628194




  `#[crate_type]` ;;; Specifies the type of crate (library, executable, etc.). = #lang/meta/attributes/builtin #lang/meta/attributes/ffi 
ID: 1751997628203



  `#[no_main]` ;;; Disables emitting the main symbol. = #lang/meta/attributes/builtin #lang/meta/attributes/ffi 
ID: 1751997628207



  `#[export_name]` ;;; Specifies the exported symbol name for a function or static. = #lang/meta/attributes/builtin #lang/meta/attributes/ffi 
ID: 1751997628212



  `#[link_section]` ;;; Specifies the section of an object file to use for a function or static. = #lang/meta/attributes/builtin #lang/meta/attributes/ffi 
ID: 1751997628216



  `#[no_mangle]` ;;; Disables symbol name encoding. = #lang/meta/attributes/builtin #lang/meta/attributes/ffi 
ID: 1751997628220



  `#[used]` ;;; Forces the compiler to keep a static item in the output object file. = #lang/meta/attributes/builtin #lang/meta/attributes/ffi 
ID: 1751997628225



  `#[crate_name]` ;;; Specifies the crate name. = #lang/meta/attributes/builtin #lang/meta/attributes/ffi 
ID: 1751997628229



  `#[inline]` ;;; Hint to inline code. = #lang/meta/attributes/builtin #lang/meta/attributes/codegen 
ID: 1751997628233



  `#[cold]` ;;; Hint that a function is unlikely to be called. = #lang/meta/attributes/builtin #lang/meta/attributes/codegen 
ID: 1751997628238



  `#[no_builtins]` ;;; Disables use of certain built-in functions. = #lang/meta/attributes/builtin #lang/meta/attributes/codegen 
ID: 1751997628242



  `#[target_feature]` ;;; Configure platform-specific code generation. = #lang/meta/attributes/builtin #lang/meta/attributes/codegen 
ID: 1751997628247



  `#[track_caller]` ;;; Pass the parent call location to std::panic::Location::caller(). = #lang/meta/attributes/builtin #lang/meta/attributes/codegen 
ID: 1751997628251



  `#[instruction_set]` ;;; Specify the instruction set used to generate a function's code. = #lang/meta/attributes/builtin #lang/meta/attributes/codegen 
ID: 1751997628256



  `#[doc]` ;;; Specifies documentation. Doc comments are transformed into doc attributes. = #lang/meta/attributes/builtin #lang/meta/attributes/docs 
ID: 1751997628260



  `#[no_std]` ;;; Removes std from the prelude. = #lang/meta/attributes/builtin #lang/meta/attributes/prelude 
ID: 1751997628264



  `#[no_implicit_prelude]` ;;; Disables prelude lookups within a module. = #lang/meta/attributes/builtin #lang/meta/attributes/prelude 
ID: 1751997628269



  `#[path]` ;;; Specifies the filename for a module. = #lang/meta/attributes/builtin #lang/meta/attributes/modules 
ID: 1751997628273



  `#[recursion_limit]` ;;; Sets the maximum recursion limit for certain compile-time operations. = #lang/meta/attributes/builtin #lang/meta/attributes/limits 
ID: 1751997628278



  `#[type_length_limit]` ;;; Sets the maximum size of a polymorphic type. = #lang/meta/attributes/builtin #lang/meta/attributes/limits 
ID: 1751997628282



  `#[panic_handler]` ;;; Sets the function to handle panics. = #lang/meta/attributes/builtin #lang/meta/attributes/runtime 
ID: 1751997628287



  `#[global_allocator]` ;;; Sets the global memory allocator. = #lang/meta/attributes/builtin #lang/meta/attributes/runtime 
ID: 1751997628291



  `#[windows_subsystem]` ;;; Specifies the Windows subsystem to link with. = #lang/meta/attributes/builtin #lang/meta/attributes/runtime 
ID: 1751997628296



  `#[feature]` ;;; Used to enable unstable or experimental compiler features. = #lang/meta/attributes/builtin #lang/meta/attributes/features 
ID: 1751997628301



  `#[non_exhaustive]` ;;; Indicate that a type will have more fields/variants added in future. = #lang/meta/attributes/builtin #lang/meta/attributes/typesystem 
ID: 1751997628305



  `#[debugger_visualizer]` ;;; Embeds a file that specifies debugger output for a type. = #lang/meta/attributes/builtin #lang/meta/attributes/debug 
ID: 1751997628310



  `#[collapse_debuginfo]` ;;; Controls how macro invocations are encoded in debuginfo. = #lang/meta/attributes/builtin #lang/meta/attributes/debug 
ID: 1751997628314


