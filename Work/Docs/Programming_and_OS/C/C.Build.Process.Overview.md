---
type: note
---
Intermediate steps can be seen based on the debugger/build IDE
## Preprocessing
- `#include` and  macros are resolved
- `.i` files created
	- Generated internally, usually not for the user
## Compilation  
### Parsing
- Processes the `.i` files, checking syntaxes. Assuming no errors, this will be passed to the code generator
### Code generator
- creates `.s` files
	- Usually generated internally, and not for the user
- Higher level language is converted to lower level language like assembly mnemonics. 
### Assembler
- Converts stuff into a `.o` file, which is a relocatable object file
## Linking
Additional Info on linking found in [[C.Linker]]
### Linking
- Linking object file
- Each `.o` file will be combined into one executable file
- `.a` files are other libraries (std and/or third party ex. `.libc`)
### Producing final executable
- Creates the debug file `.elf`
- GCC files will create the executable and debug (`.elf`)
## Post processing
- `.bin` and `.exe`



# Analyzing an Executable 
- 

