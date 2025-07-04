---
id: rizkCooperativeHeterogeneousMultiRobot2020
type: citation_note
title: "Cooperative Heterogeneous Multi-Robot Systems: A Survey"
issued:
  date-parts:
    - - 2020
      - 3
title-short: Cooperative Heterogeneous Multi-Robot Systems
page: 1-31
URL: https://dl.acm.org/doi/10.1145/3303848
DOI: 10.1145/3303848
container-title: ACM Computing Surveys
volume: 52
number: 2
language: en
abstract: The emergence of the Internet of things and the widespread deployment of diverse computing systems have led to the formation of heterogeneous multi-agent systems (MAS) to complete a variety of tasks. Motivated to highlight the state of the art on existing MAS while identifying their limitations, remaining challenges, and possible future directions, we survey recent contributions to the field. We focus on robot agents and emphasize the challenges of MAS sub-fields including task decomposition, coalition formation, task allocation, perception, and multi-agent planning and control. While some components have seen more advancements than others, more research is required before effective autonomous MAS can be deployed in real smart city settings that are less restrictive than the assumed validation environments of MAS. Specifically, more autonomous end-to-end solutions need to be experimentally tested and developed while incorporating natural language ontology and dictionaries to automate complex task decomposition and leveraging big data advancements to improve perception algorithms for robotics.
tags:
  - literature_note
  - research
  - research/MARS
  - research/MARS/heterogeneous
  - research/review
author:
  - family: Rizk
    given: Yara
    literal: ""
  - family: Awad
    given: Mariette
    literal: ""
  - family: Tunstel
    given: Edward W.
    literal: ""
accessed:
  date-parts:
    - - 2024
      - 1
      - 12
citation-label: rizkCooperativeHeterogeneousMultiRobot2020
ISSN: 0360-0300, 1557-7341
keyword: MARS/platform/notable
year: "2020"
dateCreated: 2025-05-25
reading-status: to-read
aliases:
  - "Cooperative Heterogeneous Multi-Robot Systems: A Survey"
author-links:
  - "[[Author/Yara Rizk]]"
  - "[[Author/Mariette Awad]]"
  - "[[Author/Edward W. Tunstel]]"
attachment: []
related:
  - []
citation: "[[rizkCooperativeHeterogeneousMultiRobot2020]]"
rating: "5"
---

# Cooperative Heterogeneous Multi-Robot Systems: A Survey

## Summary
summary::
rating::

## Quotes

## Notes

## Figures

## References

🔗 [Source](https://dl.acm.org/doi/10.1145/3303848)

sibling:: [[note_diasMarketBasedMultirobotCoordination2006]],  [[@parkerMultipleMob40]]

# Notes 
summary:: VERY good review on heterogeneous swarms


## Scope
Other surveys
- Two of the closest were published in ~2010
	- [[diasMarketBasedMultirobotCoordination2006]] Focused on market-based approaches, did not include coalition formation and decision-making models.
	- [[@parkerMultipleMob40]] MRS architectures, communication schemes, swarm robotics, task allocation, and learning (foraging, formation control, cooperative object manipulation and displacement, path planning, and soccer)
- Other surveys with narrower scope
	- 

## Methods/Notes
Intelligent agent
- Has definition for an intelligent agent, and different workflows
	- Sense -> Plan -> act
	- Sense -> Act

### Multi-Agent Systems
#### Intelligent Agents
Perception, reasoning, learning, decision making, problem solving, interaction, and communication. 
Evaluation based on:
- Versatility, rationality, optimality, efficiency, scalability, autonomy, improvability. 

#### Multi-agent systems
Classification systems
1. homogeneous noncommunicative, homogeneous communicative, heterogeneous non-communicative, and heterogeneous communicative (Peter Stone and Manuela Veloso. 2000. Multiagent systems: A survey from a machine learning perspective. Auton. Robots 8, 3 (2000), 345–383.)
2. Agent diversity 
	- Can come from sensory/actuation capabilities, cognition levels and algorithms, morphology, 
3. Centralized, hierarchical, decentralized, hybrid architectures
	1. No direct interaction, simple interaction, complex conditional interaction
4. MAS can have positive vs negative interactions between other agents (This paper focuses on those with symbiotic relationships)
}
#### Task Taxonomy
#### Multi-robot system workflow
Items of MRS workflow
1. Task decomposition
2. Coalition formation 
3. Task allocation
4. Task execution/planning + control 
They'll present systems that are for various tasks,. 

#### Applications
##### 3rd level of automation
Ground
- [[jonesDynamicallyFormedHeterogeneous2006]] -bad treasure hunt
- [[arslanCoordinatedRobotNavigation2016]] -hierarchical clustering
- Cooperative exploration
	- [[daiCooperativeExplorationBased2016]]
	
Aerial
- [[@padmanabhanm_CoalitionFormationTask2015]] -simulation surveillance

##### 2nd level of automation
Task allocation and execution
Coalition formation and task execution
![[rizkCooperativeHeterogeneousMultiRobot2020.png|350]]
cooperative exploration is here too...
Listed papers
[[arslanCoordinatedRobotNavigation2016]]
[[@dasguptaCOMRADESystemMultirobot2015]]
[[@padmanabhanm_CoalitionFormationTask2015]]
[[jonesDynamicallyFormedHeterogeneous2006]]
[[liuCoalitionFormationMultiple2016]]
- [[@abukhalilCoordinatingHeterogeneousRobot2016]]
[[pujol-gonzalezEfficientInterTeamTask2015]]
[[manatharaMultipleUAVCoalitions2011]]
[[dossantosEfficientMultiagentTask2011]]
- [[kienerCooperationHeterogeneousAutonomous2007]]
- [https://doi.org/10.1016/j.robot.2014.10.008](https://doi.org/10.1016/j.robot.2014.10.008 "Persistent link using digital object identifier")
- [A Generic Framework for Distributed Multirobot Cooperation | Journal of Intelligent & Robotic Systems (springer.com)](https://link.springer.com/article/10.1007/s10846-011-9558-4)
- [A Distributed Task Allocation Algorithm for a Multi-Robot System in Healthcare Facilities | Journal of Intelligent & Robotic Systems (springer.com)](https://link.springer.com/article/10.1007/s10846-014-0154-2)

##### 1st level of automation
[[simmonsFirstResultsCoordination2001]]
[[dorigoSwarmanoidNovelConcept2013a]]
- [[murphyMarineHeterogeneousMultirobot2012]]
- [[gregoryApplicationMultiRobotSystems2016]] OmniMapper SLAM
- [[lesireDistributedArchitectureSupervision2016]] distributed architecture for autonomous supervision 
- [[@pippinDesignAirGroundResearch]] Ground based air-ground research platform for cooperative surveillance. Complex UAV+UGV system that can move around and such
- [[rosaMultitaskCooperativeControl2015]] Interesting one, pretty much just a simulation
- [[olleroMultipleEyesSkies2005]]  kinda boring, not really used
- [[portugalCooperativeMultirobotPatrol2016]]

### Existing MRS

## Intelligent Agents
## Context/Related Works
Papers on things not covered in scope:
- Luis Búrdalo, Andrés Terrasa, Vicente Julián, and Ana García-Fornes. 2018. The information flow problem in multiagent systems. Eng. Appl. Artif. Intell. 70 (April 2018), 130–141.
- Rajesh Doriya, Siddharth Mishra, and Swati Gupta. 2015. A brief survey and analysis of multi-robot communication and coordination. In Proceedings of the 2015 International Conference on Computing, Communication & Automation (ICCCA’15). IEEE, 1014–1021
Similar reviews/surveys:
- [[diasMarketBasedMultirobotCoordination2006]] Focused on market-based approaches, did not include coalition formation and decision-making models.
- [[@parkerMultipleMob40]] MRS architectures, communication schemes, swarm robotics, task allocation, and learning (foraging, formation control, cooperative object manipulation and displacement, path planning, and soccer)
Narrower surveys/reviews:
- Cooperative MAS planning/control[155] Liviu Panait and Sean Luke. 2005. Cooperative multi-agent learning: The state of the art. Auton. Agents Multi-Agent Syst. 11, 3 (2005), 387–434. ()
- Robot Architectures, mapping & exploration Arai et al
- Papers for:
	- control of multi-vehicle systems for military
	- patrolling
	- Decision-making algorithms
	- Implicit/explicit communication algorithm
	- Decision-making algorithms
Survey of autonomous robotic systems stuff 
- Matt Luckcuck, Marie Farrell, Louise Dennis, Clare Dixon, and Michael Fisher. 2018. Formal specification and verification of autonomous robotic systems: A survey. Arxiv Preprint Arxiv:1807.00048 (2018).
- Two of the most similar surveys were published in ~2010

## Figures + Data Tables
![[Pasted image 20240422094753.png|225]]

## Future Work
Challenges and insights
- Big data
- IoT
- Task complexity
- Autonomous Machine Learning
- Coalition Formation and Task Allocation
- Human in the loop
- Transfer Learning
- Unified Framework

### Figures + Data Tables
## Context/Related Works
## Future Work



# Quotes
- [Q] Few end-to-end frameworks have been presented for MRS; the most notable is swarmanoids
- [Q] "To the best of our knowledge, there are no implementations of fully automated systems, i.e., a complex task was given to the MRS, and the system autonomously decomposed this complex task to sub-tasks, formed coalitions, and assigned and executed these sub-tasks."
- [Q] Military applications such as surveillance, navigation, and target tracking have also developed MAS frameworks to efficiently automate these complex tasks. For illustration purposes, we discuss two scenarios in which MAS can be used: emergency response and health care.
- [Q] In smart cities, an elderly care system can consist of one or more mobile robots capable of providing round the clock physical care to elderly patients, and a monitoring system capable of recognizing the occurrence of falls or medical emergencies and notifying the mobile robots accordingly. The system can be expanded further by allowing it to communicate with the patient’s health care team and relatives for updates and medication delivery. A similar system was envisioned in Reference [11] to improve health care for children with complex conditions but did not include a robot agent. Kraus discussed the capabilities that a robot should possess to effectively aid patients with disabilities [111]. 
- [Q] We discuss some of these systems next, grouping them based on the complexity of the cooperative tasks they execute and their level of automation, from most to least automated. In the first level (least automated), only task execution is automated, while the second level also automates either task allocation or coalition formation but not both. The third level automates both coalition formation and task allocation but does not automate task decomposition. The fourth level automates the entire system.
- [Q] However, one reason that has hindered the successful deployment of fully automated MRS is the fact that most of the work has mainly dealt with these modules independently. Taking a more holistic approach by viewing these research fields as connected within a larger field is necessary to take steps toward successful MRS deployments. ... End-to-end simulations and real-world experiments will also help in improving the formulated models by identifying major weaknesses preventing successful deployment.