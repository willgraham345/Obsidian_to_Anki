---
status: closed
type: update_log
date: 2024-07-11
week: 2024-W28
year: 2024
company: Varex
project: 
subproject:
---

# Relevant Links
- 
# Message
I'm getting errors that the function definitions within viewframedisplayinterval.cpp have already been defined elsewhere. Any chance you'd be able to walk me through the way that the viewframedisplayinterval.cpp fits into the viewFrame.cpp/viewFrame.h files?

I understand that the viewFrame.h declares the functions, and viewFrames.cpp implements functions. What confuses me is how the viewframedisplayinterval.cpp almost fills in the cracks for the viewFrames.cpp. There are separate definitions, and also an object file with the same name that are referenced. I've attached a drawing below to show the relationships I'm talking about. 