---
tags: note/python
type: note
---
- Built off of Matplotlib, where a visualization will be built from a dataframe method.
- Remember, if you import `seaborn as sns`, plots will look a bit nicer

## Visualization Methods

| Method                                               | Description                                            | Notes                                                 |
| ---------------------------------------------------- | ------------------------------------------------------ | ----------------------------------------------------- |
| `df.hist()`(column, by, grid, xlabelsize, xrot, ...) | Make a histogram of the DataFrame's columns.           |                                                       |
| `df.plot(kind='plotKind')`                           | Will plot dataframe, based on the `plotKind` parameter |                                                       |
| `df.plot.area()`                                     | Area plot                                              |                                                       |
| `df.plot.bar(stacked=False)`                         | Bar plot                                               |                                                       |
| `df.plot.line(x = df.index, y = 'string, figsize)`   |                                                        | You can add matplotlib arguments/commands within that |
| `df.plot.scatter(x='a', y='b')`                      |                                                        |                                                       |


## Visualization Graphs
- See [[Python Seaborn]] for a full list of visualizations

| Method                            | Description                                                                | Notes |
| --------------------------------- | -------------------------------------------------------------------------- | ----- |
| `sns.pairplot(df)`                  | Generates histograms, and correlation plots with all columns. REALLY cool. |       |
| `df.heatmap(df.corr(), annot=True)` | Makes a nice heatmap for you                                                                           |       |


