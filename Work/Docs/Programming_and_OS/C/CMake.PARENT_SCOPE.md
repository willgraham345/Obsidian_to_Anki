---
type: note
---
# Background
Option from the [[CMake.set]] command that sets a variable in the parent scope. 

# Usage
```cmake
function(foo)
  message(${test}) # test is 1 here
  set(test 2 PARENT_SCOPE)
  message(${test}) # test still 1 in this scope
endfunction()

set(test 1)
foo()
message(${test}) # test will now be 2 here
```