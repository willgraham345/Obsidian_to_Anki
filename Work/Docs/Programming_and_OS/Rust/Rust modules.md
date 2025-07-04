---
summary: A container for zero or more items. Has various traits which make it accessible to other objects.
headings: ["[[#Concepts of Note]]", "[[#Examples]]", "[[#Media]]"]
type: note/component
concept_of: ["[[Rust Items]]"]
date created: Friday, March 21st 2025, 10:29:18 am
date modified: Tuesday, April 22nd 2025, 4:29:32 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- Module item = A module surrounded in braces, named, and prefixed with the keyword `mod`. This introduces a new, named module into the tree of modules making up a crate.
- Modules can nest arbitrarily, defined in the type namespace of the module or block where they are located.

### Module Source Filenames
- A module without a body, is loaded in from an external file.

|Module Path|Filesystem Path|File Contents|
|---|---|---|
|`crate`|`lib.rs`|`mod util;`|
|`crate::util`|`util.rs`|`mod config;`|
|`crate::util::config`|`util/config.rs`||

## Examples
### New Module
```rust
mod math {
    type Complex = (f64, f64);
    fn sin(f: f64) -> f64 {
        /* ... */
    }
    fn cos(f: f64) -> f64 {
        /* ... */
    }
    fn tan(f: f64) -> f64 {
        /* ... */
    }
}
```

### Loading in a Module from an External File
```rust
mod app;
pub mod messages; //Declares that the module should also be made public to others at the crate level
```

## Media
[Modules - The Rust Reference](https://doc.rust-lang.org/reference/items/modules.html)