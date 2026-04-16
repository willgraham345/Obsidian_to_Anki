---
type: note
---
# Abstract
- DL = deep learning = RL = research learning
	- Gold standard in ML community. 
	- Can learn massive amounts of data
- Has a list of computational tools
	- FPGA, GPU, CPU
	- summarized with description of their influence on DL

# Intro
- Several types of features were introduced and compared in Computer vision context
	- HOG = histogram of oriented gradients
	- SIFT = Scale invariant feature transform
	- BoW = bag of words
	- These algorithms have a multi-layer data representation architecture
		- First levels extract low-level features, last levels extract high-level features
- CNN = convolutional neural network
	- Automatically detects significant features without any human supervision
- When to apply deep learning:
	- Human experts not available
	- Humans unable to explain decisions made using their expertise (languages, medical decisions, speech recognition)
	- Problem solution updates over time (price prediction, stock preference, weather prediction, tracking)
	- Solutions require adaptation based on specific cases (personalization, biometrics)
	- Cases where size of the problem is extremely large and exceeds our inadequate reasoning abilities (sentiment analysis, matching ads to Facebook, calculation webpage ranks)
# Types of DL Approaches
- Classified into three major categories: unsupervised, partially supervised, and supervised. Deep reinforcement learning (DRL, or RL), is another type typically considered to fall into partially supervised and sometimes unsupervised
## Deep supervised learning
- Labeled data
- Collection of inputs and resultant outputs $(x_t, y_t) \sim \rho$ 
- Learning techniques include:
	- RNN = recurrent neural network
		- GRU = gated recurrent units
		- LSTM = long short-term memory
	- CNN = convolutional neural network
	- DNN = deep neural netwrok
	- 
- Advantages:
	- Ability to collect data or generate a data output from the prior knowledge
- Disadvantage:
	- Decision boundary might be overstrained hen training set doesn't own samples that should be in a class. 

## Deep semi-supervised learning


# Computational Approaches
- GPU is built to do multiple parallel instructions. 
- CPU is really nice, but lacks the ability to match GPUs and FPGAs in unprocessed computational facilities.
- GPUS