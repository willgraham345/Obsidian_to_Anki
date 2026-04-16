---
type: note
---
# Background
[Good guide on Best Practice](https://gist.github.com/mbinna/c61dbb39bca0e4fb7d1f73b0d66a4fd1)
## Modern CMake configuration
### DO NOT
- Use at least CMake version 3.0.0
- Treat CMake like production code. CMake is code, treat it like that. 
- Define project properties globally. 
- Do *not* use the following commands
	- `add_compile_options`, `include_directories`, `link_directories`, `link_libraries` as they work on the directory level. This increases the chance of hidden dependencies.
- Don't touch `CMAKE_CXX_FLAGS`
- 
