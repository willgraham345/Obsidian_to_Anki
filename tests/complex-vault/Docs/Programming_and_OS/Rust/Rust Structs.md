---
summary: Similar to tuples, but values here can be different types. Values also must be named. Entire instance must be mutable, but you can construct structs with functions for immutable values.<br><br>Implementations are used as a way to define shared behavior of a trait onto a struct, and you can have as many `impl`s as you want.
headings: ["[[#Concepts of Note]]", "[[#Examples]]", "[[#Syntax]]", "[[#Usage]]"]
type: note/item
up: ["[[Rust Basics]]"]
concepts: ["[[Rust struct traits and generics]]", "[[Rust Structs Debug]]", "[[Rust Structs Ownership]]"]
similar: ["[[Rust Tuples]]"]
concept_of: ["[[Rust Basics]]"]
date created: Tuesday, August 20th 2024, 2:05:35 pm
date modified: Wednesday, July 16th 2025, 11:26:49 am
uses: ["[[Rust impl]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
󰠗  What are the three types of structs? ;; Tuple structs (unnamed fields, just a collection of data), and struct structs (named fields), and unit structs (field-less, and useful in generics). = #lang/oop/struct #lang/oop/struct/tuple_struct  
<!--ID: 1758253288345-->

󰠗  How do you make sure that a struct has a particular field and/or type? ;; Add a generic parameter to its declaration, which will require the struct to use it. This is  

### Types of Structs
There are 3 types of structures that can be created using the `struct` keyword
- Tuple structs (named tuples)
- Classic C structs
- Unit structs, which are field-less, are useful for generics

## Usage
- [p] `struct A{`
      `active: bool,`
      `username: String`
      `}` = Creates struct `A`, with a `bool` active field, and a `String` username field. = #lang/oop/struct 
- [p] `struct A(`
      `bool,`
      `String`
      `}` = Creates tuple struct `A`, with a `bool` field, then a `String` field. = #lang/oop/struct/tuple_struct 
- [p] `struct A<BigTrait: B>{`
      `B`
```rust
struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}
```

## Examples
### [[Builder]] with `impl`
- Nothing special about `new`, but `new` may be the constructor name chosen.
```rust
struct tree{
	leaf: isize,
	branch: Vec<i32>
}
impl tree{
	pub fn new(nums: &Vec<i32>) -> Self{
		let leaf: sizes = nums.len()
		Self{
			leaf: sizes
			branch: nums
		}
	}
}
```

## Syntax
You can define structs without fields
- *Unit-like* structs
- Useful when you need to implement a trait on some type but don't have any data you want to store in the type itself

### Definition
- Key value pairs
```rust
let user1 = User{
	active: true,
	username: String::from("someusername123"),
	email: String::from("someone@example.com"),
	sign_in_count: 1,
};
```

#### Definition with `impl`
- See [[#DP Builder with `impl`]]

### Indexing/access 
```rust
user1.email = String::from("anotheremail@example.com");
```

### Tuple Structs
- They have the types of the fields. Useful when you want to give the whole tuple a name and make the tuple a different type from other tuples.
- Rust supports structs that look like tuples.
- Have the added meaning the struct name provides, but don't have names associated with their fields.
```rust
struct Color(i32, i32, i32);
struct Point(i32, i32, i32);

fn main() {
    let black = Color(0, 0, 0);
    let origin = Point(0, 0, 0);
}
```

### Building a struct with immutable fields
```rust
fn build_user(email: String, username: String) -> User {
    User {
        active: true,
        username: username,
        email: email,
        sign_in_count: 1,
    }
}
```

### Creating Instances from Other Instances with Struct Update Syntax
### Struct update status
```rust
let user2 = User {
	email: String::from("another@example.com"),
	..user1
};
```
- The `..` says that the other fields not explicitly set should have the same value as the other fields.
- This uses the `=` syntax, because it moves the data like in [[Rust String Move]]

