---
title: "Cybersecurity Risk Assessment for Space Systems"
source: "https://ieeexplore.ieee.org/abstract/document/8853713"
author:
  - "[[Ly Vessels]]"
  - "[[Kenneth Heffner]]"
  - "[[Daniel Johnson]]"
published:
created: 2025-09-02
description: "When considering critical infrastructure, we rarely consider the enabling technology and systems that realize such infrastructure; such as, agribusiness' relian"
tags:
  - "clippings"
  - "toread"
---
Cybersecurity Risk Assessment for Space Systems | IEEE Conference Publication | IEEE Xplore 

## Abstract:

When considering critical infrastructure, we rarely consider the enabling technology and systems that realize such infrastructure; such as, agribusiness' reliance on weat...

---

Much of the critical infrastructure relies on satellites and space systems. Transportation depends on global positioning system (GPS) satellites. Communications depend on telecommunication satellites. The food industry uses GPS and weather and climate satellites. It is hard to find any industry that does not have a critical dependence of some form on space systems.

However, despite efforts to improve the cybersecurity of critical infrastructure, there has been little focus on cybersecurity for space systems. Challenges to secure space systems include technology development, ownership, and management perspective. This leads to the lack of guidance in the form of standards that govern space system security and, ultimately, policies that enforce these standards.

An initial step in controlling any area of risk is to put in place means for measuring and assessing the risks. This paper discusses how the unique nature of the satellite cybersecurity threat will shape a Space-system Security Engineering Risk Assessment Methodology (SSERAM). Then the paper presents a proposed approach to a SSERAM by tailoring a Honeywell technique for assessing security risks for safety-critical systems like space systems. The paper concludes with a discussion of possible next steps in advancing cybersecurity for space systems.

A framework for risk assessment for satellites must include considerations for the unique features of Space Systems. These considerations should include:

- An understanding of the assets, their required security properties, and the severity of the loss of those properties.
- An understanding of the exposure to the threat environment.
- An understanding of the threat environment, attackers and their capabilities, and the likelihood of an attack.
- An understanding of restrictions and requirements regarding candidate security controls.

**Availability and accessibility are the** major **security properties at stake in the satellite cyberthreat**.

In 2012 there was a programming challenge, DroneGames, held in San Francisco [\[2\]](https://ieeexplore.ieee.org/abstract/document/) on interesting applications for a semi-autonomous radio-controlled drone, the Parrot AR.drone. Second place was a program to control multiple drones from a single computer. But first place went to a drone that would infect any other drone it encountered, causing them to “run amok” despite the best efforts of the controllers. Like satellites, the drones had complete dependence on the radio spectrum for both data and control. A cyber-attack that renders the satellite inaccessible by ground control results in the catastrophic loss of the asset, even if it was “only” a Denial-Of-Service attack that in other sectors would be considered only a minor nuisance.

**Space Systems are continually exposed to attack from their control and data streams**.

In 2016, there were 1046 active satellites, from 47 nation-states. In the same year, Amdhi [\[1\]](https://ieeexplore.ieee.org/abstract/document/) cited several alleged cases in which satellite command and control systems were penetrated to the point where the attacker had achieved the ability to issue commands to the satellite control systems. Multiple reported instances of hijacked satellite transmissions and security research demonstrations have also shown the ready exposure of satellites to attack.

With the availability of VSAT ground systems able to directly connect to satellites, and the flexible capabilities of Software-Defined Radio (SDR), radio transmission is no longer the barrier that it was. But there is no longer even a need to go that far; satellite systems can have live connections through their ground control networks to the internet. An attacker can thus choose from multiple avenues of attack depending on the connectivity of the satellite and the resources available to the attackers:

- Attacks through co-orbital assets,
- Attacks through SDR transceivers,
- Attacks through ground terminals,
- Attacks through ground control networks,
- Attacks through proprietary ground communications networks, and
- Attacks through public networks.

**The capabilities of expected attackers are at the** Nation- **State level, so the Attack Likelihood is so high, it no longer helps in discriminating between security practices**.

It is a common dogma in cybersecurity that the likelihood of attack depends largely on the capability and motivation of the attacker. In the case of satellites, the worst-case motivation and capability are posed by the nation-state, and by those covert attack threats such as APT who have demonstrated significant resources and alignment with national interests. Nation-states have launched orbital assets with explicit anti-satellite capabilities. Anti-satellite actions are part of standard military doctrine among multiple nation-states. So, the base likelihood of an attack is a certainty - high-capability attackers will attack satellites.

In addition, satellites have long service lives and routinely function through several cycles of terrestrial technical progress. It is necessary to change the risk assessment focus from what attackers could do given their capabilities, to a worst-case assumption of what an attacker could do given the satellite's capabilities. The beginnings of this can be found in the safety analysis process for commercial aircraft, where the goal is to be able to state that any harmful event that could occur will occur unless there is verification and assurance that it won't occur. More formally, consistent with the commercial aerospace cybersecurity assessment methodologies such as DO-356A [\[5\]](https://ieeexplore.ieee.org/abstract/document/), a means to mitigate the impact of potential attacks is to reduce the likelihood of a successful attack, which in practice means to increase the coverage by the security controls, and to reduce the likelihood that the security controls fail or are defective.

**Controls on the ground control networks are necessary, but not sufficient. Assessment of technical controls needs to include consideration of detection, response, and restoration controls**.

While ground control networks can be protected through their cybersecurity controls, radios can contact satellites outside the ground control systems. In the case of attacks outside the ground control networks, the only protection are the embedded technical security controls on the satellite.

Controls that prevent access by attackers such as encryption are important, but with the long service lives of satellites, the encryption algorithms are subject to obsolescence. The ability to monitor and respond to attacks on the satellite becomes an important means to respond to the changing threat environment. An effective monitoring control would be one that can detect the technical precursors to an attack before the attack renders the satellite unresponsive to ground control. Even more critical is the ability to restore the satellite to a secure and functional state.

In financial systems, security control should be Fail-Secure. In commercial aircraft, security controls may need to be Fail-Open to retain pilot access to critical flight control functions. For satellites, the issue is maintaining the availability of the asset, even if this means a temporary loss of functional availability. For a satellite, security controls need to be Fail-Restorable- if a security control fails, it needs to fail in a manner that will allow accessibility of the satellite to be restored.

In other cyber-physical systems, an important control is “Secure Boot,” the ability to ensure that when a device resets, it will use a trusted core as the initial software basis. In the case of satellites, this functionality can be extended to “Secure Restoration,” the ability to ensure that the Secure Boot includes sufficient functionality to render the satellite accessible to its ground control.

### A. Overview of the Airworthiness Security Risk Assessment Framework

There are various techniques for evaluation vulnerabilities; the most recognize is Microsoft Vulnerability Assessment Tool (MSAT) [\[7\]](https://ieeexplore.ieee.org/abstract/document/), Operationally Critical Threat and Vulnerability Evaluation (OCTAVE) [\[1\]](https://ieeexplore.ieee.org/abstract/document/), Central Computer and Telecommunications Agency Risk Analysis and Management Method (CRAMM) [\[9\]](https://ieeexplore.ieee.org/abstract/document/), Consultative Objective and Bi-Functional Risk Analysis (COBRA) [\[10\]](https://ieeexplore.ieee.org/abstract/document/), and Information Security Risk Analysis Method (ISRAM) [\[6\]](https://ieeexplore.ieee.org/abstract/document/) to name just a few. The most recognized is MSAT. These tools evaluation domain is enterprise IT. The closest method to the critical infrastructure domain is the Boolean Logical driven Markov Processes (BDMP) [\[3\]](https://ieeexplore.ieee.org/abstract/document/). BDMP is a formalism that focuses on the modeling and lacks the complete definition for how to determine security risk acceptability. on the modeling and lacks the complete definition for how to determine security risk acceptability.

[![Figure 1: - Airworthiness security process security risk assessment framework](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8848568/8853649/8853713/319400a011-fig-1-source-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8848568/8853649/8853713/319400a011-fig-1-source-large.gif)

**Figure 1:**

Airworthiness security process security risk assessment framework

The Radio Technical Commission for Aeronautics (RTCA) has developed and published two documents that provide the process and guidance for airworthiness security certification [\[4\]](https://ieeexplore.ieee.org/abstract/document/) [\[5\]](https://ieeexplore.ieee.org/abstract/document/). Within the DO-326A Airworthiness Security Process is the framework for Security Risk Assessment (SRAF). The framework consists of three major phases (Threat Condition Identification and Evaluation, Threat Scenario Identification, Security Measure Characterization, and Level of Threat Evaluation). The *Threat Condition Identification and Evaluation* phase determines the threat conditions that arise from existence vulnerabilities of the system under evaluation. In the next phase (*Threat Scenarios Identification*), threat scenarios are identified and are used to classify pertinent information about potential successful attacks. The security measures are characterized in the phase of the framework. These are security measures that protect the system against unauthorized interaction. Next, the Security Measures Characterization Phase provides security measure is characterized by its type, effectiveness, and vulnerabilities. Finally, in the Level of Threat Evaluation step, the framework calls for an evaluation of the possibility that threat scenarios cause a threat condition, which is based on the threat scenarios, security environment, and security measure characteristics.

Per the summary in Figure 1, the SRAF requires the security scope and the system architecture to produce, and it produces the Security Risks that can be used to determine acceptability. SRAF provides an approach for assessing and determining the acceptability of security risks of safe-critical systems (e.g., space systems and avionics systems).

### B. Instantiation of the Airworthiness Security Risk Assessment Framework

The SRAF provides valuable guidance and a path to a standardized process for determining security risks for safety-critical based systems (such as space systems). This greatly advanced the maturity of cybersecurity for critical infrastructure. However, as a framework, it doesn't provide sufficient information to use it as a method for execution. An alternative tool for security risk assessment is presented to address this gap and provide for evaluation of safety-critical systems. This method (called Honeywell Security Risk Assessment (HSRA)) is an instantiation of the Airworthiness Security Risk Assessment Framework. The method is summarized in Figure 2.

[![Figure 2. - Honeywell security risk assessment method](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8848568/8853649/8853713/319400a011-fig-2-source-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8848568/8853649/8853713/319400a011-fig-2-source-large.gif)

**Figure 2.**

Honeywell security risk assessment method

#### Create Security Architecture

As captured in Figure 2, the first step, in the Honeywell Security Risk Assessment, is to create the security architecture (SA). The purpose of the SA is to establish the functional architecture of the security controls and assets, and the intended operational environment relative to information security. In specific, SA identifies the assets, document the points of entry to the assets, and determine their environment. It consists of two parts: (1) security perimeter and (2) security environment. The security perimeter is a notational boundary between the internal security context and the external system environment of the system. It is the point where security control changes. Inside the security perimeter, it contains all the security-relevant assets and security measures. The Security Environment is a notational boundary that captures everything outside the security perimeter that interacts with assets inside the Security Perimeter.

Figure 3 depicts a notational representation of the output from the Security Architecture. The artifact produced by this step captures the following security items: attacker, access vectors, threat conditions, security measures, and vulnerabilities. These elements serve as inputs into the next step.

#### Define Security Risk Elements

As captured in Figure 2, the second step, in the Honeywell Security Risk Assessment, is to define the system security risk elements and to assign risk metrics to these elements. This is the most critical step of the process because it is the step that defines the security risk elements, which are inputs into the entire analysis.

First, Honeywell uses the Security Architecture to derive the security risk elements, which are attackers, access vectors, vulnerabilities, security measures, threat conditions, and asset. Their definitions are captured in Table 1.

[![Figure 3. - Notational representation of a security architecture](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8848568/8853649/8853713/319400a011-fig-3-source-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8848568/8853649/8853713/319400a011-fig-3-source-large.gif)

**Figure 3.**

Notational representation of a security architecture

Next, the security risk elements (attackers, access vector, security measure, threat condition, vulnerability, asset) are assigned a value. Since we are determining the security risks in the safety-critical domain, Honeywell based the security risk element value type on the standard Fault Modes and Effects Analysis (FMEA) methodology. The definition of these value type is:

- SEVERITY (SEV) - What is the impact on the assets? It represents the magnitude of the harm to flight safety of a threat condition. It is expressed in a scale 1–9, and it is compatible with standard Safety Impact Metrics.
- OCCURRENCE (OCC) - What are the causes and how often will it occur? It represents the attacker characteristics, primary role, privileges, and trustworthiness. It is expressed in a scale 1–9, and it was developed to be compatible with standard Safety Reliability Metrics.
- PREVENTION (PREV) - What are the existing controls and procedures that prevent the cause or impact on assets? It represents the effectiveness of the security measures, technical and organizational. It is expressed in a scale 1–9, and it was developed to be compatible with standard Safety Assurance Levels.

**Table 1:** Security risk element

[![Table 1:- Security risk element](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8848568/8853649/8853713/319400a011-table-1-source-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8848568/8853649/8853713/319400a011-table-1-source-large.gif)

The type of value associated with each security risk element is summarized in Table 1. The value range and scale are shown in Table 2.

**Table 2:** Security risk element assigned values

[![Table 2:- Security risk element assigned values](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8848568/8853649/8853713/319400a011-table-2-source-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8848568/8853649/8853713/319400a011-table-2-source-large.gif)

The value assigned to the security risk elements will depend on the value type.

- Severity: The severity value is assigned based on the impacts of the security risk element (if it is exploited) onto the system. For example, the impact of the failure of the Avionics Noise Break System is catastrophic; thus, it is assigned the value of 9 to the asset.
- Occurrence: The occurrence value is given to the attacker based on the trustworthiness of the attacker, which is correlated to the asset. For instance, the maintenance crew has a high trust; therefore, it is given the value of 1.
- Prevention: The prevention value is allocated to the vulnerabilities. It is determined based on how much assurance is associated with the vulnerability; how robustness is the vulnerability. For example, the defect in the software of the Avionics Noise Break System is 1 since it has a high assurance level associated with the software.

Identifying the security risk elements and the associated values is a critical step in the process because it is the foundation for the analysis. The final output depends on the accuracy of these data.

#### Create Security Models

As captured in Figure 2, the third step in the Honeywell Security Risk Assessment is to create security models that can be formally analyzed to determine the paths and risks of an attack. (Identify Threat Scenarios). The basic process is (1) create the Security Ontology, (2) create the Threat Tree, and (3) calculate the Risk Level.

[![Figure 4. - Security ontology modelling](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8848568/8853649/8853713/319400a011-fig-4-source-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8848568/8853649/8853713/319400a011-fig-4-source-large.gif)

**Figure 4.**

Security ontology modelling

The first step is to define the Security Ontology Diagram, which provides a notational relationship among the assets, attackers, access vectors, vulnerabilities, threat conditions, and security measure (see Figure 4). The relationship captures the threat conditions of the systems.

[![Figure 5. - Threat T= ree eomnosition patterns](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8848568/8853649/8853713/319400a011-fig-5-source-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8848568/8853649/8853713/319400a011-fig-5-source-large.gif)

**Figure 5.**

Threat T= ree eomnosition patterns

There exist technologies that can be used to automate the modeling of security ontology. Honeywell uses Microsoft VISIO to assist in the modeling.

[![Figure 6. - Security threat tree modelling](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8848568/8853649/8853713/319400a011-fig-6-source-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8848568/8853649/8853713/319400a011-fig-6-source-large.gif)

**Figure 6.**

Security threat tree modelling

The next step is to create a threat tree using the security ontology diagram created in the previous step. A threat tree is a graphical mechanism used to model the logical computation required to calculate the probability of a security risk for each threat condition with the security measure incorporated. Figure 5 shows an example of a threat tree.

A threat tree is similar to a fault tree in safety-critical modeling. As shown in Figure 5, the threat tree uses logic gates (AND, OR) to construct the threat condition.

Once the threat tree is composed, the threat tree is used to calculate the probability of the threat condition. The inputs (leaves) of the threat tree are vulnerabilities and attackers. The output (root) of the threat tree is the threat condition. The inner nodes are a combination of security measures blocking the attacker from exploiting its weaknesses, the access vector of the exploitations, and other threat conditions.

To construct the threat tree, use the following rules. The rules are pictorially presented in Figure 6:

- Security Measure (see Figure 6a): logical AND of a vulnerability and an attacker
- Access Vector (see Figure 6b): logical OR of zero or more of security measures, threat conditions, access vectors, and at least one attacker
- Threat Condition (see Figure 6c): logical OR of zero or more of access vectors, threat conditions, a vulnerability, security measures or assets

All these patterns can be combined in various ways to create the threat tree of a threat condition.

To calculate the probability for a cutset, converted the assigned values of the threat tree inputs to probabilities. Use Table 2 to perform the conversion. As prescribed in Table 2, a vulnerability with a PREV of 5 is converted to 10E-05. Once all the inputs are converted to probabilities, perform the logical AND and OR function to get the intermediate probabilities until it reaches the root node. Every possible path through the threat tree is called a cutset. The cutsets are analyzed to find the cutsets. The probability of a given cutset is the probability of a mitigated risk of the attack path.

To find the Risk Level for mitigated risk of a cutset, use the following formula:
$$
\begin{align*}
&[Max\ (cutset\ severity)+log_{10}\ (mitigated\ risk\ of\ a\\
&\ \ \qquad\qquad\quad\qquad\qquad cutset)]/2
\end{align*}
$$
 View Source

Note, this equation amount to a subtraction because a probability is negative.

[![Figure 7. - Residual security risk level metrics](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8848568/8853649/8853713/319400a011-fig-7-source-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8848568/8853649/8853713/319400a011-fig-7-source-large.gif)

**Figure 7.**

Residual security risk level metrics

The cutset, its mitigated probability, and its risk level are used as inputs to derive the Threat Scenarios of the system.

#### Identify Threat Scenarios

As captured in Figure 2, the fourth step, in the Honeywell Security Risk Assessment, is to identify threat scenarios, the probability of mitigated risk, and the risk level. In this step, all the threat conditions are evaluated looking for commonality that can be grouped to create a threat scenario. Each group is given a name. The mitigated risk probability and risk level of a threat scenario is the probability and risk level in the collection.

These threat scenarios and their risk levels are used to determine acceptability.

#### Determine Acceptability

As captured in Figure 2, the fifth step, in the Honeywell Security Risk Assessment, is to determine acceptability for each threat scenario.

To determine whether a security risk of a threat scenario is acceptable, the residual risk level of the threat condition and the criticality of the assets to look up acceptability using the table in Figure 7.

If the residual risk level is not acceptable, then the system design needs refactoring, or additional security measures are needed.

This process is used to assess the security risk of safety-critical systems.

The security risk assessment method was used in assessing various safety-critical systems. The results have been used to certify avionics systems through the aviation authorities.

This section presents excerpts of a security risk assessment data for a fictitious space system (see Figure 8). Nothing in Figure 8 is real, including the actual system names, components, and assessment values are not real information. Any resemblance to the actual system name is to ease with readability; it is not intended for correlation with the real system.

[![Figure 8. - Example of a space system (fictitious)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8848568/8853649/8853713/319400a011-fig-8-source-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8848568/8853649/8853713/319400a011-fig-8-source-large.gif)

**Figure 8.**

Example of a space system (fictitious)

The value and meaning are not correct; it is only intended to be viewed as an example of the outputs of the HSRA method.

The main component is the Orion CEV and its experiments/payload (mission packages). The Orion CEV communicates with its command and control system and from there to the general NASA Mission Network. The mission packages may have a ground control aspect, but they primarily transmit their empirical data to sponsors in the Institutional Network. The primary means of the communications is through the Communications Relay Satellite and the various commercial Satellite Communications Systems that are hosted on the CRS.

### A. Security Architecture

Figure 9 demonstrates an example of a security architecture representing the security aspect of the Space System example in Figure 8.

### B. Security Risk Elements & Associated Values

Figure 10 (see next page) demonstrates an example of the security risk elements and their assigned values. The table does not capture all of the values of the Space System in Figure 8. Additionally, these values are assigned to the security elements based on security expert assessment.

### C. Security Ontology

Figure 11 demonstrates an example of a security ontology diagram. The security ontology shown is only a portion of the complete relationship of the Space System example in Figure 8.

### D. Security Threat Tree

Figure 12 demonstrates an example of a security threat tree diagram. The security attack tree is just a sample of the complete attack tree for the Space Systems example in Figure 8.

[![Figure 9. - Excerpt of a security architecture](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8848568/8853649/8853713/319400a011-fig-9-source-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8848568/8853649/8853713/319400a011-fig-9-source-large.gif)

**Figure 9.**

Excerpt of a security architecture

[![Figure 11. - Excerpt of a security ontology diagram](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8848568/8853649/8853713/319400a011-fig-11-source-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8848568/8853649/8853713/319400a011-fig-11-source-large.gif)

**Figure 11.**

Excerpt of a security ontology diagram

[![Figure 10. - Excerpt of the security risk elements and assigned values](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8848568/8853649/8853713/319400a011-fig-10-source-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8848568/8853649/8853713/319400a011-fig-10-source-large.gif)

**Figure 10.**

Excerpt of the security risk elements and assigned values

[![Figure 13. - Excerpt of threat scenarios and risk acceptability](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8848568/8853649/8853713/319400a011-fig-13-source-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8848568/8853649/8853713/319400a011-fig-13-source-large.gif)

**Figure 13.**

Excerpt of threat scenarios and risk acceptability

[![Figure 12. - Excerpt of a security threat tree](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8848568/8853649/8853713/319400a011-fig-12-source-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8848568/8853649/8853713/319400a011-fig-12-source-large.gif)

**Figure 12.**

Excerpt of a security threat tree

### E. Threat Scenario

Figure 13 (see the previous page) demonstrates examples of security threat scenarios.

### F. Security Risk Acceptability

Figure 12 shows the mitigated risk level. Using tables in Figure 7, CUT53 has a medium risk level with a value of 0.5, while CUT18 has a low risk level with a value of −8.0.

Note, that migrated risk of less than 0 is acceptable; however, any migrated risks above 2 is not acceptable. It requires refactoring of the system designs to incorporate additional security measures. Any migrated risk equals to 1 is acceptable with some additional operational guidance.

Cybersecurity for space systems is still in its infancy. Quantum leap in technology and standards are expected as more investments are made in commercial space, autonomous vehicle, industrial internet of things, and argumentation. The Honeywell Security Risk Assessment method will be an essential tool in ensuring that these systems are securing at the right security robustness. Therefore, the HSRA must be agile and capable of assessing all cyber-physical systems. To meet this tenet, HSRA must be agile, capable of assessing security risks of all safety-critical systems. This is accomplished through automation of the HSRA Method. This is the next step in the maturity of the method. Honeywell is automating the method such that it can be quickly pivoted to assess all safety-critical systems (including space systems).

Another improvement is adding an expert system to the tool such that it provides a list of suggested values to assign to the security risk elements. The system continuously grows and updates based on the known security vulnerabilities, threats, and the type of the system under assessment. A quintessential next step for HSRA is the adaption of the method as an augmentation to DO-356A and other cyber-physical standards. Honeywell is currently participating in multiple standard consortiums. HSRA or aspects of the method will be recommended to these workgroups.

Space systems are fast becoming a target of cyber-crimes. The effect of cyber-attacks on critical-infrastructure and cyber-physical systems will cripple the foundation that is essential to the daily operation of our lives. More importantly, in some cases, human lives are at stake. Honeywell has created a security risk assessment method (called Honeywell Security Risk Assessment (HSRA) Method) that enables for assessing security risks of a safety-critical system (e.g., space systems) to determine the system acceptability for operation. The method is being automated by Honeywell to provide an end-to-end system for quickly and easily determines the risk of any cyber-physical systems.

[PDF](https://scholar.google.com/scholar_url?url=https://ieeexplore.ieee.org/iel7/8848568/8853649/08853713.pdf&hl=en&sa=T&oi=ucasa&ct=usl&ei=pRu3aPKiPJ6s6rQPxqLhuQI&scisig=AAZF9b-ko2DM8ujIo0poankexz50) [Help](https://scholar.google.com/scholar/help.html#access)