---
company: Varex
tags:
  - archive_deprecated/Varex
  - archive_deprecated/Varex/vivaPro
---
They've been working with VivaPro in Windows for a few years, but want it to work in Linux too. 
- It's sent to the OEM customers, and they configure it for the hospitals. 

Set it up in my C drive in its own folder as an application
- Also set up an `Images\` folder on my C Drive
	- He sent me some images
	- Fluoroscopy takes tons more images
		- 



Top menu
File->open a file


Playing a video
The play button shows you how to go through frames iteratively, 
Bottom right will show you the resolution of the image, your position on the image, dimension of the image, and the index of the frame you're seeing. 

Capture Rate is how many frames per second (Hz)


Bottom left blue rectangle is for quick and fast navigation across an image. 
- You can do the same thing with a scroll bar if you need it. 
- Zoom is with the magnifying glass on the right. 
	- Number is how many pixels per your pixel
- ![[Pasted image 20240510152820.png | 850]]
Checkbox on bottom right next to the pixels
- Will toggle showing ADU values on and off (shows the value and position of the values)

Top black bar right click -> options
- Can also be selected
- Options -> User Interface
	- He selected to combine two of the tools on the Combine Bars option to move the options together. 

Two buttons on left
- Cursor
- Region of interest
	- Lets you do analysis on one area, rather than the entire image
	- Holding the alt key will let you resize it, move it, and get other data about the image. 

Right clicking the image
- Usually, you'll see the stuff related to the image. 
- Anything you see is related to that image
	- W/L
		- Pixels you choose to see. 
		- There are tons of pixels.
		- Shows you the 16-bit value for each of the pixels stored within the image. 
			- You are now seeing more or less pixels. 
		- Auto window level calculates the best possible picture for you. 
		- Window = How large the window is between the top and bottom pixel value. 
		- Level = Middle of the top pixel, and the bottom pixel value (also a 16-bit number)
		- The pixel values are what radiologists look at to categorize tissues. 
			- We'll instead use this for categorizing bad pixels. 
	- ROI
	- Image headers
	- ROI Statistics
	- Image Operations. 