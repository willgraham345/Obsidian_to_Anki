---
summary: Represents a path, which can be abstracted away from an operating system. It's also much nicer than working with strings.
headings: ["[[#Concepts of Note]]", "[[#Syntax]]", "[[#Usage]]"]
type: note/class
associations: ["[[Cpp std current_path]]"]
date created: Wednesday, May 14th 2025, 4:35:24 pm
date modified: Wednesday, May 14th 2025, 4:55:14 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[std::filesystem::path - cppreference.com](https://en.cppreference.com/w/cpp/filesystem/path)

## Concepts of Note
## Syntax
### Creating objects
```cpp
std::filesystem::path location{R"c:\test"};
std::cout << location.string(); //Outputs location
```

### Components
## Usage
  `loc /= "end_path.txt"` ;;; Append `“end_path.txt”`  to `std::filesystem::path` object `loc` (i.e. `c:\test\` -> `c:\test\end_path.txt`) = #lang/data/filepath/append 
ID: 1751997629540



  `location.filename().string()` ;;; Access filename member of a `std::filesystem::path` object = #lang/data/filepath 
ID: 1751997629545



  `location.stem().string()` ;;; Access stem member of a `std::filesystem::path` object. (i.e. `c:\test\hello.txt` -> `hello`) = #lang/data/filepath 
ID: 1751997629549



  `location.extension().string()` ;;; Access extension member of a `std::filesystem::path` object. (i.e. `c:\test\hello.txt` -> `.txt`) = #lang/data/filepath 
ID: 1751997629554



  `location.parent_path().string()` ;;; Access parent path of a `std::filesystem::path` object. (i.e. `c:\test\hello.txt` -> `c:\test`) = #lang/data/filepath 
ID: 1751997629558



  `location.root_name().string()` ;;; Access root name of a `std::filesystem::path` object. (i.e. `c:\test\hello.txt` -> `c:`) = #lang/data/filepath 
ID: 1751997629562



  `path.replace_extension("doc");` ;;; Replace extension of `std::filesystem::path` object. (i.e. `c:\test\hello.txt` -> `c:\test\hello.doc`) = #lang/data/filepath  
ID: 1751997629566



  `path.replace_filename("world.txt");` ;;; Replace extension of `std::filesystem::path` object. (i.e. `c:\test\hello.txt` -> `c:\test\world.txt`) = #lang/data/filepath  
ID: 1751997629570



  `A.is_absolute()` ;;; Method to determine if a `std::filesystem::path` object `A` is absolute (will output true if it is). = #lang/data/filepath/relative_absolute 
ID: 1751997629574



  `if (A.is_relative())` ;;; Methods to check if a `std::filesystem::path` object `A` is relative (will output true if it is). = #lang/data/filepath/relative_absolute 
ID: 1751997629578



  `if (A.exists())` ;;; Check if a `std::filesystem::path` object `A` exists (will output true if file exists) = #lang/data/filepath/exists   
ID: 1751997629582



![[Cpp std current_path#^86329e]]
### Appending
`/=` Appends elements *with* a directory separator
`+=` Appends elements without a directory separato
