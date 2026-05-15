---
type: note/class
class_of: "[[Cpp stdio]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, November 26th 2024, 12:08:15 pm
---
# Background
- Reads characters from stream and stores them as a C string into `str` until `num-1` characters have been read, a newline, or the end of the file is reached. 
- A

# Usage
```cpp
fgets(str, num, stream)
```
- `str` = Pointer to array of `char` where the string read is copied
- `num` = Maximum number of characters to be copied into `str`
- `stream` = Pointer to a FILE object that identifies an input stream. stdin can be used as an argument to read from the standard input. 

## Example
```cpp
/* fgets example */
#include <stdio.h>

int main()
{
   FILE * pFile;
   char mystring [100];

   pFile = fopen ("myfile.txt" , "r");
   if (pFile == NULL) perror ("Error opening file");
   else {
     if ( fgets (mystring , 100 , pFile) != NULL )
       puts (mystring);
     fclose (pFile);
   }
   return 0;
}
```