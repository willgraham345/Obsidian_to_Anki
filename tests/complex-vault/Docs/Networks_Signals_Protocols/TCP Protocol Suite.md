---
summary:
headings:
  - "[[#Concepts of Note]]"
  - "[[#Diagrams]]"
  - "[[#Examples]]"
  - "[[#Flashcards]]"
  - "[[#Usage]]"
type: note/item
similar:
  - "[[UDP Protocol Suite]]"
  - "[[QUIC]]"
date created: Friday, October 3rd 2025, 10:06:42 am
date modified: Wednesday, October 8th 2025, 10:53:58 am
images:
  - "[[TCP Protocol Suite.png]]"
item_of:
  - "[[Networking Protocols]]"
  - "[[TCP-IP Model|TCPIP Model]]"
template:
template-version:
used_by:
  - "[[SYN Attack]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
󰙎  TCP Connection Establishment ;;; A 3 step handshaking process between hosts. = #cs/networking/tcp-ip/tcp/connection-establishment

### Connection
1. Sender sends packet with random initial sequence number generated at sender side, with `SYN` = 1
2. Receiver responds with `SYN-ACK` packet, and an Ack number it expects to receive back, and the same sequence number it just received
3. Sender sends an `ACK` packet with the Ack number, and data transmission can begin, and the sequence number from step 1 incremented by 1

### Items in TCP Header
Flags for TCP header fields

## Diagrams

![[TCP Protocol Suite.png]]

## Flashcards
󰠗  What is the role of the source port/destination port in a TCP header field? ;; Make sure the data reaches the correct location = #cs/networking/tcp-ip/tcp 
󰠗  What is the role of the sequence number in the TCP header? ;; Makes sure packets arrive in order, and can be used to reassemble packets in order if they arrive out of order. = #cs/networking/tcp-ip/tcp
󰠗  What is the role of the acknowledgement number in the TCP header? ;; Informs the sending host that the data was received. = #cs/networking/tcp-ip/tcp
󰠗  What flags are used in the TCP connection establishment phase? What does each of them do? ;; `SYN` (start connection), `ACK` (confirm a message has been received successfully), `RST` (abruptly close connection due to security), `FIN` (signals one device wants to close connection properly) = #cs/networking/tcp-ip/tcp/flags
󰠗  What does the window number in a TCP header do? ;; Specify the buffer size available for incoming data = #cs/networking/tcp-ip/tcp 
󰠗  Who requires a window for receiving messages in a TCP header? ;; Both the sender and the receiver = #cs/networking/tcp-ip/tcp 
󰠗  What is the function of the urgent pointer? ;; A "sticker" pointing to the urgent section of the data. = #cs/networking/tcp-ip/tcp

## Usage

### Calculate TCP Checksum
1. Prepare the Data: Combine the TCP header and the data to be transmitted. Make sure to include any necessary padding for alignment.
2. Divide the Data: Split the data into 16-bit words (2-byte parts). If the last part is incomplete, pad it with zeros.
3. Sum the Words: Add up all the 16-bit words. If the sum exceeds 16 bits, wrap the overflow back around to the lower 16 bits.
4. Invert the Sum: After adding all the words, take the one’s complement (invert all the bits) of the sum. This inverted value is the checksum.
5. Attach the Checksum: The calculated checksum is then included in the TCP header for transmission.

## Examples

1. Sender starts the process with the following: 
	- Sequence number (Seq=521): contains the random initial sequence number generated at the sender side.
	- Syn flag (Syn=1): request the receiver to synchronize its sequence number with the above-provided sequence number.
	- Maximum segment size (MSS=1460 B): sender tells its maximum segment size, so that receiver sends datagram which won't require any fragmentation. MSS field is present inside Option field in TCP header.
	- Window size (window=14600 B): sender tells about his buffer capacity in which he has to store messages from the receiver.
2. TCP is a full-duplex protocol so both sender and receiver require a window for receiving messages from one another. 
	- Sequence number (Seq=2000): contains the random initial sequence number generated at the receiver side.
	- Syn flag (Syn=1): request the sender to synchronize its sequence number with the above-provided sequence number.
	- Maximum segment size (MSS=500 B): receiver tells its maximum segment size, so that sender sends datagram which won't require any fragmentation. MSS field is present inside Option field in TCP header.
	- Since MSS receiver < MSS sender , both parties agree for minimum MSS i.e., 500 B to avoid fragmentation of packets at both ends.
	- Therefore, receiver can send maximum of 14600/500 = 29 packets.
	- This is the receiver's sending window size.

	- Window size (window=10000 B): receiver tells about his buffer capacity in which he has to store messages from the sender.
	- Therefore, sender can send a maximum of 10000/500 = 20 packets.
	- This is the sender's sending window size.
	
	- Acknowledgement Number (Ack no.=522): Since sequence number 521 is received by the receiver so, it makes a request for the next sequence number with Ack no.=522 which is the next packet expected by the receiver since Syn flag consumes 1 sequence no.
	- ACK flag (ACk=1): tells that the acknowledgement number field contains the next sequence expected by the receiver.
3. Sender makes the final reply for connection establishment in the following way: 
	- Sequence number (Seq=522): since sequence number = 521 in 1 st step and SYN flag consumes one sequence number hence, the next sequence number will be 522.
	- Acknowledgement Number (Ack no.=2001): since the sender is acknowledging SYN=1 packet from the receiver with sequence number 2000 so, the next sequence number expected is 2001.
	- ACK flag (ACK=1): tells that the acknowledgement number field contains the next sequence expected by the sender.
