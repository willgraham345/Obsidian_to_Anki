- Description:
	- Handles the defect map from within VivaPro. 

## ctor
### ctor
Overview:
- Relies on `getHelper()`, `getViewFrame()`
	- `getViewFrame()` grabs the pointer to the [[VD.VivaPro.ViewFrame]] class
- This also relies on `MainGuiWindow::getViewFrame()`, which grabs the pointer for the [[VD.VivaPro.ViewFrame]] object/class (not sure which at this point)
Operations:
1. 

## public
### Fields
### Methods
#### `acquisitionImageDisplayed()`
Overview:
- Called whenever a new acquired image is acquired. (Might be what we want)
Operations:
1. 
#### `doOpenDefectMapFile()`
Overview:
- Called whenever the user selects Open-Defect-Map-File from editors menu. Opens the image file. 
Operations:
1. 

#### `transmitEmptyDefectMapFile()`
Overview:
- Transmits an empty file to the detector. 
Operations:
1. 
