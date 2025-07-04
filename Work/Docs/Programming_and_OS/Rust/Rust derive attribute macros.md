---
summary: Derive macros allow for automatic code generation, with additional customization through attributes.
headings: ["[[#Concepts of Note]]"]
type: note/concept
associations: ["[[Rust attributes]]"]
concept_of: ["[[Rust derive macros]]"]
date created: Tuesday, April 22nd 2025, 2:24:35 pm
date modified: Wednesday, May 21st 2025, 6:02:45 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- `Path`: Path, like `test` in `#[test]`
- `List`: structured list, like `derive(Debug)` in `#[derive(Debug]`
- `NameValue`: like `feature = ...`  in `#[cfg(feature = "nightly")]`

Attribute macros lack namespacing
Attribute consists of the path to the attribute, followed by an optional delimited token tree whose interpretation is defined by the attribute.

## Syntax
### Style Guide
```
// Crate-namespaced attributes
#[serde(...)] // serde
#[strum(...)] // strum
#[prost(...)] // prost

// Trait/struct-namespaced attributes
#[command(...)] // clap (Subcommand trait)
#[group(...)] // clap (ArgGroup struct)
#[arg(...)] // clap (Arg struct)
#[value(...)] // clap (PossibleValue struct)

// Non-namespaced attributes
#[backtrace] // thiserror
#[error(...)] // thiserror
#[from] // thiserror
#[source] // thiserror
```

### Container, variant, and field attributes
```
#[container_attribute]
enum Enum {
    #[variant_attribute]
    Variant {
        #[field_attribute]
        field: Type,
    }
}
```

