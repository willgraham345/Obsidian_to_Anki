---
type: note
---
The tough part of machine learning isn't finding a formula. The difficult part is determining if the formula is the "correct" formula

# What is Learning?
Learning:
- First defined in 1959
	- Talks about the differences between rote learning and generalization
- Programming computers to learn from experience
- "Learning denotes changes in the system that are adaptive in the sense that they enable the system to do the task or tasks drawn from the same population more effectively next time"


AI is a broader topic than machine learning. 
- AI is a collection of problems
	- Seeing, smelling, hearing, talking


Learning Algorithms
Online algorithms
- Learner can only access one labeled at a time
	- Perception winnow
Batch Algorithms
- Learner can access the entire dataset
	- Naive Bayes
	- Support Vector machines, logistic regression, neural networks
	- Decision trees and nearest neighbors
	- Boosting
Unsupervised/semi-supervised algorithms
- Expectation maximization
- K-means


# Representing Data
What is the best way to represent data for a particular task
- Right features
- Learning such features from data
- Dimensionality reduction


# Theory of Machine Learning
Online learning: Learner sees examples in a stream and stop making mistakes as we go along (or minimize regret in our decisions)

Probably Approximately Correct (PAC) Learning: After seeing a collection of examples, the learner will (with high probability) produce a function that makes small error

Bayesian Learning: Based on our observations, what is the probability distribution over possible functions that produced the data?


# What is this course about?
Focuses on underlying concepts and algorithmic ideas in the field of machine learning

NOT about
- Using a specific machine learning tool/framework
- Any single learning paradigm


# Course Logistics
Course website

Everything else will be on canvas



# Terminology
Model = function that a learner learns (decision trees, linear classifiers, non-linear classifiers, neural networks, kernels, ensembles of classifiers)

## Different Learning Protocols
Supervised learning
- A teacher supplies a collection of examples with labels
- The learner has to learn to label new examples using this data
Unsupervised learning
- No teacher, learner has only unlabeled examples
- Data mining
Semi-supervised learning
- Learner has access to both labeled and unlabeled examples
Active learning
- Learner and teacher interact with each other
- Learner can ask questions
Reinforcement learning
- Learner learns by interacting with the environment


## Learning Algorithms
Online algorithms
- Learner can access only one labeled at a time
	- Perceptron Winnow
Batch Algorithms
- Learner can access the entire data set
	- Naive Bayes Support
	- Vector machines, logistic regression, neural networks
	- Decision trees and nearest neighbors
	- Boosting
Unsupervised/semi-supervised algorithms
- Expectation maximization
	- K-Means
	- This may be a black box that we've used in the past


## The theory of machine learning
Online Learning
- Learner sees examples in a stream and stops making mistakes as we go along (or minimizes regret in our decisions)
Probably Approximately Correct (PAC) Learning
- After seeing a collection of examples, the learner will (with high probability)
Bayesian Learning
- Based on our observations, what is the probability distribution over possible functions that produced the data