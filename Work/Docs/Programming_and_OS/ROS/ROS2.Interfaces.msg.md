---
tags: note/ROS
type: note
---
# Background
- Simple text files that describe the fields of a ROS message
- Used to generate source code for messages in different languages

# Message Description 
- Described and defined in the `msg/` directory of a ROS package

## Fields
- Each field consists of a type and a name, separated by a space
- Field types can be:
	- A built-in type
	- Names of message descriptions described on their own (i.e. `geometry_msgs/PoseStamped`)
```msg
fieldtype1 fieldname1
fieldtype2 fieldname2
fieldtype3 fieldname3
```
### Example
```msg
int32 my_int
string my_string
```


### Field types
| Type name | [C++](https://design.ros2.org/articles/generated_interfaces_cpp.html) | [Python](https://design.ros2.org/articles/generated_interfaces_python.html) | [DDS type](https://design.ros2.org/articles/mapping_dds_types.html) |
| --------- | --------------------------------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| bool      | bool                                                                  | builtins.bool                                                               | boolean                                                             |
| byte      | uint8_t                                                               | builtins.bytes*                                                             | octet                                                               |
| char      | char                                                                  | builtins.str*                                                               | char                                                                |
| float32   | float                                                                 | builtins.float*                                                             | float                                                               |
| float64   | double                                                                | builtins.float*                                                             | double                                                              |
| int8      | int8_t                                                                | builtins.int*                                                               | octet                                                               |
| uint8     | uint8_t                                                               | builtins.int*                                                               | octet                                                               |
| int16     | int16_t                                                               | builtins.int*                                                               | short                                                               |
| uint16    | uint16_t                                                              | builtins.int*                                                               | unsigned short                                                      |
| int32     | int32_t                                                               | builtins.int*                                                               | long                                                                |
| uint32    | uint32_t                                                              | builtins.int*                                                               | unsigned long                                                       |
| int64     | int64_t                                                               | builtins.int*                                                               | long long                                                           |
| uint64    | uint64_t                                                              | builtins.int*                                                               | unsigned long long                                                  |
| string    | std::string                                                           | builtins.str                                                                | string                                                              |
| wstring   | std::u16string                                                        | builtins.str                                                                | wstring                                                             | 

|Type name|[C++](https://design.ros2.org/articles/generated_interfaces_cpp.html)|[Python](https://design.ros2.org/articles/generated_interfaces_python.html)|[DDS type](https://design.ros2.org/articles/mapping_dds_types.html)|
|---|---|---|---|
|static array|std::array<T, N>|builtins.list*|T[N]|
|unbounded dynamic array|std::vector|builtins.list|sequence|
|bounded dynamic array|custom_class<T, N>|builtins.list*|sequence<T, N>|
|bounded string|std::string|builtins.str*|string|
