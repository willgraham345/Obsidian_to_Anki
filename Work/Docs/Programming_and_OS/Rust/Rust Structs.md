---
summary: Similar to tuples, but values here can be different types. Values also must be named. Entire instance must be mutable, but you can construct structs with functions for immutable values.<br><br>Implementations are used as a way to define shared behavior of a trait onto a struct, and you can have as many `impl`s as you want.
headings:
  - "[[#Examples]]"
  - "[[#Syntax]]"
  - "[[#Usage]]"
type: note
up:
  - "[[Rust Basics]]"
concepts:
  - "[[Rust Structs Debug]]"
  - "[[Rust Structs Ownership]]"
  - "[[Rust struct traits and generics]]"
similar:
  - "[[Rust Tuples]]"
associations:
  - "[[Rust impl]]"
concept_of:
  - "[[Rust Basics]]"
date created: Tuesday, August 20th 2024, 2:05:35 pm
date modified: Monday, April 28th 2025, 12:46:36 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Usage
```rust
struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}
```

## Examples
### [[DP Builder]] with `impl`
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

