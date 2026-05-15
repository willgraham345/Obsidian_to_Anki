---
type: note
---
# Background
- Reads data from the stream and stores them into parameter format into locations provided by the additional arguments. 
- Additional arguments should point to already allocated objects of the type specified by their corresponding format specifier within the format string.

# Usage
```cpp
int fscanf (FILE * stream, const char * format, ...)
```
- `stream` = pointer to a [[Cpp stdio FILE]] object that identifies the input stream to read data from. 
- `format` = C string that contains a sequence of characters that control how characters extracted from the stream are treated. 
	- LOTS of documentation on this one, read more [here](https://cplusplus.com/reference/cstdio/fscanf/)