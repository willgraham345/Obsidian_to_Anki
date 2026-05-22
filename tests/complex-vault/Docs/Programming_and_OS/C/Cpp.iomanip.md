---
type: note
classes: ["[[Cpp fstream basic_fstream]]", "[[Cpp fstream basic_fstream]]", "[[Cpp fstream basic_ifstream]]", "[[Cpp fstream basic_ofstream]]", "[[Cpp fstream filebuf]]", "[[Cpp fstream filebuf]]", "[[Cpp fstream fstream]]", "[[Cpp fstream ifstream]]", "[[Cpp fstream wfstream]]", "[[Cpp fstream wifstream]]", "[[Cpp fstream wofstream]]", "[[Cpp.fstream.ofstream]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, November 26th 2024, 2:18:05 pm
functions: ["[[Cpp iomanip  get_time]]", "[[Cpp iomanip  put_time]]", "[[Cpp iomanip get_money]]", "[[Cpp iomanip put_money]]", "[[Cpp iomanip resetiosflags]]", "[[Cpp iomanip setbase]]", "[[Cpp iomanip setiosflags]]", "[[Cpp iomanip setprecision]]", "[[Cpp iomanip setw]]"]
---
# Background
- Header providing parametric manipulators (manipulators that take one or more parameters). 
- Manipulators are helping functions that can modify the I/O stream. Doesn't mean you change the value of a variable, it only modifies the I/O stream using insertion and extraction operators. 
Manipulator               ->          Meaning  
setw (int n)                 ->          To set field width to n  
setprecision (int p)     ->          The precision is fixed to p  
setfill (Char f)              ->          To set the character to be filled  
setiosflags (long l)      ->          Format flag is set to l  
resetiosflags (long l)   ->          Removes the flags indicated by l  
Setbase(int b)             ->          To set the base of the number to b

Parametric manipulators

[[Cpp iomanip setiosflags]]
[[Cpp iomanip resetiosflags]]
[[Cpp iomanip setbase]]
[[Cpp iomanip setprecision]]
[[Cpp iomanip setw]]
[[Cpp iomanip get_money]]
[[Cpp iomanip put_money]]
[[Cpp iomanip  get_time]]
[[Cpp iomanip  put_time]]

# Usage