---
tags: note/ROS
type: note
---
# Background
ROS applications typically communicate through interface three types: topics, services, or actions.
- ROS uses a simplified description language, the interface definition language, to describe these interfaces.
- This makes it easier for ROS to automatically generate source code for the interface type in several target languages.
- Supported types:
	- msg: `.msg` files are simple text files that describe the fields of a ROS message. They are used to generate source code for messages in different languages.
	- srv: `.srv` files describe a service. They are composed of two parts: a request and a response. The request and response are message declarations.
	- action: `.action` files describe actions. They are composed of three parts: a goal, a result, and feedback. Each part is a message declaration itself.

# Commands
| Interface                 | Description                                                   |
| ------------------------- | ------------------------------------------------------------- |
| `ros2 interface list`     | List all interface types available                            |
| `ros2 interface package`  | Output a list of available interface types within one package |
| `ros2 interface packages` | Output a list of packages that provide interfaces             |
| `ros2 interface show`     | Output the interface definition                               |

## Examples
```bash
ros2 interface list
ros2 interface package std_msgs
ros2 interface packages --only-msgs
ros2 interface proto example_interfaces/srv/AddTwoInts
ros2 interface show geometry_msgs/msg/Pose
```






# Interfaces within ROS2
## Messages
A way for a ROS2 node to send data on the network to other ROS nodes, with no expected response.
- Defined in `.msg` files in the `msg/` directory of a ROS package.
	- Composed of two parts: fields and constants
### Fields
Each field consists of a type and a name separated by a space
```
fieldtype1 fieldname1
fieldtype2 fieldname2
fieldtype3 fieldname3
```
#### Example 
```
int32 my_int
string my_string
```


### Example message definition using arrays and bounded types:
```
int32[] unbounded_integer_array
int32[5] five_integers_array
int32[<=5] up_to_five_integers_array

string string_of_unbounded_size
string<=10 up_to_ten_characters_string

string[<=5] up_to_five_unbounded_strings
string<=10[] unbounded_array_of_strings_up_to_ten_characters_each
string<=10[<=5] up_to_five_strings_up_to_ten_characters_each
```

### Field Names
Must be lowercase alphanumeric characters with underscores separating words. Must start with alphabetic character, and must not end in an underscore or have two consecutive underscores.

### Field Default Value
Can be set to any field in the message type. 

```
fieldtype fieldname fielddefaultvalue

uint8 x 42
int16 y -2000
string full_name "John Doe"
int32[] samples [-200, -100, 0, 100, 200]
```


### Constants
Each constant definition is like a field definition with a default value, except that this value can never be changed programatically
Constant names must be UPPERCASE
```
constanttype CONSTANTNAME=constantvalue
```

```
int32 X=123
int32 Y=-123
string FOO="foo"
string EXAMPLE='bar'
```
## Services
Services are a request/response communication
- Client (requester) waits for the server (responder) to make a short computation and return a result
- Defined in a `.srv` file in the `srv/` directory of a ROS package

### Example for a service that takes in a string and returns a string
```
string str
---
string str
```
### Additional Example
```
# request constants
int8 FOO=1
int8 BAR=2
# request fields
int8 foobar
another_pkg/AnotherMessage msg
---
# response constants
uint32 SECRET=123456
# response fields
another_pkg/YetAnotherMessage val
CustomMessageDefinedInThisPackage value
uint32 an_integer
```


## Actions
Actions are long-running request/response communications, where the action client (requester) is waiting for the action server (the responder) to take some action and result a result. 
- Can last many seconds or minutes
### Basic Form of Actions
```
<request_type> <request_fieldname>
---
<response_type> <response_fieldname>
---
<feedback_type> <feedback_fieldname>
```
- request fields are before, response fields are after the triple dash
- there can be an arbitrary number of request fields (including zero), arbitrary number of response fields (including zero), and arbitrary numbers of feedback files (including zero)










