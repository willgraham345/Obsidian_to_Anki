---
type: note
tags: note/Latex
---
# Latex
## Arrows
| TERM                 | LATEX             |
| -------------------- | ----------------- |
| 1. Left Arrow        | `\leftarrow`      |
| 2. Up Arrow          | `\uparrow`        |
| 3. Right Arrow       | `\rightarrow`     |
| 4. Down Arrow        | `\downarrow`      |
| 5. Left Right Arrow  | `\leftrightarrow` |
| 6. South West Arrow  | `\swarrow`        |
| 7. Up Down Arrow     | `\updownarrow`    |
| 8. North West Arrow  | `\nwarrow`        |
| 9. North East Arrow  | `\nearrow`        |
| 10. South East Arrow | `\searrow`        |
## Fractions


| Description                                   | Command            | Output                  |
| --------------------------------------------- | ------------------ | ----------------------- |
| Build a fraction like so: \frac{1}{2}         | `\frac`            | $\frac{1}{2}$           |
| You can nest fractions: \frac{\frac{1}{2}}{2} | `\frac{\frac{}}{}` | $\frac{\frac{1}{2}}{2}$ | 
## Greek Letters
#### (capitalize by capitalizing the command)
| Description | Command    | Output     |
| ----------- | ---------- | ---------- |
| alpha       | `\alpha`   | α          |
| beta        | `\beta`    | β          |
| gamma       | `\gamma`   | γ          |
| delta       | `\delta`   | δ          |
| epsilon     | `\epsilon` | ϵ          |
| zeta        | `\zeta`    | ζ          |
| eta         | `\eta`     | η          |
| theta       | `\theta`   | θ          |
| iota        | `\iota`    | ι          |
| kappa       | `\kappa`   | κ          |
| lambda      | `\lambda`  | λ          |
| mu          | `\mu`      | μ          |
| nu          | `\nu`      | ν          |
| xi          | `\xi`      | ξ          |
| omicron     | `\omicron` | $\omicron$ | 
| pi          | `\pi`      | π          |
| rho         | `\rho`     | ρ          |
| sigma       | `\sigma`   | σ          |
| tau         | `\tau`     | τ          |
| upsilon     | `\upsilon` | υ          |
| phi         | `\phi`     | ϕ          |
| chi         | `\chi`     | χ          |
| psi         | `\psi`     | ψ          |
| omega       | `\omega`   | $\omega$   |

## Logic
| Description | Command   | Output |
| ----------- | --------- | ------ |
| For all     | `\forall` | ∀     |
| Exists      | `\exists` | ∃     |
| Or          | `\lor`    | ∨     |
| And         | `\land`   | ∧     |
| Xor         | `\veebar` | ⊻     |
| Not         | `\neg`    | ¬      |

## Math
| Description | Command | Output |
| ---- | ---- | ---- |
| Absolute Value | `\|` | $\|$ |
| Sum | `\sum_{k=1}^{infty}` | $\sum_{k=1}^{\infty}$ |

## Matrix
| Type                        | LATEX markup                                                | Rendering                                                   |
| --------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| Plain                       | `\begin{matrix}   1 & 2 & 3\\   a & b & c   \end{matrix}`   | $\begin{matrix}   1 & 2 & 3\\   a & b & c   \end{matrix}$   |
| Parentheses; round brackets | `\begin{pmatrix}   1 & 2 & 3\\   a & b & c   \end{pmatrix}` | $\begin{pmatrix}   1 & 2 & 3\\   a & b & c   \end{pmatrix}$ |
| Brackets; square brackets   | `\begin{bmatrix}   1 & 2 & 3\\   a & b & c   \end{bmatrix}` | $\begin{bmatrix}   1 & 2 & 3\\   a & b & c   \end{bmatrix}$ |
| Braces; curly brackets      | `\begin{Bmatrix}   1 & 2 & 3\\   a & b & c   \end{Bmatrix}` | $\begin{Bmatrix}   1 & 2 & 3\\   a & b & c   \end{Bmatrix}$ |
| Pipes                       | `\begin{vmatrix}   1 & 2 & 3\\   a & b & c   \end{vmatrix}` |         $\begin{vmatrix}   1 & 2 & 3\\   a & b & c   \end{vmatrix}$                                                    |
| Double pipes                | `\begin{Vmatrix}   1 & 2 & 3\\   a & b & c   \end{Vmatrix}` |   $\begin{Vmatrix}   1 & 2 & 3\\   a & b & c   \end{Vmatrix}$                                                          |

## Operators
| Description        | Command      | Output       |
| ------------------ | ------------ | ------------ |
| Times              | `\times`     | ×            |
| Dot                | `\cdot`      | ⋅            |
| Division           | `\div`       | ÷            |
| Plus minus         | `\pm`        | ±            |
| Cross Product      | `\times`     | $\times$     |
| Big o Times        | `\bigotimes` | $\bigotimes$ |
| Kronecker Product  | `\otimes`    | $\otimes$    |
| Caret (XOR gatess) | `^\wedge`    | $^\wedge$             |


## Relation
| Description           | Command   | Output |
| --------------------- | --------- | ------ |
| Not equal             | `\neq`    | ≠      |
| Approximately equal   | `\approx` | ≈      |
| Less than or equal    | `\leq`    | ≤      |
| Greater than or equal | `\geq`    | ≥      |
| Much less than        | `\ll`     | ≪      |
| Much greater than     | `\gg`     | ≫      | 



## Sets
| TERM                        | LATEX       | Description                                                                                                                                                                                  | Image         |
| --------------------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| 1. empty set                | \varnothing |                                                                                                                                                                                              | $\varnothing$ |
| 2. set of natural numbers   | \mathbb{N}  | Counting numbers (i.e. 0, 1, 2, ...)                                                                                                                                                         | $\mathbb{N}$  |
| 3. set of integers          | \mathbb{Z}  | Whole numbers, including negative numbers                                                                                                                                                    | $\mathbb{Z}$  |
| 4. set of rational numbers  | \mathbb{Q}  | All numbers which can be written as fractions                                                                                                                                                | $\mathbb{Q}$  |
| 5. set of algebraic numbers | \mathbb{A}  | A number must be a root of a non-zero polynomial equation with rational coefficients. All integers and rational numbers are algebraic, but an irrational number may or may not be algebraic. | $\mathbb{A}$  |
| 6. set of real numbers      | \mathbb{R}  | The set of rational numbers with the set of irrational numbers adjoined                                                                                                                      | $\mathbb{R}$  |
| 7. set of complex numbers   | \mathbb{C}  | A number which can be written in the form $a + bi$ and $a$ and $b$ are real numbers and $i$ is the square root of -1                                                                         | $\mathbb{C}$  |
| 8. is member of             | \in         |                                                                                                                                                                                              | $\in$         |
| 9. is not member of         | \notin      |                                                                                                                                                                                              | $\notin$      |
| 10. owns (has member)       | \ni         |                                                                                                                                                                                              | $\ni$         |
| 11. is proper subset of     | \subset     |                                                                                                                                                                                              | $\subset$     |
| 12. is subset of            | \subseteq   |                                                                                                                                                                                              | $\subseteq$   |
| 13. is proper superset of   | \supset     |                                                                                                                                                                                              | $\supset$     |
| 14. is superset of          | \supseteq   |                                                                                                                                                                                              | $\supseteq$   |
| 15. set union               | \cup        |                                                                                                                                                                                              | $\cup$        |
| 15. set intersection        | \cap        |                                                                                                                                                                                              | $\cap$        |

## Super-/Subscript (Exponents / Indices)
| Command | Description                                          | Output |
| ------- | ---------------------------------------------------- | ------ |
| `^`     | Use ^ for superscript. Example: x^2                  | $x^2$  |
| `^{}`   | Use ^{} for exponents with >1 digit. Example: x^{10} | $x^{3}$       |
| `_`     | Use _ for subscript. Example: x_0                    |   $x_0$     |
| `_{}`   | Use _{} for subscript with >1 digit. Example: x_{10} |     $x_{10}$   |

## Others

| Command         | Description | Output         |
| --------------- | ----------- | -------------- |
| `\infty`        | Infinity    | ∞              |
| `\partial`      | Partial     | ∂              |
| `\hat{}`        | Estimator   | $\hat{\theta}$ |
| `\sqrt[root]{}` | Square root | $\sqrt[3]{4}$  |
| `\cdots\`       | Ellipses    | $\cdots$                |
