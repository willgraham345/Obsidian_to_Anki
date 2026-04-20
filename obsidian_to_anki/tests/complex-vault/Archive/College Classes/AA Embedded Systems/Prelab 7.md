## Question 1
Describe the following network topologies:
Point-to point
Mesh
Hub-and-spoke/star
Bus
Daisy chain
Ring
Tree
Hybrid
- Point to point = A to B communication, as simple as it gets.
- Bus = Everything along a wire talking to everything else. The central wire is a commodity with every node fighting to control it. 
- Daisy Chain = A connection of point-point to point wirings, sending messages from one spot to another.
- Ring = Everything connected in a circle, data can travel through the ring on the outside in either one or both directions. Same as a daisy chain, but it forms a loop rather than a line. 
- Tree = Same as a star, but has a parent-child relationship. 
- Hybrid = ANY combination of the stuff above.


## Question 2
What is the function of a CAN transceiver?
- An external device that converts logical signals from the CAN controller to the bus-levels.
## 3
Describe the properties of CAN that allow prioritization, error handling, and multiple bus members acting at the same time. How does CAN detect a collision?
 - CAN is a multi-master serial bus. All nodes communicate through a two-wire bus.
 - There is no central node, but there is central wire that shares media in the network. It is a shared resource, and everything is fighting over control of it. It is also unidirectional. A node cannot transmit while listening, and can't listen while transmitting. 
## 4
What is the function of an identifier in a CAN frame?
- An identifier can be used to designate the frame instead of addresses to identify nodes. This is used for masking.
## 5
What is a differential transmission line, and what advantages does it have?
- A differential transmission line uses two signal lines to transmit electrical signals. These signals will travel in opposite directions and operate in one mode. They have higher data rates, and don't have noise that comes from other transmission stuff. They also have good logic rates and precise timing.