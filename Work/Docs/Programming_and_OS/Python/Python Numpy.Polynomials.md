---
tags: note/python
type: note
---

# Convenience Classes
These are 1_d numpy arrays ordered from lowest order terrm to the highest order term.
- For example, array([1,2,3]) represents `P_0 + 2*P_1 + 3*P_2`, where P_n is the n-th order basis polynomial applicable to the specific module in question:

| **Name** |**Provides** |
|---|---|
|[`Polynomial`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.html#numpy.polynomial.polynomial.Polynomial "numpy.polynomial.polynomial.Polynomial")|Power series|
|[`Chebyshev`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html#numpy.polynomial.chebyshev.Chebyshev "numpy.polynomial.chebyshev.Chebyshev")|Chebyshev series|
|[`Legendre`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.html#numpy.polynomial.legendre.Legendre "numpy.polynomial.legendre.Legendre")|Legendre series|
|[`Laguerre`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.html#numpy.polynomial.laguerre.Laguerre "numpy.polynomial.laguerre.Laguerre")|Laguerre series|
|[`Hermite`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.html#numpy.polynomial.hermite.Hermite "numpy.polynomial.hermite.Hermite")|Hermite series|
|[`HermiteE`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.html#numpy.polynomial.hermite_e.HermiteE "numpy.polynomial.hermite_e.HermiteE")|HermiteE series|

# Methods
## Constants[](https://numpy.org/doc/stable/reference/routines.polynomials.package.html#constants "Permalink to this heading")
- `Poly.domain` – Default domain
	- The values over which the fit is valid. Most of the time, this will be the independent variable within the dataset (x in an xy plot)
- `Poly.window` – Default window
- `Poly.basis_name` – String used to represent the basis
- `Poly.maxpower` – Maximum value `n` such that `p**n` is allowed
- `Poly.nickname` – String used in printing
## Creation[](https://numpy.org/doc/stable/reference/routines.polynomials.package.html#creation "Permalink to this heading")
Methods for creating polynomial instances.
- `Poly.basis(degree)` – Basis polynomial of given degree
- `Poly.identity()` – `p` where `p(x) = x` for all `x`
- `Poly.fit(x, y, deg)` – `p` of degree `deg` with coefficients determined by the least-squares fit to the data `x`, `y`
- `Poly.fromroots(roots)` – `p` with specified roots
- `p.copy()` – Create a copy of `p`

## Conversion[](https://numpy.org/doc/stable/reference/routines.polynomials.package.html#conversion "Permalink to this heading")
Methods for converting a polynomial instance of one kind to another.
- `p.cast(Poly)` – Convert `p` to instance of kind `Poly`
- `p.convert(Poly)` – Convert `p` to instance of kind `Poly` or map between `domain` and `window`
## Calculus[](https://numpy.org/doc/stable/reference/routines.polynomials.package.html#calculus "Permalink to this heading")
- `p.deriv()` – Take the derivative of `p`
- `p.integ()` – Integrate `p`

## Validation[](https://numpy.org/doc/stable/reference/routines.polynomials.package.html#validation "Permalink to this heading")
- `Poly.has_samecoef(p1, p2)` – Check if coefficients match
- `Poly.has_samedomain(p1, p2)` – Check if domains match
- `Poly.has_sametype(p1, p2)` – Check if types match
- `Poly.has_samewindow(p1, p2)` – Check if windows match

## Misc[](https://numpy.org/doc/stable/reference/routines.polynomials.package.html#misc "Permalink to this heading")
- `p.linspace()` – Return `x, p(x)` at equally-spaced points in `domain`
- `p.mapparms()` – Return the parameters for the linear mapping between `domain` and `window`.
- `p.roots()` – Return the roots of _p_.
- `p.trim()` – Remove trailing coefficients.
- `p.cutdeg(degree)` – Truncate p to given degree
- `p.truncate(size)` – Truncate p to given size



# Examples

```python
import numpy as np
from numpy.polynomial import Polynomial

# Example data
x = np.array([1, 2, 3, 4, 5])
y = np.array([6, 9, 12, 19, 24])

# Fit cubic polynomial
poly_fit = Polynomial.fit(x, y, deg=3)

# Evaluate the polynomial at specific points
x_values = np.array([1.5, 2.5, 3.5])
y_values = poly_fit(x_values)

print(y_values)  # Array of y-values for the polynomial at x_values

```




# Legacy vs Current Polynomial Objects
`from numpy.polynomial import Polynomial`

|                                                                                                                          |                                                                                                                           |                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **How to…**                                                                                                              | Legacy ([`numpy.poly1d`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html#numpy.poly1d "numpy.poly1d")) | [`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials.package.html#module-numpy.polynomial "numpy.polynomial") |
| Create a polynomial object from coefficients [[1]](https://numpy.org/doc/stable/reference/routines.polynomials.html#id2) | `p = np.poly1d([1, 2, 3])`                                                                                                | `p = Polynomial([3, 2, 1])`                                                                                                               |
| Create a polynomial object from roots                                                                                    | `r = np.poly([-1, 1])` `p = np.poly1d(r)`                                                                                 | `p = Polynomial.fromroots([-1, 1])`                                                                                                       |
| Fit a polynomial of degree `deg` to data                                                                                 | `np.polyfit(x, y, deg)`                                                                                                   | `Polynomial.fit(x, y, deg)`                                                                                                               |
