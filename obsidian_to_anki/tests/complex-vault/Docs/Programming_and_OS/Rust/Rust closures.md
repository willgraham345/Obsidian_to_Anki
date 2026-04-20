---
summary: A unique anonymous type that cannot be written out. Anonymous functions you can save in a variable or pass as arguments to other functions. These can capture values from the scope in which they're defined.
headings: ["[[#Concepts of Note]]", "[[#Examples]]", "[[#Usage]]"]
type: note/item
concept_of: ["[[Rust Control Flow]]"]
date created: Wednesday, July 16th 2025, 11:49:14 am
date modified: Monday, August 11th 2025, 2:59:15 pm
item_of: ["[[Rust Variables and Type System]]"]
used_by: ["[[Rust std thread]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
󰙎  Move closure ;;; Uses data from one thread in another thread. = #lang/control_flow/closures/move #lang/memory/threading/thread  
<!--ID: 1758253288967-->

  `let a ``=`` |x| { // stuff }` ;;; Defines a partially annotated closure `a` which takes in a variable `x` with no type annotation. The type of `x` is inferred by the compiler. = #lang/control_flow/closures  
<!--ID: 1758253288932-->

  `let b ``=`` |num: u32| -> String { // stuff }` ;;; Defines a fully annotated closure `b` which takes in a `num` of type `u32`, and returns a `String`. = #lang/control_flow/closures  
<!--ID: 1758253288939-->

  `let mut c ``=`` || { count += 1; }` ;;; Define a closure `c` which increments a variable in the current scope/environment by 1. Note, this requires `count` to be a mutable variable. = #lang/control_flow/closures  
<!--ID: 1758253288946-->

  `let d ``=`` move |var| { var += 1; }` ;;; Define a closure which takes ownership of a variable `var`, and increments it 1. Note, it does not return this variable. = #lang/control_flow/closures/move  
<!--ID: 1758253288953-->

  `let one ``=`` || 1;` ;;; Defines a closure which takes in no arguments, but returns a `1`. = #lang/control_flow/closures  
<!--ID: 1758253288960-->

󰠗  How are closures stored in Rust? ;; The closures are stored in variables and used without naming them and/or exposing them to users of our library. = #lang/control_flow/closures   
󰠗  What are the three ways which closures capture values from their environment? ;; Borrowing immutably, borrowing mutably, and taking ownership. = #lang/control_flow/closures  
- [p] `let color ``= String::from("green");`
      `let print ``= || println!("color: {}", color)` = 

## Usage

## Examples
### T shirt giveaway by color
- A company is giving away t shirts as promotion. If a customer has their favorite color selected, they get that shirt. If they don't, they get the color the company has the most of in stock.
```rust
#[derive(Debug, PartialEq, Copy, Clone)]
enum ShirtColor {
    Red,
    Blue,
}

struct Inventory {
    shirts: Vec<ShirtColor>,
}

impl Inventory {
    fn giveaway(&self, user_preference: Option<ShirtColor>) -> ShirtColor {
        user_preference.unwrap_or_else(|| self.most_stocked())
    }

    fn most_stocked(&self) -> ShirtColor {
        let mut num_red = 0;
        let mut num_blue = 0;

        for color in &self.shirts {
            match color {
                ShirtColor::Red => num_red += 1,
                ShirtColor::Blue => num_blue += 1,
            }
        }
        if num_red > num_blue {
            ShirtColor::Red
        } else {
            ShirtColor::Blue
        }
    }
}

fn main() {
    let store = Inventory {
        shirts: vec![ShirtColor::Blue, ShirtColor::Red, ShirtColor::Blue],
    };

    let user_pref1 = Some(ShirtColor::Red);
    let giveaway1 = store.giveaway(user_pref1);
    println!(
        "The user with preference {:?} gets {:?}",
        user_pref1, giveaway1
    );

    let user_pref2 = None;
    let giveaway2 = store.giveaway(user_pref2);
    println!(
        "The user with preference {:?} gets {:?}",
        user_pref2, giveaway2
    );
}
```
