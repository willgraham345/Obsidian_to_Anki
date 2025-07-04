---
type: note
---
# Common Serial Programming Interfaces
## UART
- Universal Asynchronous Receiver-Transmitter
- Common asynchronous serial communication protocol. Often used for short-distance communication between devices. 
- Uses two wires
	- TX = transmission
	- RX = receiving 

## SPI
- Serial Peripheral Interface
- Synchronous communication, often used for high-speed communication between microcontrollers, sensors, and other peripherals.
- Synchronous serial communication using four wires:
	- SCK = clock
	- MOSI = master to slave communication
	- MISO = slave to master communication
	- CS = chip select

## I2C
- Inter-Integrated Circuit
- Synchronous, multi-master, multi-slave communication. Used for communication between integrated circuits, sensors, and other devices with moderate data transfer rates
- Requires two wires:
	- SDA = data line
	- SCL = clock line

## USB
- Universal Serial Bus
- Complex serial communication protocol used to connect various devices to a computer or other host systems. Supports multiple data transfer modes (bulk, interrupt, isochronous) and provides power supply. Offers high-speed data transfer rates, widely used within electronics. 


# Linux Serial Communication
## SPI

### Relationship between SPI and GPIO pins
#### SPI protocol
- SPI bus has 4 main lines:
	- SCLK (serial clock): Clock signal used for synchronization between the master and slave devices
	- MOSI (Master Out Slave In): Carries data from the master to the slave
	- MISO (Master In Slave Out): Transfers data from the master to the slave.
	- SS/CS (Slave Select/ Chip Select): used by the master to select the specific slave device it wants to communicate with. 
#### GPIO Pins for SPI
- The pins used for SPI are usually GPIO pins
- Linux kernel's SPI subsystem interacts with the hardware through GPIO pins configured for SPI use. These pins can be dynamically assigned.
#### Kernel SPI Framework
- Linux provides a generic SPI framework in its kernel. The SPI framework abstracts the hardware-specific details, making it easier to develop SPI drivers independent of underlying hardware
#### Device Drivers
- SPI device drivers in Linux implement communication protocols specific to individual SPI devices. Each device driver registers with the SPI subsystem and provides the necessary functions to handle data transmission and reception. 
- Device drivers use the SPI kernel framework to initiate SPI transfers and handle data exchange between the CPU and SPI devices. 
#### Device Tree and GPIO Configuration
- On embedded systems, the device tree is used to describe the hardware configuration to the Linux kernel. It contains information about the available GPIO pins and their functions including those used for the SPI bus. 
- During system boot, the device tree is parsed, and the GPIO pins are configured accordingly to set up the SPI bus for communication with the attached devices. 