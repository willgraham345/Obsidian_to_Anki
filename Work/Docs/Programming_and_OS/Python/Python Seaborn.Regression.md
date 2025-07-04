---
tags: note/python
type: note
---
### Regression Plotting
```python
sns.regplot(x = "sepal_width", y="sepal_length", data=iris, ax = ax`
```
Example:
```python
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex')
 '''This will automatically separate sex into two different colors'''
```

You can also create a "grid" by passing in a column or row argument to the function:
```python
sns.lmplot(x='total_bill',y='tip',data=tips,col='sex')
'''This will create two graphs in the columns, one for each sex. '''
```