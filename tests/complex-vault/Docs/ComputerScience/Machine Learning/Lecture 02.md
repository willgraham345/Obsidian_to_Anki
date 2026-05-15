---
type: note
---
# Representation
- Data is processed in a Batch (i.e. all of the data is available) 
- Recursively build a decision tree top down
	- Decide what attribute is at the top, and what to do for each value the root attribute takes
# Algorithm
- Learning decision trees
## ID3 Algorithm
- A greedy heuristic
- Batch Decision Tree Algorithm
- $\mathbb{S}$ = set of examples
- Attributes = set of measured attributes
1. If all examples have the same label:
	1. Return a single node tree with the label
2. Otherwise
	1. Create a `Root node` for `tree`
	2. $A$ = attribute in Attributes that *best* classifies $S$
	3. For each possible value $v$ that $A$ can take
		1. Add a new tree branch for attribute $A$ taking value $v$
		2. Let $S_v$ be the subset of examples in $S$ with $A = v$
		3. If $S_v$ is empty
			1. Add leaf node with the common value of `Label` in $S$
			2. ELSE: Below this branch add the subtree $ID3(S_v, Attributes - {A})$
		4. Return `Root node`
### Picking the Root Attribute
- The goal is to have the decision tree as small as possible
	- Finding minimal decision tree consistent with data is NP-hard
	- The recursive algorithm is a greedy heuristic search for a simple tree but cannot guarantee optimality
- The main decision in the algorithm is the selection of the next attribute to split on 
- We want attributes that split examples to sets that are relatively pure in one of the labels
	- If we pick this way, we are closer to leaf nodes
#### Example:
We have two boolean attributes $A, B$
- What should be the first attribute we select?
- ![[Pasted image 20240130110513.png]]
	- We want $A = 1, B = 1$ to be the root node
		- The idea is to make the tree as small as possible
- What if this is our feature set?
- ![[Pasted image 20240130110721.png]]
- 
### Entropy
View entropy as the number of bits required, on average, to encode information
- High entropy --> High level of uncertainty
- Low entropy --> Low uncertainty

Entropy (impurity, disorder, $H$) is a set of examples $S$ with respect to binary classification is:
$H(S) = -p_{+} log_2(p_{+}) - p_{-}log_2(p_{-})$
- $p_{+}$ = proportion of positive examples
- $p_{-}$ = proportion of negative examples

For discrete probability distribution with $K$ possible values with probabilities ${ p_1, p_2, \dots, p_k }$
$H({ p_1, p_2, \dots, p_k }) = -\sum_{i}^{K} p_i log_2p_i$
- If all examples belong to the same category, then entropy = 0
- If $p_{+} = p_{-} = 1/2$ then entropy = 1

The uniform distribution has the highest entropy

### Information Gain
The **information gain** of an attribute $A$ is the expected reduction in entropy caused by partitioning on this attribute

$Gain(S,A) = Entropy(S) - \sum_{v \in Values(a)} \dfrac{|{S_v}|}{|{S}|}Entropy(S_v)$
- $S_v$ : the subset of examples where the value of attribute $A$ is set to value $v$



