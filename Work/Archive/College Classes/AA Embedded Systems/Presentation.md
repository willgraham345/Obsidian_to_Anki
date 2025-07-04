# Stuxnet
A malicious computer worm that was believed to be responsible for causing damage to Iran's nuclear program
- Neither country has fully admitted responsibility.
	- Multiple indendent news organizations recognize Stuxnet to be a weapon built by the US and Israel in an operation known as Operation Olympic Games
- Targets Siemens PLCs
- First spyware that spies on and subverts industrial systems
	- Devised by the NSA under President Bush
- According to Eugene Kaspersky, the worm also infected a power plant in Russia
- It spread from an engineer's computer connected to the centrifuge into the internet

Uses Zero-day flaws
- A vulnerability in a computer system that was previously unknown to its developers. 


## Share of infected computers:
![[Pasted image 20231129150812.png]]
## Operation
Stuxnet doesn't harm computers unless Siemes software is found. 
- Contains safeguard to prevent each infected computer from spreading the worm to more than three others, and to erase itself on 24 June 2012

Man-in-the-middle attack
- Fakes industrial process control sensor signals so an infected system does not shut down due to abnormal behavior
	- This complexity is unusual for malware
	- Layerd attack against:
		- Windows OS
		- Siemens PCS 7, WinCC and STEP7 industrial software applications that run on Windows and
		- One or more Siemens S7 PLCs.


# Sources
[Wikipedia Stuxnet](https://en.wikipedia.org/wiki/Stuxnet)



# Slide planning
## What is stuxnet?
- 500 kb worm that infected the software of at least 14 industrial sites in Iran, including a uranium-enrichment plant. 
- Worm that spread own its own over computer networks
## How did it work?
- 3 phases
	- Targeted Microsoft Windows machines/networks repeatedly replicating itself.
	- Sought out Siemens Step7 software (also Windows based). These machines are used for controlling industrial equipment
	 - This virus could then spy on the industrial systems and cause centrifuges to tear themselves apart without letting operators know
		 - Iran has NOT confirmed reports that Stuxnet destroyed some of its centrifuges. 
	- [IEEE Spectrum](https://spectrum.ieee.org/the-real-story-of-stuxnet)
## Who did it affect?
## What is the timeline of this virus?
In 2012, US defense secretary Leon Panetta warned that the US was vulnerable to a "cyber Pearl Harbor"
- Over the next month, Chevron confirmed this speculation by being the first US company to admit that Stuxnet had spread to its machines
## Why was it created?
- Not sure. People have speculated that it's complexity and sophistication could only have been accomplished with sponsorship from a nation-state. 
- One analyst [Schouwenberg](https://spectrum.ieee.org/the-real-story-of-stuxnet) belived that a team of 10 people would have needed at least two or three years to create it. 
## Will we ever know definitively who caused it?
## Has this been done before?
Malware milestones:
- 1992, Michelangelo is hyped by computer-security exec Jon McAfee, who predicted that on March 6 the virus would wipe out info on millions of computers. He was very wrong, not much happened.
- 2003, SQL Slammer Worm (aka Sapphire worm) attacked vulnerabilities in Microsoft's SQL Server Data Engine, and crashed the internet within 15 minutes of release
- 2010, Stuxnet worm detected, the first worm known to attack SCADA systems
- 2011, Duqu worm is discovered. Designed to give information rather than interfere with industrial operations
- 2012, Flame is discovered and was found to be used in cyberespionage in Iran and other Middle Eastern countries
	- Flame is a Stuxnet variant
	- There is a belief that Flame had been a precursor to Stuxnet that had gone undetected
	- Flame is 20 mb in total (40x bigger than Stuxnet)
	- Spread via USB sticks and can infect printers shared over the same networok. 
	- Can search for keywords on top-secret PDF files then make and transmit a summary of the document without being detected.
		- It even sent things off in chunks to avoid detection. 
	- Could exchange data with any Bluetooth-enabled device. 
	- Could be attached to the Windows 7 OS update. 
- 
## What are the long-term results from it?
## How can I know if I'm being attacked by the NSA?
## What are other viruses in this same realm?
- Duqu
- Flame
- Gauss
## Questions?