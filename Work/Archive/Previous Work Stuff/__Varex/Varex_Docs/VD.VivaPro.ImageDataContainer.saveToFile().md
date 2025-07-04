# `saveToFile()`
Overview:
- Does the actual saving, and needs a filetype input. Assigning the extension should be done earlier when there's more access to the file filters
- Variables:
Operations:
1. Instantiates `file : QFile` based on the input `QString`
2. Checks to see if it can open the file
3. Checks the filetype
	1. I'm not seeing this get set. I think I found the bug here. It's cast from the `strSaveFullFileName` value. 