---
summary: How to implement an interface for different structs, which can be implemented on top of an existing struct. <br><br>Traits are "added" to the trait itself by an `impl` block.
headings: ["[[#Concepts of Note]]", "[[#Examples]]"]
type: note/concept
similar: ["[[Rust function traits and generics]]"]
associations: ["[[Rust impl]]"]
concept_of: ["[[Rust Generics]]", "[[Rust Structs]]", "[[Rust trait]]"]
date created: Friday, April 4th 2025, 3:34:22 pm
date modified: Monday, April 28th 2025, 1:25:42 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
```rust
struct Point_int32
struct Point_int64
```
:FasArrowDownLong: Simplifies towards...
```rust
struct Point<T> {
	x: T,
	y: T,
}
```

## Examples
### Default Implementations
```rust
pub trait Summary {
	fn summarize(&self) -> String {
		String::from("(Read more...)")
	}
	fn summarize_author(&self) -> String;
}

pub struct Tweet {
	pub username: String,
	pub content: String,
	pub reply: bool,
	pub retweet: bool,
}
impl Summary for Tweet {
    fn summarize_author(&self) -> String {
        format!("@{}", self.username)
    }
}
```

### Trait bound syntax
```rust
pub fn notify(item: &impl Summary) {
    println!("Breaking news! {}", item.summarize());
}
// OR
pub fn notify<T: Summary>(item: &T) {
    println!("Breaking news! {}", item.summarize());
}
```

### Less Important Examples
#### Specific Traits
```rust
pub trait Summary {
    fn summarize(&self) -> String;
}

pub struct NewsArticle {
    pub headline: String,
    pub location: String,
    pub author: String,
    pub content: String,
}

impl Summary for NewsArticle {
    fn summarize(&self) -> String {
        format!("{}, by {} ({})", self.headline, self.author, self.location)
    }
}

pub struct Tweet {
    pub username: String,
    pub content: String,
    pub reply: bool,
    pub retweet: bool,
}

impl Summary for Tweet {
    fn summarize(&self) -> String {
        format!("{}: {}", self.username, self.content)
    }
}
```

#### Multiple Generics
```rust
struct Point<T, U> {
	x: T,
	y: U,
}
fn main() {
	let int_float_combo_point = Point { x: 5, y: 4.0 }
}
```

#### Implement a Generic on a Struct Method
```rust
struct Point<T> {
    x: T,
    y: T,
}

impl<T> Point<T> {
    fn x(&self) -> &T {
        &self.x
    }
}

fn main() {
    let p = Point { x: 5, y: 10 };

    println!("p.x = {}", p.x());
}

```
- `p.x()` is now a method that returns a reference to the field at `p.x` 

##### Implementing a Specific Type
```rust
impl Point<f32> {
    fn distance_from_origin(&self) -> f32 {
        (self.x.powi(2) + self.y.powi(2)).sqrt()
    }
}
```