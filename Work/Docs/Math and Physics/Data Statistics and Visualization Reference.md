---
type: note
---


# Data
## Types of Data
- Numerical
	- Discrete
	- Continuous
- Ordinal/Categorical
	- Nominal (regular)
		- i.e. fish or bird
	- Ordinal (ordered)
		- i.e. Height, happiness level

## Data Fitting
Tools we have to fit different types of data
- Numerical Data
	- Linear regression
- Categorical data:
	- Binary Logistic regression
	- KNN model = K Nearest Neighbors (algorithm for classification problems)

# Visualization 
Input types on Horizontal, output types on vertical
## Simple Chart Guide
|Basic Chart Guide         |               |              |                                     |
| ------- | ------------- | ------------ | ----------------------------------- |
|         |               | Output       |                                     |
|         |               | *Continuous* | *Proportion*                        |
| Input | *Numerical*   | Scatterplot  | Histogram                           |
|         | *Categorical* | Box+Whisker  | Contingency Table/Non Histogram Bar |

| Plot Type    | Best Use Case                                                                                                                                                   | Notes                            |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| Bar Chart    | One or more text categorical variable, or one numerical variable                                                                                                | Not great, avoid it              |
| Line Chart   | Visualizing continuous and temporal data. One or more categorical variable on the horizontal, and one or more numerical variable on the y axis                  | Better than bar if you can do it |
| Scatter Plot | Two numerical variables. You can add a third variable to change color or size of dots                                                                           |                                  |
| Cluster Map  | A clustered version of the heatmap. It will "cluster" a heatmap together, with variables out of order, but with a hierarchical tree diagram off of y and x axis | Can also have                    |
| Grid Plots   | Can plot 2 categorical variables on x and y, with continuous data within the individual grid places                                                             | This can also have multiple plot types on each grid. REALLY useful.                                  |
|              |                                                                                                                                                                 |                                  |


## Matrix Charts
| Chart Type | Best Use                                                              | Notes |
| ---------- | --------------------------------------------------------------------- | ----- |
| Heat map   | Two variables that are continuous, with a third variable as the color |       |
A good resource
https://guides.lib.uoguelph.ca/c.php?g=700755&p=4976238


# KNN Description
Has a training algorithm and a prediction algorithm.
- Training stores all data
- Prediction:
  1. Calculates distance from $x$ to all points in data
  2. Sort points in data by increasing distance from $x$
  3. Predict the majority label of the $k$ closest points
### Pros
- Simple
- Training is trivial
- Works with any number of classes
- Easy to add data
- Few parameters ($k$, $distance$)
### Cons
- High prediction cost (worse for large data sets)
- Not good at higher dimensional data
- Categorical features don't fit well