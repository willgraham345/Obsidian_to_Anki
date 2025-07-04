---
summary: Template that provides hash functions for a variety of types. Lets you use hash-based data structures like unordered_map and unordered_set.
type: 
similar: ["[[PT Hash Table]]"]
date created: Thursday, April 3rd 2025, 5:27:37 pm
date modified: Thursday, April 3rd 2025, 5:33:03 pm
headings: ["[[#Concepts of Note]]", "[[#Examples]]", "[[#Usage]]"]
tags: [code/cpp/variables/hashing]
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- Hashing = Process of converting an input into a fixed-size string of bytes, typically for index/retrieval. 
- Hash value = Output from hashing.

- Very fast, and very uniform.
- std hash is the default hasher for C++.

## Media
[Unlocking the Power of std hash in C++ Programming - John Farrier](https://johnfarrier.com/unlocking-the-power-of-stdhash-in-c-programming/)
[std hash - cppreference.com](https://en.cppreference.com/w/cpp/utility/hash)

## Usage
- [p] `std::hash<dataType>` = Declares a hashed value of `dataType`. = #code/cpp/variables/hashing
<!--ID: 1751434091587-->


## Examples
```cpp
struct Person {
    std::string name;
    int age;
    std::string address;

    bool operator==(const Person& other) const {
        return name == other.name && age == other.age && address == other.address;
    }
};

namespace std {
    template <>
    struct hash<Person> {
        size_t operator()(const Person& p) const {
            size_t h1 = hash<std::string>()(p.name);
            size_t h2 = hash<int>()(p.age);
            size_t h3 = hash<std::string>()(p.address);
            return h1 ^ (h2 << 1) ^ (h3 << 2);  // Combine the hash values
        }
    };
}

int main() {
    std::unordered_map<Person, std::string> personRole;
    Person alice = {"Alice", 30, "123 Main St"};
    personRole[alice] = "Engineer";

    // Accessing the role of Alice
    std::cout << "Alice's Role: " << personRole[alice] << std::endl;

    return 0;
}
```