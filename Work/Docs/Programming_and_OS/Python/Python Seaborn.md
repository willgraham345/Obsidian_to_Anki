---
tags: note/python
type: note
---
# Description
Seaborn is a statistical plotting library, designed to work well with pandas dataframe objects. It can also accept other data types, but it's oriented towards data science.

# Examples
## ScatterPlot
``` python
sns.scatterplot(x=y_test,y=lm.predict(x_test))
plt.xlabel('Y Test')
plt.ylabel('Predicted Y')
```
## Residual Plot

Below both do the same thing
```python
sns.residplot(data=mpg, x="weight", y="displacement")
```
or
```python
sns.residplot(data=mpg, x="horsepower", y="mpg")
```

Adding extra terms
```python
sns.residplot(data=mpg, x="horsepower", y="mpg", order=2)
```

Adding lowess term (helps visualize trends in the residuals)