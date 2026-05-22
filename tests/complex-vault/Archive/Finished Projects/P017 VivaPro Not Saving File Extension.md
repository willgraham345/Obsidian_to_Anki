---
type: project
project_id: 3
company: Varex
project: VivaPro
subproject: VivaPro_dev
tags: 
status: stalled
---
# Related Links:
# Updates/Notes:

## 2024-07-24 11:00
Starting this up. Just tested and it indeed is not working. I will need to look into the saving process. 
- Class called [[VD VivaPro DlgSaveImageData]]
	- It doesn't get triggered when I save the image. 

While trying to test, I think I may have frozen my computer :(
- Yep. Poor VM is struggling right now.

Saving an image, I'm not sure how to save the stuff. 
- Might be saved using the `imageDataContainer` class
	- There are also `imageEditor` and `imageRetrieve`

I'm not positive where the saving functions are called/created

## 2024-07-24 15:00
[[VD.VivaPro.ImageDataContainer]] may be the class I want to look at. Hard to know with such a large codebase. 

### Testing/debugging process
1. Clicked save after opening an image
2. Found the place in the class where the thing stops [[VD.VivaPro.ImageDataContainer#^ceadda]]

### 2024-07-24 15:00
I need to figure out which file extension I should be adding onto the saved filename (`strSavedFilePath`). When opening a `.viv` file:
- Clicked saving in `.viv` format
- Triggers the `case ViewFrame::FILE_SAVE_TYPE::VIV:` file
- Which line actually saves the file?
	- line 1035 on `imageDataContainerLoadDisplay.cpp` has a `savetoFile(strSavedFilePath`

## 2024-07-24 15:00
I believe I have a fixed out and pushed for the bug. All I really did is add an extension to the end of the file as it saved. 
- One mistake, I believe I may have added it to the wrong Gerrit message. I'll be revising that now. 

## 2024-07-24 16:00
Talked with Fred, waiting on his code review

## 2024-07-25 14:00
Fred said that this is only a problem with some versions of Qt, and the fix I have will ruin Windows. Fred mentioned [this thread](https://forum.qt.io/topic/131081/qfiledialog-doesn-t-add-selected-extension/3). 

Available file types and extensions not shown in the pull-down menu without *applying* the extension

### Examples
```cpp
const QStringList filters({
				"Thingy (*.thi)",
				"Dingy (*.dni)"
				});
QFileDialog fileDialog(this);
fileDialog.setAcceptMode(QFileDialog::AcceptSave);
fileDialog.setNameFilters(filters);
fileDialog.exec();

if (!fileDialog.selectedFiles().count())
		return;
QString filename = fileDialog.selectedFiles().first();
```

Upon looking more closely at Fred's suggestions, it appears that he wants me to edit the `getSaveAsFilePath()` function (line 126 on `viewFrameFileAction.cpp`).

## 2024-07-26 13:00
I don't see that the `strFilters` matters at all. 

Based on the thread in [[#2024-07-25 14 00]], the QFileDialog's `getSaveFileName()` doesn't show the same bug as the one we're seeing in `getSaveAsFilePath()`

```
getSaveAsFilePath(
	getSharedImageContainer(),
	strFilters,
	"Image",
	"",
	folderCreated
)
```
- This function is a little weird. 
Need to look more at the `getFileTypeFromFileName()`
- There needs to be a conditional that checks whether or not the filetype has already been set. From what I can tell I don't know where. 

## 2024-07-29 11:00
Looking into how Qt decides to save files.  
- There's an object that Qt creates to handle lots of file i/o [[Qt.QtCore.QtCore.QFile]]. 
	- There are examples in the docs which say how to add save functionality. 

Within the `saveToFile()` that our Qt uses, there's a variable `targetFileType` that casts 

### Debug run-through
`targetFileType` variable in [[VD.VivaPro.ImageDataContainer.saveToFile()]] isn't getting the target file type leaving it unset. It might be easiest to modify that function instead. 

It's never set if you don't write down the file extension. 
- Is there a way to check the current filter that Qt is using?
	- Yes, getting an active filters list out of the dialog box from within [[VD.VivaPro.ViewFrame.getSaveAsFilePath()]]. I don't know if I can access that from within the [[VD.VivaPro.ImageDataContainer.saveToFile()]] function.

There's a `ViewFrame::FILE_SAVE_TYPE` enum that I might be able to use. 

#### [[VD.VivaPro.ViewFrame.getSaveAsFilePath()]]
Inputs show:
```cpp
theViewFrame->getSaveAsFilePath(
	getSharedImageContainer(), //container
	strFilters, //strFilters
	"Image", //strFileType
	"", //defaultFileName
	folderCreated); //folderCreated
```
Can I get the file extension from that? From within the `strFileType`?
- Nothing within here says much about the file extension. It has strFilters, but those don't provide any information on which thing was selected.  

Can I pass the `saveType` variable into the thing? 

### Questions for Fred
Issues I'm seeing
- File type isn't ever set
Solutions
- I can pass through a pointer on the QFileDialog class, which then be used to access the filetypes. 
- I can try to set that file class on default from within the `saveToFile()` class on ImageDataContainer. 
- Find which dialog was selected when you click `Save As .Viv`
- `FILE_SAVE_TYPE` is weird, and doesn't have values that make sense. 
Strategy I'd like
-  set an `strExtension` based on the save type and the polymorphed [[VD.VivaPro.ViewFrame.getImageFileExtensionFromType()]]
- Set that as the default for the getSaveAsFilePath option in [[VD.VivaPro.ViewFrame.getSaveAsFilePath()]] 

## 2024-07-31 14:00
Starting up again with this, sending Fred an update thi

## 2024-07-31 17:00
I believe this thing is finished, we'll see what Fred and/or Elena think.
## 2024-07-31 14:00
Starting up again with this, sending Fred an update thi

## 2024-07-31 17:00
I believe this thing is finished, we'll see what Fred and/or Elena think.

# Next steps
- [ ] Look into `saveAsImageToFile()` invocation of `getSaveAsFilePath()`
- [ ] Look into [[Qt.QtCore.QFileDialog.Class]] stuff. Not sure how this is working within our system
- [ ] Learn more about the [[Qt.QtCore.QtCore.QDir]]. I think I understand it, but I don't think there's much I can edit within this. 