---
tags: note/python
type: note
---
## Exploring Data

Following the import of your information into a Pandas data frame, you can [visualize the data](https://www.simplilearn.com/data-visualization-article) using the following techniques:

| Data Exploring                   | Description                                                               |
| -------------------------------- | -------------------------------------------------------------- |
| df.shape()                       | Prints the number of rows as well as columns in a data frame   |
| df.head(n)                       | Prints first n rows of the DataFrame                           |
| df.tail(n)                       | Prints last n rows of the DataFrame                            |
| df.info()                        | Index, Datatype, and Memory details                            |
| df.describe()                    | Summary statistics for numerical columns                       |
| s.value_counts(dropna=False)     | Views unique values and counts                                 |
| df.apply(pd.Series.value_counts) | Unique values and counts for every columns                     |
| df.describe()                    | brief statistics for numerical columns                         |
| df.mean()                        | Returns the mean of every columns                              |
| df.corr()                        | Returns the correlation between columns in a DataFrame         |
| df.count()                       | Returns the number of non-null values in each DataFrame column |
| df.max()                         | Returns the biggest value in every column                      |
| df.min()                         | Returns the lowest value in every column                       |
| df.median()                      | Returns the median of every column                             |
| df.std()                         | Returns the standard deviation of every column                 |
