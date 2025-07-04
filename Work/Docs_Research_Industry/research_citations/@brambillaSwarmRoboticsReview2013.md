---
id: brambillaSwarmRoboticsReview2013
type: citation_note
title: "Swarm robotics: a review from the swarm engineering perspective"
issued:
  date-parts:
    - - 2013
      - 3
title-short: Swarm robotics
page: 1-41
URL: https://doi.org/10.1007/s11721-012-0075-2
DOI: 10.1007/s11721-012-0075-2
container-title: Swarm Intelligence
volume: 7
number: 1
language: en
abstract: "Swarm robotics is an approach to collective robotics that takes inspiration from the self-organized behaviors of social animals. Through simple rules and local interactions, swarm robotics aims at designing robust, scalable, and flexible collective behaviors for the coordination of large numbers of robots. In this paper, we analyze the literature from the point of view of swarm engineering: we focus mainly on ideas and concepts that contribute to the advancement of swarm robotics as an engineering field and that could be relevant to tackle real-world applications. Swarm engineering is an emerging discipline that aims at defining systematic and well founded procedures for modeling, designing, realizing, verifying, validating, operating, and maintaining a swarm robotics system. We propose two taxonomies: in the first taxonomy, we classify works that deal with design and analysis methods; in the second taxonomy, we classify works according to the collective behavior studied. We conclude with a discussion of the current limits of swarm robotics as an engineering discipline and with suggestions for future research directions."
tags:
  - literature_note
  - research/influential
  - research/MARS
  - research/MARS/review
  - research/MARS/workflow/coalition_formation
  - research/MARS/workflow/communication
  - research/MARS/workflow/cooperation
  - research/MARS/workflow/cooperation/object_transport
  - research/MARS/workflow/cooperation/tasks
  - research/review
author:
  - family: Brambilla
    given: Manuele
    literal: ""
  - family: Ferrante
    given: Eliseo
    literal: ""
  - family: Birattari
    given: Mauro
    literal: ""
  - family: Dorigo
    given: Marco
    literal: ""
accessed:
  date-parts:
    - - 2023
      - 3
      - 24
citation-label: brambillaSwarmRoboticsReview2013
ISSN: 1935-3820
keyword: influential,review,MARS/review
year: "2013"
dateCreated: 2025-05-25
reading-status: to-read
aliases:
  - "Swarm robotics: a review from the swarm engineering perspective"
author-links:
  - "[[Author/Manuele Brambilla]]"
  - "[[Author/Eliseo Ferrante]]"
  - "[[Author/Mauro Birattari]]"
  - "[[Author/Marco Dorigo]]"
attachment: []
related:
  - []
citation: "[[brambillaSwarmRoboticsReview2013]]"
rating: "4"
---

# Swarm robotics: a review from the swarm engineering perspective

## Summary
summary::
rating::

## Quotes

## Notes

## Figures

## References

🔗 [Source](https://doi.org/10.1007/s11721-012-0075-2)

# Notes 
summary:: Great review on how different swarms can be characterized based on behavior, and a better outline of what that behavior entails 


## Scope
## Methods/Notes
### Figures + Data Tables
![[image-3-x42-y291.png|400]]
![[brambillaSwarmRoboticsReview2013.png| 300]]
![[brambillaSwarmRoboticsReview2013-1.png| 300]]

![[brambillaSwarmRoboticsReview2013-2.png| 300]]
![[brambillaSwarmRoboticsReview2013-3.png| 350]]
![[brambillaSwarmRoboticsReview2013-4.png|300]]

## Context/Related Works
## Future Work


# Quotes
 *format with* `- [Q]`
 - [Q] “to the swarm engineer, the important points in the design of a swarm are that the swarm will do precisely what it is designed to do, and that it will do so reliably and on time” (Kazadi 2000).
 - [Q] Behavior-based design is the most common way to develop a swarm robotics system. In an iterative way, the individual behavior of each robot is implemented, studied, and improved until the desired collective behavior is obtained. In behavior-based design, inspiration is often taken from the observation of the behaviors of social animals. This may ease the design process as, sometimes, the details of a particular behavior are already understood and mathematical models are available. Another way to develop swarm robotics systems is via automatic design methods. Automatic design methods can be used to reduce the effort of the developers in creating a collective behavior. We classify automatic design methods in two categories: evolutionary robotics and multi-robot reinforcement learning. Brambilla et al. (2012) proposed a top-down method to design swarm robotics systems. Their idea is to define the desired system using a set of properties.
- [Q] Approaches In swarm robotics, the most common way to tackle area coverage is to use virtual physics-based design to obtain a grid covering the environment. Works on swarmguided navigation instead focus on communication, thus usually employ probabilistic finite state machines and take inspiration either from network routing protocols or natural systems.
- [Q] Stirling and Floreano (2010) used a swarm of flying robots to achieve area coverage. In their work, the robots are deployed sequentially and each robot determines its position according to the position of the previously deployed robots. Only one or few robots, called explorers, are flying at the same time, whereas the great majority is attached to the ceiling and act as communication relay. One particular aspect of Stirling and Floreano’s approach is the ability to explore an environment with a limited number of robots, as the robots can leave an area once it has been visited. This work was developed for the Swarmanoid project