---
type: note
---
The badges game


Formalized supervised Learning
- Instance Space and Features
## Instances and Labels
Instance Space 
- Set of examples that need to be classified
- $\mathbb{X}$
Label Space
- Set of all possible labels
- $\mathnormal{Y}$
- e.g. {Spam, Notspam}; {+, -}
Target function -> $y = f(x)$
- The goal of learning is to find this function
Learned function: $y = g(x)$
Learning algorithm only sees examples of $f$ in action


## Supervised Learning
Given: Training examples of the form: $(x, f(x))$
- Typically the input $x$ is represented as **feature vectors** 
	- $x \in {0,1}^d$  or $x \in \mathbb{R}^d$
		- $d$ = d dimensional vectors
### Label determines what kind of problem we have
#### Binary classification
- label space = {-1, 1}
- examples:
	- Spam filtering, recommendation systems, anomaly detection, authorship identification, time series predictions (stocks)
#### Multiclass Classification
- Label space = {1, 2, 3, ..., K}

#### Regression
- Label space = $\mathbb{R}$
### Things we need to know for Supervised Learning
- Instance space?
	- Inputs? Features?
- Label space?
	- What is the prediction task?
- Hypothesis Space?
	- Functions should the learning algorithm search over?
- Learning Algorithm?
	- How do we learn from labeled data?
- Loss function or evaluation metric?
	- What is success?


## Instance Space $\mathbb{X}$
Instances $x \in \mathbb{X}$ are defined by features and attributes
- Features can be boolean, or real valued,
- Features can be hand crafted or learned themselves
![[Screenshot from 2024-01-30 10-37-30.png]]

- Features are to capture all the information needed for a learned system to make its prediction
- Not all information is necessary or relevant
Each $x \in \mathbb{X}$ is a feature vector

When designing feature functions, think of feature vectors as templates

![[Pasted image 20240130104024.png]]


## Label Space $\mathbb{Y}$
Classification
- Outputs are categorical
	- Binary: Two possible labels
	- Multiclass: K possible labels
	- Structured: Graph valued outputs (covered in a different class)
- Output space can be numerical/ordinal
	- Regression
		- Label space $\mathbb{Y}$ is the set (or subset) of real numbers
	- Ranking
		- Labels are ordinal (there is an ordering of the labels)
			- A yelp 5 star review is slightly different than a 4 star review, but VERY different than a 1 star review 
## Hypothesis Space
Learning is search over functions
- Hypothesis is to restrict the search space
	- The set of possible functions we consider

Simple conjunctions: 
M-of-n rules: 
- pick a set of n variables. At least m of them must be true
- Pick a subset with $n$ variables. The label $y = 1$ if at least $m$ of them are 1

General strategy
Pick an expressive hypothesis space expressing concepts
- Concept = the target classifier that is hidden from us. Sometimes we call it the oracle. 
- Example hypothesis spaces:
	- Decision trees, linear functions, grammars, multi-layer perception, transformer networks, convolutional neural networks
	- Develop algorithms that find an element the hypothesis space that fits data well (or well enough)
	- Hope that it generalizes
	