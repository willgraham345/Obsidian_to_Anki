---
date created: Tuesday, August 20th 2024, 2:05:36 pm
date modified: Monday, August 26th 2024, 12:39:33 pm
---
# `getSaveAsFilePath()`
Inputs:
- `std::shared_ptr<ImagDataContainer> container`
- `QString strFilters`
- `QString strFileType`
- `QString defaultFileName`
- `QString & folderCreated`
	- Reference parameter to the created folder, meaning it can modify the original variable. 
Overview:
- Instantiates `strFolder` to the last open directory. 
- Instantiates `strFullPath` to `strFolder`
Notes:
- Small thing that only seems to be called for `.viv` files
- Creates a variable `strFileName`, which takes the input from the text box. I think that needs to read for the extension. 
	- Never looks for the filetype that should be added. 
Operations:
1. Interacts with [[VD.VivaPro.ImageDataContainer#`saveAsImageToFile()`]]
2. Sends forward to [[VD.VivaPro.ImageDataContainer#`saveToFile()`]]
	1. Passes in `strFileName`, but the function has input for the fullFileName