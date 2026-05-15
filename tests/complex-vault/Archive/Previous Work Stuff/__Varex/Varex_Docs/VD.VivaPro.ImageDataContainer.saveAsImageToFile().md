---
date created: Tuesday, August 20th 2024, 2:05:36 pm
date modified: Monday, August 26th 2024, 12:39:26 pm
---
# `saveAsImageToFile()`
Overview:
- I think this is where we should check if there's a file extension, and assign one if there isn't. 
	- It passes data along to the [[VD.VivaPro.ImageDataContainer.saveToFile()]], which doesn't have capability to do that. 
- Saves image to a file, prompts user to choose a name for the file. 
	- Big call graph
- ![[VD VivaPro ImageDataContainer 2024-07-25 15.22.19.excalidraw]]
Notes:
- I don't think the `strFilters` does anything more than show different file types. Not super important from what I can tell. 
Inputs:
- `fileFullPathName` : `QString`
- `type` : `int`
Operations: ^ceadda
1. Grabs fullFilePathName, and sets the `FILE_SAVE_TYPE`
2. Prompts user for new file name, checks if that worked
3. Calls `theViewFrame->adddFileNameToRecentFiles(strSavedFilePath)`
4. Calls [[VD.VivaPro.ImageDataContainer.saveToFile()]] with `strSavedFilePath` as the input
	1. Depends on a `!strSavedFilePath.isEmpty()`