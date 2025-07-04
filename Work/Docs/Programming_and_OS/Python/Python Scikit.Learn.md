---
tags: note/python
type: note
---
## General Outline
- Every algorithm in scikit-learn is exposed via an "estimator"

```python
from sklearn.family import Model
% i.e. from sklearn.linear_model import LinearRegression
```

Available in all estimators:
- `model.fit()`: fit training data
- For supervised learning applications, this accepts two arguments, data $X$ and labels $y$
	- 	- `model.fit(X,y)`
- For unsupervised learning applications, this accepts only a single argument, the data $X$i
	- `model.fit(X)`

Available in supervised estimators
- `model.predict()`: given a trained model, predict the label of a new set of data. Accepts one argument, the new data $X_{new}$
	- i.e. `model.predict(X_new)`
- `model.score()`: for classification or regression problems, most estimators implement a score method. Scores are between 0 and 1, with a larger score indicating a better fit.

Available in unsupervised estimators
- `model.predict()`:  predict labels in clustering algorithms
	- i.e. `model.predict(X_new)`
- `model.transform()`: given an unsupervised model, transform new data into the new basis. Also accepts one argument $X_{new}$


Algorithm Cheat Sheet
![[Pasted image 20230629123258.png]]