---
type: note
tags: []
---
# `printf`
- C library function that sends formatted output to stdout.
``` C
printf(const char *format, ...)
printf("%s", string)
printf(string)
```
- `format` = String containing text to be written to stdout. Can optionally contain embedded format tags to replace values
	- Tags prototype is: `%[flags][width][.precision][length]specifier`

### Tags and Flags
|Sr.No.|Specifier & Output|
|---|---|
|1|**c**<br><br>Character|
|2|**d or i**<br><br>Signed decimal integer|
|3|**e**<br><br>Scientific notation (mantissa/exponent) using e character|
|4|**E**<br><br>Scientific notation (mantissa/exponent) using E character|
|5|**f**<br><br>Decimal floating point|
|6|**g**<br><br>Uses the shorter of %e or %f|
|7|**G**<br><br>Uses the shorter of %E or %f|
|8|**o**<br><br>Signed octal|
|9|**s**<br><br>String of characters|
|10|**u**<br><br>Unsigned decimal integer|
|11|**x**<br><br>Unsigned hexadecimal integer|
|12|**X**<br><br>Unsigned hexadecimal integer (capital letters)|
|13|**p**<br><br>Pointer address|
|14|**n**<br><br>Nothing printed|
|15|**%**<br><br>Character|

|Sr.No.|Flags & Description|
|---|---|
|1|**-**<br><br>Left-justify within the given field width; Right justification is the default (see width sub-specifier).|
|2|**+**<br><br>Forces to precede the result with a plus or minus sign (+ or -) even for positive numbers. By default, only negative numbers are preceded with a -ve sign.|
|3|**(space)**<br><br>If no sign is going to be written, a blank space is inserted before the value.|
|4|**#**<br><br>Used with o, x or X specifiers the value is preceded with 0, 0x or 0X respectively for values different than zero. Used with e, E and f, it forces the written output to contain a decimal point even if no digits would follow. By default, if no digits follow, no decimal point is written. Used with g or G the result is the same as with e or E but trailing zeros are not removed.|
|5|**0**<br><br>Left-pads the number with zeroes (0) instead of spaces, where padding is specified (see width sub-specifier).|

|Sr.No.|Width & Description|
|---|---|
|1|**(number)**<br><br>Minimum number of characters to be printed. If the value to be printed is shorter than this number, the result is padded with blank spaces. The value is not truncated even if the result is larger.|
|2|*****<br><br>The width is not specified in the format string, but as an additional integer value argument preceding the argument that has to be formatted.|

|Sr.No.|.precision & Description|
|---|---|
|1|**.number**<br><br>For integer specifiers (d, i, o, u, x, X) − precision specifies the minimum number of digits to be written. If the value to be written is shorter than this number, the result is padded with leading zeros. The value is not truncated even if the result is longer. A precision of 0 means that no character is written for the value 0. For e, E and f specifiers − this is the number of digits to be printed after the decimal point. For g and G specifiers − This is the maximum number of significant digits to be printed. For s − this is the maximum number of characters to be printed. By default all characters are printed until the ending null character is encountered. For c type − it has no effect. When no precision is specified, the default is 1. If the period is specified without an explicit value for precision, 0 is assumed.|
|2|**.***<br><br>The precision is not specified in the format string, but as an additional integer value argument preceding the argument that has to be formatted.|

|Sr.No.|Length & Description|
|---|---|
|1|**h**<br><br>The argument is interpreted as a short int or unsigned short int (only applies to integer specifiers: i, d, o, u, x and X).|
|2|**l**<br><br>The argument is interpreted as a long int or unsigned long int for integer specifiers (i, d, o, u, x and X), and as a wide character or wide character string for specifiers c and s.|
|3|**L**<br><br>The argument is interpreted as a long double (only applies to floating point specifiers: e, E, f, g and G).|

- **additional arguments** − Depending on the format string, the function may expect a sequence of additional arguments, each containing one value to be inserted instead of each %-tag specified in the format parameter (if any). There should be the same number of these arguments as the number of %-tags that expect a value.
    

## Return Value

If successful, the total number of characters written is returned. On failure, a negative number is returned.

## Example

The following example shows the usage of printf() function.

 ```c
/#include <stdio.h>
int main () {
   int ch;

   for( ch = 75 ; ch <= 100; ch++ ) {
      printf("ASCII value = %d, Character = %c\n", ch , ch );
   }

   return(0);
}
```




# `scanf`
- Reads a data type
```cpp
scanf("`format_specifier`", &val)
```

## Common Flags
- _Int ("%d"):_ 32 Bit integer
- _Long ("%ld"):_ 64 bit integer
- _Char ("%c"):_ Character type
- _Float ("%f"):_ 32 bit real value
- _Double ("%lf"):_ 64 bit real value