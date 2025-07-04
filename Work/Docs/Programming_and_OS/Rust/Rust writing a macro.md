---
summary: 
headings: ["[[#Syntax]]"]
type: note/workflow
date created: Tuesday, April 29th 2025, 2:51:38 pm
date modified: Tuesday, April 29th 2025, 2:51:59 pm
tags: [code/rust/attributes/macros/toolingDirectives]
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Syntax
[Macros By Example - The Rust Reference](https://doc.rust-lang.org/reference/macros-by-example.html)
```
macroRulesDef
```

### Metavariables
- `block`: a [_BlockExpression_](https://doc.rust-lang.org/reference/expressions/block-expr.html)
- `expr`: an [_Expression_](https://doc.rust-lang.org/reference/expressions.html)
- `expr_2021`: an [_Expression_](https://doc.rust-lang.org/reference/expressions.html) except [_UnderscoreExpression_](https://doc.rust-lang.org/reference/expressions/underscore-expr.html) and [_ConstBlockExpression_](https://doc.rust-lang.org/reference/expressions/block-expr.html#const-blocks) (see [macro.decl.meta.edition2024](https://doc.rust-lang.org/reference/macros-by-example.html#r-macro.decl.meta.edition2024))
- `ident`: an [IDENTIFIER_OR_KEYWORD](https://doc.rust-lang.org/reference/identifiers.html) or [RAW_IDENTIFIER](https://doc.rust-lang.org/reference/identifiers.html)
- `item`: an [_Item_](https://doc.rust-lang.org/reference/items.html)
- `lifetime`: a [LIFETIME_TOKEN](https://doc.rust-lang.org/reference/tokens.html#lifetimes-and-loop-labels)
- `literal`: matches `-`?[_LiteralExpression_](https://doc.rust-lang.org/reference/expressions/literal-expr.html)
- `meta`: an [_Attr_](https://doc.rust-lang.org/reference/attributes.html), the contents of an attribute
- `pat`: a [_Pattern_](https://doc.rust-lang.org/reference/patterns.html) (see [macro.decl.meta.edition2021](https://doc.rust-lang.org/reference/macros-by-example.html#r-macro.decl.meta.edition2021))
- `pat_param`: a [_PatternNoTopAlt_](https://doc.rust-lang.org/reference/patterns.html)
- `path`: a [_TypePath_](https://doc.rust-lang.org/reference/paths.html#paths-in-types) style path
- `stmt`: a [_Statement_](https://doc.rust-lang.org/reference/statements.html) without the trailing semicolon (except for item statements that require semicolons)
- `tt`: a [_TokenTree_](https://doc.rust-lang.org/reference/macros.html#macro-invocation) (a single [token](https://doc.rust-lang.org/reference/tokens.html) or tokens in matching delimiters `()`, `[]`, or `{}`)
- `ty`: a [_Type_](https://doc.rust-lang.org/reference/types.html#type-expressions)
- `vis`: a possibly empty [_Visibility_](https://doc.rust-lang.org/reference/visibility-and-privacy.html) qualifier

## Usage
- [p] `#derive` = Generates various traits for you
- [p] `#[macro_export]` = Says that the following macro should be brought into scope whenever crate in which macro is defined is brought into scope = #code/rust/attributes/macros/toolingDirectives
<!--ID: 1751434089980-->

- [p] `#[macro_export]` = Let macro persist past module, or import from `extern_crate` = #code/rust/attributes/macros/toolingDirectives
<!--ID: 1751434382626-->

- [p] `#[proc_macro]` = Mark `fn` as a function-like procedural macro, callable as `m!()` = #code/rust/attributes/macros/toolingDirectives
<!--ID: 1751434089987-->

- [p] `#[proc_macro_derive(Foo)]` = Mark `fn` as a derive macro, which can `#[derive(Foo)]` = #code/rust/attributes/macros/toolingDirectives
<!--ID: 1751434089992-->

- [p] `#[proc_macro_attribute]` = Mark `fn` as an attribute macro for new `#[x]` = #code/rust/attributes/macros/toolingDirectives
<!--ID: 1751434089996-->


|Fragment|Matches|Example|
|---|---|---|
|`expr`|An expression|`3`, `a + b`, `foo(42)`|
|`ident`|An identifier|`my_var`, `foo`, `x`|
|`ty`|A type|`u32`, `Vec<T>`, `&str`|
|`pat`|A pattern|`Some(x)`, `42`, `x @ _`|
|`block`|A block of code `{ ... }`|`{ println!("hi"); }`|
