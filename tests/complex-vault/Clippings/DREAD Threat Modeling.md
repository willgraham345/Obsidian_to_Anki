---
title: "DREAD Threat Modeling"
source: "https://threat-modeling.com/dread-threat-modeling/#0-what-is-dread-threat-modeling"
author:
  - "[[nick]]"
published: 2023-09-25
created: 2025-09-02
description: "What is DREAD Threat Modeling DREAD threat modeling is a quantitive assessment regarding the severity of a threat, with a scaled rating assigned to risk. ... <a title=\"DREAD Threat Modeling\" class=\"read-more\" href=\"https://threat-modeling.com/dread-threat-modeling/\" aria-label=\"Read more about DREAD Threat Modeling\">Read More</a>"
tags:
  - "clippings"
  - "toread"
---
## What is DREAD Threat Modeling

[DREAD](https://satoricyber.com/glossary/threat-modeling-with-microsoft-dread/) [threat modeling](https://threat-modeling.com/) is a quantitive assessment regarding the severity of a threat, with a scaled rating assigned to risk. DREAD has five categories, consisting of **D** amage, **R** eproducibility, **E** xploitability, **A** ffected Users, and **D** iscoverability.

- Damage: The total damage (or impact) that a threat can cause.
- Reproducibility: The ease at which an attack can occur (or be replicated).
- Exploitability: How likely or easy the weakness or threat can be exploited.
- Affected Users: The number of (end) users that could be affected by a threat being exploited.
- Discoverability: How likely a threat will be discovered by an attacker.

DREAD is one of the available threat modeling methods. There are many others, such as [STRIDE](https://threat-modeling.com/what-is-stride-threat-modeling/), [PASTA](https://threat-modeling.com/pasta-threat-modeling/), and [LINDDUN](https://threat-modeling.com/linddun-threat-modeling/).

**Note:** DREAD threat modeling is not widely used anymore, it was initially developed by Microsoft, but its usage was discontinued due to the belief that its ratings are subjective (from those that perform DREAD threat modeling, and assign ratings).

![DREAD threat modeling categories
](https://threat-modeling.com/wp-content/uploads/2023/09/DREAD-threat-modeling-categories-410x1024.jpg)

DREAD threat modeling categories

## What is the DREAD Model

The DREAD model consists of quantifying the categories of Damage, Reproducibility, Exploitability, Affected Users, and Discoverability.

All five of these categories are given a rating on a scale of 0 to 10. An average is also calculated based on the individual ratings. This gives the final rating of the threat in scope.

### DREAD Category: Damage

Damage relates to the potential damage (or impact) a threat could cause if it is exploited by an attacker.

The ratings consist of:

- 0, which is no damage
- 5, which is information disclosure
- 8, which is non-sensitive data of individuals being compromised
- 9, which is non-sensitive administrative data being compromised
- 10, which is destruction of the system in scope, the data, or loss of system availability

### DREAD Category: Reproducibility

Reproducibility relates to how easily (or likely) an attack can be replicated.

The ratings consist of:

- 0, which is nearly impossible or difficult
- 5, which is complex
- 7.5, which is easy
- 10, which is very easy

### DREAD Category: Exploitability

Exploitability relates to how easily or likely a weakness or threat can be exploited.

The ratings consist of:

- 2.5, which requires advanced technical skills
- 5, which requires tools that are available
- 9, which requires application proxies
- 10, which (only) requires browser

### DREAD Category: Affected Users

Affected Users relates to the number of (end) users that could be affected by a threat being exploited.

The ratings consist of:

- 0, which is no users are affected
- 2.5, which is only individual users are affected
- 6, which is few users are affected
- 8, which is administrative users are affected (these are more important users)
- 10, which is all users are affected

### DREAD Category: Discoverability

Discoverability relates to how likely a threat will be discovered by an attacker.

The ratings consist of:

- 0, which is hard to discover
- 5, which is open requests can discover the threat
- 8, which is a threat being publicly known or found
- 10, which is the threat is easily discoverable, such as in an easily accessible page or form

## Overall DREAD Rating

After having assigned a threat rating for all of the DREAD categories, an overall DREAD rating can be calculated for the threat. This is simply a matter of adding up all the ratings.

Once all the ratings have been added, the overall threat criticality can be determined:

- **Low** for overall ratings between **1-10**, which is a low risk to the application or system in scope.
- **Medium** for overall ratings between **11-24**, which is a medium or moderate risk to the application or system in scope.
- **High** for overall ratings between **25-39**, which is a high or severe risk to the application or system in scope.
- **Critical** for overall ratings between **40-50**, which is a critical risk to the application or system in scope.

## What is the difference between STRIDE and DREAD threat modeling?

[STRIDE threat modeling](https://threat-modeling.com/stride-threat-modeling/) is a different kind of threat modeling methodology (or method) compared with DREAD threat modeling.

STRIDE is a mnemonic of six types of security threats. Each letter of STRIDE stands for one of the six types of security threats:

- **S** poofing
- **T** ampering
- **R** epudiation
- **I** nformation Disclosure
- **D** enial of Service
- **E** levation of Privilege

STRIDE threat modeling is helpful because it can tell us ‘what can go wrong’ on the application, system, IT landscape, or business process that we’re (threat) modeling.

Compare that to DREAD threat modeling, where the focus is on quantifying threats and less emphasis on identifying threats.

STRIDE and DREAD threat modeling can work well together because STRIDE can identify threats, and DREAD can quantify the threats identified.

Quantifying threats with DREAD is helpful because this information can help with the prioritization of threats.

## What is an Example of DREAD

Let’s take a very simple example.

The threat in question is:

- Attackers may be able to social engineer the helpdesk in order to gain access to organization user accounts. Some of these accounts may be administrative accounts.
- **Damage: 10** – Gaining access to user accounts, or administrative user accounts would allow an attacker to perform further attacks, including destruction of applications and systems.
- **Reproducibility: 5** – Social engineering requires skill, and the helpdesk employees have been trained to look out for social engineering attacks. There are also procedures in place regarding user account actions (like resetting accounts, etc.).
- **Exploitability: 5** – Exploiting the accounts would still require access to the organization network.
- **Affected Users: 8** – Administrative accounts may be targeted.
- **Discoverability: 8** – The helpdesk is widely known within the organization, and anyone (inside or outside) can reach the helpdesk.

**Overall score: 36, which is a High overall rating.**

**Note:** See how the above scores are subjective, other professionals may assign higher or lower ratings for the DREAD categories.

## What is DREAD Analysis

DREAD analysis consists of threat modeling of an application (or product), to quantify threats.

DREAD analysis adds a layer of quantification so that threats are given category (**D** amage, **R** eproducibility, **E** xploitability, **A** ffected Users, and **D** iscoverability) ratings, and also an overall rating.

The analysis phase assigns the 0-10 values to each threat category.

## What is the DREAD Model in Cyber Security?

A DREAD model in cyber security consists of a specific DREAD threat modeling session, and its outcome (which is a threat model).

A DREAD model has DREAD ratings for all threats in scope of the threat modeling. Once DREAD ratings have been defined, the threats can be prioritized. This helps with remediation (highest threats can be remediated first).

Threat-Modeling.com Bot

Hello! I've been trained on threat modeling data. Ask me anything about threat modeling!

Show Common Questions

🤖

Chat with AI