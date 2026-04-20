---
summary: Used to write data to files, defined in the <fstream> header file.
type: note/class
inherits_classes:
  - "[[Cpp basic_ostream]]"
class_of:
  - "[[Cpp fstream]]"
date created: Friday, December 27th 2024, 4:54:01 pm
date modified: Friday, December 27th 2024, 4:59:16 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
# Usage
## Example Usage
```cpp
#include <fstream>

int main() {
  // Create an object of ofstream
  std::ofstream outputFile;

  // Open a file for writing
  outputFile.open("output.txt");

  // Check if the file is successfully opened
  if (outputFile.is_open()) {
    // Write data to the file
    outputFile << "Hello, World!";

    // Close the file
    outputFile.close();
  } else {
    // Handle error if the file cannot be opened
    std::cout << "Error opening the file.";
  }

  return 0;
}
```

## Media
[std::basic\_ofstream - cppreference.com](https://en.cppreference.com/w/cpp/io/basic_ofstream)
<iframe src="https://en.cppreference.com/w/cpp/io/basic_ofstream" style="width: 100%; height: 600px;"></iframe>