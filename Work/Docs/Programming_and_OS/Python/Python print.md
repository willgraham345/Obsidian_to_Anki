---
tags: note/python
type: note
---
# Background
- Hugely useful tool to print values to a stream or to `sys.stdout` 
- Can be very useful when debugging programs.

# Usage
## Syntax
```python
print_(object(s)_, sep=_separator_, end=_end_, file=_file_, flush=_flush_)
```

| Parameter         | Description                                                                                           |
| ----------------- | ----------------------------------------------------------------------------------------------------- |
| _object(s)_       | Any object, and as many as you like. Will be converted to string before printed                       |
| sep='_separator_' | Optional. Specify how to separate the objects, if there is more than one. Default is ' '              |
| end='_end_'       | Optional. Specify what to print at the end. Default is '\n' (line feed)                               |
| _file_            | Optional. An object with a write method. Default is sys.stdout                                        |
| _flush_           | Optional. A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False |
