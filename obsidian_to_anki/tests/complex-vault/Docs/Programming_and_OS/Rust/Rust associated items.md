---
summary: Associated types move inner types locally into a trait as output types, improving readability.<br><br>Associated items are declared in traits, or defined in impl statements. It provides simpler usage pattern when the trait is generic over its container type. As the name suggests, an associated item is an item.
headings:
  - "[[#Concepts of Note]]"
  - "[[#Examples]]"
  - "[[#Syntax]]"
type: note/concept
concept_of:
  - "[[Rust Items]]"
date created: Thursday, May 1st 2025, 9:06:03 pm
date modified: Tuesday, July 22nd 2025, 1:41:12 pm
items: 
used_by:
  - "[[Rust Items]]"
  - "[[Rust trait]]"
similar:
  - "[[Rust associated types]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
󰠗  What is the difference between an associated function, and a method? ;; A method will have `self` as its first parameter. May be invoked using `x.foo()` as well as the typical function call notation. 
󰠗  Does Rust let you customize template code for a given set of template arguments? ;; No = #lang  
<!--ID: 1758253289074-->

![[Rust trait#^9617d9]]

## Examples
### This is the problem associated types solve
```rust
struct Container(i32, i32);

// A trait which checks if 2 items are stored inside of container.
// Also retrieves first or last value.
trait Contains<A, B> {
	// Define generic types here which methods will be able to utilize.
    type A;
    type B;
    fn contains(&self, _: &A, _: &B) -> bool; // Explicitly requires `A` and `B`.
    fn first(&self) -> i32; // Doesn't explicitly require `A` or `B`.
    fn last(&self) -> i32;  // Doesn't explicitly require `A` or `B`.
}

impl Contains<i32, i32> for Container {
    // True if the numbers stored are equal.
    fn contains(&self, number_1: &i32, number_2: &i32) -> bool {
        (&self.0 == number_1) && (&self.1 == number_2)
    }

    // Grab the first number.
    fn first(&self) -> i32 { self.0 }

    // Grab the last number.
    fn last(&self) -> i32 { self.1 }
}

// `C` contains `A` and `B`. In light of that, having to express `A` and
// `B` again is a nuisance.
fn difference<A, B, C>(container: &C) -> i32 where
    C: Contains<A, B> {
    container.last() - container.first()
}

fn main() {
    let number_1 = 3;
    let number_2 = 10;

    let container = Container(number_1, number_2);

    println!("Does container contain {} and {}: {}",
        &number_1, &number_2,
        container.contains(&number_1, &number_2));
    println!("First number: {}", container.first());
    println!("Last number: {}", container.last());

    println!("The difference is: {}", difference(&container));
}
```
- ![[associated_types.svg | 500]]
