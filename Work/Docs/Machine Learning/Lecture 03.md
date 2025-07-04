---
type: note
---
Supervised learning: instances, concepts, and hypotheses
Specific learners
- Decision trees
General ML ideas
- Features as high dimensional vectors
- Overfitting


# Linear Models
## Intro
Restrict search space
Linear classifciation is about predicting a discrete class label
Simplicity vs accuracy
### Example
Suppose we want to determine whether a robot arm is defective or not using two measurements:
- Max angle the robot arm can reach $d$
- Max angle it can rotate $a$
Suppose we have a linear decision rule that predicts defective if $2d + 0.01a \geq 7$
- This is a linear classifier
- Inputs are $d$ dimensional feature vectors denoted by $x$
	- Output is a label $y \in {-1, 1}$
Linear Threshold Units classify an example $x$ using parameters $\mathbb{w}$ (a $d$ dimensional vector) and $b$ (a real number) according to the following classification rule
- $b$ = bias term
$Output = sign(\mathbb{w}^T\mathbb(x) + b) = sign(\sum_{i}w_ix_i + b)$
- if $\mathbb{w}^T\mathbb{x} + b \leq 0$  --> predict $y = 1$
- if $\mathbb{w}^T\mathbb{x} + b < 0$  --> predict $y = 1$

## Geometry
![[Pasted image 20240130122751.png]]
## Notational Simplification
We can stop writing $b$ at each step using notiational sugar
$sgn(\mathbb{w}^T\mathbb{x} + b) = sgn(\sum_iw_ix_i + b)$

Rewrite $\mathbb{x}$ as $\begin{bmatrix} x \\ 1 \end{bmatrix}$. Call this $x'$
Rewrite $\mathbb{w}$ as $\begin{bmatrix} w \\ 1 \end{bmatrix}$. Call this $w'$

$w^Tx + b$ is the same as $w'^Tx'$
- Increases dimensionality by 1
- Equivalent to adding a feature that is always constant
Prediction function is now $sgn(w'^Tx')$
- In this increase dimensional space, the vector $w'$ goes through the origin
	- We sometimes hide the bias $b$, and instead fold the bias term into the weights by adding an extra constant feature. *Remember it is there*

## Learning Linear Classifiers
## Functions that Linear Classifiers Express

