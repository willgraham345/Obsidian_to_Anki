---
type: note
---
# Questions
1. State of Swarm Research? State of multi-robot systems
	1. State of robotic frameworks and platforms?
	2. [[MARS.Reviews]]
3. What advantages does our approach to swarm and systems present?
	1. Other notable papers in the field?
	2. How can this work be built upon?
4. What is our ROS2 architecture?
	1. What capabilities does this present?
5. How does the lighthouse compare to a Vicon motion-capture system?
6. How does the lighthouse manage faults?
7. Latency and accuracy?


Why did we choose this platform
- Lightweight
- A standard in the research community, with lots of open-source development support
- Easily replaceable parts if failure occurs. 

Advantages we have
- The smaller the object, the more necessary motion capture becomes. We need motion capture to push forward towards mm-level robotic platforms. Quadrotors are the most common aerial platform in robotics. Other quadrotor platforms include [[kushleyevSwarmAgileMicro2013]], 

Future Work Section
This paper and system's contribution is when people are able to take this framework and corresponding source code and implement it onto their own robotic systems. There are a variety of papers that can be helpful for discussing aerial quadrotor dynamics in [[@lupashinPlatformAerialRobotics2014]], [[@michaelGRASPMultipleMicroUAV2010]], 

- Better mapping algorithms i.e. [[bothaPrototypeDesignAerial2023]]
- Adapting this to other systems [[bothaPrototypeDesignAerial2023]]
- Implementation of a low-level controller [[lambertLowLevelControlQuadrotor2019]]
- Implementation of battery Discharge Model [[poskartMultiParameterPredictiveModel2022]]