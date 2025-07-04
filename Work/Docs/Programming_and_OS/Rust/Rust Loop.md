---
type: note/concept
concept_of: ["[[Rust Control_Flow]]"]
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Monday, March 31st 2025, 11:54:28 am
---
# Background
- `loop` tells Rust to execute a block of code over and over again forever or until you tell it to stop.

# Usage
## Unconditional Loops
### Infinite Loop
```rust
fn main() {
    loop {
        println!("again!");
    }
}
```

### Returning Values from Loops
```rust
fn main() {
    let mut counter = 0;

    let result = loop {
        counter += 1;

        if counter == 10 {
            break counter * 2;
        }
    };

    println!("The result is {result}");
}
```

### Loop Labels to Disambiguate Between Multiple Loops
```rust
fn main() {
    let mut count = 0;
    'counting_up: loop {
        println!("count = {count}");
        let mut remaining = 10;

        loop {
            println!("remaining = {remaining}");
            if remaining == 9 {
                break;
            }
            if count == 2 {
                break 'counting_up;
            }
            remaining -= 1;
        }

        count += 1;
    }
    println!("End count = {count}");
}
```

## Conditional Loops
### Basic
```rust
fn main() {
    let mut number = 3;

    while number != 0 {
        println!("{number}!");

        number -= 1;
    }

    println!("LIFTOFF!!!");
}
```

### Looping through a Collection
```rust
fn main() {
    let a = [10, 20, 30, 40, 50];
    let mut index = 0;

    while index < 5 {
        println!("the value is: {}", a[index]);

        index += 1;
    }
}
```