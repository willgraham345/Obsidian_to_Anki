# 3.1 Intro
Foundry model: Company sells space within the fab line to fabless semiconductor firms.
- TSMC, UMC, Chartered, IBM work on this model


### Raising Conductivity of Silicon
The conductivity of silicon can be raised by introducing impurity atoms into the silicon crystal lattice
#### Group 3 Atoms
- Impurity elements, referred to as acceptors, because they accept some of the electrons already in the silicon, leaving holes
- Boron
#### Group 5
- Donor elements, which provide electrons
- Arsenic and phosphorous

### N-type and P-type
- N-type = has more electrons than holes (negative)
- P-type = has more holes than electrons (positive)

A junction is a region where n-type and p-type are brought together and combine. 


# 3.2 CMOS Technologies
## 3.2.1 Wafer Formation
Boule = a cylindrical ingot of single-crystal silicon, which has been pulled from a crucible of pure molten silicon
## 3.2.2 Photolithograhy
Carving pictures using light

Photoresists = thing you put on stuff where you want it removed
- Photomask = Subjective illumination
- Constructed using chromium covered quartz glass. A UV light then exposes the photoresist

The wavelength of the light source influences the minimum size that can be printed. Define the minimum pitch (width + spacing) of a process to be 2*b*. The resolution of a lens depends on the wavelength $\lambda$ of the light and the *numerical aperture* NA of the lens:
$2b = k_1 \dfrac{\lambda}{NA}$ 
Nikon and ASML broke the 1.0 barrier by using immersion lithography, that takes advantage of water's higher refractive index. In 2008, NA=1.35 was reached.

## 3.2.3 Well and Channel Formation
Wells and other features require regions of doped silicon






# 3.3 Layout Design Rules
- Layout rules = design rules

### 3.3.1 Design Rules Background
#### 3.3.1.1 Well Rules
- The n-well is usually a deeper implant (especially a deep n-well) than the transistor source/drain implants, and needs clearance between the n-well edges and adjacent n+ diffusions. 
#### 3.3.1.2 Transistor Rules
- CMOS transistors are usually defined by four physical masks:
	- Active = diffusion, diff, OD, RX
	- n-select = n-implant, nimp, or nplus
	- p-select = p-implant, pimp, pplus
	- polysilicon = poly, polyg, PO, PC
	- 





