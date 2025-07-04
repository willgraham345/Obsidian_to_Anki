---
type: note
---
# Background
## ASCII
- ASCII = Unaccented English letters
	- Can represent every character using a number between 32 and 127
		- Space was 32, "A" was 65
	- Could be stored in 7 bits
	- Codes below 32 were called unprintable and used for control characters

## ANSI
- ANSI standard = everyone agreed what to do below 128 bits
	- Different systems of handling above 128 are called code pages
	- Asian systems needed two bytes to handle their lexicon

## Unicode
- Unicode = Effort to create a single character set that included every reasonable writing system on the planet.
	- Unicode has a different way of thinking about characters. A letter maps to something called a code point which is a theoretical concept
	- Every platonic letter in every alphabet is assigned a magic number which is written like U+0639. 
		- That's a code point. 
			- The numbers are hexadecimal
		- Arabic Ain is U+0639
		- English A is U+0041
	- There's not a real limit on the letters that Unicode can define. 

### Encodings
You can have different meanings if you're on low endian or high endian (which high bit is what)

Every Unicode has an FF FF at the beginning of each Unicode string.
- Unicode byte order mark
- If you swap the low and high bytes, it will look like FF FE and the other person will know that they have to swap every other byte. 

#### UTF-8
Every code point from 0-127 is stored in a single byte
- This meant that english text looks exactly the same as it would in ASCII
	- Only other languages would have to store additional bytes

#### UTF-16
- Stores in two bytes. 

#### Other Encodings
##### UTF-7
Requires the high bit to always be zero, so it can be passed through a 7 bit deal

##### UTF-4
Stores each code point in 4 bytes, which has the nice property that every single code point can be stored in the same number of bytes

# Usage
It doesn't make sense to have a string without knowing what type of encoding it uses
There is no such thing as plain text
You HAVE to know what type of encoding it is in order to process it correctly.

[More information here](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)