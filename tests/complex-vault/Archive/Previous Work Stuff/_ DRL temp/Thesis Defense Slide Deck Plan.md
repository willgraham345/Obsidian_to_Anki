---
type: presentation
---
 Outline
- Introduction
- Problem Statement
- Related works
- Methods
- Results
	- Rotation Matrix Testing
	- Documentation
- Future work
- Conclusion
	- Q&A

---

# Intro
Will Graham
Dr. Daniel Drew

---

# Field Overview
Multi-agent robotic systems (MARS) is a research area that has wide ranging applications. 
- Construction [[@petersenTERMESAutonomousRobotic]]
- Surveillance, Search and Rescue
	- Military
- Foraging and Flocking
	- Mining [[thangavelauthamAutonomousRobotSwarms2020]]
- Exploration
	- Inspection
- Cooperative Manipulation
- Team heterogeneity
- Adversarial Environment
- Agriculture
- IoT [[kamilarisPenetrationInternetThings2020]]

Most of these other ones are included in [[@schranzSwarmRoboticBehaviors2020]]

---

## Classification Frameworks 
### By behavior
- [[@brambillaSwarmRoboticsReview2013]]
	- ![[image-3-x42-y291.png| 100]]
![[brambillaSwarmRoboticsReview2013-2.png| 300]]
![[brambillaSwarmRoboticsReview2013-3.png| 350]]
![[brambillaSwarmRoboticsReview2013.png| 300]]
- ![[xieReconfigurableMagneticMicrorobot2019.png|275]]

### By testbed/agent type
- ![[schranzSwarmRoboticBehaviors2020.png |425]]
	- ![[arvinColiasAutonomousMicro2014.png|150]]
	- ![[KilobotsThousandRobotSwarm2014-3.png|175]]
![[arvinMonaAffordableOpenSource2019-1.png|250]]
![[kangMarsbeeSwarmFlapping2019-1.png|400]]

### Level of task automation [[@rizkCooperativeHeterogeneousMultiRobot2020]]
- ![[rizkCooperativeHeterogeneousMultiRobot2020.png|450]]
- ![[shahzadReviewSwarmRobotics2023-5.png|450]]

### Communication/control/architecture
- ![[anMultiRobotSystemsCooperative2023-1 1.png|375]]
- ![[anMultiRobotSystemsCooperative2023-2.png|400]]

![[parkerMultipleMob40-3.png|325]]
![[parkerMultipleMob40-2.png|325]]

## Notable Platforms
- Kilobot [[@KilobotsThousandRobotSwarm2014]]
- Khepera [[@fariasDevelopmentEasyUseMultiAgent2019]]
- Marsbee [[@kangMarsbeeSwarmFlapping2019]]
- RoboFly?
- Comrade system [[@dasguptaCOMRADESystemMultirobot2015]]
- Swarmanoid [[@dorigoSwarmanoidNovelConcept2013]]
- TraderBots [[@diasTraderBotsNewParadigm]]
- Robotarium [[wilsonRobotariumGloballyImpactful2020]]
- Particle robot swarm

## Notes
There isn't a shortage of capability, but there's absolutely a shortage of integration.

---

## Example Design Process
- "Behavior-based design is the most common way to develop a swarm robotics system" - [[@brambillaSwarmRoboticsReview2013]]
- Example workflow
	- Collective object transport
		- UGV vs UAV?
		- Communication scheme?
		- Existing testbench?
		- Redundancy?
		- Task allocation?
	- What if you want to apply the same method using different testbeds?
- We are reinventing the wheel each time we redo these systems papers

# Standardization Efforts
Naturally attempts to standardize and incorporate differing strengths from a variety of platforms has been undertaken

- ![[schranzSwarmRoboticBehaviors2020.png |500]]
[[@ramroopBioinspiredAggregationRobot2018]]
- Swarmanoid
- [ ] Research rabbit Swarmanoid

There hasn't been the widespread industry and/or research adoption. 

- There are quite a few examples within the industry , but there's a lack of entry-level standardization. 

A review on multi-robot systems categorized by application domains have happened repeatedly. 

---

# Problem Statement
There is a lack of standardization for entry-level end-to-end solutions in MARS research. 
- There is *especially* an issue with the entry costs and reinventing these robotic objects. 
- There is a gap between the educational platforms, the educational documentation/software, and the true cutting-edge robotic systems.
- We have the ingredients.

"To the best of our knowledge, there are no implementations of fully automated systems, i.e., a complex task was given to the MRS, and the system autonomously decomposed this complex task to sub-tasks, formed coalitions, and assigned and executed these sub-tasks." [[@rizkCooperativeHeterogeneousMultiRobot2020]]

## What has been proposed by the field?
Quotes from [[@dorigoReflectionsFutureSwarm2020]]:
 - [Q] First, the increasing complexity of swarm systems is such that their design cannot be accomplished solely by traditional approaches.
 - [Q] Second, in order for robot swarms to perform ever more complex tasks, they will likely need to be heterogeneous, both in hardware features and in roles that individual robots can play within the swarm.
 - [Q] Last, robot swarms should include mechanisms to allow hierarchical forms of control beyond traditional pure self-organization.

---

## Our proposal solution
We want to create a robotic system which bridges the gap between entry-level roboticists and the rest of the field. 
- Use open source code
- Avoid custom-built robots for demonstration, but provide a framework 

---

# Localization Methods
- Mocap
- SLAM
- IMU/gyroscope
- Beacon-based
	- Needs to have elicit search

![[michaelGRASPMultipleMicroUAV2010.png|250]]
[[preissCrazyswarmLargeNanoquadcopter2017]]
[[@pichierriCrazyChoirFlyingSwarms2023]]

# Methods
Place a lighthouse IR basestation on the underside of a Turtlebot, and use it to localize an aerial robot. 


---

# Results
## Simulation Success
WeBots exploring a graph

## Tracking Accuracy Graph
We were able to 

## Documentation source and walkthrough
## Nav2
I was focused on testing the rotation matrix. 

## Rotation Matrix Testing