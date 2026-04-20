---
type: note
associations: ["[[Cpp For Loops]]"]
concept_of: ["[[Cpp Control Flow]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, May 30th 2025, 4:37:49 pm
---
# Syntax
## Inifinite Loops
```cpp
int alarm = 9;  
while (alarm > 8) {  
  std::cout << "ding\n";  
}
```
- you could also write `while True{}`
- This would not one time if `alarm < 8`

## While Loops
```cpp
int price = 300;  
do {  
  std::cout << "Too expensive!";  
} while (price > 500);
```
Executes only one time