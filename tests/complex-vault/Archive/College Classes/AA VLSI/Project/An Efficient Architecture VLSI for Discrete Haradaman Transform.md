

# Introduction
DSPs are needed for essential real time processing. 

Discrete transform is used to change the signal from one domain to another, reducing the complexity of a particular DSP application. 

Discrete Hadamard Transform
- Real discrete orthogonal transform (DOT)
	- Used widely in CDMA and MPEG applications

#### CDMA
- CDMA = code division multiple access
	- Happens where several transmitters can send information simultaneously over a single communication channel. 
		- Allows users to share a band of frequencies
			- Optimizes the use of available bandwidth
- Refers to many protocols used in 3G and 2G wireless communications. 
	- The purpose is to transmit digital information in the form of ones and zeros over the air. 
#### MPEG (a.k.a .mpg)
- Video file
- Designed to compress VHS-quality raw video and CD audio down to 1.5 megabits per second without losing too much in quality. 
- Video data for MPEG-2 is normally 30 fps, with a max resolution of 720x480

#### DHT
- DHT is used for an efficient implementation of image compression and coding. 

### Example
- $H_N$ = $N\times N$ discrete Hadamard co-efficient matrix
- $Y$ = $N$-point output signal sample values
- $X$ = N-point input signal sample values

1D forward discrete Hadamard transform of N-point input singnal sample values:
- $Y_N = H_N X_N$ 
2 point Hadamard co-efficient matrix
- $H_2 = \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}$
4 point Hadamard co-efficient matrix
- $H_4 = \begin{bmatrix} 1 & 1 & 1 &1 \\ 1 & -1 & 1 & -1 \\ 1 &1 &-1 &-1 \\ 1 &-1 &-1 &1 \end{bmatrix}$
8 point Hadamard co-efficient matrix
- $H_8 = \begin{bmatrix} H_4 & H_4 \\ H_4 & -H_4 \end{bmatrix}$
General equation
- $H_N = \begin{bmatrix} H_{N/2} & H_{N/2} \\ H_{N/2}  & H_{N/2} \end{bmatrix}$

## Contribution of this Paper
- Improve the performance of DHT architecture for DSP applications. The performance of a circuit usually depends on circuit delay, circuit area, and net power requirements.
	- Circuit delay is the primary objective for this paper. 
- Proposed $N$-point Hadamard transform architecture is designed with a signed carry save adder (CSA) tree. Depth of the architecture falls within the bounds of $O(\log_2 N)$ 

# Motivation of Proposed Design
Worst critcial path time complexity of conventional design is: $2\log_2N$ number of CLAs
- This can be replaced by 4-point signed CSA
	- ![[Pasted image 20231004121441.png]]

We have 3 stages, how should we split it up

In the conventional design of an $N$-point 1D-DHT, the worst critical path includes $2log_2N$ number of CLAs. Each stage includes 2 CLAs (one for taking 2's complement according to hadamard coefficient and an another for addition of 2 input values)

Last 2 signed addition stages of conventional design are replaced by 4-point signed CSA