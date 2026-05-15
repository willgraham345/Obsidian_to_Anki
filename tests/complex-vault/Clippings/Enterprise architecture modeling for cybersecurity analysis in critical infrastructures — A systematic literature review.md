---
title: "Enterprise architecture modeling for cybersecurity analysis in critical infrastructures — A systematic literature review"
source: "https://www.sciencedirect.com/science/article/pii/S1874548224000416"
author:
  - "[[AbstractAs digital landscapes become increasingly complex]]"
  - "[[safeguarding sensitive information and systems against cyber threats has become a paramount concern for organizations. This paper provides a comprehensive review of how enterprise architecture modeling is used in the context of cybersecurity assessment]]"
  - "[[particularly focusing on critical infrastructures. The use of enterprise architecture models for cybersecurity is motivated by the main purpose of enterprise architecture]]"
  - "[[namely to represent and manage business and IT assets and their interdependence. While enterprise architecture modeling originally served to assess Business/IT alignment]]"
  - "[[they are increasingly used to assess the cybersecurity of the enterprise. The research questions explored include the types of enterprise architecture models used for cybersecurity assessment]]"
  - "[[how security aspects are incorporated into these models]]"
  - "[[the theoretical frameworks and reference theories applied]]"
  - "[[the research methods used for evaluation]]"
  - "[[and the strengths and limitations of these models in supporting cybersecurity assessment. This review encompasses research papers published before 2024]]"
  - "[[focusing on high-quality research from peer-reviewed journals and reputable conferences]]"
published:
created: 2025-09-02
description: "As digital landscapes become increasingly complex, safeguarding sensitive information and systems against cyber threats has become a paramount concern…"
tags:
  - "clippings"
  - "toread"
---
- [View **PDF**](https://www.sciencedirect.com/science/article/pii/S1874548224000416/pdfft?md5=3326a4f8e4e756d23a99269e52d923f9&pid=1-s2.0-S1874548224000416-main.pdf)

[![Elsevier](https://www.sciencedirect.com/us-east-1/prod/109afa3497c088f78e984e28c290d9e4dcc120bf/image/elsevier-non-solus.svg)](https://www.sciencedirect.com/journal/international-journal-of-critical-infrastructure-protection "Go to International Journal of Critical Infrastructure Protection on ScienceDirect")

## International Journal of Critical Infrastructure Protection

[Volume 46](https://www.sciencedirect.com/journal/international-journal-of-critical-infrastructure-protection/vol/46/suppl/C "Go to table of contents for this volume/issue"), September 2024, 100700

## Enterprise architecture modeling for cybersecurity analysis in critical infrastructures — A systematic literature review

[https://doi.org/10.1016/j.ijcip.2024.100700](https://doi.org/10.1016/j.ijcip.2024.100700 "Persistent link using digital object identifier") [Get rights and content](https://s100.copyright.com/AppDispatchServlet?publisherName=ELS&contentID=S1874548224000416&orderBeanReset=true)

Under a Creative Commons [license](http://creativecommons.org/licenses/by-nc/4.0/)

Open access

## Highlights

- •
	Provided a comprehensive review of enterprise architecture models published before 2024 from Scopus, IEEE Xplore, and ACM, emphasizing the critical role in cybersecurity for critical infrastructures.
- •
	Showcased diverse methodologies and need for rigorous validation to ensure enterprise architecture models’ reliability and real-world applicability.
- •
	Identified the key strengths and limitations of enterprise architecture models in integrating security aspects.
- •
	Discussed practical application of models like Purdue model and IEC62443 standards, while recommending standardization, semantic foundations, and the development of tools to address rapid changes in enterprise cybersecurity landscapes.

- [Next article in issue](https://www.sciencedirect.com/science/article/pii/S187454822400043X)

## Keywords

Enterprise architecture

Enterprise model

Cybersecurity

Critical infrastructure

## 1\. Introduction

The governance of information security within enterprise information technology (IT) management has become increasingly vital, especially in organizations characterized by complex IT and (ICSs) landscapes, coupled with a substantial dependence on automated information processing involving many operational technology (OT) components. This is particularly true for critical infrastructure (CI) enterprises, which utilize sophisticated ICSs, including supervisory control and data acquisition (SCADA) systems , . These systems are prevalent across various sectors such as energy, manufacturing, transportation, healthcare, environmental management, and smart urban development, as highlighted by Yaacoub et al. . The integration of such advanced technologies has been a driving force behind the digital transformation of physical entities and their inter-connectivity in cyberspace, fulfilling the stringent demands for ultra-reliable services in .

The cybersecurity landscape has been marked by significant threats to CIs, particularly targeting ICSs, as evidenced by instances like the worm and the *WannaCry*. Attackers frequently aim to disrupt business operations by targeting key enterprise goals, thereby affecting applications and their underlying infrastructure, such as platform systems. Vulnerabilities in one segment can lead to repercussions in others, thereby magnifying potential losses through the inter-dependencies of different layers . These attacks, which exploit system vulnerabilities, have led to substantial disruptions and economic impacts, including production halts in European automotive factories, as analyzed by Santangelo et al. .

In this context, managing cybersecurity within enterprises is an ongoing, dynamic endeavor, requiring continuous adaptation to changing environmental conditions . It is imperative to perceive cybersecurity not as a standalone operation, but as an integral component of broader enterprise-level strategies. To do so, enterprises need to have a comprehensive understanding of their IT infrastructure and how its business depends on it. A comprehensive overview of such dependencies is of great importance to critical infrastructure operators due to the very large number of assets in the IT and OT domain.

, in particular , has emerged as a valuable tool to support enterprise security analysis. Defined by Mylopoulos as a formal description of certain aspects of the world for understanding and communication, conceptual modeling aids in managing complexity and fostering communication among stakeholders. It offers benefits such as promoting a shared understanding of threats, linking IT assets to enterprise processes, and facilitating . The use of necessitates specificity to enhance the value of the analysis, particularly in enterprise modeling. Several modeling approaches, like risk assessment methods , , have been developed to aid security analysis across various abstraction levels, from organizational to individual software systems.

Enterprise architecture offers a detailed overview of business operations, highlighting the inter-dependencies among business assets, processes, and information technology , , . Integrating enterprise architecture practices into the development and implementation of security strategies enables organizations to effectively manage complex business processes and enhance their overall business strategies , . Ekstedt and Sommestad presented one of the initial proposals for employing enterprise architecture in cybersecurity. They emphasized the creation of attack and defense trees as formal components within the meta-model for enterprise architectures. Reference models typically act as the foundational framework for developing specific architectures, including enterprise architecture modeling , . Adherence to a reference model ensures the use of standardized definitions, terms, and concepts within the enterprise modeling, fostering consistency and interoperability.

The goal of this paper is to simplify the process for researchers and practitioners seeking pertinent studies in the field of enterprise architecture modeling for cybersecurity assessment, especially in the context of critical infrastructures. Additionally, by methodically and thoroughly structuring the literature, we aim to highlight areas that are under-researched. Our goal is to pinpoint these gaps in knowledge and potential areas for further investigation, thereby directing the trajectory of future research in this domain.

### 1.1. Research questions

The research questions specifically addressed by this study are as follows:

- RQ1:
	What enterprise architecture reference frameworks and models have been explored for cyber security assessment? This question aims to catalog the various enterprise architecture reference frameworks and models that have been studied or proposed for addressing cybersecurity concerns.
- RQ2:
	What semantic foundations are applied in these models to incorporate ? The goal here is to identify the underlying semantic foundations that inform the design and implementation of in the context of cybersecurity.
- RQ3:
	Which research methods have been used to evaluate these models? This question intends to identify and categorize the research methods (conceptual, empirical, , etc.) used to assess the effectiveness of enterprise architecture models in cybersecurity.
- RQ4:
	What are the integrated cybersecurity aspects in enterprise modeling, especially in the context of critical infrastructures? The aim is to summarize and analyze findings from existing research to understand how different enterprise models address cybersecurity risks.

### 1.2. Scope

This paper focuses on enterprise architectures and models proposed for cyber security analysis and assessment, while particularly explored such model usage in critical infrastructures.

### 1.3. Contribution

For this review, we have defined the time frame to include studies published in Scopus, IEEE Xplore and ACM Digital Library before 2024. Our focus is on high-quality research, which entails considering only those articles published in peer-reviewed journals and presented at reputable conferences. In doing so, this paper contributes to the following:

- •
	The paper delves into the methodologies and approaches used by different enterprise architectures and models to incorporate security aspects, with identification of the theoretical frameworks and reference theories that underpin these enterprise architecture models.
- •
	The paper also categorizes and discusses the various research methods, such as conceptual analysis, empirical studies, and case studies, used to evaluate the effectiveness of these enterprise architectures and models in addressing cyber security issues.

### 1.4. Structure of the paper

Section provides background of the , including cybersecurity standards, conceptual models, and enterprise architecture models. This section also includes discussions and gap identification in related works. Section details the research methodology utilized for executing the systematic literature review. In Section , we delve into an analysis of the results, systematically addressing the five research questions that form the core of this study. Section offers a comprehensive discussion of the key findings and their implications, also considering the potential threats to the validity of our research. The paper concludes in Section 7, where we summarize our findings and propose directions for future research, thereby setting the stage for subsequent investigations in this domain.

## 2\. Background and related works

We summarize the commonly used terminologies in this paper, as shown in . In the literature, the terms enterprise architecture and enterprise model are sometimes used as synonyms and indeed they overlap to a large extent. An enterprise architecture is a rather informal framework on how the IT systems of an enterprise are aligned with the business goals. A widely used standard for enterprise architectures is TOGAF . It does not only specify, which aspects of an enterprise shall be included in an architecture but also formulates rules for architecture governance, such as defining roles and responsibilities. TOGAF is technology-independent. Specifically, it does not prescribe the use of certain . Enterprise models are explicit representations of enterprise assets using a set of modeling constructs. They can be seen as multi-perspective languages. A widely used example is ArchiMate . It closely follows the architecture layers of TOGAF but has a specific set of constructs, *i.e.* it commits to a certain language to represent information about an enterprise. To summarize, an enterprise architecture is about what to represent, and an enterprise model is about how to represent it. An early precursor of ArchiMate is Aris . It covers similar aspects of an enterprise but lacks the clear differentiation of layers found it ArchiMate. Likewise, a predecessor of TOGAF is the . It identifies architecture levels (such as conceptual, logical and physical)) and perspectives such as the data perspective and the goal perspective. Like TOGAF, the Zachman framework is informal and does not prescribe any modeling language. A notable difference between an enterprise model and an enterprise architecture is that the latter is rather agnostic of the dependencies between the different layers and perspectives. In contrast, one of the prime functions of an enterprise model is to support tracing dependencies between artifacts defined in different layers, *e.g.* the dependency between business goals and the IT systems used for the business processes that shall accomplish the goals.

The standard defines an architecture as the fundamental concepts of an entity and its environment, and an architecture description is a work product to express an architecture. In this sense, an enterprise model is an architecture description. An early framework for is GERAM , with the goal to facilitate the integration of enterprise application systems.

While enterprise architectures and models were initially designed for Business-IT alignment including IT security, they have increasingly drawn the attention of cyber security experts in the last decade. Rather than only assessing the cyber security based on hardware and software components, an enterprise architecture model allows to explicitly link security assessments to the of an enterprise at all levels, from strategic, business, application to networks, hardware, and physical processes.

Table 1. Definitions of some key terms.

| Key terms | Descriptions |
| --- | --- |
| Conceptual model | Refers to a formal description that abstractly represents and organizes key principles and structures of a system or concept, focusing on essential aspects and relationships relevant to a specific domain . |
| Enterprise architecture | Refers to a comprehensive framework that defines an organization’s structure and operation, aligning its business processes, information systems, technologies, and infrastructures with strategic objectives. Examples include TOGAF and Zachman framework . |
| Enterprise model | Refers to a detailed representation of an organization’s structure, processes, information, and policies, serving as a blueprint for analyzing, designing, and improving operations and supporting strategic planning. Examples include Archimate and Aris . |
| Cybersecurity framework | Refers to a set of guidelines and best practices for managing cybersecurity risks, providing a structured approach to identify, protect, detect, respond to, and recover from cyber threats and vulnerabilities . Examples include C.I.S. Control Community and Echeverría et al. . |

### 2.1. Cybersecurity standards

To facilitate the effective utilization of security metrics, cybersecurity standards have been developed to offer metrics that measure the outcomes of each milestone, enabling organizations to assess historical issues, current stances, ongoing improvements, and projected goals. Currently, the most recognized and adopted are laid out by the Center for Internet Security (CIS), the International Standards Organization (ISO), and the National Institute of Standards and Technology (NIST) .

C.I.S. Control Community enumerates 18 primary controls for managers to bolster the security of their . Some key controls from this list encompass secure configurations for both hardware and software, account management, diligent maintenance and analysis of audit logs, defenses against , capabilities for data recovery, boundary protections and access controls based on necessity .

ISO has released a series of standards under the ISO 27000 family, each tailored to specific technological areas to assess varying risk levels and their consequences . A notable instance is ISO/IEC 27001, recognized globally as the standard for overseeing information security .

### 2.2. Critical infrastructure cybersecurity

As defined by the U.S. Cybersecurity & Infrastructure Security Agency (CISA) and the European Program for , , CIs play a pivotal role in societal sustenance. For instance, the critical manufacturing sector produces essential items for other sectors, such as power grids. Such systems employ an interconnected array of sensors, devices, and actuators to understand and influence a physical process, often necessitating assured set by safety-critical applications . For instance, the smart grid integrates various electric power generation facilities with diverse loads, utilizing dynamic load-balancing and pricing to align with demand–response tactics . This integration is heavily dependent on .

### 2.3. Related works

Korman et al. compared 12 established methods and examines how well ArchiMate, a modeling language for enterprise architecture, can accommodate the information suggested by these methods.

Diefenbach et al. offered a comprehensive literature review concerning the integration of information security into enterprise architectures. A key observation is the existing contribution of enterprise architecture management in enhancing risk and . Nonetheless, they contend that further research is imperative to seamlessly weave information security and into enterprise architectures.

Ellerm and Morales-Trujillo discussed the lack of elements to model security in current enterprise architecture modeling languages, with a specific focus on the micro-mobility context.

McClintock et al. evaluated 25 existing security frameworks and identify a lack of research process and a disjointed focus. Yet they argue that with proper design and integration, enterprise architecture can address the identified organizational security gaps and provide security benefits by reducing unnecessary costs, improving process innovation, standardizing business processes, increasing risk management effectiveness, and improving business/IT alignment.

Insights are also provided on the challenges of integrating enterprise models with security analysis. For example, presents challenges identified through interactions with domain experts, which provide insights into the practical uptake of modeling. These challenges include automated model creation, accounting for changing security requirements, multi-level model management, and incentivizing users.

These identified challenges not only highlight the complexities in integrating enterprise modeling with security measures but also underscore a critical need for a systematic review paper . Our paper delves into these issues, exploring the current state of enterprise architecture modeling in the context of cybersecurity, and identifying potential areas for further research and development to address these pressing challenges.

## 3\. Research methodology

Systematic literature reviews (SLR) is chosen to comprehensively identify relevant empirical evidence on the pre-defined research questions by following explicit, systematic methods while ensuring transparency, inclusiveness, explanatory and heuristic qualities .

For example, focused on usability capability/maturity models and emphasizes a structured approach to evaluating these models. This method is particularly well-suited for maturity models in usability contexts, offering a robust framework for assessing . Fink provided guidelines for conducting research literature reviews provide a thorough and practical approach, especially valuable for its step-by-step procedures. However, Fink’s methods are generally broad and may lack the specificity needed for certain fields like . Page et al. offered PRISMA guidelines that are essential for ensuring transparency and completeness in systematic reviews. They are particularly effective in the health sciences for their stringent reporting standards, ensuring thorough and unbiased reviews.

In this paper, we adhere to the 8-step SLR methods outlined by Okoli and Schabram , which are based on the frameworks proposed by Webster and Watson and for analyzing information systems. This 8-step SLR method by Okoli and Schabram is specifically tailored for information systems research and encompasses a comprehensive approach from planning to reporting, ensuring the inclusion and synthesis of both quantitative and qualitative studies.

This section clearly defines the criteria for literature selection, databases, and used, as well as inclusion and exclusion criteria. These principles enable a more objective summary of the search findings while minimizing selection bias, publication bias, and data extraction bias , as summarized in . The planning stage is already introduced in Section and is therefore not discussed here.

![](https://ars.els-cdn.com/content/image/1-s2.0-S1874548224000416-gr1.jpg)

Download: Download high-res image (163KB)

### 3.1. Databases and search keywords

To ensure the inclusion of papers where the full term is present in the abstract or title, abbreviations were excluded. This was done to avoid artificially increasing the search results with texts where those abbreviations might have different meanings. Consequently, the search query was structured to focus on titles, keywords, and abstracts, targeting papers published before 2024. Querying IEEE Xplore Command Search, Scopus Advanced Search and ACM Digital Database Advanced Search engines using the search strings listed in gave us 154, 212 and 11 results published before 2024, respectively. Combining all the search results we got an initial pool of 377 papers, as of the query result on May 6th, 2024.

Table 2. Search strings for the review.

| Database | Search string |
| --- | --- |
| IEEE Xplore | *((“Full Text & Metadata”:“enterprise arch\*” OR “Full Text & Metadata”:“enterprise mod\*”) AND (“Full Text & Metadata”:“cyber sec\*” OR “Full Text & Metadata”:“cybersec\*”) AND (“Full Text & Metadata”:“critical infra\*”))* (Note that manual setting in year range to *“-2023”* is needed.) |
| Scopus | *(“enterprise arch\*” OR “enterprise mod\*”) AND (“cyber sec\*” OR cybersec\*) AND “critical infra\*” AND PUBYEAR ¡ 2024* |
| ACM | *((Fulltext:(enterprise mod?) OR Fulltext:(enterprise arch?)) AND ((Fulltext:(cyber sec?) OR Fulltext:(cybersec?)) AND Fulltext:(critical infra?) AND ((Keyword:(enterprise mod?) OR Keyword:(enterprise arch?)) AND ((Keyword:(cyber sec?) OR Keyword:(cybersec?)) AND (E-Publication Date: (01/01/1908 TO 12/31/2023))* |

### 3.2. Inclusion and exclusion criteria

After removing duplicates, we still have 356 papers in the pool. Our methodology for selection was structured into three distinct phases: an initial assessment based on the publication titles, followed by a detailed examination of the abstracts, and culminating in a thorough analysis of the full documents. The were specifically designed to encompass papers that either introduce new enterprise architectures or models, or contribute segments to existing ones, or provide validation on existing approaches.

Conversely, our exclusion criteria were stringent, disqualifying papers consider that following perspectives:

- •
	Relevant Content: Papers that do not directly address the research questions and objectives of this study will be excluded.
- •
	Language: Any papers not published in English will be excluded.
- •
	Standard of Quality: Our review will exclude any papers that are not peer-reviewed.

Beyond applying our inclusion and exclusion criteria, we assessed the quality of the identified studies. We prioritized articles that provided substantial details and insights into enterprise architectures or models, including a comprehensive description of their components and their application within the context of cybersecurity.

This process was collaboratively executed by two researchers, each bringing a specialized lens to the study: one with expertise in the cybersecurity domain and the other in enterprise modeling. The cybersecurity researcher was responsible for steering the entire search and selection process, while the enterprise modeling expert provided critical insights through inclusion and exclusion. Then two other researchers who were not involved in the screening process further checked through the included and excluded papers to ensure quality. After this thorough filtering process, 38 papers remained to be reviewed in depth.

Subsequent to the initial filtering round, each article underwent a further round of snowballing based scrutiny, in both backward and forward manners. In the forward snowballing process, we examined the subsequent literature that cited each of the selected papers using Google Scholar which provided an efficient means to track these citations. Conversely, the backward snowballing involved a thorough examination of the references within each paper to ascertain if any pertinent research had been overlooked. This backward review was iteratively conducted until no additional relevant papers were discovered. Particularly, this process extended beyond the references of the initially accepted articles, encompassing the references of the cited papers as well, thereby implementing multiple layers of snowballing. The initial exclusion step led to the snowballing process uncovering a significant number of additional papers, totaling 6. Consequently, the overall count of papers considered in this study amounted to 44, with yearly distribution illustrated in which shows more efforts in this field in the recent five years.

![](https://ars.els-cdn.com/content/image/1-s2.0-S1874548224000416-gr2.jpg)

Download: Download high-res image (100KB)

### 3.3. Data extraction

A template was employed for the purpose of extracting data, which included several fields: paper ID, authors, title, publication year, source of the publication, type of document, abstract, and key words. We then manually extract and categorize the reviewed literature based on their utilized methodologies, theories, evaluations, and whether real-world applications are involved, following the suggestions of added values through literature review discussed by Wee and Banister . We mapped relationships among these articles based on their predominant methodologies, design features and implemented frameworks to analyze possibilities for synthesis. Qualitative aspects are introduced through summarizing the contributions of the reviewed papers remaining after rigorous filtering via SLR approach introduced by Okoli and Schabram .

Throughout the coding process, we conducted regular quality checks and spot checks to identify and rectify any coding errors or inconsistencies. This process is collaboratively carried out by two researchers, and further checked by the other two researchers, to reduce potential misinterpretation of text or coding bias.

## 4\. Findings

The findings are structured according to each Research Question (RQ), with the primary papers being classified based on their respective contributions to these RQs.

### 4.1. Answer to RQ1: What enterprise architecture reference frameworks and models have been explored for cyber security assessment?

provides a comprehensive summary of the enterprise architecture reference frameworks and standards employed in the 44 papers reviewed. This includes the utilization of traditional enterprise architecture frameworks like Zachman, GERAM, SABSA, and newer ones like ArchiMate. Meanwhile, modeling languages like the (UML) is also integrated to model software-intensive enterprise architecture. UML, primarily a modeling framework, lacks built-in concepts for enterprise artifacts, functioning without domain-specific constructs. Its meta-concepts encompass elements such as “class”, attribute, association, actors, and task, among others. In contrast, frameworks like ArchiMate offer a more extensive array of domain-specific constructs. These include, but are not limited to, business goals, , and network infrastructure, providing a richer and more nuanced toolkit for enterprise architecture modeling. This diversity in frameworks reflects the varied approaches and methodologies adopted in the field, each contributing uniquely to the understanding and development of enterprise architecture.

#### 4.1.1. Traditional commercial enterprise architectures

Traditional commercial EAs include the by Zachman , GERAM , TOGAF , and SABSA .

Zachman presented a structured framework that systematically classifies architectural depictions using a matrix-based approach. Specifically, the framework delineates unique representations for data, process, and location from the perspectives of the owner, designer, and builder. Zachman underscores the distinctiveness of each description, noting that while they may refer to the same entity, they are crafted for specific purposes and should be viewed as independent constructs. Tatar et al. explored how the Zachman Framework can be applied to depict the United States’ program for protecting critical infrastructure. While the Zachman Framework allows for a comprehensive representation of the roles and responsibilities of stakeholders, it has limitations in terms of complexity, flexibility, and standardization.

The Sherwood Applied Business Security Architecture (SABSA) has a structure similar to the Zachman framework, but specifically aimed at risk and . SABSA employs a matrix organized around the interrogative terms: What, Why, How, Who, Where, and When . SABSA analyzes trust relationships between entities to identify security requirements. Burkett leveraged SABSA to infuse information security considerations into the enterprise architecture landscape. Their methodology aligns with renowned enterprise architecture frameworks like the Zachman framework and TOGAF. Instead of introducing a novel framework, they advocated for enhancing existing enterprise architecture frameworks with security dimensions. They did not employ a formal enterprise modeling language. Yet identified in their study that very few security failures linked to ‘Where’, while ‘Who’ presented intricate and diverse failures, encompassing aspects like end-user behaviors, oversight challenges, and governance complications. Loft et al. further suggested that the configuration of mainstream enterprise architecture frameworks does not aptly address the fundamental causes of security failures. Wood et al. focused on the contextual and conceptual layers of the SABSA framework. Pleinevaux highlighted the importance of Attributes, Domains, and Risks in the SABSA framework. The proposed meta-model for SABSA in this study focuses only on the conceptual level and does not include elements needed at other levels such as the logical or physical component architecture levels.

Adhering to these frameworks necessitates significant resources and dedication, as they mandate the creation of specific documentation and the systematic integration of enterprise architecture activities with business operations . Consequently, many practical enterprise architecture implementations diverge from the theoretical constructs presented in enterprise architecture frameworks .

#### 4.1.2. Archimate

When integrating cyber security into enterprise models, model-driven engineering (MDE) offers significant tools and methodologies , . Particularly, enterprise modeling frameworks such as Aris Architecture and ArchiMate aim at creating integrated models of the business and IT levels of an enterprise and to establish their dependencies, to support model-driven security analysis, as presented in .

Table 4. Utilized modeling language.

ArchiMate is increasingly becoming the standard language within the enterprise architecture modeling communities, largely due to its alignment with TOGAF . Korman et al. found that ArchiMate is capable of modeling a significant portion of the information required for information . In ArchiMate, enterprise models are categorized into three primary layers for simplicity and clarity. The business layer focuses on elements like business processes and roles. The application layer deals with software applications, their services, and interfaces. Finally, the technology layer is about system software (like operating systems) and physical hardware, such as computers and network devices.

According to the survey conducted by Ellerm and Morales-Trujillo , ArchiMate is the most commonly used modeling languages for security till Jan 2020, but it is also the most criticized due to limitations in its existing security modeling capabilities. It allows representation of both enterprise architecture management and security domains. The Motivation Extension in ArchiMate, incorporating the Business Motivation Model, proves especially effective in articulating the distinct motivations related to for and decisions. For example, refined the ArchiMate meta-model by integrating cybersecurity elements from a domain-specific framework ISSRM (or information system security risk management) following enterprise model integration (EMI) approach, including risks, threats, vulnerabilities, security objectives, and .

San Martín et al. adopted ArchiMate to model the business layer and developing 19 in the Atlas Transformation Language (ATL) to map these elements to BPSec, a security-enhanced version of BPMN, aiming to derive secure business process models from enterprise architecture models by integrating security requirements. The analysis demonstrates that these transformation rules effectively handle complex mappings, ensuring accurate correspondences between enterprise architecture elements and business process models. Nonetheless, implementing this approach requires expertise in both enterprise architecture and model-driven transformation techniques.

Similar efforts are seen to enrich ArchiMate with security information. For example, developed a method that integrates with using ArchiMate. They developed the Intra Model Security Assurance (IMSA) approach, combining security assurance cases and architecture diagrams with quantitative evaluation methods. Aldea et al. proposed a method for enhancing resilience in enterprise architecture by integrating resilience considerations from the design phase. They used ArchiMate to model the current state of an organization’s processes, systems, data, and infrastructure, using resilience-focused viewpoints. For example, the OR and AND junctions of ArchiMate are used to model disruption and redundancy, respectively. They also adopted the definitions of probability and impact from TOGAF standard in their risk assessment. The analysis reveals that this approach enhances the system’s ability to withstand disruptions and aligns business processes with resilience objectives.

#### 4.1.3. Other architecture models

Korman et al. argued that a standalone reference model might fall short in addressing aspects like flexibility, availability, and constraint validation. However, when paired with a modeling tool, these challenges can be addressed more comprehensively.

Accordingly, some works utilized UML that provides a standardized notation and set of diagrams to get visual representation and documentation of the system’s structure, behavior, and interactions.

For instance, aimed to enhance cybersecurity protection for critical infrastructures by generating security policies for SCADA systems using UML Use Cases. When modeling cybersecurity policies, they represent roles as actors, and depict collaborations to show connections. Similarly, discussed the need for security in cyber–physical systems (CPS) and proposes a security reference architecture for CPS using UML, consisting of business layer, , application layer, service layer, infrastructure layer, sensor & actuator layer and network fabric.

Johnson et al. developed a Predictive, Probabilistic Architecture Modeling Framework ($P2AMF$) in the form of UML classes while integrating the Object Constraint Language (OCL) with a mechanism. Their goal was to enhance prediction accuracy for system properties under uncertainty. Holm et al. combined and extended $P2AMF$ and CySeMoL into $P2CySeMoL$ for cyber security analysis while focusing on logical and physical components that can be compromised by attackers. Their model supports prediction and analysis of the probability of successful cyber-attacks, validated through real-world scenarios. Korman et al. further extended $P2AMF$ into a reference architecture that melds advanced metering infrastructure with cybersecurity analysis. In this context, their smart metering model, adhering to UML syntax, serves as a manifestation of their meta-model. Their subsequent enhancements to the smart-grid model yield architectures that facilitate automated security assessments and cyber-attack simulations, with a primary emphasis on smart metering and load-balancing functionalities.

Similar to the other proposed enterprise architectures, a data model called CRUSOE is introduced by Komárková et al. as a layered data model consisting of business, application, technical, and . It is created through interviews with and formalizes the requirements for modern network environments. and then further extended by Husák et al. .

Akailvi et al. proposed a software architecture and prototype HELOT that enables the continuous capture of events in OT systems, IT systems, and interconnected networks. HELOT facilitated the real-time capture of and the automation of cybersecurity operations. The architecture supports proactive threat hunting and in OT environments. The proposed architecture is validated in two application cases: capturing forensics artifacts from a live OT system and automating cybersecurity operations in combined IT/OT environments.

Casola et al. developed their layered model by extending the foundational structure of the Purdue Enterprise Reference Architecture (PERA), or the Purdue Model. Purdue model is originated from Purdue University in the 1990s. Purdue model systematically delineates five distinct levels, starting from physical components at Level 0 and extending up to the enterprise network at Level 4/5. Purdue framework encompasses various critical aspects, including control systems at Level 1, supervisory systems at Level 2, manufacturing operations systems at Level 3, and the integration of data collection for informed business decision-making at the highest levels. This layered approach effectively captures the complexity and hierarchical nature of modern industrial systems.

In conclusion, traditional frameworks such as Zachman, GERAM, TOGAF, and SABSA provide robust structures for integrating security considerations into enterprise architecture, each with unique strengths and limitations. Zachman and GERAM offer comprehensive, flexible frameworks, while SABSA and TOGAF emphasize risk and security aspects. ArchiMate stands out with its domain-specific constructs and alignment with TOGAF, despite some limitations in security modeling capabilities. Other models like UML and CRUSOE extend the flexibility required for specific cybersecurity contexts or provide better visibility.

### 4.2. Answer to RQ2: What semantic foundations are applied to incorporate security aspects into enterprise architecture models?

Utilizing ontology, taxonomy, and domain-specific language (DSL), these approaches focus on integrating detailed security aspects into enterprise architecture models. The principal aim is to reduce the complexity of creating various enterprise architecture artifacts in the security domain by abstracting security-specific details into domain models and using model-driven tools.

#### 4.2.1. Ontology

Ontology provides a structured framework for representing knowledge as a set of concepts within a domain, and the relationships between those concepts. In enterprise modeling, ontology is used to define and standardize the terminology, enabling consistent interpretation of the model elements across different stakeholders and systems.

Janulevičius et al. employed an ontology to delineate enterprise architecture elements pertinent to , enriching the enterprise architecture model with security-centered concepts. They specifically address the security dimensions of governance, virtualization, and cloud service operations. This ontology aims to steer the design of enterprise architecture.

are tailored to a specific aspect of enterprise modeling, providing semantics that are particularly suited to that domain. For example, a DSL might be designed specifically for modeling supply chain processes or IT infrastructure.

Jiang et al. proposed a DSL and repository in relation to cyber security for smart grids is to categorize and represent the components of power grids and their related IT systems. Their taxonomy and smart grid models are represented in Telos language and implemented through ConceptBase . ConceptBase provides a database that stores both the classes (taxonomy) and instances (sample models) of smart grids. This integration allows for the extension of the taxonomy even when sample smart grids are already represented. The properties of , such as serial number, model, version, and vendor, are attached using the “property” relation in ConceptBase. Jiang et al. built upon the CPS taxonomy to allow complex CI , partitioning dependencies into cyber and cyber–physical . They conducted cascade modeling for , and proposed power-grid reference models to allow enterprise architecture related information reused for security analysis.

Similarly, positioned services as the core of their enterprise modeling instrument. These services are characterized by their providers, the data exchanges among them, and communication channels. The framework is built upon ConceptBase and leverages its query functionalities to scrutinize vulnerabilities within a specified enterprise model.

Hause presented how Unified Architecture Framework (UAF) enable engineers to define security goals and requirements and implement them throughout the architecture, on top of Systems Modeling Language (SysML) . Hoffmann et al. utilized UAF to delineate the overarching objectives, strategies, capabilities, interactions, standards, , and system patterns. They also pointed out a limitation in UAF as it permits the development of that may be inconsistent or incoherent.

Table 5. Meta models and .

#### 4.2.2. Meta models

In enterprise modeling, meta-models define the syntax and semantics of the modeling language, ensuring that models are built in a consistent and standardized manner. In total, 18 (out of 44) papers address meta models in their works, as shown in .

Sommestad et al. introduced a meta-probabilistic rational model comprising classes with attributes such as countermeasures and attack steps, as well as reference slots that link to other classes, expressing the relationships between them. This probabilistic rational model was further developed into the Cyber Security Modeling Language (CySeMoL), which centers on assessing the probability of success for attempted attack paths, given the defined model elements and their interconnections.

Hacks et al. proposed the use of domain-specific attack languages, specifically the Meta Attack Language (MAL), encompassing 56 attack steps spread over 28 diverse assets, to codify common attack logic in the power sector. The tool set of MAL is combined with ArchiMate notation to model security domains and create instances of MAL that reflect the concepts modeled in ArchiMate. This combination is used to assess the safety and security of power infrastructure by simulating attacks on power grids and plants. A number of MAL-based DSLs are developed, such as coreLang , that models IT entities and vehicleLang that support attack simulation in vehicles. The structure of coreLang includes concepts such as Application, Network, Data, Connection, Vulnerability, Exploit, and Defense, which can be used to model different aspects of the architecture and simulate attacks. On top of coreLang, created a method to convert Business Process Modeling Notation (BPMN) into coreLang, enabling the automatic transformation of these models into a graph format for conducting attack simulations using securiCAD . MAL has also being extended to represent the behavior of adversaries, their tactics, techniques, and procedures (TTPs) through mapping to the MITRE ATT&CK Matrix, as seen in the works of Xiong et al. .

Meta models are created on top of ArchiMate or integrating Archimate with other languages. Feltus et al. modified the structure of ArchiMate to fit the specificity and domain constraints of SCADA components, and validate their model in the field of petroleum supply chains. Feltus and Khadraoui further evaluated their proposed meta-model and policy management method through a laboratory and feedback from the users. They also enriched the SCADA meta-model to provide support for the definition and deployment of semantic and cognitive policies.

Several other meta-models have been developed, each grounded in diverse semantic foundations tailored to specific . For instance, developed SecKit, a model-based security toolkit that adopts an enterprise architecture approach for , particularly in systems. This toolkit is based on the principles of the Interaction System Design Language (ISDL), forming a versatile and comprehensive framework applicable to a broad spectrum of distributed systems.

Similarly, introduced the S-cube model, a unique approach for the joint modeling of safety and security in SCADA systems. This model encompasses a meta-model that delineates the components of digital industrial architectures, their attributes, and potential security (attacks) and safety (failures) events affecting each component.

Furthermore, introduced ThreMA, a proposal for a standard meta-model accompanied by a formal vocabulary, specifically designed for modeling ICT infrastructures. These diverse meta-models, each with their unique semantic underpinnings, contribute significantly to the field by addressing specific needs and challenges in system architecture and security.

#### 4.2.3. Reference models

Reference models play a pivotal role in system modeling and model-based system engineering, particularly in facilitating security-centric analyses, as noted by Vernotte et al. . These models are instrumental in encapsulating the standard topological configurations and functional interconnections inherent in various architectures.

Among the reviewed 44 papers, 7 works research into reference models has been conducted within the domain of CI studies , , , , , , . The SEGRID project , for example, offered insightful reference models for smart grids, with a concentration on communication and enterprise modeling, sidelining the physical components. More specially, their model includes SCADA systems as part of the overall architecture and analyzes their role, functions, and data flows within the smart grid, specifically in relation to load balancing of renewable energy . Their guidance on network control and associated elements remains somewhat circumscribed.

Pavleska et al. crafted a guideline to assess enterprise cyber security embedded within reference architecture. Their theoretical framework encompasses security objectives, susceptibilities, potential threats, and protective measures, all interconnected with the overarching enterprise model. This conceptual framework serves as a manual guide to evaluate an enterprise’s through its enterprise model. The proposed framework was integrated to assess high-level design artifacts and operational solutions, validated through practical application in the e-SENS project.

Sellitto et al. adeptly mapped their enterprise architecture views, which were utilized to depict a cooperative intelligent transport system use case, into a threat-focused . This mapping was conducted in accordance with the Reference Architecture Model for (RAMI 4.0), facilitating a comprehensive description of the system’s life cycle.

Reference models for CIs are usually multi-level, whereby two predominant strategies exist: top-down and bottom-up techniques. The top-down strategy initiates modeling from the highest abstraction level, first outlining concepts at the upper echelons of classification. These concepts are then further elaborated upon as one descends to more detailed classification tiers. Conversely, the bottom-up strategy starts at a detailed abstraction level. As commonalities among these foundational concepts are discerned, they are abstracted into broader concepts at superior levels. In instances where shared properties are identified across multiple concepts, their definitions are elevated to these higher tiers. For example, advocated for a flexible creation process that intertwines top-down and bottom-up strategies, particularly for models created using the XModeler and the Flexible Meta-Modeling and Execution Language (FMMLx). FMMLx is utilized by Hacks et al. to align two reference models, namely NISTIR 7628 and powerLang. NISTIR 7628 is a reference architecture for defining ideal-type smart grid scenarios and associated security requirements.

Jiang et al. constructed their reference model by integrating and aligning with established and reliable frameworks, notably the Purdue model, NIST SP 800-82, and the IEC 62351 series.

Kinderen et al. developed a multi-level reference model that integrates terminology from the community, good practices, and existing standards. This model provides an integrated view of relevant aspects such as assets, vulnerabilities, and attacks. The method also includes a process model that consists of six main steps, primarily supported by the reference model.

Utilizing reference models can lead to significant time savings in the modeling process and reduce the risk of often associated with real scanning processes. As such, reference models are particularly well-suited for situations where data collection is either not feasible or restricted, such as in the domains of CIs.

#### 4.2.4. Formal semantics and logical foundations

in modeling provides a rigorous and precise interpretation of the model’s elements and their relationships, often using mathematical logic or other formal systems. It ensures that the model’s meaning is clear, unambiguous, and consistent.

Some works ground their concepts in foundational ontologies such as Object Constraint Language (OCL). OCL is a formal language that allows the user to state expressions on , specifying invariant conditions and queries over objects in the model. It is compatible with UML and provides the necessary for system property analysis. For instance, integrated their proposed framework with OCL, which enables the handling of uncertainties in both attribute values and model structures, making the framework suitable for various analyses, including performance, reliability, security, and compliance with regulations.

Logical foundations provide a basis for reasoning about the model and verifying properties like consistency and completeness. We also assessed how the reviewed papers use logical foundations in their modeling, including the use of , , or other formal logical systems to define the semantics of the model.

The probabilistic rational model proposed by Sommestad et al. integrates qualitative parameters, expert inputs, and for distributions. It models both logical dependencies with deterministic influences and probabilistic dependencies with uncertain impacts.

Johnson et al. incorporated probability distribution mechanisms into their model, grounding it in first-order logical relations to establish a foundation for deductive formalism. Their approach to is based on the Monte Carlo method, which allows for the effective handling of uncertainty and complexity in their model.

The S-cube KB model, as proposed by Kriaa et al. , leverages the object-oriented capabilities of the Figaro modeling language, complemented by tools based on Figaro. This integration facilitates the importation of system architectures through intuitive . Figaro, incorporates an inheritance mechanism, is adept at constructing probabilistic models. This feature of Figaro enhances the model’s ability to handle complex probabilistic scenarios, making it a robust tool in the realm of system architecture modeling.

Deductive rules have been effectively implemented in the cyber–physical dependence rules and reference architecture as proposed by Jiang et al. , supporting statistic query analysis. This implementation has been further refined and formalized in the subsequent work of Jiang et al. . Similarly, developed a formal vocabulary for modeling ICT infrastructures, a threat catalog, and a set of inference rules based on the Semantic Web Rule Language (SWRL) to support automated threat identification.

Valenza et al. provided a framework for modeling system entities, their interrelationships, and their relationships with potential threats. Building upon this foundational model, the authors then formulated a set of derivation rules to systematically infer which entities could become vulnerable, compromised, or experience malfunctions as a consequence of the defined threats and system inter-dependencies.

In summary, the review of semantic foundations for incorporating security aspects into enterprise architecture models highlights several approaches. Ontologies, such as SafecareOnto, provide structured frameworks for representing knowledge and ensuring consistent interpretation across stakeholders. Domain-Specific Languages (DSLs) like those proposed by Jiang et al. and for smart grids, offer tailored semantics for specific modeling needs, facilitating detailed security representations. Meta models, like MAL , integrate with tools such as ArchiMate to model and simulate security domains. Reference models play a crucial role in system modeling and model-based system engineering, enabling security-centric analyses and encapsulating standard configurations and functional interconnections, as seen in works like SEGRID for smart grids . Formal semantics, using mathematical logic or other formal systems, provide a rigorous interpretation of model elements, ensuring clarity and consistency, as demonstrated in frameworks using OCL and probabilistic models like CySeMoL , .

As seen in these works, risk modeling languages (*e.g.*, semantic maps and ontology) for model-based security engineering have been proven to be scalable and flexible. Such method not only ensures robust and well-defined security within the architecture but also facilitates the generation of security mechanisms, protocols, and the identification of . Additionally, it allows modelers to develop these artifacts with minimal need for in-depth technological knowledge, exemplified by the separation of process definitions from simulation and security performance aspects in business process simulations for security, enabling automated transitions between different facets.

### 4.3. Answer to RQ3: What research methods have been used to evaluate these models?

Out of the 44 papers selected for review, 20 do not specify any form of evaluation or validation. Conversely, 24 studies do incorporate validation, with 16 of these papers extending their validation efforts to real-world systems or scenarios, as shown in .

18 researches utilize case studies for validation. For example, by incorporating domain knowledge through ontology, proposed a framework to enhance the precision and accuracy of automated threat models, and is validated using three different case studies, namely a small-scale utility lab, water utility control network, and university IT environment. Dedousis et al. introduced a security-aware framework that utilized material flow networks (MFN) for modeling and designing the , aiming to ensure the safety and security of critical infrastructures right from the early design stages. Their proposed framework is evaluated by modeling and assessing the production chain of an oil refinery plant’s liquefied petroleum gas purification process. The ThreMA approach propose by De Rosa et al. is validated through case studies from the Italian Public Sector, demonstrating its effectiveness in automating threat modeling and enhancing threat identification processes. Similarly, performed validation through two case studies of instantiated power-grid models and expert interviews demonstrated the structural and functional adequacy, compatibility, and coverage of the proposed taxonomy and models.

Table 6. Utilized validation method for enterprise modeling.

6 papers employed interviews or questionnaires as methods to collect user insights for validation purposes. Aldea et al. initially conducted a case study within an actual production organization in Lithuania. Subsequently, they expanded their research methodology to include survey questionnaires and expert panel studies, aiming to gather comprehensive feedback on their proposed enterprise architecture model. Meanwhile, utilized interviews to obtain feedback on the practicality and applicability of their proposed reference model, specifically focusing on its relevance to a power grid operator’s network that encompasses both IT and OT components.

6 works adopt experiments or simulations for validation. For instance, presented a CAD tool for enterprise cyber security management called SecuriCAD as a modeling framework and calculation engine that estimates the cyber security of systems-of-systems-level architectures. Aldea and Hacks and performed analysis of the possible with the help of the SecuriCAD attack simulations. Ellerhold et al. utilized a combination of probability distributions and to quantify the potential risk associated with a loss event.

Overall, nearly half of the reviewed papers (20 out of 44) lack any form of evaluation or validation, raising concerns about the reliability and applicability of the proposed models in practical scenarios. The diversity in validation methods, including case studies, simulations, experiments, interviews, and questionnaires, highlights the importance of multi-faceted evaluation approaches in advancing research and practice in this field.

### 4.4. Answer to RQ4: What are the integrated cybersecurity aspects in enterprise modeling, especially in the context of critical infrastructures?

The enterprise-central methodology for cybersecurity necessitates the concurrent execution of risk management across various layers, including business, application, data, and technology, integrating these aspects cohesively , . Fundamental to risk assessment is the business impact analysis, while business continuity planning stands as the cornerstone of risk response. Both these processes demand accurate and detailed information about the enterprise. This knowledge should, at a minimum, encompass a simplified set of principles that define the enterprise’s mission and the methods employed to achieve it. Moreover, the enterprise architecture should guide the process of change management, encompassing significant updates in security policies and their execution.

#### 4.4.1. Explored critical infrastructure sectors

The reviewed 44 papers reveal a diverse range of CI sectors being addressed in enterprise architecture modeling, with a predominant focus on the energy sector, with 13 papers, indicating it as the most explored area, as presented in . Transportation also receives notable attention with 4 papers. In contrast, sectors like healthcare and public health, food and agriculture, water and wastewater systems, and critical manufacturing are less represented, each discussed in only one paper.

The prominent representation of the energy sector in enterprise modeling research can be attributed to its critical role in modern infrastructure systems and the intricate interconnections within its network , . Energy systems frequently serve as a foundation for other vital sectors, naturally positioning them as a focal point for enterprise modeling research endeavors. Particularly, the communication, energy, transportation, water, and waste sectors are regarded as “lifeline” infrastructures by the US Department of Homeland Security .

In contrast, sectors like healthcare, public health, food and agriculture, water and wastewater systems are less represented, each discussed in only one paper. This disparity may stem from several factors. For instance, the healthcare sector, while critical, may have unique complexities and regulatory challenges that make it less amenable to general enterprise modeling approaches.

Additionally, there are 5 papers addressing CIs in a more general context without specifying a particular sector. This distribution highlights a strong research focus on energy and transportation, while other critical sectors like healthcare and water systems present opportunities for further exploration in enterprise modeling.

Table 7. Critical infrastructure sectors involved in the enterprise modeling.

#### 4.4.2. Enterprise modeling for cyber security

categorizes the reviewed papers based on different security perspectives in the context of enterprise modeling. The most prominent category is “Attack Simulation” with 12 papers, indicating a strong research focus on simulating to test system defenses.

“Security by Design” follows with 7 papers, emphasizing the integration of security measures in the initial design stages of systems. 4 papers explicitly incorporate the concept of ‘security by design’ in their discussions and analyses, while 3 more papers utilize this concept in their reference models. Each of these studies emphasizes the importance of integrating security considerations into the design phase of system development, underscoring the critical role of measures in contemporary enterprise modeling. In the works of Casola et al. , for example, their conceptual model of CPS supports the implementation of the model-based (MTD) approach by providing a comprehensive system model that describes the main architectural elements (assets) and the associated data flow. The MTD techniques, as described in their work, encompass a strategy of continuously altering the system’s configuration. This serves to augment uncertainty for potential attackers, thereby diminishing the likelihood of successful cyber attacks.

“Security by Design” emphasizes integrating security considerations into the early stages of system development, ensuring that security measures are inherent in the system’s architecture and design principles . In contrast, works focused on security requirements primarily concentrate on identifying and specifying the security needs and objectives for a given system, typically as a part of the overall functional and non-functional requirements .

Initiatives (5 out of 44 papers) are being undertaken to enhance the reusability of threat models within the context of enterprise architecture models. For instance, emphasized the importance of incorporating security measures from the early stages of development and addresses the challenges of cost-effectiveness in analyzing . ThreMA, proposed by De Rosa et al. , utilizes ontology and inference rules to automate the threat modeling process.

Table 8. Enterprise modeling for cyber security.

Enterprise architecture models are utilized to enhance resilience analysis of such complex systems. For example, conducted a to determine the usefulness of their proposed resilience assessment framework (RAF), both with and without the incorporation of the enterprise architecture model. Their conclusion affirmed the hypothesis that the inclusion of an enterprise model significantly enhances the assessment of resilience. Hoffmann et al. applied enterprise architecture modeling to analyze and address security and resilience in the context of urban air mobility operations.

To effectively identify vulnerabilities, a comprehensive risk analysis is required, encompassing a top-down evaluation from business principles and objectives to business functions, and extending to security controls , . This should be complemented by a bottom-up approach for thorough traceability and assessment. Such an analysis is facilitated by a detailed understanding of the enterprise architecture, coupled with a corresponding risk assessment.

Researchers have proposed methods aimed at evaluating the impacts of risks on enterprises. Ellerhold et al. incorporated the MITRE ATT&CK Matrix into their approach, mapping it to a unified kill chain model. This integration enabled them to account for chronological factors within their factor analysis of risk and risk calculation processes. Furthermore, system dependencies are analyzed to support fine-grained risk analysis. As an illustration, employed a risk assessment and dependency analysis methodology to evaluate the cascading impacts resulting from process disruptions. Their approach involved constructing a material flow network graph and utilizing a recursive algorithm to calculate the associated dependency risks.

#### 4.4.3. Challenges of integrating security

The papers under review shed light on the integration of cybersecurity within enterprise modeling, particularly evident in their modeling processes and the validation of their proposed models.

Hause addressed the difficulties in integrating security into existing . They highlighted the frameworks’ lack of traceability between security requirements and corresponding architectural elements, limited coverage of security requirements, and inadequate support for trade-off analysis.

de Kinderen et al. delved into the challenges associated with employing reference models for cybersecurity objectives. These challenges encompass the simultaneous consideration of both broad and specific elements, the difficulty in articulating variability while minimizing repetition within the model, and the complexities inherent in facilitating the application and modification of a reference model while ensuring compliance with standards.

Aldea and Hacks identified a significant deficiency in enterprise architecture models concerning security. They observed that commonly used enterprise modeling languages, such as ArchiMate, do not possess the necessary features for conducting security analysis. This gap indicates that enterprise architecture models lack critical information required for performing security evaluations, thereby presenting substantial challenges in identifying specific vulnerabilities and conducting thorough security assessments. Moreover, the vastness of enterprise , combined with a lack of comprehensive security expertise among enterprise architects, presents considerable obstacles to the automation of cybersecurity analysis in this domain.

Furthermore, the scale of enterprise architecture model repositories and the scarcity of in-depth security expertise among enterprise architects are major hindrances to the automation of cybersecurity analysis. For instance, identified practical challenges in adopting modeling, such as automated model creation, adaptation to evolving security requirements, management of multi-level models, and incentivization of users. Aldea and Hacks also noted that popular enterprise modeling languages like ArchiMate are deficient in capabilities for conducting security analysis. This limitation impedes the identification of vulnerabilities and the execution of comprehensive security assessments. These challenges underscore the complexities in effectively integrating enterprise modeling with security measures, emphasizing the necessity for continued research and development in this field to surmount these barriers.

To summarize, while significant progress has been made in integrating cybersecurity into enterprise modeling, several challenges remain. The energy sector has received the most attention, reflecting its critical importance, while other vital sectors like healthcare and water systems are underrepresented, indicating areas that require further research. Cybersecurity perspectives such as attack simulations and security-by-design are commonly incorporated into enterprise modeling, yet other crucial aspects like security assurance are often overlooked. Simultaneously, the lack of comprehensive security features in widely-used modeling languages and the complexity of integrating detailed security requirements highlight the ongoing need for research and development in this field. Addressing these challenges is pivotal to enhancing the robustness and practical applicability of enterprise architecture models in safeguarding critical infrastructures against ever-evolving cyber threats.

## 5\. Discussion

### 5.1. Status of current models

Research efforts in the realm of CIs, especially within the sub-domain of smart grids, have been directed toward offering structured and clear directives for the design of CI frameworks, as seen in . It has been observed that previously proposed enterprise architecture models tend to be specific to particular domains and technologies. While the principles underlying the creation of an enterprise architecture framework can be adapted to new domains, modifications from the original framework are often necessary.

Among the 44 papers reviewed, only 18 incorporate a meta-model or a domain-specifc language (as seen in ). This observation highlights a significant gap in the current research landscape, emphasizing the necessity for a comprehensive, CI agnostic meta-model. The absence of such a model underscores the challenges associated with domain or industry-specific enterprise architecture models, which often suffer from limited adaptability and reduced applicability across various contexts. Furthermore, another limitation in the current methodologies is evident in defining components and their interrelationships within these frameworks (only 7 out of 44 papers include reference models). The existing lack of detail hinders a thorough understanding that is essential to navigate the complex realm of ICS.

The review of 44 papers on enterprise modeling for security reveals a concerning trend regarding the maturity of these models, particularly in terms of their validation. As presented in , the fact that nearly half of the papers (20 out of 44) do not specify any form of evaluation or validation underscores a significant gap in the field. This lack of validation raises questions about the reliability and applicability of the proposed models in real-world scenarios. Among the papers that do incorporate validation, the majority rely on case studies. While case studies, such as those conducted by Välja et al. and , provide valuable insights into the practical application of these models, they may not fully capture the complexity and variability of real-world environments. Case studies often focus on specific scenarios or contexts, which may limit the of the findings. Moreover, the diversity in the case studies – ranging from utility labs to university IT environments – suggests a wide range of , yet it also indicates a potential lack of standardized approaches in validation.

### 5.2. Threats to validity

- 1.
- 2.
	To assess the reliability of findings, we evaluated factors such as publication bias, author affiliation, and study methodology to gauge the methodological rigor and validity of the included studies.
- 3.
	To address the potential for review bias, we developed clear inclusion and exclusion criteria to guide the selection of studies, and multiple reviewers independently conducted screening and data extraction processes to minimize the risk of bias.

### 5.3. Recommendations

We draw the following recommendations from this review, to address gaps and to develop the potential of enterprise architecture models for assessing the cyber security of enterprises:

- 1.
	Standardize the enterprise architecture framework for cybersecurity assessment. The reviews shows that ArchiMate is most-widely used and thus appears as a prominent candidate for standardization. The standardization would allow easier sharing of cybersecurity assessment methods.
- 2.
	Improve the semantic foundation of enterprise architecture models. While ArchiMate is most widely used, it lacks a foundations to detect flaws and weaknesses in enterprise models, in particular relating to cybersecurity assessment.
- 3.
	Include more artifact types in enterprise modeling languages to components to allow for a more comprehensive representation of modern enterprise systems that often involve a convergence of IT and OT elements.
- 4.
	Support the extraction of partial models from enterprise architecture models, such as models of the computer network, as input for external analysis tools such as attack simulators.
- 5.
	Develop tools for automatic of enterprise architecture models from existing sources such as software registries and log files. A manual maintenance of enterprise architecture models is increasingly difficult at the high rate of changes in the real enterprise. In particular for cybersecurity assessment, an up-to-date enterprise architecture model is important.

### 5.4. Models, standards, and practical considerations

Practitioners lean on established models and standards to craft secure and resilient OT environments. A historical bedrock of this field is the Purdue model as also discussed earlier. This model structured OT environments hierarchically from Levels 0 to 4, offering a systematic approach to understanding information flow. The model found practical application in operational segmentation, enhancing security by isolating critical control systems from enterprise networks.

Complementing this, the IEC62443 series, developed by the International Electrotechnical Commission (IEC) and International Society of Automation (ISA), stands as a contemporary set of standards tailored for industrial automation and control systems security. These standards have evolved from the collaborative efforts of international organizations, reflecting a response to the increasing sophistication of cyber threats in industrial environments. IEC62443 takes a comprehensive approach, encompassing risk assessment, policies, procedures, and technical controls, providing practitioners with a robust toolkit. The standards also feature sector-specific adaptations, ensuring applicability across diverse industries and offering tailored security measures.

While the Purdue Model stands as a pioneering framework, its roots in a pre-Industry 4.0 era pose challenges in adapting to the dynamic, interconnected nature of modern industrial environments. The model’s historical focus on traditional systems may not fully address the security implications of emerging technologies, leading to gaps in overall .

In contrast, the IEC62443 series, grounded in international collaboration, represents a responsive effort to the evolving threat landscape. Despite its strengths, the depth of IEC62443 can pose challenges in implementation, particularly for smaller enterprises with limited resources. The standards emphasize robust guidelines for mitigating cyber threats, yet there is a perceived bias toward reactive measures rather than proactive strategies. A more anticipatory approach to threat prevention is desired to enhance overall cybersecurity resilience, aligning with the dynamic nature of emerging threats. Understanding these limitations is crucial for organizations aiming to implement the IEC62443 standards effectively within the context of existing industrial environments. Despite these challenges, the standards remain a valuable tool for enhancing the cybersecurity posture of ICS when implemented thoughtfully and with due consideration for the specific context of each organization.

However, as the cybersecurity landscape evolves with the integration of more sophisticated technologies, a critical challenge emerges. The focus of current standards and models, while predominantly security-oriented, may not adequately address the need for end-to-end visibility in the entire . The increasing complexity of industrial environments requires a balanced approach across all architecture layers, encompassing not only security aspects but also the broader design considerations. The absence of a comprehensive end-to-end reference model hinders practitioners from gaining holistic insights and designing ICS environments that are not only secure but also optimized for efficiency and resilience.

One challenge arises from the difficulty to identify and manage assets in both IT and OT environments. In OT environments, only about 20% of the assets are traditional IT systems, which can be easily documented using standard IT asset discovery tools . The remaining 80% of OT assets, however, are challenging to identify and document due to their non-standard protocols. This leads to limited visibility over these assets, as information is often manually collected and maintained, increasing the risk of missing assets. The heterogeneity of industrial environments, with a mix of devices from various vendors and both legacy and modern systems, further complicates comprehensive asset documentation.

Stakeholders, who have varied responsibilities, currently face the absence of a unified framework, which obstructs effective . Consider a scenario where a CI depends on a of devices, encompassing both legacy systems and contemporary technologies. In traditional IT environments, frameworks like TOGAF provide specific data architecture artifacts that guide the organization and management of data. However, these established norms may not be directly applicable to OT systems, presenting a distinct challenge. The lack of a detailed understanding of data architecture components and their interrelationships in the OT domain poses significant challenges for stakeholders in selecting and implementing suitable cybersecurity controls.

The current state of affairs, characterized by an incomplete representation in the ICS architecture, underscores a challenge in achieving comprehensive insights across diverse layers, including business, data, application, and technology. Existing standards and frameworks, while providing valuable guidance, often exhibit gaps that hinder a holistic understanding of the entire industrial control landscape. This leaves asset owners ill-equipped to make informed decisions on cybersecurity measures. The adoption of emerging technologies in ICS further amplifies this challenge, as traditional frameworks may not adequately address the security implications of these advancements. This limitation not only affects the current cyber but also creates a hurdle in anticipating changes from both cyber and operational perspectives in the unique context of ICS. The void in understanding restricts the ability to proactively assess and mitigate potential risks, especially in the face of accelerating technological advancements.

## 6\. Conclusion

In conclusion, this paper has provided a comprehensive exploration of enterprise architecture models in the context of cybersecurity, particularly within CIs. Our systematic literature review on papers published in Scopus, IEEE Xplore and ACM Digital Library before 2024 has highlighted the various methodologies, theoretical frameworks, and research methods employed in the development and evaluation of enterprise architecture models for cybersecurity assessment. We have identified key areas where enterprise architecture models excel in integrating security aspects and pinpointed their strengths and limitations in supporting cybersecurity assessments.

While there are efforts to validate enterprise modeling for security, the current state reflects a certain level of immaturity. The reliance on case studies, while valuable, is not sufficient to fully validate the models. There is a need for more standardized, rigorous, and diverse validation methods, including controlled experiments and simulations, to ensure the reliability and of these models. This gap in validation not only limits the practical application of the models but also hinders the advancement of the field as a whole.

As we move forward, it is imperative for researchers and practitioners to focus on enhancing the interoperability, consistency, timeliness, and comprehensiveness of enterprise architecture models in cybersecurity. Future research should aim to address the identified gaps, explore new methodologies, and test the effectiveness of these models in diverse and evolving cybersecurity landscapes. By doing so, we can ensure that enterprise architecture models remains a robust and dynamic tool in the fight against cyber threats in critical infrastructure sectors.

## CRediT authorship contribution statement

**Yuning Jiang:** Writing – review & editing, Writing – original draft, Methodology, Formal analysis, , Conceptualization. **Manfred A. Jeusfeld:** Writing – review & editing, Methodology, Formal analysis. **Michael Mosaad:** Writing – original draft, Conceptualization. **Nay Oo:** Writing – review & editing.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgments

The 2nd author was supported in part by the PICS collaboration platform at the University of Skövde, [https://www.his.se/en/pics](https://www.his.se/en/pics). This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

## Data availability

No data was used for the research described in the article.