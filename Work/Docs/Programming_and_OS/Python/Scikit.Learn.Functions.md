---
tags: note/python
type: note
---
# Creating Test Data

| Function                                                                                                                              | Description                                                                                                                                          | Notes                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `sklearn.model_selection.train_test_split`(\*arrays, test_size=None, train_size=None, random_state=None, shuffle=True, stratify=None) | Splits arrays or matrices into random train and test subsets. Allowed inputs include lists, numpy arrays, scipy-sparse matrices or pandas dataframes | i.e`X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)` |




# Linear Regression
- To perform linear regression, you'll need to separate the code into both features and what you're trying to predict (i.e. dependent vs independent variables)
## LinearRegression
```python
from sklearn.linear_model import LinearRegression
// df is already intialized
X = df[['col1', 'col2', 'col3']]
y = df['OutputCol']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
lm = LinearRegression()
lm.fit(X_train, y_train)
print(lm.intercept_)
```

### Methods

| Method           | Description                                            | Notes |
| ---------------- | ------------------------------------------------------ | ----- |
| `lm.coef_`       | Grabs the coefficients for each feature in the dataset |       |
| `lm.inetercept_` | Prints intercept                                                        |       |



# Measuring Wellness of Fit
```python
from sklearn import metrics
```

| Functions                       | Description | Notes |
| ------------------------------- | ----------- | ----- |
| `metrics.mean_absolute_error()` |             |       |
| `metrics.mean_squared_error()`  |             |       |
| `metrics`                                |             |       |
