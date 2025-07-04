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
- [p] `partial_location /= "end_path.txt"` = Append to `std::filesystem::path` object (i.e. `c:\test\` -> `c:\test\end_path.txt`) = #code/cpp/variables/filepath/append
<!--ID: 1751434091527-->

- [p] `location.filename().string()` = Access filename member of a `std::filesystem::path` object = #code/cpp/variables/filepath
<!--ID: 1751434091531-->

- [p] `location.stem().string()` = Access stem member of a `std::filesystem::path` object. (i.e. `c:\test\hello.txt` -> `hello`) = #code/cpp/variables/filepath
<!--ID: 1751434091534-->

- [p] `location.extension().string()` = Access extension member of a `std::filesystem::path` object. (i.e. `c:\test\hello.txt` -> `.txt`) = #code/cpp/variables/filepath
<!--ID: 1751434091538-->

- [p] `location.parent_path().string()` = Access parent path of a `std::filesystem::path` object. (i.e. `c:\test\hello.txt` -> `c:\test`) = #code/cpp/variables/filepath
<!--ID: 1751434091542-->

- [p] `location.root_name().string()` = Access root name of a `std::filesystem::path` object. (i.e. `c:\test\hello.txt` -> `c:`) = #code/cpp/variables/filepath
<!--ID: 1751434091546-->

- [p] `path.replace_extension("doc");` = Replace extension of `std::filesystem::path` object. (i.e. `c:\test\hello.txt` -> `c:\test\hello.doc`) = #code/cpp/variables/filepath 
<!--ID: 1751434091550-->

- [p] `path.replace_filename("world.txt");` = Replace extension of `std::filesystem::path` object. (i.e. `c:\test\hello.txt` -> `c:\test\world.txt`) = #code/cpp/variables/filepath 
<!--ID: 1751434091554-->

- [p] `if (A.is_absolute())` = Check if a `std::filesystem::path` object `A` is absolute (will output true if it is) = #code/cpp/variables/filepath/relative_absolute
<!--ID: 1751434091558-->

- [p] `if (A.is_relative())` = Check if a `std::filesystem::path` object `A` is relative (will output true if it is) = #code/cpp/variables/filepath/relative_absolute
<!--ID: 1751434091562-->

- [p] `if (A.exists())` = Check if a `std::filesystem::path` object `A` exists (will output true if file exists) = #code/cpp/variables/filepath/exists  
<!--ID: 1751434091566-->

![[Cpp std current_path#^86329e]]
### Appending
`/=` Appends elements *with* a directory separator
`+=` Appends elements without a directory separato