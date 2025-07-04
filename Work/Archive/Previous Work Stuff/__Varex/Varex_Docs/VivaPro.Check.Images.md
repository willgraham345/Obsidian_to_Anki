---
company: Varex
tags:
  - archive_deprecated/Varex/vivaPro
---
# Ubuntu
## 1-      **Connection and Acquisition**:

a-       Run VivaPro from the same SDK build
✅
b-      Make sure it can connect to the detector.
✅
c-       Make sure It can do acquisition.
✅
d-      Make sure it can do offset calibration.
✅
e-      Make sure it can do gain calibration.
✅
## **2-**      **Product Info:**
a-       From menu Tools -> Product Info, check the Software Tab (the first tab) in the displayed dialog and make sure the info displayed is same on Windows.
✅
b-      Select the Detector Tab (second tab) and make sure the info displayed is same on Windows.
![[VivaPro.Check.Images.png|325]]

c-       Try to compare the other tabs (Temperature, Voltages, Currents) and compare them to the Windows (Data should not be exact but close).
Temps ~31-33
Voltages
![[VivaPro.Check.Images-1.png|350]]
Currents not showing up
❗

## **3-**      **Open/Save** ❗(can't do this one)

a-       Acquire a Fluoro Image (about 20 frames)

b-      From menu, select File -> Save -> Save in Seq File Format and make sure it saved.

c-       open the saved sequence file and compare the ADU values with the original and make sure the ADU values (top 10 pixels and last 10 pixels) are same.

d-      From menu, select File -> Save ->Save Range -> Save in .raw File Format and select frame index 2 – 5 and save it. Make sure the saved images are same as the original (checking the top and bottom pixels).

## **4-**      **Image Data**

a-       Open a Fluoro image.


b-      Right click on the first frame (frame index 0) and from the popup menu select Image Header… Compare the displayed data with the same file opened on Windows and make sure the displayed data are same.
- ![[VivaPro.Check.Images-2.png|138]]

c-       Right click on the first frame (frame index 0) and from the popup menu select Image Information… Compare the displayed data with the same file opened on Windows and make sure the displayed data are same.
- ![[VivaPro.Check.Images-3.png|250]]
d-      Right click on the first frame (frame index 0) and from the popup menu select Image Operation. Add a value to all pixels (say 100), Compare the displayed new image’s data with the original image and make sure all pixel values (ADU values) are 100 more than the original.
- ❗Potentially broken, not working on either. 

e-      For the same image and same frame, right click on the image and from popup menu select Pixel Intensity Distribution Plot and make sure it matches the same frame on Windows.
- ✅

## **5-**      **View Menu**

a-       From the top menu, click View -> Show Thumbnail View and make sure the Thumbnail View is hidden. Try it again  and make sure the Thumbnail View is visible.

- ✅

b-      From the top menu, click View -> Show Fluoro Sequence Bar and make sure the Fluoro Sequence Bar is hidden. Try it again  and make sure the Fluoro Sequence Bar is visible.

- ✅

## **6-**      **Detector Menu / Transfer Files**

a-       From the top menu, select Tools -> Detector -> Transmit Files…  Transmit Files dialog should show.

b-      From the Map Files tab (the first tab), select mode 0 and Offset map and click on “Get Map File” button and make sure it succeeds.

c-       From the same dialog put back the same Offset Map file by clicking the  “Put Map File”  button, and make sure it succeeds.

d-      Do same for Config file (second tab) and user Files (you can put up to 10 user file, any file and get it back and you can also delete it).

e-      Get the Defect Map File (for mode 0) and save the .def for later.
- ❗Not working. Got this:
- ![[VivaPro.Check.Images-4.png|225]]

## **7-**      **Detector Menu / Change Network Settings**

a-       From the top menu, select Tools -> Detector -> Change Network Settings…  Change Network Settings dialog should show.

b-      Change the IPV4 Address to 192.168. 1. 32 and apply the change. This will change the IP address on detector and now you need to disconnect and reconnect with the new IP address.

- ![[VivaPro.Check.Images-5.png|600]]
	 - Didn't change the network configuration
c-       Once successful, change the IP address to the original 192.168. 1.31 and reconnect.

## **8-**      **System Resources/Resources**

- System resources immediately closes VivaPro. Couldn't test anything relating to that. 
a-       From the top menu, select Tools -> System Resources…  System Resources dialog should show.
- ❗Broken.

b-      Check the Memory Tab (the first tab) and make sure the Physical memory data is correct.
- 
c-       Select the Disk Drives tab and make sure the disk data is correct.
	
d-      Select the Ports and check the Ports data is correct.

e-      Same with Network Interfaces tab.

## **9-**      **System Resources/Commands**

- ❗Broken, can't access.
a-       From the top menu, select Tools -> System Resources…  System Resources dialog should show.

b-      From the Commands tab, enter 192.168.1.31 in the Host Address Edit box and click the ping and make sure the ping is successful.

c-       In the Commands edit box enter a Linux system command and press the Run button and make sure it runs. (Currently we have ipConfig command for Windows, we need to remove those and replace it with some useful Linux commands.)

## **10-**   **Tools/Launch Menu**

a-       From the top menu, select Tools -> Launch -> Edit .ini File and make sure a text editor launches with the vivaPro.ini to edit (just like Windows).

b-      From the top menu, select Tools -> Launch -> View Log Files and select the  “Client Log File” and make sure the log file is displayed to the user.
- Opened, but I get this error:
  ![[VivaPro.Check.Images-6.png|350]]

## **11-**   **Help Menu**

a-       From the top menu, select Help -> Quick Tips and make sure the Quick Tips dialog shows up.
- ✅
b-      Select About VivaPro and make sure the About dialog shows up.
- ✅
c-       Select “Context Help” and make sure the vivaPro.pdf file is displayed to the user.
- ✅

## **12-**   **Defect Map Editor**

Unable to open. 
a-       From the top menu, select Tools -> Defects -> Defect Map Editor. The main view changes to Defect Map Editor.

b-      From File menu, select “Open Defect Map File…”, and open the .dft file saved in #6 test cases above.
- ❗Didn't work. 

c-       Double click on the image and then, right click on the image and select “Set Row as Defect”.

d-      Right click on the image and select “Set Column as Defect”.

e-      Select File -> Save Defect Map and save the file.

f-        Open the saved .dft file and make sure your changes are there.

g-       Close the Editor and make sure the main window has the files you had opened prior to the Defect Map Editor command.