---
summary:
headings: ["[[#Examples]]"]
type: note/process
similar: ["[[Python argparse]]"]
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Thursday, December 11th 2025, 10:18:19 am
tags: []
template: "[[base_note_template]]"
template-version: 1.0.0
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
- Sys lets you parse through command line arguments with the `sys.argv` function. 
- This isn't as helpful as `argparse module`

## Examples


```python3
# script.py
import sys

def main():
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) < 3:
        print("Usage: python script.py -f <input_file> [-o <output_file>] [-v]")
        sys.exit(1)

    # Default values
    input_file = None
    output_file = 'output.txt'
    verbose_mode = False

    # Parse command line arguments
    i = 1
    while i < len(sys.argv):
        if sys.argv[i] in ['-f', '--file']:
            i += 1
            input_file = sys.argv[i]
        elif sys.argv[i] in ['-o', '--output']:
            i += 1
            output_file = sys.argv[i]
        elif sys.argv[i] in ['-v', '--verbose']:
            verbose_mode = True
        else:
            print("Unknown option:", sys.argv[i])
            sys.exit(1)

        i += 1

    # Your script logic here
    print("Input file:", input_file)
    print("Output file:", output_file)
    print("Verbose mode:", verbose_mode)

if __name__ == "__main__":
    main()
```
```bash
python script.py -f input.txt -o output.txt -v
```
