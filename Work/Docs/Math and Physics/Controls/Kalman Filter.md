---
type: note
---
# Covariance Correction Step for Kalman Filtering with an Attitude
## Background
- The Extended Kalman Filter (EKF) is a first-order approximation of an underlying nonlinear system, with the approximation evaluated at the current state estimate.
- An Unscented Kalman Filter (UKF) uses a set of deterministically chosen points that approximate the underlying distribution, and these points are transformed through nonlinear equations.
- For strongly non-linear systems, the Kalman filter may be inadequate. It can be extended to higher-order effects, but it may not work. 
## Goal of the paper
1) Propose an algorithm that allows estimation of the dynamic state of a system (where the state includes an attitude) by making use of a reference attitude and an attitude error. When based on the extended Kalman filter, the result is an extension to and correction of the MEKF and, when based on the unscented Kalman filter, it may be seen as a correction of the USQUE. The algorithm may be directly applied to systems with arbitrarily complicated dynamics including, for example, angular velocity dynamics dependent on other states. 
2) Show that the widely used method as presented in does not keep track of the estimate statistics correctly, even to the first order. 
3) Demystify the attitude reset step, deriving the first-order correction using a 3 × 3 rotation matrix.

##  Attitude Representations


## Problem and Solution
### Problem Statement
1. Estimating the dynamic state of a system using measurements
2. A model for the state dynamics
3. A model for the measurement system
4. Information about the dynamic states' initial probability distributions
### Variables
- $R$ = attitude
- $\xi \in \mathbb{R}^{\xi_n}$  = State dynamics
	- $R$ = Attitude, which can be both a rotation matrix and/or a quaternion.
		- Random variable
	- $\xi$ = State variables
		- Random variable
- Can be represented into discrete time steps $k$, with the random variable $\eta[k]$ representing process noise. 
- $\delta[k] = rot^{-1}(R[k]R_{ref}[k]^{-1})$ = Random variable representing a small attitude error parameterized through a rotation vector. 
- $R[k] = \exp(\delta[k])R_{ref}[k]$ 
	- If $R_ref[k]$ as deterministic attitude
	- Redundant so to avoid singularities and constraints in attitude representations
### Dynamic Equations
#### System Dynamics
$x[k] = f(k-1, x[k-1], R_{ref}[k-1], \eta[k-1])$ 
- $x[k]$ is the stochastic state
- $R_{ref}[k]$ is reference attitude
- $R_{ref}[k-1]$ is a constant, and changes in attitude affect components of $\delta[k]$ and $x[k]$

#### Measurement Equations
$z[k] = h(k, x[k], R_ref[k], \zeta[k])$ 


### Steps of Kalman Filter
1. Kalman prediction step that uses process to propagate estimate through the dynamics. During this step, the reference attitude is unchanged.
2. Prediction reset step, where reference attitude is changed such that the estimate of the post-reset attitude error equals zero (it's FAR from singularities)
3. Kalman measurement update that uses the measurement model to correct the estimate with a given estimate. During this step, the reference attitude is again unchanged
4. Measurement reset step, where again the reference attitude is adapted such that the estimate of the post-reset attitude is reset to zero
5. 