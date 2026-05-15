---
type: project
project_id: 9
company: Will
project: 
subproject: 
tags: 
status: stalled
---
# Related Links:
# Updates/Notes:
## Todo 
- [ ] ~~Add RPE to editor~~
- [ ] ~~Current exercise editors~~
	- [ ] ~~Choose exercise button~~
	- [ ] ~~Next exercise button~~
	- [ ] ~~field1 editor~~
	- [ ] ~~field2 editor~~
	- [ ] ~~RPE Slider/inputs~~
- [ ] ~~Add set counter~~
- [x] Post to obsidian forums

### Design Thoughts
## 2024-07-23 09:00
I'm not really using quickadd much anymore. I'm instead binding straight to templater with the meta-bind. 

#### Templates I want to use

| Template        | Metadata                                                                                                                                | Buttons                                                 |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| Create exercise | muscleGroups<br>- primaryMuscle<br>- secondaryMuscle<br>exercise_type<br>- field1<br>- field2<br>- field3<br>type: exercise_description |                                                         |
| Create plan     | Exercise tasks<br>- workout type                                                                                                        | Add exercise to exercise plan                           |
| Workout log     | exercise tasks<br>- workout type<br>selected_exercise<br>count<br>workout_template<br>calories_burned<br>                               | Modify current exercise<br><br>Add exercise to exercise |


Create exercise
Create exercise plan
- 
Log workout
- Should point to created workouts
- One should be blank

#### Views/buttons I want
Exercise history viewer
- Let's have a separate thing that we build rather than within the actual exercise

##### Homepage
Views
 - Time since last workout for each type of workout, with links to those workouts
	- Show calories burned
buttons
- Log workout
- New workout plan
- Create New exercise
- Open workout viewer
- Open exercise veiwer

##### Workout viewer
- Choose from workouts in workout-plans, then from workout logs

##### Exercise viewer
- Suggest a workout from workout list, or have that bound to a metadata field

## 2024-07-23 10:00
Realizing I can use the metadata menu edit to make the managing of different input fields much better. I think it'll make it easier to build the editor tab in the log-workout template



Making different field views for the various stuff

## 2024-07-23 16:00
Did a much better job here of using meta_edit. The only thing I'm struggling with at this point is getting the table to update within the updated workout. 

## 2024-07-25 10:00
### Obsidian Help post
Hi all! I'm looking for some guidance/help on how I can better leverage the metadata within a note for accessing and quickly editing. My goal here is to build two vaults. One that will keep track of my exercise/workouts, and another for meal planning/recipes. I'm an avid user of Obsidian and this seems like the perfect application for a few of the open-source plugins. 

I started with the workout application and I've run into some difficulty. There are great example vaults ([kaylesworth/workout-tracker: A workout tracker created in obsidian to control your data around exercises and workouts (github.com)](https://github.com/kaylesworth/workout-tracker), [martinjo/obsidian-gym-log: Gym workout log for obsidian (github.com)](https://github.com/martinjo/obsidian-gym-log)) but I wanted something that had more visibility, tracking, and mobile editing capabilities. I've found that when I'm able to quickly edit something is when I use it often. I plan to build on these works and upload what I have to all. 

My ideal structure goes something of the following demonstrated in the excalidraw chart below:

![[P015 Workout App 2024-07-25 10.23.48.excalidraw]]
Within this chart, the groups/folders are different file templates or file classes. I'm flexible on either, as I've played with both. 

Here's a few screenshots of my current fileClass for metadata menu, and what I've tried. 



There are two challenges that I have. 
1. How to consistently query Metadata Menu objects/object lists within a JS query or DQL query. I haven't been able to find reliable documentation on how to display an objectList as one table. 
2. How to quickly edit different fields with any amount of speed. Metadata Menu is great, but with these increasingly deep fields it gets to be a headache trying to modify any sets while I'm actively working out. I'd love to have a sort of interactive table similar to what's seen in this article()

I'm still learning JavaScript (more of a Python/C++ guy myself), and I'm unfamiliar with the intricacies of mapping different objects and sub-objects. I'd love any pointers and/or constructive criticism on the project. As I said previously, I'd love to upload all of this directly to GitHub for as many people to use as possible!  

## 2024-07-25 11:00
Had a breakthrough finding a better dataview table. There's a MUCH easier way to deal with it by using tasks. You can then query and modify the stuff. 

## 2024-07-25 14:00
Just about done with it all! Got through making all new workouts, with obsidian class edits. Happy to have it finished and ready to go. 