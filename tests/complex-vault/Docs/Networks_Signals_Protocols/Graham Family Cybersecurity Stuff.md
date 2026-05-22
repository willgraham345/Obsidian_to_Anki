---
date created: Sunday, August 3rd 2025, 1:33:16 pm
date modified: Sunday, August 3rd 2025, 3:09:37 pm
theme: consult
---

# **How does my phone find me such great TikToks?**

---

# The heck is a network?

![[Pasted image 20231211134556.jpg]]
- Networking topology refers to the physical or logical arrangement of the devices in a network. It's the layout that determines how devices are connected and how data flows between them.


---

# What's this internet thing?
![[OSI Network Model 2.jpg|400]]

Good words to know
- WAN = wide area network (the internet)
- VLAN = Virtual local area network (complicated, we'll talk about it later)
- MLAN = Metropolitan area network

---

# What is WiFi?
- There's a tiny transistor (or a group of em, I dunno) that takes in a wave, and turns it into 1's and 0's.
- Your phone sends out a "help me, I'm in need of a network"
	- The router (more info later) says, gimme a password. You do that, and bada bing bada boom, you are part of the network.

![[Graham Family Cybersecurity Stuff.png]]
![[Network OSI Model.png]]

---

# What's my local network?
* **IP Address:** Every device connected to the internet has a unique IP address, which acts as its identifier on the network.
* **Data Packets:** When you send information (e.g., loading a webpage, sending an email), that information is broken down into small units called packets.
* **Routers:** These devices direct the data packets from their source to their destination, ensuring they reach the correct IP address.
* **Internet Service Provider (ISP):** Your ISP is the company that provides your internet access. All of your online activity passes through their servers, meaning they can see every website you visit and every piece of data you send or receive.

---

# Introducing TikTok

---

# I clicked on TikTok, what happens?

My processor starts the TikTok app, which opens a bunch of computer sockets (think of this as little garage for internet stuff)

That little socket starts a chain of gimmes
1. Gimme internet to the router
2. The router asks for help from the ISP
3. The ISP goes and finds TikTok.com
4. TikTok.com says "open a server for whoever this is"
5. TikTok.com says "This is Will"
6. TikTok.com saves *all* of my information
	1. This is spooky, and we don't like it. More info to follow.
7. I close tiktok and it says ok

---

# How do I avoid the spooky "steal my money" guys?
Don't use google, tiktok, or any social media. 
- They take everything you upload, and they use it to do whatever they want with. 

---

# **Why Everyone Needs a VPN**

A **VPN** (Virtual Private Network) is a service that secures your internet connection by creating an encrypted tunnel for your data.

* **IP Address Masking:** A VPN hides your true IP address. To the websites you visit, your traffic appears to be coming from the VPN server's location, making it harder to track your physical location.
* **Data Encryption:** A VPN encrypts all of your internet traffic. This means that even if someone intercepts your data, it will be unreadable and useless to them.
* **Public Wi-Fi Security:** Using a VPN on public Wi-Fi networks (like at a cafe or airport) is crucial. It prevents hackers who may be monitoring the unsecured network from seeing your private information.
* **ISP Privacy:** A VPN also prevents your ISP from seeing your Browse history and online activities.


---

# AI Generated Slides for our education

---

### **Fun terms**

Understanding the hardware that gets you online is important for security.

* **Modem:** The modem is the device that connects your home to your **ISP**. It translates the digital signals from your network into a format that can be sent over the internet lines and vice-versa.
* **Router:** The router is the device that creates your home network. It takes the internet connection from the modem and shares it with all your devices (computers, phones, smart TVs) via a wired connection or wirelessly through a **WLAN** (Wireless Local Area Network), which is what we call Wi-Fi.
* **ISP (Internet Service Provider):** This is the company you pay for internet service. The ISP provides the connection and an IP address for your home network. All of your internet traffic flows through their systems.

---

### **Cookies**

Cookies are small text files that websites store on your computer. They are used to save information about you to improve your experience, but they can also be used for tracking.

* **Session Cookies:** These cookies are temporary and are deleted when you close your browser. They are used for things like keeping you logged in to a website while you are Browse it.
* **Persistent Cookies:** These cookies remain on your computer for a set amount of time or until you delete them. They are used to remember your preferences, like language settings, or for tracking your Browse habits across different websites.
* **Third-Party Cookies:** These are cookies set by a website other than the one you are currently visiting. They are most commonly used for advertising and tracking.

**Security Tip:** You can configure your browser to block third-party cookies or to delete all cookies when you close the browser.

---

### **Computer Sockets**

A computer socket is an endpoint for sending and receiving data across a network. It is made up of an IP address and a port number.

* **Port Numbers:** These are logical addresses that identify specific applications or services running on a computer. For example, web browsers often use port `80` (HTTP) or `443` (HTTPS) to communicate. There are over $65,000$ possible port numbers.
* **Firewalls:** A firewall is a security system that monitors and controls incoming and outgoing network traffic. It uses rules to determine whether to allow or block data packets based on their source, destination, and port number.
* **The threat:** An attacker may try to exploit open, unprotected ports on your computer to gain unauthorized access. A firewall's job is to close these ports unless a service explicitly needs them to be open.

---

# **The Threat of AI Attack Vectors**

Attackers are leveraging advanced AI tools to make their malicious activities more convincing and effective.

* **Deepfakes:** AI is used to create highly realistic fake videos or audio.
    * **The threat:** You might receive a video call that appears to be from a family member, a friend, or a colleague, but it is actually a deepfake designed to manipulate you into providing information or money.
* **Advanced Phishing:** Traditional phishing emails are becoming more sophisticated.
    * **The threat:** AI can craft perfectly worded, grammatically flawless emails that are highly personalized. These are much more difficult to identify as fraudulent compared to older, more obvious scams.
* **Malicious Chatbots:** AI-powered chatbots can be used to engage in realistic conversations.
    * **The threat:** A chatbot could impersonate a customer service representative from a trusted company and use the conversation to extract sensitive information like passwords or financial details.

---

# Stuff to do

- Trust no one
- Use a VPN
- Use a password manager
	- Pass that password to your spouse or a trusted adult 
- Don't download things unless you know what you're doing