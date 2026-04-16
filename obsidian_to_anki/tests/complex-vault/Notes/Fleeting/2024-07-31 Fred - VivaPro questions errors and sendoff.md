---
type: update_log
date: 2024-07-31
week: 2024-W31
year: 2024
company: Varex
project: 
subproject: 
tags: 
status: closed
---
# Relevant Links
- 

# Message
Fred and Elena,

I wanted to reach out to both of you before I finish my time here to give an update on [bug 31759](https://fpbugs/issues/31759). As the bio says, the extension names are not being saved automatically. 

After entering a debugging view, I was able to follow the stack trace which jumps into a few different functions. My basic understanding is that there are a few different functions at work:
1. `imageDataContainer::saveAsImageToFile()`
2. `imageDataContainer::saveToFile()`
3. `ViewFrame::getSaveAsFilePath()`

The `imageDataContainer::saveAsImageToFile()` interacts with the GUI, and determines which of the other two functions is called. In the situation where the file extension isn't being saved, I believe it's because there isn't a compatible type passed into `getSaveAsFilePath()` from the `saveAsImageToFile()`.  Essentially, the class enum `ViewFrame::FILE_OPEN_TYPES` is used as there isn't functionality supported to get type using the `ViewFrame::FILE_SAVE_TYPES`. 

As such, I added an additional implementation to the `ViewFrame::getImageFileExtensionFromType()` so it can handle `ViewFrame::FILE_SAVE_TYPES` in addition to `ViewFrame::FILE_OPEN_TYPES`. I also updated the `getSaveAsFilePath` to have an additional argument called: `defaultFileExt`. The `defaultFileExt` is used in a conditional within `getSaveAsFilePath` to ensure a filepath is added.

I've tested functionality for .viv, .raw, and .seq files. I've pushed the files and I'm looking forward to your reviews.  


the `saveAsImageToFile()` takes input from GUI signals/slots, grabs necessary things like file extensions, performs checks, interacts with the `ViewFrame` and forwards necessary info into the `saveToFile()` member. Unfortunately, I think the file extension isn't being set correctly as it stands. The `saveAsImageToFile()` doesn't set a default file class extension within 
The function I've found to be at the center is the `imageDataContainer::SaveAsImageToFile()`. This file takes input from a variety of different slots present in the GUI. One of its two inputs is the enumerator for save type, which is cast as an int. 

That int should be passed through the function and 

The current state

Solutions...?