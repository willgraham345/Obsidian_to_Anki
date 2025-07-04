---
company: Varex
tags: archive_deprecated/Varex
---
Similar to Jira
# Redmine
TO1 is the project we want to be involved with
- Tooele was started by calling TO1
- Paul manages everything in there, based on the feature.
	- He creates queries on the right to help group things together
		- 20.0.6 is a version number that contains a target
- TO1 vs TO2?
	- Both are Tooele
	- TO2 is an evolution based on architectural changes
	- Transports changed (might be a term to look up)
	- TO2 is under the same project in Redmine

3 types of cases (changes in code)
- Task (not used)
- Bug
	- Something broken
	- Commit messages
		- When you push code, you'll need a bug number
		- We want information into the bug that has all sorts of stuff in it. 
		- Refs takes you to the feature or the bug that has all the details. 
- Feature
	- Something new
	- Often have less detail (description = problem)
Most projects have a bug number
- We want
## Documentation
There is a 130 page SOP that describes everything we should be doing
- We do this so we can be FDA approved
- All of it starts upstream within the 
- requirements -> product spec -> subspec -> software subsystem -> work that gets done
- verification/validation -> production build -> work that gets done
	- These two things need to match and be documented in an FDA process. 
	- We have to prove that our process supports the software that we are using. 
		- Code reviews are based on requirements
Requirement tools is the PTC Windchill
- Gen7 is coming (Customer/marketing requirement)
- GUI testing is *really* difficult because you can't just write a unittest
	- You need to write a completely different tool to test the GUI
		- The higher the logic, the more difficult it is to test
		- If we need to write something to the detector, we can write that functionality within the GUI, or within an API. It's much easier to test the API rather than the GUI. 
	- Tests create an xml output
		- That is then put back into the the Redline tool
		- A trace matrix can be run to then determine if it is correct and verifies that the test is met with a `PASS` or `FAIL`
- Changing tools is a big process
	- Does this build system build what it's supposed to build?
Gerrit has git, and has code review stuff
- Just a fancy diff
## Cases and their fields
We won't often edit the description fields, but we can add codes.
- Copy/paste is great. 
- Here's what I did to fix this


### Stages of code review
See [[VD.Git.Gerrit.Intro]] for a better idea of how this goes. 
- In test = terminal state
- New
- Open
- Duplicate
- Closed (not sure if we can even do this)
- Rejected
- Not a Bug
- Not reproducible

Jim is a tough on code requests
- -2 is a "we can't push this through"

When we make a push or comment, the rest of the team gets an email. 
- 


### Scores
Repo owners will have a "Submit" button if you get a high enough score
Score from the build system (need at least +1)
Score from the Jenkins
Scores by other developers
Spelling mistakes (they should be fixed)
#### Different Numbers
+2 looks good, lets merge
-1 should be fixed, but we could potentially go through with it. Something that could or could not be passed through.
-2 can't merge, needs to be fixed