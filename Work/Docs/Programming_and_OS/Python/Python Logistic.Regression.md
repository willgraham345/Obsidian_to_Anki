---
tags: note/python
type: note
---
# Description
Solves categorization problems through use of the Sigmoid function (a.k.a. Logistic function)
- $\phi(z) = \dfrac{1}{1 + e^{-z}}$ 
	- Takes in any input, and outputs it to be between 0 and 1
	- We can use this to set cutoff points. 
- We can take a linear regression solution and place it into the Sigmoid function to create a logistic model 

We use a confusion matrix to evaluate our model with the terminology:
- TP = true positive
- TN = true negative
- FP = false positive (Type 1 error)
- FN = false negative (Type 2 error)

# Training and Predicting
```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)

predictions = logmodel.predict(X_test)

print(classifications_report(y_test, predictions))
```