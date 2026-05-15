---
type: update_log
date: 2024-07-26
week: 2024-W30
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
Here are the docs which I was able to build for ConfigCreator. They're not an official build, and it may be difficult to reproduce. If you'd like to view them, click on the `index.html` shortcut and a web browser should pop up. I'd start exploring the different files and classes. The Qt class is mostly defined within the src/ folder and the ConfigCreator.cpp/ConfigCreator.h files. There's a couple of good diagrams on the inheritance behind these. Once you feel like you have a good idea of what's going on let's talk more on what Greg wants to have happen. 

As an additional note, I'd try to clone the ConfigCreator, XConfigure, and config repositories to your computer. You'll likely need to build each of these locally to see the features. You can also find example configurations in the configuration repository. There's a huge amount of ones in there, Greg specifically pointed out the "1313_MJI_32051" as a good example. See if you can build configCreator and open that file. 