---
type: note
---
# Background
- Virtual network adapter = software-emulated device
[More info here]([VirtualBox Network Settings: All You Need to Know (nakivo.com)](https://www.nakivo.com/blog/virtualbox-network-setting-guide/#:~:text=VirtualBox%20network%20adapter%20settings%20can,default%20after%20virtual%20machine%20creation.))

![[VirtualBox-Network-Settings-for-Adapter-1.webp|250]]

## VirtualBox Network Modes
### Not attached
Similar to unplugging the Ethernet network cable when using a physical network adapter. You can also simulate this by unchecking the cable connected checkbox.

### NAT
This is a great mode for when users who just want to use the VM for only internet access.
Enabled by default
![[VirtualBox-network-modes-–-how-the-NAT-mode-works.webp|275]]
A guest OS on a VM can access hosts in a physical LAN by using a virtual network address translation (NAT) device. 
- External networks, including the internet, are accessible from a guest OS. 
- A guest machine is not accessible from a host machine. 

# Usage 
## Virtual Network Adapter Types recognized by Virtualbox
- **AMD PCnet-PCI II (Am79C970A)**. This network adapter is based on AMD chip and can be used in many situations. As for Windows guests, this network adapter can be used for older Windows versions (such as Windows 2000) because newer Windows versions such as Windows 7, 8 and 10 do not contain a built-in driver for this adapter. Originally, the **_Am79C970A_** PCI device contained a single chip 10-Mbit controller and the DMA engine was integrated. This network adapter also supports AMD’s Magic Packet technology for remote wake-up.
- **AMD PCnet-FAST III (Am79C973)**. This virtualized network adapter is supported by almost all guest operating systems that can run on VirtualBox. GRUB (the boot loader) can use this adapter for network boot. Similarly to the previous network adapter, this one is based AMD chip.
- **Intel PRO/1000 MT Desktop (82540EM)**. This adapter works perfectly with Windows Vista and newer Windows versions. The most of Linux distributions support this adapter as well.
- **Intel PRO/1000 T Server (82543GC)**. Windows XP recognizes this adapter without installing additional drivers.
- **Intel PRO/1000 MT Server (82545EM)**. This adapter model is useful to import OVF templates from other platforms and can facilitate import process.
- **Paravirtualized Network Adapter (virtio-net)** is a special case. Instead of virtualizing networking hardware that is supported by most operating systems, a guest operating system must provide a special software interface for virtualized environments. This approach allows you to avoid the complexity of networking hardware emulating and, as a result, can improve network performance.