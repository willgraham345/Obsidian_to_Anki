---
summary: Sequence containers representing arrays, but can change size. Storage is handled automatically, and they are initialized with a given type. Can change size dynamically. Performs worse than other data types when removing/inserting elements at positions that are not the end.
headings: ["[[#Concepts of Note]]", "[[#Methods]]", "[[#Syntax]]", "[[#Usage]]"]
type: note/class
methods: ["[[#Indexing and Access]]", "[[#Iterators]]"]
child_classes: ["[[Cpp std vector const_iterator]]"]
component_of: ["[[Cpp std]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, June 26th 2025, 3:05:41 pm
library_used_in: 
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
### Indexing/Access
For viewing in a debugger, a good hack is to use `std::copy()` to view data (i.e. `std::copy(vector.begin(), vector.end(), locationToCopy)`)

## Methods
- [E] [[Cpp std vector]] = `.push_back()` = Pushes an element into the back of a vector, complexity `O(1)`. Similar to `.insert()`, but only at the back.
- [E] [[Cpp std vector]] = `.insert()` = Pushes an element into the back of a vector, complexity `O(1)`. Similar to `.insert()`, but only at the back. Will either copy or "move" an item into the back of a container. 
- [E] [[Cpp std vector]] = `.emplace()` = Allocates and constructs an object directly in a container's memory. Allows us to allocate a piece of memory and construct our object directly at that location in memory.  ^8ad293
- [E] [[Cpp std vector]] = `.emplace_back()` = Allocates and constructs an object directly in a container's memory. Allows us to allocate a piece of memory and construct our object directly at that location in memory. (Same as `.emplace()` but in the back).
- [E] [[Cpp std vector]] = `.clear()` = Removes all the elements of a vector container

## Usage
- [p] `vectorName.pop_back()` = "Pops" (removes) the element in the last slot of a vector = #code/cpp/variables/vectors 
<!--ID: 1751434091467-->

- [p] `vectorName.push_back()` = "Pushes" (adds) an element element in the last slot of a vector. Importantly, it does this by copy constructing as it pushes to the back. = #code/cpp/variables/vectors 
<!--ID: 1751434091470-->

- [p] `vectorName.assign(numValsToAssign, value)` = Reassigns an element within a vector = #code/cpp/variables/vectors 
<!--ID: 1751434091475-->

- [p] `vectorName.insert(elementIdx, value)` = Inserts a new element(s) before the element at the specified location. = #code/cpp/variables/vectors 
<!--ID: 1751434091478-->

- [p] `vectorName.clear()` = Empties a vector's values = #code/cpp/variables/vectors 
<!--ID: 1751434091482-->

- [p] `vectorName.emplace()` = Extends the container by inserting a new element at this position. Notably, it instantiates the vector within this position. = #code/cpp/variables/vectors 
<!--ID: 1751434091485-->

- [p] `vectorName.emplace(vectorName.begin() + i, std::move(obj))` = Extends container with an already built `obj`, to a place defined by iterator `i`. = #code/cpp/variables/vectors 
<!--ID: 1751434091489-->

- [p] `vectorName.emplace_back()` = Extends the container by inserting a new element at the back of a vector. Notably, it instantiates the vector within this position. = #code/cpp/variables/vectors 
<!--ID: 1751434091493-->

- [p] `vectorName[0]` = Indexes the first element within the vector = #code/cpp/variables/vectors 
<!--ID: 1751434091497-->

- [p] `vectorName.at(g)` = Returns a reference to the element at `g` = #code/cpp/variables/vectors 
<!--ID: 1751434091500-->

- [p] `vectorName.begin()` = Returns a reference to the first element = #code/cpp/variables/vectors 
<!--ID: 1751434091504-->

- [p] `vectorName.back()` = Returns a reference to the last element = #code/cpp/variables/vectors 
<!--ID: 1751434091509-->

- [p] `vectorName.data()` = Returns a reference to the internal array used here. Basically, what the vector is containing.= #code/cpp/variables/vectors 

### emplace() with mutate back()
Great when you don't have a copy constructor set
```cpp
 std::vector<Measurement> measurements;
    measurements.reserve(10);  // Important to avoid reallocation!
    measurements.emplace_back();  // Default-construct in-place
    {
        auto& m = measurements.back();
        m.setValue(9.81);
        m.setUnit("m/s^2");
        m.setSensor("IMU1");
        m.setTimestamp(1625849302);
    }
```


| Method      | Description                                                                                                                     |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `.begin()`  | Returns an iterator pointing to the first element in the vector                                                                 |
| `.end`      | Returns an iterator pointing to the theoretical element that follows the last element in the vector                             |
| `.rbegin()` | Returns a reverse iterator pointing to the last element in the vector (reverse beginning). It moves from last to first element. |
| `.rend()`   | Returns a reverse iterator                                                                                                      |

###  Iterate through a vector
#### Vector Methods
```cpp
#include <iostream>
#include <vector>
int main() {
    // Create a vector of integers
    std::vector<int> numbers = {1, 2, 3, 4, 5};
    // Iterate through the vector using iterators
    std::cout << "Iterating through the vector using iterators:" << std::endl;
    for (auto it = numbers.begin(); it != numbers.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;
    return 0;
}
```

#### Range-based Loop
```cpp
#include <iostream>
#include <vector>

int main() {
    // Create a vector of integers
    std::vector<int> numbers = {1, 2, 3, 4, 5};

    // Iterate through the vector using a range-based loop
    std::cout << "Iterating through the vector using a range-based loop:" << std::endl;
    for (int num : numbers) { //num will take on the value of each element in numbers
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
```

#### Index-based Loop
```cpp
#include <iostream>
#include <vector>
int main() {
    // Create a vector of integers
    std::vector<int> numbers = {1, 2, 3, 4, 5};
    // Iterate through the vector using an index-based loop
    std::cout << "Iterating through the vector using an index-based loop:" << std::endl;
    for (int i = 0; i < numbers.size(); i++) {
        std::cout << numbers[i] << " ";
    }
    std::cout << std::endl;
    return 0;
}
```

## Syntax
``` cpp
vector <data_type> vector_name__;    // 1D Vector
vector < vector<data_type> > vector_name;    // 2D Vector
```

### Vector Syntax
#### Vector
```cpp
vector<int> nums{1, 2, 3, 4, 5};
vector<string> fruits{"orange", "apple", "raspberry"};
```

#### Vector of the same values
```cpp
vector<int> vector3(5,12); vector3 = {12, 12, 12, 12, 12}
```

## Member Functions
### Basic Operation
| Method/Operation           | Description                                                        |
| -------------------------- | ------------------------------------------------------------------ |
| `vector::size()`           | Returns the number of elements in the vector.                      |
| `vector::empty()`          | Returns `true` if the vector is empty; otherwise, returns `false`. |
| `vector::push_back(value)` | Adds an element with the given value to the end of the vector.     |
| `vector::pop_back()`       | Removes the last element from the vector.                          |
| `vector::clear()`          | Removes all elements from the vector, leaving it with a size of 0. |

### Element Access
|Method/Operation|Description|
|---|---|
|`vector::at(index)`|Returns a reference to the element at the specified index, with bounds checking.|
|`vector::front()`|Returns a reference to the first element of the vector.|
|`vector::back()`|Returns a reference to the last element of the vector.|
|`vector::data()`|Returns a pointer to the underlying array serving as storage.|

### Iteration and Range Operations
|Method/Operation|Description|
|---|---|
|`vector::begin()`|Returns an iterator pointing to the first element of the vector.|
|`vector::end()`|Returns an iterator pointing to the position just beyond the last element of the vector.|

### Modification and Manipulation
| Method/Operation                  | Description                                                                              |
| --------------------------------- | ---------------------------------------------------------------------------------------- |
| `vector::insert(position, value)` | Inserts an element with the given value at the specified position in the vector.         |
| `vector::erase(position)`         | Removes the element at the specified position from the vector.                           |
| `vector::resize(new_size)`        | Resizes the vector to contain the specified number of elements.                          |
| `vector::reserve(new_capacity)`   | Requests that the vector capacity be at least enough to contain `new_capacity` elements. |
| `vector::shrink_to_fit()`         | Requests the removal of unused capacity.                                                 |

### Other
| Method/Operation                    | Description                                                                                |
| ----------------------------------- | ------------------------------------------------------------------------------------------ |
| `std::accumulate(begin, end, init)` | Computes the sum of the elements in the range `[begin, end)` with an initial value `init`. |
