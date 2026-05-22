$X(k)$ = Fourier coefficients of $x(n)$


The computational problem for the DFT is to compute the sequence of $\{X(k)\}$ of $N$ complex-valued numbers given another sequence of data $\{x(n)\}$ of length $N$


For each value of $k$, direct computation of $X(k)$ involves N complex multiplications ($4N$ real multiplications) and $N-1$ complex additions. To compute all $N$ values of the DFT requires $N^2$ complex multiplications and $N^2 - N$ complex additions. 
- We can exploit symmetry and periodicity properties of the phase factor $W_N$

## Radix-4 vs Radix-2
One radix-4 buttefly contains 4 radix-2 butterflies. Two butteflies in one pass and two butterflies in the following apss. 

## Radix-2 FFT Algorithms
Considering the computation of the $N = 2^v$ point DFT with dividing and conquering. We can split the N-point data sequence into two $N/2$ point data sequences $f_1(n), f_2(n)$  which correspond to the even-numbered and odd-numbered samples of $x(n)$
- $f_1(n) = x(2n)$
- $f_2(n) = x(2n + 1), n = 0, 1, \dots , N/2 - 1$

$f_1(n)$ and $f_2(n)$ are obtained by decimating $x(n)$ by a factor of 2. Now we can call it an N-point DFT. 