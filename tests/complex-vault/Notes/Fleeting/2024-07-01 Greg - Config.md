---
status: closed
type: update_log
date: 2024-07-01
week: 2024-W27
year: 2024
company: Varex
project: 
subproject:
---
# Relevant Links
- [[Greg Gerber]]
- [[P003 ConfigCreator_Integration]]

# Message
Hey Greg, hope you had a good weekend and you're doing well. 

I've had a chance to look at the config creator again and jump back into the project. I think I'm in a good spot to ask questions. Any chance you'd have some time to talk today? I'm flexible and I can work around your availability. If today doesn't work, I can put together an email with the questions I have. 

## Questions for Greg
Integrating the `isModular()` into the checks on the `reloadAllWidgets()`
I have a GUI built (the `.ui` files). How do I add the appropriate headers/source files to integrate that with the project?
- Things that I'm guessing I'll need to do:
	- Add header file to declaration
	- Add associated source files to declaration
	- Something to the ui on the ConfigCreator.ui
		- I think this should be handled by the internal stuff on QtCreator, since I designed it there. 
	- ConfigCreator.cpp
		- Add ui->tabWidget->setTabEnabled(TAB_NON_MODULAR, false)
		- Add case TAB_NON_MODULAR to the else if statement on line 860.
I have errors building from both VS as well as VS code