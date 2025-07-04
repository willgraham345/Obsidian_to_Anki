---
tags: note/python
type: note
---
# Description
KNN = k nearest neighbors
Has a training algorithm and a prediction algorithm.
- Training stores all data
- Prediction:
  1. Calculates distance from $x$ to all points in data
  2. Sort points in data by increasing distance from $x$
  3. Predict the majority label of the $k$ closest points


# Example
```python
from sklearn.preprocessing import StandardScalar
scaler = StandardScaler()

scaler.fit(df) ## Fitting to data


scaled_features = scalar.transform(df)
```

