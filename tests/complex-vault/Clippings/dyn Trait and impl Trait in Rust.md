---
title: "dyn Trait and impl Trait in Rust"
source: "https://www.ncameron.org/blog/dyn-trait-and-impl-trait-in-rust/"
author:
  - "[[Nick Cameron]]"
published: 2021-02-14
created: 2025-10-15
description: "One of the more subtle aspects of Rust is how traits can be used as types. In this blog post I will attempt a bit of a deep dive into how to use traits as types and how to choose between the different forms. Preliminary: traits are not typesA type"
tags:
  - "clippings"
  - "toread"
---
One of the more subtle aspects of Rust is how traits can be used as types. In this blog post I will attempt a bit of a deep dive into how to use traits as types and how to choose between the different forms.

## Preliminary: traits are not types

A type describes a set of values. Types are written on variable declarations (e.g., in `x: u8`, `u8` is a type) and can be inferred by the compiler (e.g., in `let x = 42u8;`, the type of `x` is inferred to be `u8`). In Rust, types come from built-in types (like `u8`, `bool`, etc.) and from datatype declarations, e.g., if there is a declaration `struct Foo { ... }`, then `Foo` is a type.

Traits are not types, if there is a declaration `trait Bar { ... }`, you cannot write `x: Bar`. Traits are bounds on types. When we declare a type variable we can bound it using a trait name and the bound limits the types which the type variable can take. E.g., we can write `<T: Bar>` and the type variable `T` can only be instantiated with types which implement `Bar`.

In some languages (e.g., C++, Java), types are also used as bounds on types; this is not the case in Rust.

## A running example

We're going to use several iterations of a simple example in the next few sections, we'll assume the following:

```rust
trait Bar {
    fn bar(&self) -> Vec<Self>;
}

impl Bar for Foo { ... }
impl Bar for Baz { ... }
```

The requirement is that we want to write a function `f` which takes any value which implements `Bar`:

```rust
fn f(b: Bar) -> usize {
    b.bar().len()
}
```

that won't compile, because as I mentioned above, traits aren't types. In the next few sections we'll look at versions which will compile.

## Using generics

We can use a generic type parameter:

```rust
fn f<B: Bar>(b: B) -> usize
```

This version takes `b` by value, we could also take a borrowed reference (`b: &B`) or a boxed reference `b: Box<B>`, etc. As required, this function can be passed any value which has a type which implements Bar.

## impl Trait

In argument position, `impl Trait` is simply a shorthand for the above generic version:

```rust
fn f(b: impl Bar) -> usize
```

This version of `f` is exactly the same as the previous version, just with a different syntax. You can also use `b: &impl Bar` or `b: Box<impl Bar>`, etc.

Since the trait is written in the type, not separately, there is one less indirection when reading the shorthand version, so it can make code easier to read. I would recommend using `impl Bar` rather than the previous generic version unless there are complex bounds.

If you want to use the type variable in multiple places you will need to use the longer version. E.g.,

```rust
fn f(b1: impl Bar, b2: impl Bar) -> usize
```

is equivalent to

```rust
fn f<B1: Bar, B2: Bar>(b1: B1, b2: B2) -> usize
```

not

```rust
fn f<B: Bar>(b1: B, b2: B) -> usize
```

The impl Trait shorthand can only be used for function arguments, it cannot be used for the types of fields or local variables, etc.

## dyn Trait

A trait object in Rust is similar to an object in Java or a virtual object in C++. A trait object is always passed by pointer (a borrowed reference, `Box`, or other smart pointer) and has a vtable so that methods can be dispatched dynamically. The type of trait objects uses `dyn Trait`, e.g., `&dyn Bar` or `Box<dyn Bar>`. Unlike `impl Trait`, you cannot use `dyn Trait` as a type without a wrapping pointer.

At compile time, only the trait bound is known; at runtime any concrete type which implements the trait can be used as a trait object via an implicit coercion, e.g., `let obj: &dyn Bar = &Foo { ... };`.

We can write a version of our function using trait objects:

```rust
fn f(b: &dyn Bar) -> usize
```

This is not a generic function, it only takes values with a single type, but that type is a trait object type, so there may be values with different concrete types within the trait object. The effect is that we have a function which can take any value which implements `Bar` (but only by reference, not by value).

## impl Trait in return position

impl Trait can also be used in the return type of a function. In this case it is not a shorthand for a generic type parameter, but has a somewhat different meaning. The key difference is whether the caller or the callee chooses the concrete type. If using a generic parameter (e.g., `fn f<T: Bar>(...) -> T`), the caller chooses the concrete type, therefore the callee must provide functions with any return type that the caller could choose. If using impl Trait (e.g., `fn f(...) -> impl Bar`), then the callee chooses the concrete type (i.e., the compiler infers the concrete type from the function body). Therefore there is only ever one concrete type, however, that concrete type is not known to the caller, so the caller can only assume the trait bound.

For example,

```rust
fn f() -> impl Bar {
    Foo { ... }
}

fn main() {
    let b = f();
    let _ = b.bar();
}
```

In this case the implementer of `f` has chosen to return an instance of `Foo` but the caller only knows that it is *some* implementation of `Bar`. The implementation of `f` can change to return an instance of `Baz` (or any other implementation of `Bar`) without changing the function signature.

Note that there can only be one concrete type, the following is an error even though both types implement `Bar`:

```rust
fn f(a: bool) -> impl Bar {
    if a {
        Foo { ... }
    } else {
        Baz { ... }
    }
}
```

## Implementation

To choose which type to use, it is helpful to understand how the different types are implemented. Disclaimer: the compiler is pretty smart and it is possible that your code will end up looking quite different from these explanations due to optimisation.

Generic functions and impl Trait in argument position are implemented using monomorphisation. This means that the compiler makes a copy of the function for each concrete type (or combination of types) that are used to call the function. For example, if our function `fn f(b: impl Bar)` is called with both `Foo` and `Baz` values, then the compiler will make two copies of the function, one which takes `b: Foo` and one which takes `b: Baz`.

Consequently, a call to a generic function does not require any indirection, it is a simple function call. However, the function code is duplicated, potentially many times.

impl Trait in return position does not need monomorphisation, the abstract type can simply be replaced with the concrete type in the calling code.

Using trait objects does not require monomorphisation because a function taking a trait object is not a generic function, it only takes a single type. Trait objects themselves are implemented as *fat pointers*. That means that a type like `&dyn Bar` is not just a pointer to a value, but is two pointers passed around together (or in a trench coat, if you like): one pointer to the value and one pointer to a vtable which is used to map the methods declared in the trait into methods on the concrete type.

This means that calling a function on a trait object involves an indirection via the vtable, i.e., a dynamic dispatch rather than a simple function call.

## Choosing impl Trait or dyn Trait

We have two different types with some similar properties, so how do you choose which to use?

Like most things in software engineering, there is a trade-off:

Advantages of impl Trait or generics:

- fine-grained control of properties of types using `where` clauses,
- can have multiple trait bounds (e.g., `impl (Foo + Qux)` is allowed, but `dyn (Foo + Qux)` is not),

Disadvantages of impl Trait or generics:

- monomorphisation causes increased code size.

Advantages of dyn Trait:

- a single variable, argument, or return value can take values of multiple different types.

Disadvantages of dyn Trait:

- virtual dispatch means slower method calls,
- objects must always be passed by pointer,
- requires object safety.

### Object safety

Not all traits can be made into trait objects, only those which are [object safe](https://rust-lang.github.io/rfcs/0255-object-safety.html). Object safety exists so that trait objects can satisfy trait bounds, in other words so that you can pass an object of type `&dyn Foo` to a function expecting `&impl Foo`. This might seem trivial, but it isn't. Effectively, there is an implicit impl `impl<T: Trait> T for dyn T {...}` for all traits; note that the ellipsis here is doing a lot of work, every method must be implemented for every type to delegate to the trait object.

If you were to write out this impl you'd find that it could not be written without errors for some traits. Roughly, object safety is a conservative measure of the traits for which the impl could be written without errors.

A trait is object safe if it is not bound by `Sized` (e.g, `trait Foo: Sized`) and for all methods in the trait which do not have `Self: Sized` in their `where` clause:

- the method is not static (i.e., it has a `self` argument of some kind),
- the method does not use `Self` in an argument or return type,
- the method has no type parameters.

### Implicit bounds

Auto traits (previously called OIBITs) are traits like `Send` and `Sync` which do not need to be explicitly implemented, but are implemented by default if all components of a type implement that trait.

When `impl Trait` is used in return position (but not argument position) auto traits will be implicitly inferred for the return value from the function body. That means you never need to write `+ Send + Sync` on `impl Trait` in return position. This is not the case with trait objects, where you must include the auto traits.

Lifetime bounds are even more subtle. `dyn Trait` includes a default lifetime bound of `'static` (unless you specify a lifetime). Type parameters and `impl Trait` in argument position have no implicit lifetime bound. The concrete type behind `impl Trait` can depend on any type parameters in scope. Therefore, any bound on any type-parameter in scope becomes a bound on the `impl Trait` type (as well as any explicit lifetime bounds, e.g., `'a` in `impl (Foo + 'a)`). If there are no lifetimes in scope via explicit bounds or type parameters, then `impl Trait` has a `'static` bound (c.f., generic types which would have no bounds).

Is that clear? Honestly it is not completely clear to me, so I may have made a mistake here. I doubt this will cause you much trouble in your Rust programming career, however.

### impl Trait in traits

It is not allowed to use `impl Trait` as a return type on a trait method. There are both theoretical issues (it lets you simulate higher kinded types, and the interactions with any future higher kinder types in Rust might be complex) and implementation issues. However, you can use `impl Trait` to instantiate an associated type, then use the associated type as a return type, thus getting some of the abstraction benefits in a trait impl, e.g.,

```rust
trait Qux {
    type T;
    
    fn qux(&self) -> Self::T;
}

impl Qux for Foo {
    type T = impl Bar;

    fn qux(&self) -> Self::T {
        ...
    }
}
```

`impl Trait` in associated types is an unstable feature, you'll need to use the `type_alias_impl_trait` feature attribute.

You can also use `impl Trait` in type aliases using the same feature. This is a really powerful feature since it lets you express that two types which are `impl Trait` types hide the same underlying type, but that stuff deserves a blog post all of its own.

### Pre-2018 edition

If you read older Rust code, you may see trait object types without the `dyn` (e.g., `&Bar`). This is an older syntax and you should avoid it in new code. It was deprecated as part of the 2018 edition of Rust.

RFCs:

- [impl Trait (return position)](https://rust-lang.github.io/rfcs/1522-conservative-impl-trait.html)
- [impl Trait (argument position, refinements)](https://rust-lang.github.io/rfcs/1951-expand-impl-trait.html)
- [dyn Trait](https://rust-lang.github.io/rfcs/2113-dyn-trait-syntax.html)
- [finalisation of impl Trait and dyn Trait](https://rust-lang.github.io/rfcs/2250-finalize-impl-dyn-syntax.html)
- [impl Trait in associated types and type aliases](https://rust-lang.github.io/rfcs/2515-type_alias_impl_trait.html)

Other:

- [Aaron's blog post](http://aturon.github.io/blog/2015/09/28/impl-trait/)
- 2018 Edition book: [impl Trait](https://doc.rust-lang.org/edition-guide/rust-2018/trait-system/impl-trait-for-returning-complex-types-with-ease.html) and [dyn Trait](https://doc.rust-lang.org/edition-guide/rust-2018/trait-system/dyn-trait-for-trait-objects.html)
- [The Rust book](https://doc.rust-lang.org/book/ch10-02-traits.html#traits-as-parameters) (and following sections)
- The Rust reference: [dyn Trait](https://doc.rust-lang.org/reference/types/trait-object.html) and [impl Trait](https://doc.rust-lang.org/reference/types/impl-trait.html).