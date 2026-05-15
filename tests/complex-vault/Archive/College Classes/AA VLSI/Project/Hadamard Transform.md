# Section Paper Notes
a generalized class of Fourier transforms
- Performs orthogonal, symmetric, inclusive, and linear operations on 2m real numbers. 
- Can be viewed as being constructed from the Discrete Fourier Transform of size 2
- It basically decomposes a given function into smaller basis functions (just like harmonics in Fourier transforms). Resolution is determined by the scaling number ($\dfrac{1}{N}$).
	- Rectangular or square waves (+1, -1) are the functions. 

$y_n=\frac{1}{N}\sum x_i=\sum y_n WAL(n,i)$
- $WAL(n, i)$ are the walsh functions

$\begin{vmatrix}y_1\\y_2\\:\\:\\y_N\end{vmatrix}=\frac{1}{N}\begin{vmatrix}H_{11}&H_{12}....&H_{1N}\\H_{21}&H_{22}....&H_{2N}\\:\\:\\H_{N1}&H_{N2}....&H_{NN}\end{vmatrix}\begin{vmatrix}x_1\\x_2\\:\\:\\x_N\end{vmatrix}$

- $H_N$ = Hadamard matrix
- $N = 2^n$
Inverse transform rules:
$x = H_n^{-1}=H_ny$
$H_n^{-1}=H_n^T=H_n$

## Hadamard Matrix
### Definition
An NxN matrix containing values $\pm1$ such that each row of the matrix agrees with all other rows on exactly $N/2$, or half, of their positions.
- "Agreeing" means that rows have the same element ($\pm 1$) in the same column position. This means that for a 1 in the (1, 1) index, exactly $N/2$ of the other rows have 1 in the (N,1) position. 
	- This means that the Hadamard matrices have to be 2 or any multiple of 4. The values do not have to be 1 and -1, but can be in any binary system. A hadamard matrix made of only 1's is said to be normalized. 
	- Additionally, the top left corner of a matrix must be the inverse of the bottom right corner of a hadamard matrix. 


- Dimensions given by $2^N$
- First order: $H_1= \left(\begin{array}{cc} 1 & 1\\ 1 & -1 \end{array}\right)$
- Second order: $H_2= \left(\begin{array}{cc} 1 & 1 & 1 & 1\\ 1 & -1 & 1 & -1\\ 1 & 1 & -1 & -1\\ 1 & -1 & -1 & 1 \end{array}\right)$
	- Can be obtained using $H_1$ using the Kronecker product $H_2 = H_1 * H_1$
		- See [[Kronecker Product]] for more information


# Old Notes
The hadamard transform $H_m$ is a $2m \times 2m$ matrix. transforming $2m$ real $xn$ to $2m$ real $Xk$. Can be defined in two ways:
- Recursively
- binary representation of the indices $n$ and $k$. 

A non-sinusoidal, orthogonal transformation technique that decomposes a signal into a set of basis functions. 
- Basis functions are Walsh functions, which are rectangular or square waves with values of +1 or -1. 
- Basis functions are a set of orthogonal, rectangular waveforms called Walsh functions. 
	- Has no multipliers and is real because of the amplitude of Walsh (or Hadamard) functions has only two values +1 or -1. 
- WHT can be used in many different applications


The fast walsh-hadamard transform is able to represent signals with sharp discontinuities more accurately using fewer coefficients than the FFT. 


Given $n$ qubits, the transform allows us to construct a quantum mechanical system, with $N = 2^n$ states. The walsh-hadamard transform $H^{\bigotimes n}$, rotates each of the $n$ qubits independently:
$H^{\bigotimes n} = H(N)$ with $N = 2^n$

- Used to create an equal superposition of qubits when the input is in the state