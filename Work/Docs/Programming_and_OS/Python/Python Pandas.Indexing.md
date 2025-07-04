---
tags: note/python
type: note
---
## Indexing

| Selecting          | Description                                                                                                                            |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| `df[col]`          | Returns column with label col as Series                                                                                                |
| `df[[col1, col2]]` | Returns Columns as a new DataFrame                                                                                                     |
| `s.iloc[0]`        | Selection by position (selects first element)                                                                                          |
| `s.loc[0]`         | Selection by index (selects element at index 0)                                                                                        |
| `df.iloc[0,:]`     | First row                                                                                                                              |
| `df.iloc[0,0]`     | First element of first column                                                                                                          |
| `df.set_index(col1)`   | Sets the index to a chosen column                                                                                                                                       |
| `df.reset_index()` | Resets index to numbers to default of integer. Does NOT occur inplace unless `inplace=True`. This turns our index into another column. |
 