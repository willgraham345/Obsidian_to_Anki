---
type: note/library
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Wednesday, February 26th 2025, 9:02:35 am
tags:
  - note/python
summary: How python does argument parsing
---
# Background
Lets you handle command line inputs with flags and parameter naming stuff

# Usage
## Example For Files
```python
# script.py
import argparse

def main():
    parser = argparse.ArgumentParser(description='A script with command line arguments.')

    # Define command line arguments with flags and parameter names
    parser.add_argument('-f', '--file', type=str, help='Input file path', required=True)
    parser.add_argument('-o', '--output', type=str, default='output.txt', help='Output file path')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode')

    args = parser.parse_args()

    # Retrieve command line arguments and save them to local variables
    input_file = args.file
    output_file = args.output
    verbose_mode = args.verbose

    # Your script logic here
    print("Input file:", input_file)
    print("Output file:", output_file)
    print("Verbose mode:", verbose_mode)

if __name__ == "__main__":
    main()
```

```shell
python3 script.py -f input.txt
%% OR %%
python3 script.py -f input.txt -o output.txt -v
```

## Lists Example
```python3
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Process integer pairs and save them into lists.')
    
    parser.add_argument('-a', '--pair1', nargs=2, type=int, required=True, help='First pair of integers')
    parser.add_argument('-b', '--pair2', nargs=2, type=int, required=True, help='Second pair of integers')
    parser.add_argument('-c', '--pair3', nargs=2, type=int, required=True, help='Third pair of integers')
    parser.add_argument('-d', '--pair4', nargs=2, type=int, required=True, help='Fourth pair of integers')

    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()

    list1 = list(args.pair1)
    list2 = list(args.pair2)
    list3 = list(args.pair3)
    list4 = list(args.pair4)

    print("List 1:", list1)
    print("List 2:", list2)
    print("List 3:", list3)
    print("List 4:", list4)

if __name__ == '__main__':
    main()
```
```shell
python script.py -a 1 2 -b 3 4 -c 5 6 -d 7 8
```