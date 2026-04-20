---
type: note/function
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Wednesday, January 8th 2025, 2:50:29 pm
function_of:
  - "[[Rust std String]]"
---
# Usage

### String Creation and Conversion Functions

|Function|Description|
|---|---|
|`String::from("some string")`|Creates a new `String` from a string literal.|
|`String::new()`|Creates a new empty `String`.|
|`String::from_utf8_lossy()`|Converts a slice of bytes (`&[u8]`) to a `String`, replacing invalid UTF-8 sequences with replacement characters.|
|`str::to_string()`|Converts a string slice (`&str`) to a `String`.|

### String Manipulation Functions

|Function|Description|
|---|---|
|`chars()`|Returns an iterator over the characters of a `String`.|
|`insert()`|Inserts a string slice at a specified index in a `String`.|
|`push()`|Appends a single character to a `String`.|
|`push_str()`|Appends a string slice to a `String`.|
|`remove()`|Removes the character at the specified index in a `String`.|
|`replace()`|Replaces all occurrences of a pattern with another string.|
|`split()`|Splits a `String` into substrings based on a delimiter.|
|`to_lowercase()`|Converts all characters in a `String` to lowercase.|
|`to_uppercase()`|Converts all characters in a `String` to uppercase.|
|`trim()`|Removes leading and trailing whitespace from a `String`.|

### String Searching and Matching Functions

|Function|Description|
|---|---|
|`contains()`|Checks if a `String` contains a substring.|
|`ends_with()`|Checks if a `String` ends with a specified suffix.|
|`find()`|Finds the first occurrence of a substring in a `String`, returning its index.|
|`matches()`|Returns an iterator over the substrings of a `String` that match a given pattern.|
|`rfind()`|Finds the last occurrence of a substring in a `String`, returning its index.|
|`split_whitespace()`|Splits a `String` into substrings at whitespace boundaries.|
|`starts_with()`|Checks if a `String` starts with a specified prefix.|

### String Formatting and Display Functions

|Function|Description|
|---|---|
|`eprint!()`|Prints formatted strings to the standard error.|
|`format!()`|Formats strings with similar syntax to `println!`.|
|`format_args!()`|Builds a `fmt::Arguments` structure for later use in printing.|
|`println!()`|Prints formatted strings to the standard output.|
|`std::fmt::Debug`|Trait for string formatting with the `{:?}` marker.|
|`std::fmt::Display`|Trait for string formatting with the `{}` marker.|
|`write!()`|Writes formatted data into a buffer.|
