# Background
![[Pasted image 20230929153941.png]]
UART transmits data asynchronously (two different clock signals)
[UART Communication Circuit Basics](https://www.circuitbasics.com/basics-uart-communication/)
[UART communication ](https://www.analog.com/en/analog-dialogue/articles/uart-a-hardware-communication-protocol.html)



## Receiving
Upon detecting a start bit, it reads the incoming bits at a specific frequency known as the baud rate. The transmitting UART converts parallel data 
### Start bit
UART transmission is usually held at a high voltage when it's not transmitting data. To start the transfer of data, the UART pulls the transmission line from high to low for one clock cycle. When the receiving UART detects the high to low voltage transition, it begins reading the bits in the data frame at the frequency of the baud rate.



