---
tags: note/python
type: note
---
# Important Note
**This is the older version of numpy's fitting capability. See [[Python Numpy.Polynomials]] for better information.**

### yntax and parameters of NumPy polyfit

Below is the syntax of the polyfit method in numpy.

```python
numpy.polyfit( x , y , deg , rcond = None , full = False, w = None, cov = False)
```

Parameters:
- **x**array_like, shape (M,)
	- x-coordinates of the M sample points `(x[i], y[i])`.
- **y**array_like, shape (M,) or (M, K)
	- y-coordinates of the sample points. Several data sets of sample points sharing the same x-coordinates can be fitted at once by passing in a 2D-array that contains one dataset per column.
- **deg**int
	- Degree of the fitting polynomial
- **rcond**float, optional
	- Relative condition number of the fit. Singular values smaller than this relative to the largest singular value will be ignored. The default value is len(x)*eps, where eps is the relative precision of the float type, about 2e-16 in most cases.
- **full**bool, optional
	- Switch determining nature of return value. When it is False (the default) just the coefficients are returned, when True diagnostic information from the singular value decomposition is also returned.
- **w**array_like, shape (M,), optional
	- Weights. If not None, the weight `w[i]` applies to the unsquared residual `y[i] - y_hat[i]` at `x[i]`. Ideally the weights are chosen so that the errors of the products `w[i]*y[i]` all have the same variance. When using inverse-variance weighting, use `w[i] = 1/sigma(y[i])`. The default value is None.
- **cov**bool or str, optional
	- If given and not _False_, return not just the estimate but also its covariance matrix. By default, the covariance are scaled by chi2/dof, where dof = M - (deg + 1), i.e., the weights are presumed to be unreliable except in a relative sense and everything is scaled such that the reduced chi2 is unity. This scaling is omitted if `cov='unscaled'`, as is relevant for the case that the weights are w = 1/sigma, with sigma known to be a reliable estimate of the uncertainty.

Returns:
- **p**: ndarray, shape (deg + 1,) or (deg + 1, K)
	- Polynomial coefficients, highest power first. If _y_ was 2-D, the coefficients for _k_-th data set are in `p[:,k]`.
		- residuals, rank, singular_values, rcond
		- These values are only returned if `full == True`	
		- residuals – sum of squared residuals of the least squares fit
		- rank – the effective rank of the scaled Vandermonde
		    - coefficient matrix
		- singular_values – singular values of the scaled Vandermonde
		    - coefficient matrix
		- rcond – value of _rcond_.
- **V**: ndarray, shape (M,M) or (M,M,K)
- Present only if `full == False` and `cov == True`. The covariance matrix of the polynomial coefficient estimates. The diagonal of this matrix are the variance estimates for each coefficient. If y is a 2-D array, then the covariance matrix for the _k_-th data set are in `V[:,:,k]`