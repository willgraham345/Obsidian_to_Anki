---
type: note
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Monday, December 2nd 2024, 11:26:12 am
---
Phil Garner (L3H) was the presenter

## Part 1 (Comms)
### Signals intro
- Signal = a disturbance which one entity can generate, and another can detect.
- Signals channel through a medium.
- There's usually a reference level, and movement of (passband) through the channel. 


- Carrier wave = a signal that transmits in a perfectly regular medium. 
- Modulating signal types:
  - *FSK* = frequency modulation
    - Faster/slower frequency than normal
  - *ASK* = Amplitude Modulation 
    - Bigger/smaller than normal
  - *PSK* = phase modulation a.k.a Phase shift keying
    - Can be combined with amplitude modulation to pack even more info into a signal (Quadrature Amplitude Modulation = *QAM*)
- Baseband signaling = low for zero, high for 1. 
  - This is used within systems
  - This falls apart when you don't' have complete control over the channel. Multiple different signals can't use the channel.
  - Passband signaling enables multiple different conversations taking place at different frequencies. 
    - You can use Fourier analysis to focus in on a particular part of the frequency spectrum
      - This is true on radio waves, light waves, electrical wires, or the EM fields. 

- Symbol rate = number of symbols in a second

- Modem = modulates or demodulates into 0's and 1's. 

### Serial vs parallel interface
- Serial
  - Bits transmitted one after another
  - Typically used in modern devices 
-  Parallel
   -  Bits transmitted simultaneously over multiple channels. You can get all the bits transmitted at once. 
   -  Take up a ton of space
   -  Interference between different thigns
   -  Twisted cable interface is twisted because it mitigates the interference

### Types of channels
- Point to point
  - Goes from one transmitter to one receiver. Usually use a physical wire, or something that behaves like a physical wire
    - i.e. ethernet card to a ethernet switch
  - Types:
    - Simplex = one way channel
    - Half duplex = info can flow one way, but only works in one direction
    - Full duplex = info can flow both ways
- Broadcast
  - Signals go from one transmitter to multiple receivers. Every receiver in range hears the same signal (though some may be "louder" or "clearer") 
    - i.e. WiFi
  - Types:
    - Prefix each message with some kind of an address
    - Medium access control (MAC) address. 
  - Controlling access to broadcast channels
    - FDM = Frequency division multiplexing
      - Different sender-receiver sub-groups use deferent frequencies. Outside things are passed out using a filter 
    - TDM = Time division multiplexing
      - Wasteful, but it works. You can also use variable time slots (digital equivalent of a talking stick)
    - CDMA = Code Division Multiple Access
      - Everyone talks at the same time using same frequency band, but conversation is mathematically encoded to allow receivers to pick a particular sender's signal out of the noise. (similar to low voices at a party)
    - Carrier Sense Multiple Access
- The Speckled band (width) (spectrum allocation)
  - Real physical wireless communication devices can only operate within specific frequency ranges.
  - Operating band = range of radio frequencies that a device can operate in
    - There are differnt bands designated by letters (google radio spectrum)
  - Bandwidth = difference between lowest and highest frequency of a given operating band determines its bandwidth. 
    - Things need to be within the same band to talk with one another
      - The wider the bandwidth between them, the higher the rate at which the two devices can exchange information. 
        - You can use more complicated modulation schemes with this. 
    - Governments are also carefully involved in policing different bandwidths

## Summary to this point
- For communication, there is a written agreement of:
  - Communication channel/medium
  - Modulation
  - Symbol tuning and encoding
  - Mapping from bits to characters
  - Type of channel
  - Rules for acessing the channel
  - Operating band
- The above specifies a *waveform*
- Waveforms are known as *Layer 1* 

---

### Cryptography
- *COMSEC* = communications security
- *Cleartext* = readable by anyone
  - Referred to as *Red*
- Ciper = scrambling algorithm
- Ciphertext = a text that has been encrypted
  - Reffered to as *black*
- Ciper + key = cipertext
- Symmetric cryptography
  - Cipertext is decrypted by running "backwards" through the same ciper, using the same key that was used to encrypt it. 
    - All participants must somehow exchange a copy of this same shared secret key
      - Secret keys must be closely guarded in this situation, and key distribution is a challenge

- Public key cryptography
  - Each person has a pair fo keys, one public, one private
    - Public key is not secret, enabling anyone to send him a secret message
    - A private key is used to decrpyt the message

- *Bulk encryption* refers to a device that encrypts ALL information flowing through the link.
  - Goes from red to black
  - Traditionally use a symmetric cipher

### Generic wireless data link
- Switch and/or Router
  - Switches forward info from source to desired over common medium
  - Routers do the same as switches, but for many networks (with a variety of media)
- "Black/Red" boundary (where COMSEC lives)
- Modem (Modulator/Demodulator)
  - 1's and 0's into signal within frequency band
- Frequency upconverter (BUC = Block UpConverter)
  - Translate outgoing signal from data links intermediate frequency band to high external operation band
- Frequency Downconverter
- Amplifier (often HPA = high power amplifier)
- Amplifier (LNA = Low nosie amplifier)
  - hears low power signals and boosts them to a working level. 
- Antenna
  - Translates electrical signals to radio waves and vice versa
  
Antennae
- Types:
  - Omni-directional
  - Directional 
    - Fixed
    - Mechanically steerable
    - Electronically steerable
      - Elements that can cause the direction of antenna beam to be changed. Think of tiny grid prisms that can change angle at which they bend light. 
- Challenges
  - Getting antenna to "see" each other

## Part 2
### Local Area Networks
- We have:
  - Broadcast channel accessible by a group of people
  - Waveform that specifies how bits are encoded onto modulated signals on the channel
- We'll add:
  - Framing scheme = specifies how to group stream of bits into a message
    - Usually some kind of pattern to start and end a message 
  - Addressing scheme = identifies recipient of a given message
  - Channel access scheme = a way to control of who speaks when (FDM, TDM, CDM, or CSMA)
- Definition of a LAN
  - Broadcast channel, waveform specifying how bits are encoded onto modulated signals, framing scheme, addressing scheme, and a channel access scheme
  - a.k.a. *Layer 2* or *Datalink Layer*, *MAC Layer*

- Notes about LAN's:
  - Message addresses must be unique wihtin teh LAN. There is usually one special "broadcast address" which goes to everyone
  - Each participant in a LAN can send messages directly to any other LAN participant without a middleman.
  - LAN's often have error detection schemes. Can be a simple checksum, or a sophisticated CRC (CRC = cyclic redundancy check). FEC = forward error correction schemes do even more, by even repairing the error (sometimes FEC's are built into the Layer1 waveform. )

Classic Ethernet LANs
- Classic setup has one cable, physically plugged into every computer.
- Each computer has a NIC = network interface card
- Waveform specifies how bits are encoded (IEEE standards)
- Framing scheme
  - Ethernet frames are between 64 and 1500 bytes long. Each frame starts with a distinctive Preamble bit pattern and includes info so that the receiver can determine the length of an incoming frame. 
- Addressing scheme to identify the recipient of a given message
  - Ethernet MAC (Medium access control) addresses. 
  - Every Ethernet NIC on the planet has a unique 48-bit long address. 
  - MAC ddresses are so closely identified with Layer2/Datalink layer that Layer2/Datalink layers are called the MAC layer 
- LAN's have error detection schemes for detecting whether a message was garbled in transit



Modern Ethernet
- Hubs
  - Went from a solid copper cable into a hub. The hub simulated teh behavior of old physically-connected cables. These are "dumb", sending all messages to all participants
- Switch
  - Work like hubs, but they learn MAC addresses of the Ethernet NIC's attached to each of their ports. When the frame arrives, the switch only sends it out to the port to which the actual addresses is attached
  - a.k.a. bridge

### Datalink Layer
Protocol = set of etiquette rules
- Types of rules found in network protocols(at various layers)
  - What size can PDU's be?How long is this one?
  - Which bits are address part? Where does the payload start?
  - Whose turn is it to talk?
  - What form are questions and answers allowed to take?
  - How does one party say that another party is sending data too quickly?
  - How does one party say that another party's message was lost? (retransmission)
- Minor questions to answer
  - What if parties are on different LANs, maybe far apart? How do they identify and locate one another?
    - Network layer
  - What if parts of messages are corrupted along the way?
  - How do different applications running on a computer keep things straight when they all want to use the same network connection?
Different LAN types may have totally different Layer 2 address formats. Even if a foreign LAN has the same Layer 2 address format, it only knows about connections within it's own neighborhood.

### Networking Layer
- IP = Internet protocol
  - IPv4
  - IPv6
- Each LAN gets an address of it's own. IPv4 address is split into network part and host (computer part). Network part tells you which LAN you are talking about and host part tells you which computer on that LAN you are referencing
- *Subnet mask* tells you how much of the address is dedicated to the network number, and how much is dedicated to the host number.
  - Host addresses "all zeros" and "all ones" have special meanings.
- Now, every computer has 2 addresses.
  - (Datalink/MAC) addresses that make sense to immediate neighbors
  - Layer 3 (Network/IP) that makes sense by all LANs in the world
- Unit
  - packet
  - ipv4 addresses are 23 bits long, ipv6 addresses are 128 bits long.  
- Example datalink packet
  - From: (MAC address) 
  - To: (MAC address)
  - From:(IPv4)
  - To: (IPv4)
  - MESSAGE
  - Frame checksum

### Routing
- A router is a specialized computer with the following properties:
  - Multiple NIC's, each connected to a different LAN, each is a separate *interface*
  - Separate IP addresss for each interface
  - Willingness to receive someone else's IPpackets on one interface and send them out in another interface that is "generally in right direction" (*forwarding*)
  - Maintiains a *routing table* that lets it know which interface is in "generally" the right direction for any possible destination. 
    - Keeping this table properly updated is *routing*, a huge complex topic all by itself.
    - A converged IP network means that routers have generally agreed how to get to separate locations. It takes time to associate things. 
- Some groups of routers primarily connect to other routers by high speed connections, usually from large corporations or *Internet Service Providers*. 
- Forwarding Algorithms
  - Is IP address of this packet my own? If yes, *consume* the packet by sending it to the correct host.
  - IS IP destination special "loopback" value? If yes, *consume* it
  - Does network part of this IP destination match my own network, if yes, send it on my own LAN. 
  - If packet isn't on my LAN, consult routing table to see which outgoing line is generally in the right direction and send it out that line. 
    - End user computers typically only have one interface.
    - Typically, there is a default address. This is the "router doesn't know what to do, send it to this other station that will figure it out" address

### Firewalls
- A firewall is essentially an anti-forwarder.
  - If a packets source or destination IP matches such and such pattern that you don't like, the firewall will stop it in its tracks (refuse to forward)
- Might be standalone devices, built into routers, or running on a computer
  - These may also employ *deep packet inspection*, where they don't only inspect the IPaddresses but also look at what they're carrying.
- COMSEC's are bulk encryption devices, entities that encrypt all traffic flowign over a single layer 2 hop between a pair of devices.
- IPSec = Internet protocol security
  - Operates at Layer 3, encrypting IPpackets flowing between two particular endpoint.
  - Military version of IPSec is called HAIPE (High assurance internet protocol encryptor)

### Transport Layers
- Transport Layer 4 is directly above the network Layer
  - Similar to administrative assistants
- Above the transport Layer is an application Layer, and Layer 7
  - Applications are like the managers 
- Ports = Inbox/outbox stuff
  - These are different from physical ports where you plug cables in
  - Port 80 is always used for web servers of some kind
- Socket = combination of a port number and an IP address
  - A socket is where a given application can "plug in" to the networking stack.
- A given server application can use a socket to *attach* to a port on a given computer and will then *listen* on that port for any client requests that come in
- TCP = Transport Control Protocol
  - Detail oriented admin in the transport layer
- UDP = User Datagram Protocol
  - Fast admin

### Application Layer
- Applications that involve networking take advantage of a "helper" service called DNS (Domain Name Service)
  - DNS is an Internet-wide directory that maps from user-friendly domain names, to the IPaddresses that are associated with those names. 
- Applications will determine TCP or UDP.

### ipconfig
- ipv4 shown as a group of 4 (decimal), ipv6 is shown as a hex
- DCHP Enabled = Dynamic Host Configuration Protocol
  - Workstations automatically assign themselves IP addresses. In olden times, people would need to manually do that
ipconfig /all
- will pull up the networking configuration of your computer
- Shows information about the NIC, the physical address
  - The physical address is a hex digit, with each hex digit representing a four-bit "nibble. Basically, two hex digits represent an 8 bit byte.
- Shows the default gateway the router sends things. 
  - The "when all else fails" destination, the default outbound gateway. 
- DNS naemspace: the namespace your computer belongs to.

### IP Stack
- Physical -> Datalink -> Network -> Transport ->Application 

## The Layer Cake
- OSI (open systems interconnection) model created by the ISO (International Organization for Standardization) 
- OSI 1 [[Networking Link Layer 1]]
  - Various baseband or passband signaling schemes. Provide the medium through which signal passes, everything above is carred in a modulated coded signal
  - Example protocols: a variety of baseband or passband signaling schemes
  - Requires 
    - communication medium
    - waveform
  - Unit
    - Bit (0 or 1)
- OSI 2 [[Networking Link Layer 2]]
  - Delivers *frames* to other computers on the same LAN.
  - Example protocols: Ethernet, 802.3, WiFi, 
  - Requires:
    - A Layer 1 to ride
    - Framing scheme
    - Addressing scheme
    - Channel access scheme
  - Name of unit:
    - Frame - group of bits that can be validated as a unit 
- OSI 3 [[Networking Network Layer 3]]
  - Transmits packets from a source computer all the way to a destination computer, possibly transversing many LANs along the way. Forwarding is a job of consulting a table to see which outgoing line to send a packet out on. Routing is a job of keeping the tables updated so you know which next hop is in the best direction for ultimately getting to the destination. 
  - Example protocols: IPv4, IPv6
  - Unit
    - Packet (encapsulates segments or datagrams)
- OSI 4 [[Networking Transport Layer 4]]
  - TCP: Transfers segments (streams of characters from user messages) from source to destination with acknowledgements and retransmissions to ensure communication. UDP transfers datagrams (each carrying a user message) from source to destination with no confirmations. 
  - Example Protocols: TCP, UDP
  - Addressing
    - Combination of IP address plus port number
      - This combination is called a socket. 
  - Unit:
    - Segment (TCP)
    - Datagram (UDP)
- OSI 7 [[Networking Application Layer 7]]
  - Provide real-world service or benefit to end user by passing "user messages" among computers. All layers below exist to support this mission.
  - Example Protocols: HTTP (web traffic), FTP (file transfer)
  - Addressing:
    - URL
  - Name of unit:
    - web page
    - file
    - song