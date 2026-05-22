---
title: "Understanding and investigating adversary threats and countermeasures in the context of space cybersecurity"
source: "https://ieeexplore.ieee.org/abstract/document/9925759"
author:
  - "[[Kathiravan Thangavel]]"
  - "[[Jordan Joseph Plotnek]]"
  - "[[Alessandro Gardi]]"
  - "[[Roberto Sabatini]]"
published:
created: 2025-09-02
description: "Satellite technologies are used for both civil and military purposes in the modern world, and typical applications include Communication, Navigation and Surveil"
tags:
  - "clippings"
  - "toread"
---
Loading \[MathJax\]/extensions/MathZoom.js

Understanding and investigating adversary threats and countermeasures in the context of space cybersecurity | IEEE Conference Publication | IEEE Xplore 

---

With the digital revolution, our reliance on space, and particularly satellites, for telecommunications, defense, intelligence, and commerce has increased rapidly. Unfortunately, the threats have also increased, necessitating the urgent need to strengthen cybersecurity practices surrounding space assets. The proliferation of satellites, rockets, and space shuttles have increased the attack surface for threat actors looking to impact the space ecosystem. Critical businesses such as transportation, energy, and other critical infrastructures as shown in Fig. 1, depend on space systems to operate effectively, and hence such systems require protection. This expansion is fueled by a growing reliance on space applications as well as a dynamically changing environment characterized by the New Space Age, which is being fueled by competitive private investments. As a result, access to space has become less expensive, faster, and easier. It has also led to innovations in the ability to deploy end-to-end space systems and use ‘Ground Segment as a Service’ (GSaaS). Although threats to space-based assets have long been recognized, securing against them has not been a high priority. Space systems have grown in prominence, significance, and technological complexity, making them a prime target for cybercriminals. Despite the global reliance on them, space products and services are also inherently valuable due to their incorporation of cutting-edge technologies and valuable intellectual property.

[![Fig 1. - 
Satellite infrastructure operations.
](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/9925245/9925721/9925759/thang1-p10-thang-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/9925245/9925721/9925759/thang1-p10-thang-large.gif)

**Fig 1.**

Satellite infrastructure operations.

They are also a key target for state actors due to their use by governments and defense organizations for applications and services such as communications, observation, and navigation. Given the amount of equipment in space and our reliance on it, it has increasingly become designated as critical infrastructure by nations around the world. Cellular communications, GPS navigation, weather, and climate monitoring, managing Internet of Things (IoT) systems for agribusiness, and keeping energy or other critical infrastructure operating are all dependent on operational space infrastructure. And this infrastructure is alarmingly vulnerable. Outages can have far-reaching, cascading, and potentially fatal repercussions. A single damaged satellite can disrupt global networks, leaving areas lacking cellular and other critical operations. As a result, malicious attackers find them appealing targets. Satellites could be attacked in a variety of ways. Hackers might get access to ground control systems to remotely operate space equipment, or they could implant malware via communication channels between computers on the ground and deployed satellites. They can counterfeit, snoop on, or disrupt communications for espionage objectives. Consider a weather data outage during a hurricane, or data errors that cause power outages or supply chain disruptions. The financial and societal costs can be enoromous.

Space technology gives countries and their entities a huge civil and defense advantage, meaning that an adversary will almost certainly try to degrade, deny, or disrupt access to space system capabilities [\[1\]](https://ieeexplore.ieee.org/abstract/document/). Fig. 2 depicts a list of the most common hazards and threats, as well as the severity associated with each. From the figure it is evident that cyber-attacks cannot be avoided, and last year alone more than 20 cyber-attacks have occurred as per the Space Threat Assessment 2022 Report by CSIS Aerospace Security Project [\[2\]](https://ieeexplore.ieee.org/abstract/document/). By its very nature, space systems security is an interdisciplinary field of study. Various technical disciplines play an important role in safeguarding the space technology ecosystem from outside threats. Table I below attempts to map the domain of space systems security. The table’s rows reflect various threats to space systems in general, while the columns indicate the attack surface (i.e., vectors/entrance points into the system). Although most cyberattacks on space systems are reversible to some extent, their trusted autonomous operation in space necessitates cybersecurity against cyber threats. Autonomous orbit replanning is required in the event of orbital threats such as debris or satellite collision. Table II presents the different types of counter space weapons [\[2\]](https://ieeexplore.ieee.org/abstract/document/), [\[3\]](https://ieeexplore.ieee.org/abstract/document/).

[![Fig. 2. - 
Range of threats to spacecraft [1].
](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/9925245/9925721/9925759/thang2-p10-thang-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/9925245/9925721/9925759/thang2-p10-thang-large.gif)

**Fig. 2.**

Range of threats to spacecraft [\[1\]](https://ieeexplore.ieee.org/abstract/document/).

**TABLE 1.** SPACE SYSTEMS SECURITY KNOWLEDGE DOMAIN \[4\].

**TABLE II.** TYPES OF COUNTERSPACE WEAPONS \[2\].

### A. Cyberspace

Cyberspace is the notional environment in which communication over computer networks occurs. Within the aerospace domain, research in cyberspace has increased significantly over the past number of years. The Fourth Industrial Revolution (Industry 4.0) of the twenty-first century, fueled by the rapid and disrupting exponential growth of machine learning and accelerated by the synergy of cyberspace and Artificial Intelligence (AI), has taken on a vital role in modern defense and security [\[5\]](https://ieeexplore.ieee.org/abstract/document/) - [\[7\]](https://ieeexplore.ieee.org/abstract/document/). Cyberspace is a complex hierarchal structure of interconnected technological and semantic layers (physical, logical, information, and human). People regularly employ information in their day-to-day activities, making it the most valuable resource in this domain. Information is a critical ontological unit in cyberspace, and it may also be viewed through the lens of traditional metaphysics. Aristotle’s metaphysics, for example, is made up of substance (material correlate) and form (idea correlate). Its potency is derived from data, and its authenticity is derived from the information or quality of the information [\[8\]](https://ieeexplore.ieee.org/abstract/document/). As demand for space assets has expanded, the threat environment they face has altered. Satellites have long benefited from ‘security by obscurity,’ in which the system’s complexity and high equipment costs dissuade all but the most sophisticated cyber-attackers. However, implementation diversity and complexity are unlikely to ensure long-term security due to the increasing digitization and usage of Commercial Off-The-Shelf (COTS) software and components, and constellations containing thousands of satellites with similar vulnerabilities and attack surface [\[9\]](https://ieeexplore.ieee.org/abstract/document/). The cyber threat to satellites is now widely recognized and somewhat intuitive in today’s highly connected and digital world.

Military C4ISR (Command, Control, Communications, Computers, Intelligence, Surveillance, and Reconnaissance) capabilities rely heavily on space systems [\[10\]](https://ieeexplore.ieee.org/abstract/document/). In fact, rivals seeking to ‘level the playing field’ with great powers have a strong motivation to target satellites [\[11\]](https://ieeexplore.ieee.org/abstract/document/). Whether it is positioning data for modern transportation and logistics or meteorological facilities that safeguard millions from disasters, the general public is heavily reliant on space services, whether they know it or not. Satellites may appeal to those seeking to disrupt society as a ‘single point of failure’ in critical infrastructures [\[12\]](https://ieeexplore.ieee.org/abstract/document/). When we refer to cyberspace, it possesses cyber-threats which have to be explicitly considered and addressed during both the design and operational phases. By integrating intelligent agents for trusted autonomous operation, extra care should be taken to ensure a resilient system that is able to withstand cyber threats [\[8\]](https://ieeexplore.ieee.org/abstract/document/), [\[13\]](https://ieeexplore.ieee.org/abstract/document/) - [\[17\]](https://ieeexplore.ieee.org/abstract/document/).

Fig. 3 depicts the NIST Cybersecurity Framework (CSF), which is built on a cybersecurity risk management strategy that can be customized for various sectors. It creates a common language and approach that organizations can employ in accordance with their resources and business requirements. The CSF has five functions: identify, protect, detect, respond, and recover. The functions are shown in a circular pattern to highlight that cybersecurity is a never-ending process that allows an enterprise to traverse the ever-changing world of cybersecurity threats [\[18\]](https://ieeexplore.ieee.org/abstract/document/), [\[19\]](https://ieeexplore.ieee.org/abstract/document/).

**Fig. 3.**

Cybersecurity framework [\[18\]](https://ieeexplore.ieee.org/abstract/document/).

### B. Inter-vehicle cybersecurity

In the case of space systems, inter-vehicle cybersecurity refers to the ability of a space vehicle (e.g., a satellite) to defend itself from cybersecurity threats as per Fig. 3, including pre-emptively identifying and protecting against cyber threats, detecting and responding to an attack, and recovering post-impact. These elements should be implemented early in the system’s life cycle and incorporated into the system development process, commonly referred to as ‘security by design’. Inter-vehicle cybersecurity is frequently the responsibility of small commercial satellite owners and operators, while most of the rest of the infrastructure is outsourced to other suppliers and providers. Table III is taken from a NIST publication and provides a list of common cyber events that can occur in satellite operations and their corresponding impacts on business [\[18\]](https://ieeexplore.ieee.org/abstract/document/). Notably a number of these cybersecurity impacts can result in a total loss of the satellite vehicle itself. Table IV is taken from a paper by Pavur and Martinovic and gives a complete list of satellite threat actors, their primary motivations for attack, and their relative technical capabilities based on open source data [\[9\]](https://ieeexplore.ieee.org/abstract/document/).

**TABLE III:** COMMON CYBERSECURITY EVENTS \[18\].

TABLE IV provides a composite summary of threat actors as a starting point for developing threat models. It primarily considers motivation and the technological capabilities of space actors [\[9\]](https://ieeexplore.ieee.org/abstract/document/), [\[20\]](https://ieeexplore.ieee.org/abstract/document/).

**TABLE IV.** COMPLETE LIST OF SATELLITE THREAT ACTORS \[9\].

A high-level summary of the space-cyber threat environment as described above was provided by Plotnek and Slay in Fig. 4 below [\[21\]](https://ieeexplore.ieee.org/abstract/document/),

**Fig. 4.**

High-level overview of cyberthreats to space infrastructure [\[21\]](https://ieeexplore.ieee.org/abstract/document/).

When thinking about space-cyber security it is crucial to think not only about who might want to harm space systems, but also how they might go about doing so. Scenario modelling is a common component of strategic analysis in security studies and international relations and similarly provides a useful perspective for technical security analysis. Chatham House divides assaults on satellites (for example, via control system exploitation) and cyberattacks on satellite ground stations (for example, by ordinary network intrusion) as two categories [\[22\]](https://ieeexplore.ieee.org/abstract/document/). Pavur and Martinovic expand on Chatham House’s taxonomy [\[9\]](https://ieeexplore.ieee.org/abstract/document/) to provide a greater diversity of viewpoints on space system attacks. They identified three assault surfaces: those involving satellite signals, the space platform, and the satellite ground systems. Although other alternative models divide ground systems into "Customer" and "Mission" sectors, Pavur and Martinovic discovered that the bulk of investigated threat models affect both use-cases and hence separating the two does not provide much utility in the context of space-cyber threats. The proposed attack surface categories from this same paper are shown in TABLE V [\[9\]](https://ieeexplore.ieee.org/abstract/document/).

**TABLE V.** BROAD CATEGORIES OF ATTACK SURFACES. ADAPTED FROM \[9\].

The space community recognizes that the operational space environment is changing quickly. Nation states do not have a monopoly on space technology any longer. The only certainty is that the space community will have to navigate an increasingly crowded future filled with friendly, hostile, and new players competing for bandwidth and dominance. As a result of this shift, threats to the space domain and its supporting infrastructure have increased [\[23\]](https://ieeexplore.ieee.org/abstract/document/). To guarantee mission success, ground and space system architectures are required to provide a high level of resilience. During decision-making, resilience should be treated as an essential design consideration to be traded alongside cost and capability [\[24\]](https://ieeexplore.ieee.org/abstract/document/).

When it comes to high-tech civil and military applications, space is almost ubiquitous, from GPS-guided munitions to Communications, and Intelligence, Surveillance, and Reconnaissance (ISR). The importance of space-based services for military operations has grown to the point where most states openly acknowledge their reliance on the domain. Most states assume the presence of space support in any operation for these reasons. Still, only a few clearly understand its contributions, let alone the consequences of disruption or substantial degradation of any space services [\[1\]](https://ieeexplore.ieee.org/abstract/document/), [\[5\]](https://ieeexplore.ieee.org/abstract/document/), [\[24\]](https://ieeexplore.ieee.org/abstract/document/) - [\[26\]](https://ieeexplore.ieee.org/abstract/document/). The Aerospace Corporation has created a taxonomy that examines a system’s ability to meet mission requirements throughout its entire lifecycle. Although the metrics identified in this framework are notably missing any reference to cyber threats, as shown in Fig. 5, they can nevertheless be used to aid in identifying mission assurance metrics from a cybersecurity perspective. Detailed definitions of each metric can be found in Ref [\[26\]](https://ieeexplore.ieee.org/abstract/document/).

**Fig. 5.**

Overview of the resiliency framework [\[26\]](https://ieeexplore.ieee.org/abstract/document/).

Threats that may impact the mission, as well as possible strategies, can be identified once mission requirements and essential functions have been identified. The strategy is a means of achieving a goal, and it is critical to determine the threat’s objectives. Before mission threats can be completely understood and evaluated for all consumers in the community, mission criteria and objectives must be properly established. This taxonomy framework, at a high level, encompasses any space assets that require resilient solutions. The taxonomy presented in Fig. 5 takes into account mission, operational, and acquisition considerations, highlighting the multitude of resilience solutions available to meet community needs. It is purposefully mission independent and organization agnostic. An example of how the framework presented can be applied to a cyber-attack (Control System Hijack) at a mission and functional level is shown in Fig. 6.

**Fig. 6.**

Threat illustration Adapted from [\[26\]](https://ieeexplore.ieee.org/abstract/document/).

From a conceptual standpoint, mission assurance can be considered in terms of domains: alternative domain mission assurance (which in this case means non-space), multi-domain or ‘cross-domain’ mission assurance (which includes both space and non-space domains), and in-domain (space only) mission assurance [\[24\]](https://ieeexplore.ieee.org/abstract/document/). Fig. 7, illustrates the mission assurance-related approach. Although the cybersecurity resilience of space systems requires an approach that considers all three domains, the six principles of Disaggregation, Distribution, Diversification, Deception, Protection, and Proliferation (D4P2) are examples of complementary resilience strategies that can be implemented to assure the space segment mission. These strategies are further elaborated in Ref [\[24\]](https://ieeexplore.ieee.org/abstract/document/).

**Fig. 7.**

Mission Assurance Taxonomy [\[24\]](https://ieeexplore.ieee.org/abstract/document/).

Where the framework at Fig. 5, provides an approach to derive the needs for architectural resiliency based on mission requirements, and the D4P2 taxonomy at Fig. 7, provides a list of strategies to assure space mission resilience against cyber threats, the final component to implementing resilience by design is an understanding of what space systems must achieve to be considered resilient to cyber threats.

In a recently published whitepaper, Plotnek and Slay propose an initial definition of Space Systems Resilience based on tangential critical infrastructure resilience literature [\[27\]](https://ieeexplore.ieee.org/abstract/document/):

*"The recurring ability of a space system, including all sub-components and supporting functions, to anticipate, survive, sustain, recover from, and adapt to high impact low frequency (HILF) events".*

In this definition the five key resilience features shown in Fig. 8 are defined as:

1. ***Anticipate***: the space system’s features in place to prevent, detect, and avoid cyber events,
2. ***Survive***: the space system’s features in place to mitigate, absorb, and withstand the impacts of a cyber event,
3. ***Sustain***: the space system’s features in place to contain any impacts and preserve core functions during a cyber event,
4. ***Recover***: the space system’s features in place to respond, restore operations, and ‘bounce back’ from a cyber event, and
5. ***Adapt***: the space system’s features in place to reflect on lessons learned and adopt new mechanisms to increase resilience for any similar cyber events in the future.

**Fig. 8.**

Space resilience taxonomy.

**Fig. 9.**

Space resilience lifecycle.

Another key feature of this definition is the emphasis on High Impact Low Frequency (HILF) events, also commonly referred to as ‘black swan’ events. This contrasts to Low Impact High Frequency (LIHF) events, which are primarily a function of reliability rather than resilience. In either case, once an impact is detected it sets off a survival response (i.e., a state transition from Anticipate to Survive). The ultimate post-cycle residual impact as shown in Fig. 9 is then felt by both the system and/or the environment in which the system is situated. It should also be noted that these phases or states are not mutually exclusive nor linear and can occur simultaneously and in varied sequence.

Numerous methods exist to reduce the risks inherent in operating civilian and commercial space systems, while also increasing the cyber-resilience of that space system. To effectively manage risk, decision-makers should first model the threat environment of the given system and then determine the likelihood (i.e., vulnerability vs threat intent vs threat capability) of various attacks targeting the availability, integrity, or confidentiality of the system’s core components. Then they should assess the potential impacts of each attack, considering the operational criticality of each component under attack as well as the technical, economic (including reputational), and social impacts. Next, the risk assessors should select the most appropriate strategy for treating the identified risks, which could be to avoid, transfer, accept, or mitigate them. In the case of risks requiring mitigation, stakeholders have the final responsibility of deciding which security controls should be implemented in order to reduce the risk to an acceptable level. This decision should be based on a cost-benefit analysis or a feasibility assessment to justify the control choice, or lack thereof. It is unrealistic to expect to completely remove all potential risks, and no decision-maker possesses the limitless budget or manpower to eradicate all potential threats. When acquiring or constructing a cyber-resilient spacecraft, decision-makers, acquisition professionals, program managers, and system designers should keep the following critical considerations in mind [\[28\]](https://ieeexplore.ieee.org/abstract/document/):

- ❖ Intrusion detection and prevention onboard spacecraft using signatures and machine learning to detect and prevent cyber intrusions
- ❖ A supply chain risk management approach to guard against the introduction of malware into parts and modules
- ❖ Software assurance procedures used across the software supply chain to limit the risk of cyberattacks on flight software and firmware
- ❖ Logging onboard the spaceship to ensure that genuine operations are being carried out and to aid in forensic investigations in the event of an anomaly
- ❖ Software and firmware integrity is ensured by the Root of Trust (RoT).
- ❖ A tamper-resistant method of restoring the spacecraft to a known cyber-safe mode
- ❖ Cryptographic systems that are light enough to be used in small satellites
- ❖ Employ a zero-trust security strategy in space systems to minimize risk of compromise post-deployment.

### A. Zero-Trust Architecture

Zero trust is a security framework that states that no individual or service should be trusted by default. Zero trust is a cybersecurity technique in which security policies are applied based on context – not assumed trust – established through least-privilege access control and stringent user authentication. A well-tuned Zero Trust Architecture (ZTA) simplifies network infrastructure and strengthens cybersecurity. The maxim "never trust, always verify" is followed by a ZTA. To prevent inappropriate access and lateral movement around an environment, a ZTA enforces access regulations, depending on context, the participant’s role and location, their equipment, and the data they are requesting. Establishing a ZTA necessitates visibility and control over users and traffic in the environment, including encrypted traffic; monitoring and verification of traffic among parts of the environment; and robust multifactor authentication (MFA) methods other than passwords, such as biometrics or one-time codes. In a ZTA, the network location of a resource is no longer the most important factor in its security posture. Instead of inflexible network segmentation, software-defined micro segmentation protects data, workflows, services, and other assets, allowing you to keep them secure wherever, whether in your data center or in dispersed hybrid and multi-cloud settings. User identity, segmentation, and protected access aren’t the only aspects of zero trust, it is a plan for establishing a cybersecurity ecosystem. Three principles are at the heart of it [\[29\]](https://ieeexplore.ieee.org/abstract/document/):

- ❖ Terminate every connection
- ❖ Granular context-based policies are used to protect data
- ❖ Reduce the risk of an attack by reducing the attack surface.

A review of assets, subjects, data flows, and workflows should be conducted before attempting to add ZTA to an organization. This is the foundational state that must be achieved before a ZTA deployment can be carried out. Without knowledge about the current state of operations, an organization cannot identify what new procedures or systems are required. These surveys can be undertaken concurrently, but they are both linked to an analysis of the organization’s business operations. Fig. 9. depicts the steps involved in implementing a ZTA.

**Fig. 10.**

ZTA deployment cycle [\[29\]](https://ieeexplore.ieee.org/abstract/document/).

In larger debates about cybersecurity threats to critical national infrastructure, the susceptibility of satellites as well as other space assets to cyberattack is sometimes underestimated. Neither space policy nor cybersecurity policy, particularly for spacecraft, are equipped for the difficulties posed by the merging of space and cyberspace (i.e., space-cyber). In the lack of official policies and rules, corporations and governments can begin to implement defenses across the entire space system to strengthen security. Decision makers must finally decide which Defense-in-Depth (DiD) concepts to employ in order to limit risks. Not all risks can be avoided, and no decision-maker has unrestricted budget or sufficient personnel to address all threats. Along the entire space supply chain, governments and international entities must develop international standards for protecting space technology. There are existing cybersecurity guidelines that can be modified and used to improve the security of the space industrial environment. The zero trust architecture is one such approach that is currently being promoted for space systems. Devices and hardware are hermetically sealed from the standpoint of a system’s access with zero trust, restricting unwanted user authentication and authorization even within an organization. Because of the decentralized nature of zero trust architecture, even when a hacker is able to access systems on the ground, acquiring additional access is greatly impaired. The United States’ National Institute of Standards and Technology (NIST) could also play a key role in promoting uniform cybersecurity protocols. With the private sector taking even more adventurous forays into space, it is inevitable that space technology and activities will become increasingly entwined with our terrestrial economy. The task of protecting such critical infrastructure from malicious cyber actors is immense, but not insurmountable. By building on existing private-public partnerships and creating creative frameworks that all space firms may use internationally, we can explore the final frontier in a safe and secure manner.

[PDF](https://scholar.google.com/scholar_url?url=https://ieeexplore.ieee.org/iel7/9925245/9925721/09925759.pdf&hl=en&sa=T&oi=ucasa&ct=usl&ei=Lx23aPD6A4fC6rQPgLuo8Qc&scisig=AAZF9b9resHmcxLmbgbMXDrMIT5-) [Help](https://scholar.google.com/scholar/help.html#access)