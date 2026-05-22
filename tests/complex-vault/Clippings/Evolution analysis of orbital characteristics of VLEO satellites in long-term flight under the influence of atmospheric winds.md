---
title: "Evolution analysis of orbital characteristics of VLEO satellites in long-term flight under the influence of atmospheric winds"
source: "https://www.sciencedirect.com/science/article/abs/pii/S0094576525008641"
author:
  - "[[AbstractVery Low Earth Orbit (VLEO) has attracted growing attention due to its unique advantages in Earth observation and communication applications; however]]"
  - "[[it also faces severe challenges arising from atmospheric perturbations. Although orbital decay caused by atmospheric drag can now be compensated by high-efficiency electric propulsion systems]]"
  - "[[the evolution of the spacecraft’s dynamic state under the influence of atmospheric winds continues to pose substantial challenges for attitude and orbit control in long-duration VLEO missions]]"
  - "[[warranting further systematic investigation. However]]"
  - "[[quantitative analyses describing this effect remain limited]]"
  - "[[particularly those employing coupled aerodynamic attitude–orbit dynamics models that comprehensively account for atmospheric density]]"
  - "[[temperature]]"
  - "[[and wind variations.To address this issue]]"
  - "[[an analytical expression for the variation of orbital inclination (i) in a near-circular VLEO orbit (e¡0.001) is first derived based on the Gaussian Variational Equations in this paper. The derivation elucidates the mechanism through which the orbital angular momentum vector gradually evolves toward the North Pole under the influence of atmospheric winds. In parallel]]"
  - "[[the study investigates the effect of winds on the Right Ascension of the Ascending Node (Ω<math><mi is=\"true\">Ω</mi></math>)]]"
published:
created: 2025-12-09
description: "Very Low Earth Orbit (VLEO) has attracted growing attention due to its unique advantages in Earth observation and communication applications; however,…"
tags:
  - "clippings"
  - "toread"
---
[![Elsevier](https://www.sciencedirect.com/us-east-1/prod/2db38c166d265b778aaea2e2f0075e275b306509/image/elsevier-non-solus.svg)](https://www.sciencedirect.com/journal/acta-astronautica "Go to Acta Astronautica on ScienceDirect")

## Acta Astronautica

Available online 5 December 2025

[In Press, Journal Pre-proof](https://www.sciencedirect.com/journal/acta-astronautica/articles-in-press)

## Research paperEvolution analysis of orbital characteristics of VLEO satellites in long-term flight under the influence of atmospheric winds

[https://doi.org/10.1016/j.actaastro.2025.12.009](https://doi.org/10.1016/j.actaastro.2025.12.009 "Persistent link using digital object identifier") [Get rights and content](https://s100.copyright.com/AppDispatchServlet?publisherName=ELS&contentID=S0094576525008641&orderBeanReset=true)

## Highlights

- •
	The wind’s effect on VLEO satellite’s RAAN is identified as primarily indirect, realized through coupling with J2 perturbations via inclination change.
- •
	In-orbit data validation confirms that including the wind-inclination coupling is crucial for the accurate long-term prediction of VLEO orbits.

## Introduction

The Very Low Earth Orbit (VLEO) regime, spanning altitudes of approximately 100–350 km, offers substantial advantages over conventional Low Earth Orbits (LEO). Specifically, compared with a 500 km orbit, VLEO enables approximately a twofold improvement in remote sensing resolution for the same payload, a two- to fourfold enhancement in communication data rates at equivalent power, and a 20%–40% reduction in launch costs. Consequently, VLEO holds immense potential for deploying next-generation large-scale communication and remote sensing constellations \[1\], \[2\], \[3\]. In recent years, a series of pioneering flight demonstration missions and cutting-edge technology studies have been undertaken globally to validate the engineering feasibility of VLEO and to explore its complex space environment. The European Space Agency’s (ESA) Gravity field and steady-state Ocean Circulation Explorer (GOCE) satellite achieved long-term drag-free flight at an altitude of approximately 250 km using an ion propulsion system. This mission not only established a milestone for VLEO flight but also left a valuable legacy of in-situ atmospheric data—particularly the thermospheric density and wind information retrieved from its thruster and accelerometer data, which has provided a critical foundation for understanding the complex dynamics of this region \[4\]. Japan Aerospace Exploration Agency’s (JAXA) Super Low Altitude Test Satellite (SLATS) ventured even lower, into orbits below 200 km, with a focus on in-orbit measurements of material degradation in the high-flux Atomic Oxygen (AO) environment \[5\]. Similarly, the Satellite for Orbital Aerodynamics Research (SOAR) mission was dedicated to the in-orbit measurement of aerodynamic coefficients and the validation of Gas-Surface Interaction (GSI) models in a rarefied atmosphere \[6\]. Concurrently, to fundamentally overcome the mission lifetime limitations imposed by propellant constraints, Air-Breathing Electric Propulsion (ABEP) and related commercial concepts are developing rapidly. The European Union’s DISCOVERER project has deeply explored mission scenarios and key technologies for ABEP \[7\], while the REGULUS project by T4i has successfully demonstrated a cathode-less radio-frequency thruster suitable for the VLEO environment in orbit \[8\]. Furthermore, the vibrant activity in this domain is evidenced by other initiatives, including the EU’s AETHER project and various studies on commercial VLEO concepts. These research efforts are not limited to system-level architecture but also delve into micro-scale physical mechanisms. Examples include the optimized design of air intakes for rarefied flow conditions \[9\] and the complex coupling effects between electric thruster plumes and the ionosphere/thermosphere—specifically, plume-induced Charge-Exchange (CEX) and its potential impact on aerodynamic drag \[10\]. These pioneering works demonstrate that the successful implementation of VLEO missions is highly dependent on a profound understanding of the atmospheric environment and its interaction mechanisms with spacecraft.

Despite these significant advantages, the dense atmosphere in this region poses severe challenges. The atmospheric density—several orders of magnitude higher than that in conventional LEO \[11\]—gives rise to two primary perturbation effects. First, the intense atmospheric drag necessitates that spacecraft maintain continuous and efficient thrust to compensate for the associated energy loss. This “thrust–drag balance” is crucial for maintaining orbital altitude, a challenge that is now being addressed through rapid advancements in technologies such as high-efficiency electric propulsion (e.g., air-breathing and metal-ion systems) and drag reduction techniques for rarefied atmospheres \[12\], \[13\], \[14\]. Second, atmospheric winds, with velocities reaching several hundred meters per second in inertial space \[15\], generate considerable lateral aerodynamic forces. These forces continuously perturb the orbital plane, profoundly affecting missions that require precise orbit determination and complicating the long-term trajectory of spacecraft.

For instance, conventional Sun-synchronous orbits (SSOs) are designed to exploit the nodal precession caused by Earth’s oblateness (primarily the $J2$ term), matching the precession rate to Earth’s mean orbital rate around the Sun to ensure consistent surface illumination conditions. In VLEO, however, the superposition of aerodynamic forces induced by winds and $J2$ perturbations can disrupt this delicate balance, leading to a precession rate mismatch that causes traditional SSOs to lose their synchronicity. Furthermore, a special class of SSOs, the “dawn–dusk” orbits, rely on this synchronicity to remain continuously sunlit, thereby maximizing solar energy acquisition \[16\]. This feature is of paramount importance for power-demanding VLEO satellites, as it directly affects their energy budget and operational lifetime \[17\].

Therefore, with the along-track drag problem being progressively mitigated, it becomes crucial to understand and predict the long-term evolution of coupled attitude–orbit dynamics induced by atmospheric winds, necessitating the development of precise dynamical models. Accordingly, this paper investigates the orbital perturbation characteristics of a satellite undergoing long-term thrust–drag balanced flight under the influence of atmospheric winds, aiming to provide insights for station-keeping technologies in future large-scale VLEO constellations.

The study first analyzes the perturbation characteristics of a near-circular satellite orbit under atmospheric wind influence using a theoretical approximate model. Subsequently, a dynamic simulation platform was developed that integrates the HWM14 atmospheric wind model and the NRLMSIS2.1 atmospheric density model. This platform is employed to further investigate the coupled perturbation effects of atmospheric winds and the $J2$ term in a complex environment. Finally, the findings are validated against in-orbit data from an operational satellite.

## Section snippets

## Atmospheric density distribution

The most prominent feature of the VLEO region relevant to orbital flight is its exceptionally high atmospheric density \[11\]. Compared with conventional LEO altitudes above 400 km, the density in VLEO is more than two orders of magnitude greater and can exceed that of higher altitudes by several hundred times. Fig. 2 presents a logarithmic plot of the mean atmospheric density as a function of altitude (see Fig. 1).

Moreover, the atmospheric density in the VLEO regime exhibits pronounced

## Fundamental assumptions

To perform a preliminary analysis of the orbital evolution of VLEO satellites influenced by atmospheric winds, the following fundamental assumptions are introduced to simplify the analytical model:

**Assumption 1**

The spacecraft maintains a continuous thrust–drag equilibrium in the along-track direction, with its solar panels confined to the orbital plane. Consequently, atmospheric winds are considered the primary source of perturbative acceleration normal to the orbital plane. However, it is important to note

## Conclusion

This study presents a comprehensive investigation into the effects of atmospheric winds on the long-term orbital evolution of Very Low Earth Orbit (VLEO) satellites operating in near-circular orbits ($e<0.001$). A unified analytical framework was developed, encompassing theoretical derivation, numerical simulation, and in-orbit data validation. The main conclusions are summarized as follows:

- (1)
	**Atmospheric winds induce a monotonic decay of orbital inclination.** The inertial wind serves as the dominant

## CRediT authorship contribution statement

**Guanzhong Chen:** Writing – original draft, Visualization, Software, Methodology, Formal analysis, Data curation. **Zhengrui Li:** Visualization, Software. **Guanhua Feng:** Writing – review & editing, Visualization, Resources. **Wenhao Li:** Writing – review & editing, Supervision, Resources. **Yuxian Yue:** Writing – review & editing, Supervision, Project administration, Methodology, Investigation, Formal analysis, Conceptualization.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

- *et al.*
	### The benefits of very low earth orbit for earth observation missions
	### Prog. Aerosp. Sci.
	(2020)
- *et al.*
	### System modelling of very low earth orbit satellites for earth observation
	### Acta Astronaut.
	(2021)
- *et al.*
	### MDM: A flight mission to observe materials degradation in-situ on satellite in super low Earth orbit
	### Acta Astronaut.
	(2021)
- *et al.*
	### In-orbit aerodynamic coefficient measurements using SOAR (satellite for orbital aerodynamics research)
	### Acta Astronaut.
	(2021)
- *et al.*
	### Cathode-less RF plasma thruster design and optimisation for an atmosphere-breathing electric propulsion (ABEP) system
	### Acta Astronaut.
	(2024)
- *et al.*
	### Design and optimisation of a passive atmosphere-breathing electric propulsion (ABEP) intake
	### Acta Astronaut.
	(2023)
- *et al.*
	### Characterising satellite aerodynamics in very low Earth orbit inclusive of ion thruster plume-thermosphere/ionosphere interactions
	### Acta Astronaut.
	(2020)
- *et al.*
	### Atmospheric density estimation in very low Earth orbit based on nanosatellite measurement data using machine learning
	### Aerosp. Sci. Technol.
	(2024)
- *et al.*
	### Air-breathing electric propulsion: Flight envelope identification and development of control for long-term orbital stability
	### Acta Astronaut.
	(2022)
- *et al.*
	### Aerodynamic drag analysis and reduction strategy for satellites in very low Earth orbit
	### Aerosp. Sci. Technol.
	(2023)

- *et al.*
	### CHAMP and GOCE thermospheric wind characterization with improved gas-surface interactions modelling
	### Adv. Space Res.
	(2019)
- ### Thermospheric mass density: A review
	### Adv. Space Res.
	(2015)
- *et al.*
	### A planning tool for optimal three-dimensional formation flight maneuvers of satellites in VLEO using aerodynamic lift and drag via yaw angle deviations
	### Acta Astronaut.
	(2022)
- *et al.*
	### Investigation of very low earth orbits (VLEOs) for global spaceborne lidar
	### CEAS Space J.
	(2022)

This work is supported by Chinese Academy of Sciences ().

[View full text](https://www.sciencedirect.com/science/article/pii/S0094576525008641)