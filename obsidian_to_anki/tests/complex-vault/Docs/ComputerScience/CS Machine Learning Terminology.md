---
type: note
---
# Definitions
- **Accuracy** = Number of correction predictions divided by total number of predictions
	- Not a good choice with unbalanced classes
- **Classification** = A model attempting to predict categorical values
- **Confusion Matrix** = Precited values compared to real values
- | True 
- **F1 Score** = Harmonic mean of precision and recall, taking both metrics into account
	- $F_1 = 2*\dfrac{precision*recall}{precision+recall}$
	- This punishes extreme values
- **Mean Absolute Error (MAE)** = Mean of the absolute value of errors. Does not punish large outliers.
- **Mean Squared Error (MSE)** = Mean of the squared errors. Larger errors are noted more with MSE. Unfortunately, our mean will also square the units of the error
- **Precision** = Ability of a classification model to identify only relevant data types
	- Number of true positives divided by the number of true positives plus the number of false positives 
	- Ability to find all relevant instances in a dataset
- **Recall** = ability of a model to find all relevant cases within a dataset. 
	- Formally, it is the number of true positives divided by the number of true positives plus the number of false negatives
	- Proportion of the data points our model said were relevant, that actually were relevant
- **Regression** = A task when a model attempts to predict continuous values 
	- Common metrics include: mean absolute error, mean squared error, root mean square error 
- **Root Mean Square Error (RMSE)** = Root of the mean of the squared errors. It's the most popular, because it has the same units as your truth values

# Data Types
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
		- Can have multiple predictors, using multiple logistic regression
		
	- KNN model = K Nearest Neighbors (algorithm for classification problems)


# Classification 
## Logistic Regression 
- One predictor, binary prediction
## Multiple logistic regression
### Description
- Multiple predictors with a binary prediction
- Negative coefficients mean an inverse correlation. 

### Formula:
	- $p(X) = \dfrac{e^{\beta_0 + \beta_1X_1 + \ldots + \beta_pX_p}}{1+e^{\beta_0 + \beta_1X_1 + \ldots + \beta_pX_p}}$
## Multinomial Logistic Regression
### Description
- We first select a single class to serve as the baseline, without a loss of generality, we select the Kth class for this role. Then we replace the Multiple Logistic Regression model.
- The general idea is that you hold one variable constant, predict it against the other variables, and then redo the whole thing so every variable is kept constant. 
	- Interpretation of coefficients in a multinomial logistic regression model is tied to choice of baseline. As such, it must be interpreted with caution. 
### Formula
- $Pr(Y=k|X = x) = \dfrac{e^{\beta_{k0} + \beta_{k1}x_1 + \ldots + \beta_{kp}x_p}}{1+\sum_{l=1}^{K-1} e^{\beta_{l0} + \beta_{l1}x_1 + \ldots + \beta_{lp}x_p}}$
### Softmax coding
- An equal but alternative coding for multinomial logistic regression. Used extensively in machine learning literature. Rather than selecting a baseline class, we treat all $K$ classes symmetrically, and assume that for $k=1,\ldots, K,$
- $Pr(Y=k|X = x) = \dfrac{e^{\beta_{k0} + \beta_{k1}x_1 + \ldots + \beta_{kp}xp}}{\sum_{l=1}^{K} e^{\beta_{l0} + \beta_{l1}x_1 + \ldots + \beta_{lp}x_p}}$
	- Rather than estimating coefficients for $K-1$ classes, we estimate coefficients for all $K$ classes. 

## Generative Models for Classification 
### Description
- Logistic regression models the conditional distribution of the response $Y$ given the predictor(s) $X$. Instead, we model distribution of the predictors $X$ separately in each of the response classes. We then uses Bayes' theorem to flip these aroudn into estimates for $Pr(Y = k | X = x)$. When distribution of $X$ is assumed to be normal, it turns out this is very similar to logistic regression. 
	- Warnings: 
		- When substantial separation is between two classes, the parameters can become unstable.
		- If distribution of predictors $X$ is approximately normal in each of the classes and small