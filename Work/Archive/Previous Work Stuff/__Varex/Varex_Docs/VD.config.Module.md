---
company: Varex
tags:
  - archive_deprecated/Varex
  - archive_deprecated/Varex/config
---
# Background

## Concepts
### Concepts
### Formats
#### Integer On-Disk Format
- All tokens and integers are stored as 32 bit big endian integers
- Reading (parsing) of config files on a little endian platform the bytes within a 32 bit integer must be swapped so the correct values will be interpreted. 

#### String (byte array)
- [Read here](http://slfpbuildmstr.vic.ad.vareximaging.com/jenkins/static-files/_Gj9YuRhNL2Ep7ZvxYfelcNE8xfUzObJvaGtI7KuIzF3aTk5NDI2OToxNzE4MTM0NTQ0MjI1OnZpZXcvVG9vZWxlL2pvYi9Ub29lbGUtQ29uZmlnL2xhc3RTdWNjZXNzZnVsQnVpbGQvYXJ0aWZhY3Q=/doxygen/html/index.html)

### Scope
#### System scope
Token-value pairs that apply to all of the modules

#### Mode level scope
- Bounded in input stream by a begin and end mode tokens. 
- All token-value pairs (properties) between those tokens correspond to the mode identified by the index of stream placement
- First mode is index 0, each successive mode after is incremented by 1, until we're done parsing. 

### Serialized Registers
Control methods can give access to the individual controls. 

#### Standard Configuration
#### Modular Configuration
Modular configurations have a module global and modular mode registers

##### Types of Registers
Registers come in 2 distinct types within this configuration:
- UDR = Universal defined register
	- Defined at the module scope and apply to all the modular modes within the module
- mode registers
	- Only apply within the scope of the module to which they belong

### Module Properties
Has the following properties
```
Type: (uint32)
Number of instance(s): (uint8)
Major Version Number: (uint8)
Minor Version Number: (uint8)
Description: (string)
```

### Tokens
Tokens are stored in a database table in order to use them
- For any applications that are for customers or are to be distributed these must be compiled prior to distribution. 
- Method to do this is by using the old XConfigure app.
	- This generates an unordered map of the tokens (new) or a `tokens.h` (old) file which can be included in your project for compilation. 
		- New method gets a complete token structure rather than a `#define`, so you can have greater verification. 
		- 

### Modular Configuration
For better OOP design, the idea was to keep properties contained within the areas that needed them, and isolate them from scopes that don't need them. 
- Centered around firmware, but used in software too.
- ![[VD.config.general.terminology.2024-06-18.10.59.25.excalidraw| 250]]
	- Properties are encapsulated around the areas that need them. 

### Modular controls
Module registers & Modular Mode registers. These are 32bit unsigned offsets, with accompanying 32bit unsigned values.
`1104 = MODULE_NUM_REGISTERS`
`1200 = MODULAR_MODE_REGISTERS`

# Usage