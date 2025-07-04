---
summary: Procedural macro for generating basic getters/setters on fields.
headings: 
type: 
date created: Friday, April 18th 2025, 11:43:11 am
date modified: Friday, April 18th 2025, 11:44:05 am
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note
Getters are generated as `fn field(&self) -> &type`, while setters are generated as `fn field(&mut self, val: type)`. These macros are not intended to be used on fields which require custom logic inside of their setters and getters. Just write your own in that case!

## Examples
```rust
use getset::{CopyGetters, Getters, MutGetters, Setters, WithSetters};

#[derive(Getters, Setters, MutGetters, CopyGetters, WithSetters, Default)]
pub struct Foo<T>
where
    T: Copy + Clone + Default,
{
    /// Doc comments are supported!
    /// Multiline, even.
    #[getset(get, set, get_mut, set_with)]
    private: T,

    /// Doc comments are supported!
    /// Multiline, even.
    #[getset(get_copy = "pub", set = "pub", get_mut = "pub", set_with = "pub")]
    public: T,
}

fn main() {
    let mut foo = Foo::default();
    foo.set_private(1);
    (*foo.private_mut()) += 1;
    assert_eq!(*foo.private(), 2);
    foo = foo.with_private(3);
    assert_eq!(*foo.private(), 3);
}
```
- [p] `getset::{get, `