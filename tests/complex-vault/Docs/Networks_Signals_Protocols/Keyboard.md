---
type: note
---
USB circuitry of the keyboard is powered by 5V supply.
## Protocols 
Many keyboards use a cable with a PS/2 or USB connector (laptops have internal connectors)
- Wireless keyboards have infrared (IR), RF, or Bluetooth connections.
## Internal Circuits/Controllers 
An integrated circuit that processes all of the data coming from the keyboard. This is a register titled "endpoint". 
- Operates at ~10 ms monitoring for endpoint.
	- An electrical circuit specific to each key controls when signals are sent. 
- Forwards information to the operating system
	- The OS will check to see if the keyboard data is a system-level command (i.e. `ctrl+alt+delete`)
	- If not, the OS passes the information off to the current application
- Values of the "endpoint" are forwarded to the USB SIE (Serial Interface Engine) and converted into one or more USB packets that follow the low-level USB protocol

Video on [PS/2 keyboard interface](https://www.youtube.com/watch?v=7aXbh9VUB3U&t=3s)
Great open-source repo on what happens when you type [google into your browser](https://github.com/alex/what-happens-when)