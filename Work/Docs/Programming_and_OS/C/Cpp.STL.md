---
components: ["[[Cpp.Smart Pointers]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, November 5th 2024, 10:06:01 am
type: note
---
# Background
- STL is a collection of C++ classes that provide common data structures (lists, stacks, arrays, etc.) and has containers for algorithms and iterators. 
	- A subset of the std library

|STD|STL|
|---|---|
|Std stands for standard|Stl stands for standard template library|
|Std falls under the standard C++ Library|Stl is a subset of std|
|All libraries fall under std.|There are 4 categories of stl:<br><br>- Algorithms<br>- Functions.<br>- Iterators<br>- Containers.|
|Space resolution operator is used(::)|No operator is used|
|**Examples:** <br><br>cin, cout under iostream header|**Example:**<br><br>sort(),lower_bound().|

## Advantages/Disadvantages
### Advantages
1. Reusability: One of the key advantages of the STL is that it provides a way to write generic, reusable code that can be applied to different data types. This can lead to more efficient and maintainable code.
2. Efficient algorithms: Many of the algorithms and data structures in the STL are implemented using optimized algorithms, which can result in faster execution times compared to custom code.
3. Improved code readability: The STL provides a consistent and well-documented way of working with data, which can make your code easier to understand and maintain.
4. Large community of users: The STL is widely used, which means that there is a large community of developers who can provide support and resources, such as tutorials and forums.

### Disadvantages
1. Learning curve: The STL can be difficult to learn, especially for beginners, due to its complex syntax and use of advanced features like iterators and function objects.
2. Lack of control: When using the STL, you have to rely on the implementation provided by the library, which can limit your control over certain aspects of your code.
3. Performance: In some cases, using the STL can result in slower execution times compared to custom code, especially when dealing with small amounts of data.