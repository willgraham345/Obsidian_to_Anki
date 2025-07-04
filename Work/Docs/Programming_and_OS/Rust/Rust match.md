---
summary: Similar to a switch statement, branches on a pattern
headings:
  - "[[#Concepts of Note]]"
  - "[[#Examples]]"
  - "[[#Syntax]]"
type: note/concept
associations:
  - "[[Rust macros]]"
  - "[[Rust question mark operator]]"
date created: Thursday, April 17th 2025, 5:26:07 pm
date modified: Wednesday, May 7th 2025, 12:37:56 pm
used_by:
  - "[[Rust std result]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- [I] Match guard = Refines criteria for accepting a case. Appear after the pattern, and are a `bool`-typed expression = #term/rust 
- [p] `match x { 1=>println!("one"), 2=>println!("two"), _=>println!("not 1 or 2") }` = Match in Rust. Basically you throw a  = #code/rust/control_flow/match
<!--ID: 1751434090524-->

- [I] Match arm = If the pattern on the left matches, execute the expression on the right #code/rust 
- [p] `=>` = A match arm. (If the pattern on the left matches, execute the expression on the right) = #code/rust/control_flow/match 
<!--ID: 1751434090528-->


## Syntax
> _MatchExpression_ :  
>    `match` _Scrutinee_ `{`  
>       [_InnerAttribute_](https://doc.rust-lang.org/reference/attributes.html)*  
>       _MatchArms_?  
>    `}`
> 
> _Scrutinee_ :  
>    [_Expression_](https://doc.rust-lang.org/reference/expressions.html)_except struct expression_
> 
> _MatchArms_ :  
>    ( _MatchArm_ `=>` ( [_ExpressionWithoutBlock_](https://doc.rust-lang.org/reference/expressions.html) `,` | [_ExpressionWithBlock_](https://doc.rust-lang.org/reference/expressions.html) `,`? ) )*  
>    _MatchArm_ `=>` [_Expression_](https://doc.rust-lang.org/reference/expressions.html) `,`?
> 
> _MatchArm_ :  
>    [_OuterAttribute_](https://doc.rust-lang.org/reference/attributes.html)* [_Pattern_](https://doc.rust-lang.org/reference/patterns.html) _MatchArmGuard_?
> 
> _MatchArmGuard_ :  
>    `if` [_Expression_](https://doc.rust-lang.org/reference/expressions.html)

## Examples
### Print a "one"/"two"/"something else" based on input
```rust
let x = 1;
match x {
    1 => println!("one"),
    2 => println!("two"),
    _ => println!("something else"),
}

```

### Return a different variable
```rust
let x = 1;
match x {
    1 => y,
    2 => z,
    __ => !
}

```

## Media
[Match expressions - The Rust Reference](https://doc.rust-lang.org/reference/expressions/match-expr.html)
