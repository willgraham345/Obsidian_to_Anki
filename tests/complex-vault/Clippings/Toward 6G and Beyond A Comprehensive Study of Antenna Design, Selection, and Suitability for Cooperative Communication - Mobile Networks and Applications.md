---
summary: 
headings:
type:
source: "https://link.springer.com/article/10.1007/s11036-025-02464-7"
author: ["[[Ali Nauman]]", "[[Sung Won Kim]]", "[[Syed Kamran Haider]]", "[[Tahir Khurshaid]]"]
created: 2025-10-09
date created: Thursday, October 9th 2025, 3:34:01 pm
date modified: Thursday, October 9th 2025, 3:35:22 pm
description: "Sixth Generation (6G) networks target minimal latency, elevated data throughput, and uninterrupted connectivity. Cooperative communication improves reliabi"
published: 2025-10-05
tags: ["clippings", "toread"]
template:
template-version:
title: "Toward 6G and Beyond: A Comprehensive Study of Antenna Design, Selection, and Suitability for Cooperative Communication - Mobile Networks and Applications"
---

## Toward 6G and Beyond: A Comprehensive Study of Antenna Design, Selection, and Suitability for Cooperative Communication

- Review
- Published:
- (2025)
- [Cite this article](https://link.springer.com/article/10.1007/#citeas)

Access provided by Utah State University Libraries

 [![](https://media.springernature.com/w72/springer-static/cover-hires/journal/11036?as=webp) Mobile Networks and Applications](https://link.springer.com/journal/11036) [Aims and scope](https://link.springer.com/journal/11036/aims-and-scope) [Submit manuscript](https://submission.springernature.com/new-submission/11036/3)

## Abstract

Sixth Generation (6G) networks target minimal latency, elevated data throughput, and uninterrupted connectivity. Cooperative communication improves reliability via collaborative devices and networks. Antennas are pivotal signal interfaces in these complex systems. This paper presents an exhaustive analysis of antenna design and its appropriateness for cooperative communication in 6G and future advancements. The study addresses the essential conditions requisite for 6G communication. These conditions primarily involve the utilization of higher-frequency bands, an increased number of connected terminals, and advanced beamforming techniques. It examines antennas such as the Multiple-Input-Multiple-Output (MIMO) and Reconfigurable Intelligent Surfaces (RIS) to assess their role in meeting 6G requirements. The article further reviews high-frequency communication phenomena like path loss, which intensifies with frequency, and improved transmission direction accuracy. It explores innovative antenna designs that alleviate these issues through developments in materials, configurations, and adaptability. Additionally, the importance of these antennas for prospective 6G applications, including autonomous vehicles, smart cities, and the Internet of Things (IoT), is analyzed.

### Similar content being viewed by others

### Future prospects of 6G wireless communication: review of antenna technologies

Article Open access 24 December 2024

### A Novel MIMO Antenna for 6G Applications

Chapter © 2023

### A Survey of 6G Wireless Communications: Emerging Technologies

Chapter © 2021

[Use our pre-submission checklist](https://beta.springernature.com/pre-submission?journalId=11036)

Avoid common mistakes on your manuscript.

## 1 Introduction

The rapid and notable advancements in wireless communication networks have not only introduced new modes of connectivity but also created fertile ground for the next generation of networks, known as Sixth Generation (6G). The capabilities of 6G are expected to revolutionize current technology by delivering features that were previously considered extraordinary and unattainable \[[^1], [^2]\]. The goals of 6G networks are to realize ultra-wideband communication capable of data transmission rates far beyond the existing figures and achieving a global coverage with extremely low latencies \[[^3],[^4],[^5]\]. This will afford a variety of complex applications ranging from fully autonomous real-time systems to high levels of Augmented Reality (AR) and Virtual Reality (VR) interactivity \[[^6], [^7]\]. Nonetheless, achieving these capabilities means that there has to be a radical rethinking of the architecture of the network, introducing new concepts – especially in respect to cooperative communication networks. This approach necessitates the concerted effort of multiple devices and network elements to enable reliable signal transmission over Long distances, enhance service delivery, and improve the overall efficiency of the system. In the context of 6G, where network conditions will be more challenging than ever before, cooperative communication is expected to play a crucial role in establishing stable, high-quality connections. It will serve as one of the core elements to ensure the performance and reliability of future networks.

In this context, antennas emerge as fundamental elements of 6G networks. As the primary interfaces for signal transmission and reception, antennas play a critical role in managing the data flows central to cooperative communication. Given 6G’s reliance on higher frequency bands, such as the Terahertz (THz) spectrum, antennas must also contend with unique challenges, including increased path loss, propagation constraints, and the need for precise directional transmission \[[^8],[^9],[^10],[^11]\]. These conditions necessitate advanced antenna designs that can deliver robust performance under 6G’s demanding operational conditions. Thus, exploring and optimizing antenna technologies for 6G is essential to meeting the network’s performance targets and enabling effective cooperative communication \[[^12],[^13],[^14]\].

This article has three objectives. First, it aims at an in-depth study of Various antenna technologies that can play a very crucial role in the advancement of 6G communication in terms of design architectures, performance standards and possible shortfalls. Second, and on the same scope, how these antenna technologies, for example, the emerging Multiple-Input-Multiple-Output (MIMO) systems and Reconfigurable Intelligent Surfaces (RIS) address the high-frequency particularities of 6G and beyond \[[^15],[^16],[^17],[^18],[^19]\]. Thirdly, moving beyond the participatory focus, these implications carry for critical 6G applications such as self-driving cars, smart cities, Internet of Things (IoT) and most importantly, advancements in antennas to facilitate all these superior applications.

In summary, this paper contributes a comprehensive analysis of the design, selection, and suitability of antenna technologies for cooperative communication in 6G and beyond. By evaluating the technological adaptations needed to meet 6G’s requirements, this study provides valuable insights for researchers and engineers aiming to advance antenna capabilities in support of the next generation of wireless networks.

## 2 6G Wireless communication: antenna perspective overview

The ongoing evolution of communication technologies vividly illustrates how each generation reshapes the core focus of network infrastructures and wireless systems. The transition from the Second Generation(2G) of mobile communication, to the Fifth Generation(5G),, distinctly illuminates the evolving priorities within this domain \[[^20], [^21]\]. Early generations like 2G and Third Generation (3G) were primarily designed for basic communication such as voice calls and text messaging. However, with the advent of Fourth Generation (4G), the focus moved to more advanced, data-driven, and multimedia applications. This trend continues with 5G, which supports more complex connectivity, including the IoT and automation capabilities \[[^22],[^23],[^24]\]. Figure  [1](https://link.springer.com/article/10.1007/s11036-025-02464-7#Fig1) offers a detailed visual timeline tracing the development of wireless communication technologies, extending through the anticipated arrival of 6G.

![figure 1](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs11036-025-02464-7/MediaObjects/11036_2025_2464_Fig1_HTML.png?as=webp)

**Fig. 1**

The shift to 6G wireless technology is expected to bring about an even greater transformation by enabling the seamless blending of the digital, physical, and human realms. This integration is poised to enhance sensory experiences, combining advanced computing capabilities with complex knowledge systems to boost human productivity and drive innovation across industries and daily life \[[^25],[^26],[^27],[^28],[^29]\]. Moreover, 6G aims to go beyond just faster networks; it seeks to elevate experiences in areas like VR, AR, and holographic communication, while embedding intelligence throughout its infrastructure to support automation and the development of smart environments \[[^30]\].

A pivotal element of the 6G epoch will be the implementation of the Network Operation Support System (NOSS), which is anticipated to augment network governance through the facilitation of sophisticated automation, intelligence, and the establishment of digital twins \[[^31], [^32]\]. These digital representations of tangible systems will enable real-time observation, administration, and interaction among interconnected agents, thereby contributing to the development of more intelligent and efficient systems. In conjunction with advancements in positioning and sensing technologies, 6G networks are poised not only to realize unparalleled communication capabilities but also to advance broader objectives of sustainability, inclusivity, and trust \[[^33], [^34]\].

Central to the overarching efficacy and operational success of the impending 6G technology will indisputably be the cutting-edge and innovative antenna technology, which will be essential in effectively addressing and accommodating the escalating demand for not only superior performance metrics and enhanced operational efficiency but also designs that are aesthetically pleasing and visually appealing to the end user \[[^35],[^36],[^37]\].In this complex landscape of telecommunications, antennas will occupy a crucial and indispensable position in enabling the ultra-fast, exceptionally reliable, and fundamentally secure communication that is critical for the ambitious and transformative applications anticipated for 6G technology \[[^38]\]. Moreover, substantial innovations in antenna design, with a specific focus on advancements in beamforming technology, will be indispensable and vital for the improvement of signal accuracy while concurrently striving to reduce latency to levels that are acceptable for real-time communication \[[^39],[^40],[^41]\]. Furthermore, the deployment of advanced and sophisticated antenna systems will be of paramount significance in effectively addressing the diverse security challenges that are increasingly prominent in our swiftly evolving digital environment, as these systems must be fortified with robust defenses against the ever-growing and increasingly intricate nature of cyber threats that endanger our information and communication infrastructures \[[^42]\].

As 6G pushes the boundaries of wireless communication, it will rely heavily on operating at higher frequencies, such as millimeter-wave (mmW) and THz bands, as depicted in Fig. [2](https://link.springer.com/article/10.1007/s11036-025-02464-7#Fig2). These higher frequencies promise to deliver data rates exceeding 100 Gbps, which will enable new applications such as, health monitoring systems, the Internet of Nano-Things (IoNT), ultra-fast on-chip communication, environmental pollution detection, military uses, entertainment technologies, AR, satellite communications, directional communication links, and heterogeneous networks \[[^8], [^43]\]. To enable these THz-based applications, new 6G use cases will be developed, as these applications fall under the emerging 6G scenarios. The future of 6G will integrate existing use cases from the 5G standard with new advancements, such as Mobile Broadband Reliable Low Latency Communication (MBRLLC), massive Ultra Reliable Low Latency communication (mURLLC), Human-Centered Services (HCS), and multi-purpose energy services \[[^3]\]. However, with the shift to higher frequencies comes significant challenges, including increased free-space path loss and greater material absorption. These challenges will require the development of high-gain antenna arrays, intelligent beamforming techniques, and multi-frequency band support to ensure robust communication across longer distances \[[^44]\].

![figure 2](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs11036-025-02464-7/MediaObjects/11036_2025_2464_Fig2_HTML.png?as=webp)

**Fig. 2**

In summary, 6G will not only revolutionize wireless communication with its intelligent, immersive, and ultra-fast connectivity but will also depend Heavily on advanced antenna technologies to support its ambitious vision. From enabling digital twins to facilitating next-generation applications, antenna systems will be pivotal in overcoming the technical challenges posed by high-frequency operation and ensuring the success of 6G across diverse sectors.

## 3 Antenna technologies for 6G

The 6G communication network must be precisely designed for various applications requiring ultra-high data rates, potentially reaching terabits per second, while ensuring broad coverage and high reliability \[[^45]\]. Advanced multi-antenna technologies, such as MIMO and RIS, are essential for enhancing the network’s functionality \[[^46], [^47]\]. The next subsection will provide a detailed explanation of MIMO and RIS.

### 3.1 MIMO

MIMO enables simultaneous data stream transmission and reception through multiple transmitters and receivers in a single channel. MIMO devices, particularly those compliant with the 802.11 n standard, demonstrate increased data transfer rates relative to non-MIMO counterparts \[[^48], [^49]\]. Successful MIMO performance requires both the mobile device (station) and the Access Point (AP) to have MIMO capabilities. To achieve optimal performance and extended range, both the station and the AP must be designed to be MIMO-compatible \[[^50]\].

MIMO technology takes advantage of a radio-wave phenomenon called multipath, where transmitted signals bounce off surfaces such as walls and ceilings, arriving at the receiver at different angles and times. Previously, multipath caused interference and degraded signal quality, but MIMO leverages it by using multiple intelligent transmitters and receivers. This introduces a spatial dimension that enhances performance and range. By combining data streams from different paths and times, MIMO improves signal reception. It utilizes spatial diversity technology, allowing additional antennas to boost signal strength and extend range when there are more antennas than spatial streams \[[^51], [^52]\].

Increased antennas correlate with enhanced speeds. For instance, a three-antenna wireless adapter can attain 600 Mbps, whereas a two-antenna Variant reaches 300 Mbps \[[^53]\]. Nevertheless, achieving these speeds necessitates a router with multiple antennas that fully complies with the 802.11 n standard. Legacy wireless devices utilize Single-Input-Single-Output (SISO) technology, which permits the transmission or reception of only one spatial stream at any given time \[[^53]\]. An example of MIMO technology is depicted in Fig. [3](https://link.springer.com/article/10.1007/s11036-025-02464-7#Fig3).

![figure 3](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs11036-025-02464-7/MediaObjects/11036_2025_2464_Fig3_HTML.png?as=webp)

**Fig. 3**

MIMO will see enhanced capabilities in 6G networks, building on its current use in 5G. massive MIMO (mMIMO) utilizes extensive antenna arrays to boost spectral efficiency and capacity by serving multiple users concurrently. Cooperative Full-Duplex MIMO (CF-MIMO) integrates full-duplex communication with MIMO, thereby enhancing spectral efficiency and potentially doubling capacity compared to half-duplex systems. Extra-Large MIMO (XL-MIMO) extends mMIMO by significantly increasing antenna numbers, facilitating higher capacity and broader coverage in densely populated areas \[[^54], [^55]\].

Multiband MIMO further enhances wireless communication by allowing the simultaneous use of multiple frequency bands \[[^56], [^57]\]. This enables the system to cover multiple applications while reducing interference and device size \[[^58]\]. Multiband antennas provide a significant advantage by eliminating the need for separate antennas for different wireless applications. The design of a multiband antenna begins with the careful selection of the patch, followed by numerous iterative simulations and optimizations to achieve the desired operating frequency \[[^59]\]. A common method for realizing multiband antennas is through the use of multiple branches, with each branch acting as a resonating element. Additional methods for achieving multiband functionality are outlined in Fig. [4](https://link.springer.com/article/10.1007/s11036-025-02464-7#Fig4).

![figure 4](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs11036-025-02464-7/MediaObjects/11036_2025_2464_Fig4_HTML.png?as=webp)

**Fig. 4**

![figure 5](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs11036-025-02464-7/MediaObjects/11036_2025_2464_Fig5_HTML.png?as=webp)

**Fig. 5**

### 3.2 Reconfigurable intelligent surfaces

RIS are two-dimensional structure composed of materials with large-scale programmable physical properties \[[^60]\]. Its key feature is the ability to modify its interaction with electromagnetic waves, enabling dynamic control over communication channels between transmitters and receivers. This adaptability enhances signal strength at receiving devices, a capability that sets RIS apart from traditional wireless systems, where channel conditions are static \[[^61]\]. An illustration of RIS is provided in Fig. [5](https://link.springer.com/article/10.1007/s11036-025-02464-7#Fig5).

RIS can be realized using either metamaterial-based or patch-array technologies. When built with metamaterials, RIS is referred to as a metasurface. Based on their deployment, RIS can act as reflecting or refracting surfaces between the Base Station (BS) and the user or serve as waveguides directly at the BS. RIS can be tuned through various mechanisms—electrical, mechanical, or thermal—to achieve reconfigurability \[[^62]\]. Based on their energy consumption, RIS are categorized as passive-lossy, passive-lossless, or active, with the active/passive nature influencing their performance potential. However, it is important to note that RIS cannot be completely passive due to the inherent requirement for reconfiguration \[[^62], [^63]\].

The electromagnetic properties of RIS, such as phase discontinuity, can be fine-tuned by adjusting the surface impedance through several approaches \[[^64], [^65]\].Besides electrical voltage, other methods like thermal excitation, optical pumping, and physical stretching can be employed. Among these, electrical control is the most convenient and practical, as electrical voltage is easier to quantify and control through Field Programmable Gate Array (FPGA) chips. Common materials used in RIS construction include semiconductors and graphene, which support efficient tuning \[[^64]\].

In recent years, RIS technology has gained significant attention in both academia and the wireless industry due to its wide-ranging benefits for modern mmW and traditional sub-6 GHz communication systems. These benefits include enhanced radio coverage and reduced energy consumption for radio subsystems \[[^66]\]. RIS technology presents a viable solution to coverage issues by enabling configurable reflection, refraction, and scattering of radio signals, particularly in the mmW range. For example, RIS can assist radio signals from BS in reaching mobile devices more efficiently and vice versa \[[^67]\]. Additionally, RIS improves multipath propagation, leading to better spatial multiplexing and higher network throughput. Moreover, RIS can be strategically used to create intentional dead zones, minimizing interference or preventing eavesdropping by unauthorized devices. Given these advantages, RIS has numerous potential applications in wireless networks \[[^68]\].

The long-term vision for RIS technology is to create intelligent radio environments where wireless propagation conditions are co-engineered with physical-layer signaling to fully leverage this new capability. Traditionally, wireless technology focuses on the first three layers of the protocol stack: physical, Link, and network. Typically, the design process starts at Layer 1, where physical signals are generated by the transmitter, then measured and decoded by the receiver. The wireless medium between the transmitter and receiver, known as Layer 0, has traditionally been viewed as uncontrollable and governed by Natural conditions. However, RIS technology revolutionizes this concept by extending the protocol design to Layer 0, offering unprecedented control over the wireless environment. This development could significantly advance wireless systems beyond 5G, unlocking new possibilities for optimized communication networks, more specifically for cooperative communication scenarios \[[^69]\].

## 4 Antennas requirements: a 6G-enabled cooperative communication vision

As we transition from 5G to 6G wireless communication, it is crucial to acknowledge the expected revolutionary enhancements in transmission speed, latency, and connectivity. These improvements will significantly alter the global communications framework. Key innovations in 6G systems include the use of high-frequency bands, extensive connectivity capabilities, and advanced antenna technologies that improve network efficiency. This section provides an in-depth analysis of essential aspects of 6G technology, focusing on challenges related to high-frequency THz bands, the implications of massive connectivity, advanced beamforming techniques, and the unique requirements for cooperative communication strategies \[[^70]\].

### 4.1 High-frequency bands (THz frequencies) and their challenges

One of the most salient characteristics that distinguishes 6G is its innovative and strategic utilization of high-frequency electromagnetic bands, particularly the THz frequency range, which encompasses a spectrum from 0.1 to 10 THz. The frequencies employed in this advanced communication paradigm are markedly higher than those used in 5G, which predominantly operates within sub-6 GHz frequency ranges and mmW bands. This presents an extraordinary augmentation in bandwidth availability. However, engaging with THz frequencies brings forth a multitude of intricate technical challenges that profoundly impact the design and optimization of antennas, necessitating innovative solutions and a reevaluation of existing methodologies in antenna engineering \[[^44]\].

### 4.2 Path loss and signal attenuation

THz waves experience significantly elevated levels of path loss when compared to their lower frequency counterparts, particularly when traversing extended distances, which presents a notable challenge in communication technologies. This heightened level of attenuation necessitates the implementation of highly directional antennas that possess the capability to effectively concentrate the signal, thereby reducing the extent of dispersion that occurs during transmission. In the absence of such specialized directional antennas, engaging in effective communication within the THz frequency range would be rendered impractical, as the rapid degradation of the signal would ultimately inhibit reliable data transfer \[[^8]\].

### 4.3 Material considerations

Materials, along with Various environmental factors, exert a considerable influence on the overall effectiveness and efficiency of THz communication systems, which are increasingly being explored for advanced telecommunications. It is noteworthy that certain materials exhibit a higher propensity to absorb THz waves compared to others, and additionally, atmospheric conditions, including but not limited to humidity levels, can profoundly affect the quality and reliability of signal transmission, potentially leading to significant degradation of communication performance. As a direct result of these observations, it becomes imperative that antennas designed for the upcoming 6G communication systems are meticulously engineered with careful consideration of these environmental variables, potentially necessitating the integration of innovative materials or the implementation of adaptive technologies that could effectively counteract or mitigate the adverse impacts posed by such factors \[[^43]\].

### 4.4 Massive connectivity needs and antenna design implications

The 6G of wireless communication is anticipated to enable the concurrent connectivity of an extraordinary number of devices, thereby delivering vital support for a multifaceted array of applications, which encompasses, but is not confined to, the IoT, the conceptualization and administration of smart cities, alongside a myriad of additional technological advancements and services that are surfacing in our progressively interconnected global framework \[[^71]\]. The projected density of interconnected devices that 6G is expected to accommodate will necessitate, and in turn catalyze, significant advancements and innovations in antenna design, which must adapt to effectively address the extensive connectivity demands engendered by such a substantial volume of simultaneously connected devices. In consideration of this transformative capacity, the ensuing updates and developments are crucial factors that must be meticulously assessed and analyzed in order to comprehensively grasp the ramifications of 6G technology on our societal and technological ecosystem \[[^54]\].

- **Multi-Antenna Arrays:** To handle the Vast number of devices, 6G antennas must be designed to support mMIMO systems. This involves large arrays of antennas that can transmit and receive data from many devices simultaneously, increasing system capacity without consuming excessive bandwidth \[[^55]\].
- **Beamforming and Spatial Division:** Efficient beamforming will be essential in managing massive connectivity. By focusing energy in specific directions, antennas can simultaneously communicate with multiple devices while minimizing interference. This requires complex antenna architectures that can dynamically adjust beam patterns and direct transmission toward specific users \[[^72]\].
- **Dense Network Infrastructure:** Massive connectivity also demands a dense deployment of BSs, which will likely need to be equipped with advanced antennas capable of handling high traffic loads. The design must balance power efficiency, scalability, and spatial reuse to ensure these dense networks operate efficiently \[[^73], [^74]\].

### 4.5 Advanced beamforming techniques and directional antennas

Beamforming constitutes an essential technological advancement within the domain of 6G communications, particularly at elevated frequency ranges where signal degradation presents significant challenges. Sophisticated beamforming methodologies shall employ directional antennas to concentrate signal energy, thereby enhancing transmission range and mitigating interference \[[^72]\]. Hybrid beamforming, which integrates both digital and analog processing approaches, will be instrumental in the effective modulation of both signal amplitude and phase, facilitating adaptable and precise beam steering to optimize coverage while concurrently reducing energy expenditure and signal attenuation. Furthermore, RIS will augment beamforming capabilities by leveraging intelligent surfaces to dynamically reflect and redirect electromagnetic waves, thereby bolstering signal strength and surmounting obstacles in environments characterized by physical impediments, such as metropolitan settings \[[^75]\].

![figure 6](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs11036-025-02464-7/MediaObjects/11036_2025_2464_Fig6_HTML.png?as=webp)

**Fig. 6**

### 4.6 Cooperative communication perspective

Cooperative communication in 6G is crucial for improving signal quality and coverage, particularly when direct communication links are obstructed. Figure [6](https://link.springer.com/article/10.1007/s11036-025-02464-7#Fig6) illustrates the complexities involved in cooperative communication dynamics. In cooperative systems, various devices or BSs work together to relay information, enhancing system reliability and throughput \[[^76], [^77]\]. Effective cooperative communication requires the use of distributed antennas that can transmit and receive signals simultaneously across interconnected nodes. This may involve designing antennas that can swiftly switch between modes or create multifunctional antennas capable of efficiently performing various cooperative tasks. In cooperative communication systems, beamforming can be improved through precise synchronization of multiple antennas in different locations, optimizing network performance. This approach can greatly enhance signal quality in adverse conditions by allowing multiple devices to create and sustain a focused communication beam \[[^70]\].

## 5 Antenna suitability for cooperative communication-enabled 6G applications

The evolution of 6G wireless networks about to occur will bring a jump in many aspects such as self-driving cars, smart cities, and the IoT devices \[[^78]\]. Such improvements would be gotten owing to the advances in the technology of the communication systems as particularly diverse antennas since, without them, the speed, reliability and the smoothness of the connection would have been impossible \[[^79]\]. In the context of cooperative communication, wherein multiple devices and systems operate in concert, the appropriateness of antennas becomes increasingly vital. This section examines the specific antenna specifications and recommendations for Various 6G applications, encompassing AutonomousVehicles (AV), smart cities, and IoT, while also addressing future considerations for antenna design and implementation within the 6G framework \[[^71]\].

### 5.1 Autonomous vehicles: antenna requirements for real-time communication and high mobility

For efficient and safe operation AV require a stable and efficient communication systems. A major challenge is however providing real time low latency communication to the moving vehicles. The antennas in such systems must be able to withstand varying environmental speeds, different ranges of the target and most importantly a network topology that is very fluid. The broadband communication between autonomous cars implies that vehicle to Vehicle (V2V), Vehicle to Infrastructure (V2I) and Vehicle to Everything (V2X) modes of communication work constantly and information is exchanged quickly and continuously.

For AV, the antennas must support multiple features simultaneously. First, the antennas must provide a wide coverage area to maintain stable connectivity over long distances, enabling the vehicles to communicate with nearby infrastructure or other vehicles in the network \[[^80],[^81],[^82]\]. Moreover, they must achieve low latency to enable the quick decision-making required for tasks such as obstacle avoidance, route planning, and accident prevention. This requires antennas with high directional gain to reduce interference and enhance communication efficiency. Beamforming techniques, which allow antennas to direct the communication signal towards a specific target, are critical in high-mobility environments like highways or urban settings with heavy traffic \[[^83]\].

### Recommended antenna types and configurations for reliable vehicular connectivity

The most suitable antenna types for AV include phased-array antennas and MIMO configurations \[[^18]\]. Phased-array antennas offer flexibility by electronically steering the beam, allowing continuous connectivity as vehicles move through different areas. This adaptability is essential for AV, which frequently shift between communication nodes, such as other vehicles or roadside infrastructure. MIMO antennas use multiple data transmission streams at once, thus adding to the communication system’s capacity and reliability. This, in turn, guarantees higher throughput which is very important for the extensive data produced from autonomous driving sensors, cameras, and lidar systems \[[^84], [^85]\].

Another promising antenna configuration for AV involves the integration of mmW technologies. The mmW spectrum, which offers higher bandwidth and faster data rates than current sub-6 GHz frequencies, will play a pivotal role in 6G. However, due to its shorter range and higher susceptibility to obstacles like buildings and vehicles, advanced antenna designs that can mitigate signal blockages, such as RIS, will be necessary to enhance connectivity in dense urban environments \[[^86], [^87]\].

### 5.2 Smart cities: 6G antennas for urban IoT networks, sensor connectivity, and public safety

The apparatuses and systems having sensors and IoT devices are further exploited for the management of urban engineering structures, improvement of public services, and protection of inhabitants is so innate smart cities. In the intelligent transport system, all the devices will be connected with high-speed transmission and reception systems making it possible to cope with millions of communicating devices which will be possible with a 6G network. Antennas are very important hardware components of such enormous networks, which provide medium for effective communication between many applications such as managing traffic systems, monitoring the environment, and dealing with situations that require urgent reaction \[[^88]\].

The antennas in smart city IoT networks must accommodate dense, urban environments where obstacles such as buildings, trees, and vehicles can obstruct signals. To overcome these challenges, 6G antennas will leverage technologies such as mMIMO, which offers enhanced capacity by simultaneously connecting multiple devices over the same frequency band. This is especially important in crowded areas where public safety applications, like surveillance systems and disaster alert networks, require reliable communication to function effectively \[[^89]\].

### Antenna configurations for public safety and emergency applications

In public safety scenarios, where timely data transmission is essential, communication must be both fast and reliable. Beamforming-enabled antennas play a key role in focusing signals for efficient delivery, particularly in densely populated urban environments, ensuring robust connectivity even in critical situations such as Natural disasters. Additionally, the integration of mmW and THz frequencies in 6G antennas will offer higher bandwidth for applications like high-definition video streaming for surveillance or advanced sensor connectivity for monitoring hazardous areas \[[^90],[^91],[^92]\].

6G antennas in smart cities will also support vehicular networks that link public transportation, emergency vehicles, and infrastructure systems to improve traffic flow and respond rapidly to incidents. This level of interconnectedness ensures smooth communication between vehicles and the city’s traffic management system, enhancing overall safety and efficiency \[[^93], [^94]\].

### 5.3 Antenna demands for massive IoT: efficient, low-latency, and resilient communication

A key challenge in the 6G era is managing the vast scale of IoT, which will encompass billions of devices operating in a wide range of environments. From wearables to industrial sensors, these devices need to communicate efficiently and reliably. Antennas for massive IoT must be optimized for high-density networks while minimizing power consumption, as many IoT devices will depend on batteries or energy-harvesting technologies. The antenna requirements vary based on the application. For instance, Industrial IoT (IIoT) antennas need to withstand interference and support long-range communication, while those in healthcare IoT must deliver ultra-low latency and high reliability for real-time data from medical devices \[[^20]\].

### Recommended antenna types for massive IoT networks

The use of sub-6 GHz antennas will remain crucial for IoT applications, especially those requiring wide-area coverage and low-power operation. However, with 6G, we can expect the proliferation of mmW and THz antennas to handle data-heavy applications, such as real-time video analytics or high-precision location tracking in smart factories or warehouses. Antennas utilizing RIS technology will also be beneficial in improving the energy efficiency of IoT networks by dynamically adjusting the signal propagation based on the surrounding environment \[[^20]\].

In addition, MIMO configurations and antenna arrays will be critical in supporting massive IoT by enabling multiple devices to communicate simultaneously without degrading network performance. These configurations will help reduce latency and improve the overall throughput of IoT networks, ensuring reliable communication even in highly congested areas \[[^18]\].

### 5.4 Future considerations

As we look toward the future of wireless communications, antennas are poised to become even more vital to the success of 6G networks and beyond. With the rise of immersive technologies like AR, VR, and Extended Reality (XR), alongside increasingly complex cooperative communication systems, the expectations placed on antenna systems are evolving rapidly. These emerging applications require not only faster speeds and lower latency, but also a higher level of responsiveness, reliability, and adaptability from the communication infrastructure, starting with the antennas themselves.

### Multi-band and ultra-wideband operation

A major shift in 6G will be the expansion into new spectrum ranges, particularly mmW and THz frequencies. These higher bands offer immense bandwidth potential, but come with propagation challenges such as high path loss and limited penetration. To bridge this, future antenna systems must be capable of multi-band or ultra-wideband operation, supporting frequencies from traditional sub-6 GHz bands up to 300 GHz or more. This will allow devices and BS to dynamically switch or aggregate across multiple bands to maintain consistent performance. For instance, low-frequency bands could be used for coverage and control signaling, while higher frequencies could provide high capacity data channels. Designing antennas that can support this kind of frequency agility without sacrificing size, cost, or energy efficiency will be a major area of innovation.

### Reconfigurability and intelligent adaptation

Another key direction is the development of reconfigurable and adaptive antennas. In future 6G networks, user contexts and network conditions will vary widely and change rapidly. Antennas will need to autonomously adjust parameters such as beam direction, impedance, polarization, and operational frequency in real time. This level of adaptability can be enabled through the integration of artificial intelligence (AI) directly into antenna control systems. For example, intelligent beamforming could allow an antenna to track a user’s movement and adjust its radiation pattern accordingly, maintaining a strong link even in complex environments such as urban canyons or moving vehicles. Technologies such as liquid-metal antennas, varactor-based tuning, and graphene-based materials are being explored to make antennas physically reconfigurable at the hardware level. Meanwhile, software-defined antennas may allow unprecedented levels of control over antenna behavior, making them responsive to both device-level and network-level inputs.

### Reconfigurable intelligent surfaces and metamaterials

Beyond traditional antennas, RIS and metamaterial-based designs represent a paradigm shift. These technologies allow the wireless environment itself to become programmable. For example, RIS panels placed on building surfaces could reflect or refract signals intelligently to enhance coverage and capacity, particularly in non-line-of-sight (NLoS) conditions. In cooperative communicatios, RIS can serve as passive or semi-passive relays, significantly reducing energy consumption while improving link quality. Antennas in such systems must be designed to work seamlessly with RIS, adapting in real time to changes in the reflective environment.

### Cooperative communication and distributed MIMO

6G is expected to push beyond traditional cellular architectures with the adoption of cell-free massive MIMO and other distributed antenna systems. Here, hundreds or even thousands of antennas may be deployed across a large area and managed as a single coherent system. This allows for higher spatial resolution, better interference management, and improved spectral efficiency. Antenna designs for such systems must be modular, cost-effective, and energy-efficient, supporting decentralized control and plug-and-play deployment. Furthermore, antennas must be able to function reliably in a wide variety of physical environments, from underground smart infrastructure to airborne networks supported by drones or high-altitude platform Stations.

### Integration into emerging applications

The role of antennas extends beyond traditional mobile communications. In autonomous vehicles, antennas will need to handle V2X (vehicle-to-everything) communication, including vehicle-to-vehicle (V2V), vehicle-to-infrastructure (V2I), and vehicle-to-network (V2N) links. These systems will rely on extremely low-latency and high-reliability connections to support critical safety and navigation features. Similarly, drones require lightweight, omnidirectional or beam-steerable antennas that can maintain stable links during fast maneuvers and changing orientations. In telemedicine and robotic surgery, antennas must support real-time video transmission and haptic feedback with near-zero latency and high reliability, a task made more difficult by the need for compact form factors and electromagnetic compatibility in clinical settings. In smart cities, millions of connected devices will require antennas that are not only compact and low-cost, but also rugged and capable of performing reliably in dense urban environments with significant interference and multipath propagation.

### Sustainability and energy efficiency

Finally, as the scale of connectivity increases, the need for energy-efficient and sustainable antenna designs increases. This includes using recyclable materials, optimizing radiation efficiency, and minimizing the energy consumption of adaptive features. Antennas that can harvest ambient energy or support simultaneous wireless information and power transfer may become essential in powering low-energy IoT devices distributed across smart environments.

## 6 Conclusion

This paper presents an overview of antenna suitability for 6G cooperative communication. It emphasizes the critical role of antennas in addressing challenges associated with higher frequency bands, extensive device connectivity, and advanced beamforming in 6G communication. Effective technologies such as MIMO and RIS are noted, alongside their challenges including increased path loss and high-frequency directionality. The study highlights innovations in antenna design and materials as solutions for applications like AV, smart cities, and IoT. These advancements are crucial for ensuring reliable V2X communication, urban sensor networks, and supporting large IoT ecosystems. In conclusion, the development of 6G cooperative communication is contingent upon advanced antenna technologies optimized for high-frequency, high-capacity, and interconnected environments. Ongoing research and development in this field are essential for realizing the full potential of 6G networks and their transformative impact on various industries and societal structures.

## Data Availability

No datasets were generated or analysed during the current study.

## References

[Download references](https://citation-needed.springer.com/v2/references/10.1007/s11036-025-02464-7?format=refman&flavour=references)

## Acknowledgements

This research was supported in part by the Basic Science Research Program through the National Research Foundation of Korea(NRF) funded by the Ministry of Education (NRF-2021R1A6A1A03039493) and in part by the NRF grant funded by the Korean government (MSIT) (NRF-2022R1A2C1004401)

## Author information

### Authors and Affiliations

1. Department of Computer Science and Engineering, Yeungnam University, Gyeongsan, Republic of Korea
	Ali Nauman & Sung Won Kim
2. College of Internet of Things (IoT) Engineering, Hohai University, Changzhou, 213001, China
	Syed Kamran Haider
3. Department of Electrical Engineering, Yeungnam University, Gyeongsan, Republic of Korea
	Tahir Khurshaid

Authors
1. Ali Nauman
	[View author publications](https://link.springer.com/search?sortBy=newestFirst&dc.creator=Ali%20Nauman)
	Search author on:[PubMed](https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Ali%20Nauman)
2. Syed Kamran Haider
	[View author publications](https://link.springer.com/search?sortBy=newestFirst&dc.creator=Syed%20Kamran%20Haider)
	Search author on:[PubMed](https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Syed%20Kamran%20Haider)
3. Tahir Khurshaid
	[View author publications](https://link.springer.com/search?sortBy=newestFirst&dc.creator=Tahir%20Khurshaid)
	Search author on:[PubMed](https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Tahir%20Khurshaid)
4. Sung Won Kim
	[View author publications](https://link.springer.com/search?sortBy=newestFirst&dc.creator=Sung%20Won%20Kim)
	Search author on:[PubMed](https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Sung%20Won%20Kim)

### Contributions

Conceptualization: A.N., S.K.H, T.K.; writing original draft preparation: A.N., S.K.H; writing review and editing: A.N., T.K., and S.W.K.; Supervision and funding: S.W.K. All authors have read and agreed to the published version of the manuscript.

### Corresponding authors

Correspondence to [Ali Nauman](https://link.springer.com/article/10.1007/) or [Tahir Khurshaid](https://link.springer.com/article/10.1007/).

## Ethics declarations

### Competing Interests

The authors declare no competing interests.

## Additional information

### Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Rights and permissions

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.

## About this article

[![Check for updates. Verify currency and authenticity via CrossMark](https://link.springer.com/article/10.1007/)](https://crossmark.crossref.org/dialog/?doi=10.1007/s11036-025-02464-7)

### Cite this article

Nauman, A., Haider, S.K., Khurshaid, T. *et al.* Toward 6G and Beyond: A Comprehensive Study of Antenna Design, Selection, and Suitability for Cooperative Communication. *Mobile Netw Appl* (2025). https://doi.org/10.1007/s11036-025-02464-7

[Download citation](https://citation-needed.springer.com/v2/references/10.1007/s11036-025-02464-7?format=refman&flavour=citation)

- Accepted:
- Published:
- DOI: https://doi.org/10.1007/s11036-025-02464-7

### Share this article

Anyone you share the following link with will be able to read this content:

Provided by the Springer Nature SharedIt content-sharing initiative

### Keywords

- [Sixth generation (6G)](https://link.springer.com/search?query=Sixth%20generation%20%286G%29&facet-discipline=%22Engineering%22)
- [Internet of things (IoT)](https://link.springer.com/search?query=Internet%20of%20things%20%28IoT%29&facet-discipline=%22Engineering%22)
- [Cooperative communication](https://link.springer.com/search?query=Cooperative%20communication&facet-discipline=%22Engineering%22)
- [Antennas](https://link.springer.com/search?query=Antennas&facet-discipline=%22Engineering%22)
- [Multiple-input-multiple-output (MIMO)](https://link.springer.com/search?query=Multiple-input-multiple-output%20%28MIMO%29&facet-discipline=%22Engineering%22)
- [Reconfigurable intelligent surfaces (RIS)](https://link.springer.com/search?query=Reconfigurable%20intelligent%20surfaces%20%28RIS%29&facet-discipline=%22Engineering%22)

[^1]: Jamshed MA, Ali K, Abbasi QH, Imran MA, Ur-Rehman M (2022) Challenges, applications, and future of wireless sensors in internet of things: A review. IEEE Sens J 22(6):5482–5494

[Article](https://doi.org/10.1109%2FJSEN.2022.3148128)

[^2]: Jiang W, Han B, Habibi MA, Schotten HD (2021) The road towards 6g: A comprehensive survey. IEEE Open J Commun Soc 2:334–366

[Article](https://doi.org/10.1109%2FOJCOMS.2021.3057679)

[^3]: Tataria H, Shafi M, Molisch AF, Dohler M, Sjöland H, Tufvesson F (2021) 6g wireless systems: Vision, requirements, challenges, insights, and opportunities. Proc IEEE 109(7):1166–1199

[Article](https://doi.org/10.1109%2FJPROC.2021.3061701)

[^4]: Viswanathan H, Mogensen PE (2020) Communications in the 6g era. IEEE Access 8:57063–57074

[Article](https://doi.org/10.1109%2FACCESS.2020.2981745)

[^5]: Akyildiz IF, Kak A, Nie S (2020) 6g and beyond: The future of wireless communications systems. IEEE Access 8:133995–134030

[Article](https://doi.org/10.1109%2FACCESS.2020.3010896)

[^6]: Bhattacharya P, Saraswat D, Dave A, Acharya M, Tanwar S, Sharma G, Davidson IE (2021) Coalition of 6g and blockchain in ar/vr space: Challenges and future directions. IEEE Access 9:168455–168484

[Article](https://doi.org/10.1109%2FACCESS.2021.3136860)

[^7]: Liao S, Wu J, Li J, Konstantin K (2020) Information-centric massive iot-based ubiquitous connected vr/ar in 6g: A proposed caching consensus approach. IEEE Internet Things J 8(7):5172–5184

[Article](https://doi.org/10.1109%2FJIOT.2020.3030718)

[^8]: Jamshed MA, Nauman A, Abbasi MAB, Kim SW (2020) Antenna selection and designing for thz applications: suitability and performance evaluation: a survey. IEEE Access 8:113246–113261

[Article](https://doi.org/10.1109%2FACCESS.2020.3002989)

[^9]: Siegel PH (2003) Thz technology: An overview. Int J High Speed Electron Syst 13(02):351–394

[Article](https://doi.org/10.1142%2FS0129156403001776)

[^10]: Xue Q, Ji C, Ma S, Guo J, Xu Y, Chen Q, Zhang W (2024) “A survey of beam management for mmwave and thz communications towards 6g,” IEEE Commun Surv Tutor

[^11]: Lyu J, Huang L, Chen L, Zhu Y, Zhuang S (2024) Review on the terahertz metasensor: from featureless refractive index sensing to molecular identification. Photo Res 12(2):194–217

[Article](https://doi.org/10.1364%2FPRJ.508136)

[^12]: Yakub B, Kumar A (2024) Quad-band circularly polarized graphene tunable siw-dielectric resonator antenna for 6g thz applications. Opt Quant Electron 56(8):1296

[Article](https://link.springer.com/doi/10.1007/s11082-024-07207-8)

[^13]: Nauman A, Jamshed MA, Qadri YA, Ali R, Kim SW (2021) Reliability optimization in narrowband device-to-device communication for 5g and beyond-5g networks. IEEE Access 9:157584–157596

[Article](https://doi.org/10.1109%2FACCESS.2021.3129896)

[^14]: Bello O, Zeadally S (2014) Intelligent device-to-device communication in the internet of things. IEEE Syst J 10(3):1172–1182

[Article](https://doi.org/10.1109%2FJSYST.2014.2298837)

[^15]: Hassouna S, Jamshed M A, Rains J, Kazim J u R, Rehman M U, Abualhayja M, Mohjazi L, Cui T J, Imran M A, Abbasi Q H (2023) “A survey on reconfigurable intelligent surfaces: Wireless communication perspective,” IET Commun, vol 17, no 5, pp 497–537.

[^16]: Jamshed MA, Kaushik A, Toka M, Shin W, Shakir MZ, Dash SP, Dardari D (2024) Synergizing airborne non-terrestrial networks and reconfigurable intelligent surfaces-aided 6g iot. IEEE Internet of Things Magaz 7(2):46–52

[Article](https://doi.org/10.1109%2FIOTM.001.2300242)

[^17]: Héliot F, Jamshed M A, Brown T W (2020) “Exposure modelling and minimization for multi-antenna communication systems,” In: 2020 IEEE 91st Vehicular Technology Conference (VTC2020-Spring), pp 1–6, IEEE

[^18]: He H, Yu X, Zhang J, Song S, Letaief KB (2021) Cell-free massive mimo for 6g wireless communication networks. J Commun Inf Netw 6(4):321–335

[Article](https://doi.org/10.23919%2FJCIN.2021.9663100)

[^19]: Bhattacharya S, Rajabalifardi K, Mohsin M A, Cioffi J M (2025) “Optimum power-subcarrier allocation and time-sharing in multicarrier noma uplink,” [arXiv:2501.11230](http://arxiv.org/abs/2501.11230),

[^20]: Arya K V, Bhadoria R S, Chaudhari N S (2018) “Emerging wireless communication and network technologies,” Realizing the Wireless Technology in Internet of Things (IoT), Springer,

[^21]: Saunders S R, Aragón-Zavala A A (2024) Antennas and propagation for wireless communication systems. John Wiley & Sons,

[^22]: Gupta A, Jha RK (2015) A survey of 5g network: Architecture and emerging technologies. IEEE Access 3:1206–1232

[Article](https://doi.org/10.1109%2FACCESS.2015.2461602)

[^23]: Jamshed M A, Amjad O, Zeydan E (2017) “Multicore energy efficient scheduling with energy harvesting for wireless multimedia sensor networks,” In: *2017 International Multi-topic Conference (INMIC)*, pp 1–5, IEEE,

[^24]: Jameel F, Nabeel M, Jamshed M A, Jäntti R (2020) “Minimizing forking in blockchain-based iot networks,” In: 2020 IEEE International Conference on Communications Workshops (ICC Workshops), pp 1–6, IEEE,

[^25]: Na M, Lee J, Choi G, Yu T, Choi J, Lee J, Bahk S (2024) Operator’s perspective on 6g: 6g services, vision, and spectrum. IEEE Commun Mag 62(8):178–184

[Article](https://doi.org/10.1109%2FMCOM.001.2400060)

[^26]: Zawish M, Dharejo FA, Khowaja SA, Raza S, Davy S, Dev K, Bellavista P (2024) Ai and 6g into the metaverse: Fundamentals, challenges and future research trends. IEEE Open J Commun Soc 5:730–778

[Article](https://doi.org/10.1109%2FOJCOMS.2024.3349465)

[^27]: Alhussien N, Gulliver T A (2024) “Toward ai-enabled green 6g networks: A resource management perspective,” IEEE Access,

[^28]: Jabbar A, Jamshed M A, Shawky M A, Abbasi Q H, Imran M A, Rehman M U (2022) “Multi-gigabit millimeter-wave industrial communication: A solution for industry 4.0 and beyond,” In: GLOBECOM 2022-2022 IEEE Global Communications Conference, pp 5001–5006, IEEE,

[^29]: Khan M F, Raza A, Iqbal A, Rashid A, Jamshed M A, Pesch D (2024) “Performance analysis of intelligent reflecting surfaces for 5g/6g-enabled future smart industries with a focus on millimeter-wave band communications,” In: 2024 IEEE International Conference on Communications Workshops (ICC Workshops), pp 2040–2045, IEEE,

[^30]: Alsamhi SH, Hawbani A, Sahal R, Srivastava S, Kumar S, Zhao L, Al-qaness MA, Hassan J, Guizani M, Curry E (2024) Towards sustainable industry 4.0: A survey on greening ioe in 6g networks. Ad Hoc Netw 165:103610

[^31]: Yang P, Xiao Y, Xiao M, Li S (2019) 6g wireless communications: Vision and potential techniques. IEEE Netw 33(4):70–75

[Article](https://doi.org/10.1109%2FMNET.2019.1800418) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=4039110)

[^32]: Jamshed M A, Kaushik A, Dajer M, Guidotti A, Parzysz F, Lagunas E, Di Renzo M, Chatzinotas S, Dobre O A (2024) “Non-terrestrial networks for 6g: Integrated, intelligent and ubiquitous connectivity,” [arXiv:2407.02184](http://arxiv.org/abs/2407.02184),

[^33]: Behravan A, Yajnanarayana V, Keskin MF, Chen H, Shrestha D, Abrudan TE, Svensson T, Schindhelm K, Wolfgang A, Lindberg S et al (2022) Positioning and sensing in 6g: Gaps, challenges, and opportunities. IEEE Veh Technol Mag 18(1):40–48

[Article](https://doi.org/10.1109%2FMVT.2022.3219999)

[^34]: Säily M, Yilmaz O N, Michalopoulos D S, Pérez E, Keating R, Schaepperle J (2021) “Positioning technology trends and solutions toward 6g,” In: 2021 IEEE 32nd Annual International Symposium on Personal, Indoor and Mobile Radio Communications (PIMRC), pp 1–7, IEEE

[^35]: Ikram M, Sultan K, Lateef MF, Alqadami AS (2022) A road towards 6g communication—a review of 5g antennas, arrays, and wearable devices. Electronics 11(1):169

[Article](https://doi.org/10.3390%2Felectronics11010169)

[^36]: Rasilainen K, Phan TD, Berg M, Pärssinen A, Soh PJ (2023) Hardware aspects of sub-thz antennas and reconfigurable intelligent surfaces for 6g communications. IEEE J Sel Areas Commun 41(8):2530–2546

[Article](https://doi.org/10.1109%2FJSAC.2023.3288250)

[^37]: Jamshed MA, Brown TW, Héliot F (2022) Dual antenna coupling manipulation for low sar smartphone terminals in talk position. IEEE Trans Antennas Propag 70(6):4299–4306

[Article](https://doi.org/10.1109%2FTAP.2022.3141218)

[^38]: Meng R, Shah A A, Jamshed M A, Pezaros D (2024) “Federated learning-based intrusion detection framework for internet of things and edge computing backed critical infrastructure,” In: 2024 IEEE International Conference on Communications Workshops (ICC Workshops), pp 810–815, IEEE,

[^39]: Saeed MA, Nwajana AO (2024) A review of beamforming microstrip patch antenna array for future 5g/6g networks. Frontier Mech Eng 9:1288171

[Article](https://doi.org/10.3389%2Ffmech.2023.1288171)

[^40]: Guo YJ, Ansari M, Fonseca NJ (2021) Circuit type multiple beamforming networks for antenna arrays in 5g and 6g terrestrial and non-terrestrial networks. IEEE J Microw 1(3):704–722

[Article](https://doi.org/10.1109%2FJMW.2021.3072873)

[^41]: Nissanov U, Singh G (2023) “Multi-beam and beamforming terahertz array antenna for 6g communication,” In: Antenna Technology for Terahertz Wireless Communication, pp 219–262, Springer,

[^42]: Nguyen V-L, Lin P-C, Cheng B-C, Hwang R-H, Lin Y-D (2021) Security and privacy for 6g: A survey on prospective technologies and challenges. IEEE Commun Surv Tutor 23(4):2384–2428

[Article](https://doi.org/10.1109%2FCOMST.2021.3108618)

[^43]: Pant R, Malviya L (2023) Thz antennas design, developments, challenges, and applications: A review. Int J Commun Syst 36(8):e5474

[^44]: Rikkinen K, Kyosti P, Leinonen ME, Berg M, Parssinen A (2020) Thz radio communication: Link budget analysis toward 6g. IEEE Commun Mag 58(11):22–27

[Article](https://doi.org/10.1109%2FMCOM.001.2000310)

[^45]: You L, Xiong J, Ng DWK, Yuen C, Wang W, Gao X (2020) Energy efficiency and spectral efficiency tradeoff in ris-aided multiuser mimo uplink transmission. IEEE Trans Signal Process 69:1407–1421

[Article](https://doi.org/10.1109%2FTSP.2020.3047474) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=4233911)

[^46]: He J, Wymeersch H, Juntti M (2021) Channel estimation for ris-aided mmwave mimo systems via atomic norm minimization. IEEE Trans Wireless Commun 20(9):5786–5797

[Article](https://doi.org/10.1109%2FTWC.2021.3070064)

[^47]: Yang Z, Zhang Y (2021) Optimal swipt in ris-aided mimo networks. IEEE Access 9:112552–112560

[Article](https://doi.org/10.1109%2FACCESS.2021.3099698)

[^48]: Wang C-Y, Wei H-Y (2009) Ieee 802.11 n mac enhancement and performance evaluation. Mobile Netw Appl 14:760–771

[Article](https://link.springer.com/doi/10.1007/s11036-008-0129-2)

[^49]: Perahia E, Stacey R (2013) Next generation wireless LANs: 802.11 n and 802.11 ac. Cambridge university press,

[^50]: Larsson EG, Edfors O, Tufvesson F, Marzetta TL (2014) Massive mimo for next generation wireless systems. IEEE Commun Mag 52(2):186–195

[Article](https://doi.org/10.1109%2FMCOM.2014.6736761)

[^51]: Khan D, Ahmad A, Choi D-Y (2024) Dual-band 5g mimo antenna with enhanced coupling reduction using metamaterials. Sci Rep 14(1):96

[Article](https://doi.org/10.1038%2Fs41598-023-50446-0)

[^52]: Salehi M, Oraizi H (2024) Wideband high gain metasurface-based 4t4r mimo antenna with highly isolated ports for sub-6 ghz 5g applications. Sci Rep 14(1):14448

[Article](https://doi.org/10.1038%2Fs41598-024-65135-9)

[^53]: Wang Z, Zhang J, Du H, Niyato D, Cui S, Ai B, Debbah M, Letaief K B, Poor H V (2024) “A tutorial on extremely large-scale mimo for 6g: Fundamentals, signal processing, and applications,” IEEE Commun Surv Tutor,

[^54]: Lu H, Zeng Y, You C, Han Y, Zhang J, Wang Z, Dong Z, Jin S, Wang C-X, Jiang T, et al (2024) “A tutorial on near-field xl-mimo communications towards 6g,” IEEE Commun Surv Tutor,

[^55]: Chataut R, Akl R (2020) Massive mimo systems for 5g and beyond networks—overview, recent trends, challenges, and future research direction. Sensors 20(10):2753

[Article](https://doi.org/10.3390%2Fs20102753)

[^56]: Sharma U, Srivastava G, Khandelwal M K, Roges R (2024) “Design challenges and solutions of multiband mimo antenna for 5g/6g wireless applications: A comprehensive review.,” Progress Electromagnet Res B, vol 104,

[^57]: Jamshed MA, Ur-Rehman M, Frnda J, Althuwayb AA, Nauman A, Cengiz K (2021) Dual band and dual diversity four-element mimo dipole for 5g handsets. Sensors 21(3):767

[Article](https://doi.org/10.3390%2Fs21030767)

[^58]: Ojaroudi Parchin N, Jahanbakhsh Basherlou H, Al-Yasir Y I, Ullah A, Abd-Alhameed R A, Noras J M (2019) “Multi-band mimo antenna design with user-impact investigation for 4g and 5g mobile terminals,” Sensors, vol 19, no 3, p 456,

[^59]: Sandi E, Marani T, et al (2020) “Design of multiband mimo antenna for 5g millimeterwave application,” In: IOP conference series: materials science and engineering, vol 852, p 012154, IOP Publishing,

[^60]: Liu Y, Liu X, Mu X, Hou T, Xu J, Renzo M, Al-Dhahir N (2021) Reconfigurable intelligent surfaces: Principles and opportunities. IEEE Commun Surv Tutor 23(3):1546–1577

[Article](https://doi.org/10.1109%2FCOMST.2021.3077737)

[^61]: ElMossallamy MA, Zhang H, Song L, Seddik KG, Han Z, Li GY (2020) Reconfigurable intelligent surfaces for wireless communications: Principles, challenges, and opportunities. IEEE Trans Cogn Commun Netw 6(3):990–1002

[Article](https://doi.org/10.1109%2FTCCN.2020.2992604)

[^62]: Trichopoulos GC, Theofanopoulos P, Kashyap B, Shekhawat A, Modi A, Osman T, Kumar S, Sengar A, Chang A, Alkhateeb A (2022) Design and evaluation of reconfigurable intelligent surfaces in real-world environment. IEEE Open J Commun Soc 3:462–474

[Article](https://doi.org/10.1109%2FOJCOMS.2022.3158310)

[^63]: Yuan X, Zhang Y-JA, Shi Y, Yan W, Liu H (2021) Reconfigurable-intelligent-surface empowered wireless communications: Challenges and opportunities. IEEE Wirel Commun 28(2):136–143

[Article](https://doi.org/10.1109%2FMWC.001.2000256)

[^64]: Björnson E, Wymeersch H, Matthiesen B, Popovski P, Sanguinetti L, Carvalho E (2022) Reconfigurable intelligent surfaces: A signal processing perspective with wireless applications. IEEE Signal Process Mag 39(2):135–158

[Article](https://doi.org/10.1109%2FMSP.2021.3130549)

[^65]: Jamshed M A, Abbasi Q H, Ur-Rehman M (2022) “Feasibility of intelligent reflecting surfaces to combine terrestrial and non-terrestrial networks,” Intelligent Reconfigurable Surfaces (IRS) for Prospective 6G Wireless Networks, pp 25–40,

[^66]: Long R, Liang Y-C, Pei Y, Larsson EG (2021) Active reconfigurable intelligent surface-aided wireless communications. IEEE Trans Wireless Commun 20(8):4962–4975

[Article](https://doi.org/10.1109%2FTWC.2021.3064024)

[^67]: Xu J, Liu Y, Mu X, Dobre OA (2021) Star-riss: Simultaneous transmitting and reflecting reconfigurable intelligent surfaces. IEEE Commun Lett 25(9):3134–3138

[Article](https://doi.org/10.1109%2FLCOMM.2021.3082214)

[^68]: Faisal K, Choi W (2022) Machine learning approaches for reconfigurable intelligent surfaces: A survey. IEEE Access 10:27343–27367

[Article](https://doi.org/10.1109%2FACCESS.2022.3157651)

[^69]: Jian M, Alexandropoulos GC, Basar E, Huang C, Liu R, Liu Y, Yuen C (2022) Reconfigurable intelligent surfaces for wireless communications: Overview of hardware designs, channel models, and estimation techniques. Intell Conver Netw 3(1):1–32

[Article](https://doi.org/10.23919%2FICN.2022.0005)

[^70]: Lin W, Yan Y, Li L, Han Z, Matsumoto T (2024) “Semantic-forward relaying: A novel framework towards 6g cooperative communications,” IEEE Commun Lett

[^71]: Alberti A M, Pivoto D G, Rezende T T, Leal A V, Both C B, Facina M S, Moreira R, de Oliveira Silva F (2024) “Disruptive 6g architecture: Software-centric, ai-driven, and digital market-based mobile networks,” Comput Netw, vol 252, p 110682,

[^72]: Rojhani N, Shaker G (2024) Comprehensive review: Effectiveness of mimo and beamforming technologies in detecting low rcs uavs. Remote Sens 16(6):1016

[Article](https://doi.org/10.3390%2Frs16061016)

[^73]: Katsaros G N, Nikitopoulos K (2024) “Power efficient and ultra dense open-ran vehicular networks with non-linear processing,” IEEE Access,

[^74]: Malik AA, Jamshed MA, Nauman A, Iqbal A, Shakeel A, Hussain R (2024) Performance evaluation of handover triggering condition estimation using mobility models in heterogeneous mobile networks. IET Netw 13(4):291–300

[Article](https://doi.org/10.1049%2Fntw2.12120)

[^75]: Ji R, Huang C, Chen X, Wei E, Dai L, He J, Zhang Z, Yuen C, Debbah M (2024) “Electromagnetic hybrid beamforming for holographic mimo communications,” IEEE Trans Wireless Commun

[^76]: Mustari N, Karabulut MA, Shah AS, Tureli U (2024) Cooperative thz communication for uavs in 6g and beyond. Green Energy Intell Transport 3(1):100131

[^77]: Jamshed M A, Haq B, Mohsin M A, Nauman A, Yanikomeroglu H (2025) “Artificial intelligence, ambient backscatter communication and non-terrestrial networks: A 6g commixture,” [arXiv:2501.09405](http://arxiv.org/abs/2501.09405)

[^78]: Guo Z, Shen Y, Chakraborty C, Alblehai F, Yu K (2024) “Industrial 6g-iot and machine learning-supported intelligent sensing framework for indicator control strategy in sewage treatment process,” IEEE Internet of Things J

[^79]: Plastras S, Tsoumatidis D, Skoutas DN, Rouskas A, Kormentzas G, Skianis C (2024) Non-terrestrial networks for energy-efficient connectivity of remote iot devices in the 6g era: A survey. Sensors 24(4):1227

[Article](https://doi.org/10.3390%2Fs24041227)

[^80]: Jamshed MA, Amjad O, Maqsood M, Rehman MU, Jayakody DNK, Pervaiz H (2019) A dipole sub-array with reduced mutual coupling for large antenna array applications. IEEE Access 7:171495–171502

[Article](https://doi.org/10.1109%2FACCESS.2019.2955855)

[^81]: Ahangar MN, Ahmed QZ, Khan FA, Hafeez M (2021) A survey of autonomous vehicles: Enabling communication technologies and challenges. Sensors 21(3):706

[Article](https://doi.org/10.3390%2Fs21030706)

[^82]: Kong L, Khan MK, Wu F, Chen G, Zeng P (2017) Millimeter-wave wireless communications for iot-cloud supported autonomous vehicles: Overview, design, and challenges. IEEE Commun Mag 55(1):62–68

[Article](https://doi.org/10.1109%2FMCOM.2017.1600422CM)

[^83]: Bazan O, Jaseemuddin M (2011) A survey on mac protocols for wireless adhoc networks with beamforming antennas. IEEE Commun Surv Tutor 14(2):216–239

[Article](https://doi.org/10.1109%2FSURV.2011.041311.00099)

[^84]: Nguyen HC, Amorim R, Wigard J, Kovács IZ, Sørensen TB, Mogensen PE (2018) How to ensure reliable connectivity for aerial vehicles over cellular networks. Ieee Access 6:12304–12317

[Article](https://doi.org/10.1109%2FACCESS.2018.2808998)

[^85]: Rasheed I, Hu F, Hong Y-K, Balasubramanian B (2020) Intelligent vehicle network routing with adaptive 3d beam alignment for mmwave 5g-based v2x communications. IEEE Trans Intell Transp Syst 22(5):2706–2718

[Article](https://doi.org/10.1109%2FTITS.2020.2973859)

[^86]: Va V, Shimizu T, Bansal G, Heath Jr R W, et al (2016) “Millimeter wave vehicular communications: A survey,” Foundations and Trends® in Networking, vol 10, no 1, pp 1–113,

[^87]: He R, Schneider C, Ai B, Wang G, Zhong Z, Dupleich DA, Thomae RS, Boban M, Luo J, Zhang Y (2019) Propagation channels of 5g millimeter-wave vehicle-to-vehicle communications: Recent advances and future challenges. IEEE Veh Technol Mag 15(1):16–26

[Article](https://doi.org/10.1109%2FMVT.2019.2928898)

[^88]: Murroni M, Anedda M, Fadda M, Ruiu P, Popescu V, Zaharia C, Giusto D (2023) 6g—enabling the new smart city: A survey. Sensors 23(17):7528

[Article](https://doi.org/10.3390%2Fs23177528)

[^89]: Sharma S, Popli R, Singh S, Chhabra G, Saini GS, Singh M, Sandhu A, Sharma A, Kumar R (2024) The role of 6g technologies in advancing smart city applications: Opportunities and challenges. Sustainability 16(16):7039

[Article](https://doi.org/10.3390%2Fsu16167039)

[^90]: Jamshed M A, Ayaz F, Kaushik A, Fischione C, Ur-Rehman M (2023) “Green uav-enabled internet-of-things network with ai-assisted noma for disaster management,” [arXiv:2304.13802](http://arxiv.org/abs/2304.13802),

[^91]: Mezzavilla M, Polese M, Zanella A, Dhananjay A, Rangan S, Kessler C, Rappaport TS, Zorzi M (2017) Public safety communications above 6 ghz: Challenges and opportunities. IEEE Access 6:316–329

[Article](https://doi.org/10.1109%2FACCESS.2017.2762471)

[^92]: Gorcin A, Arslan H (2008) “Public safety and emergency case communications: Opportunities from the aspect of cognitive radio,” In: 2008 3rd IEEE symposium on new frontiers in dynamic spectrum access networks, pp 1–10, IEEE

[^93]: Pervez F, Qadir J, Khalil M, Yaqoob T, Ashraf U, Younis S (2018) Wireless technologies for emergency response: A comprehensive review and some guidelines. Ieee Access 6:71814–71838

[Article](https://doi.org/10.1109%2FACCESS.2018.2878898)

[^94]: Kumbhar A, Koohifar F, Güvenç I, Mueller B (2016) A survey on legacy and emerging technologies for public safety communications. IEEE Commun Surv Tutor 19(1):97–124

[Article](https://doi.org/10.1109%2FCOMST.2016.2612223)