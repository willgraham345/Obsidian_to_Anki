---
summary: A simpler-to-write functor (function object) useful when you'd like to perform an operation on an object in a repeatable and easy-to-define way, defined by a given capture clause. Can be thought of as temporary "classes" where the capture clause is the data, and the arguments are method inputs.<br><br>Typically used to encapsulate a few lines of code passed to algorithms or asynchronous functions. Introduced in C++ 11. Can be considered syntactic sugar over classes with the `operator()` defined.
headings: ["[[#Concepts of Note]]", "[[#Media]]", "[[#Syntax]]"]
type: note/concept
concepts: ["[[Cpp Lambda Function Capturing Variables]]"]
functions: ["[[Cpp std for each]]", "[[Cpp std transform]]"]
similar: ["[[Cpp functors]]", "[[Cpp std function (class)]]"]
concept_of: ["[[Cpp Basics]]", "[[Cpp Functions]]"]
date created: Thursday, November 21st 2024, 1:00:00 pm
date modified: Tuesday, June 17th 2025, 10:24:10 am
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Syntax
3 parts to lambda declaration:
1. Capture list (variables to be copied inside the lambda)
2. Argument list (arguments passed to lambda at execution)
3. Code 
```cpp
auto lambda = [captureList](typeArg argList) {
	// statements
	
};
```

Other options
- Type for lambdas
	- Go with `auto`, or with `std::function`. See [[#Lambda types]] for more info
- Mutability
	- See [[#Mutable lambdas]]

![[Cpp Lambda Functions.png | 300]]

## Concepts of Note
### Capture clause
Determines which variables from the surrounding scope should be accessible inside the lambda, and whether they are captured by value or by reference.

Options
- `[]`: Captures nothing.
- `[=]`: Captures all variables in the surrounding scope by value.
- `[&]`: Captures all variables in the surrounding scope by reference.
- `[x, &y]`: Captures `x` by value and `y` by reference.
- `[this]`: Capture the current class instance

### Lambda types
Lambdas each have their own unique type assigned by the compiler. You'll probably need to store them as `auto` or as templates.

This means you typically want to wrap them in [[Cpp std function (class)]] objects to make them easier to move around.

### Use cases
1. Capturing local variables to another scope (i.e. local -> global; which is not possible with normal functions)
2. Passing a function or template arguments
3. Creating function options
4. Short lived functions
5. Inline declarations

### Mutable lambdas
Lambda's `operator()` is const by default, meaning it can't modify the variables captured by value. To change that, add `mutable` to the declaration.

## Media
[Fetching Title#na1d](https://shaharmike.com/cpp/lambdas-and-functions/)
<iframe src="https://shaharmike.com/cpp/lambdas-and-functions/" style="width: 100%; height: 600px;"></iframe>

[Lambda expressions in C++ | Microsoft Learn](https://learn.microsoft.com/en-us/cpp/cpp/lambda-expressions-in-cpp?view=msvc-170)
<iframe src="https://learn.microsoft.com/en-us/cpp/cpp/lambda-expressions-in-cpp?view=msvc-170" style="width: 100%; height: 600px;"></iframe>