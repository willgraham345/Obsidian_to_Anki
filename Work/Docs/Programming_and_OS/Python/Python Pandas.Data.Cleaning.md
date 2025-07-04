---
tags: note/python
type: note
---
## Cleaning Data

It is likely that you will need to clean up the data if you are using real-world examples. These are a few beneficial techniques:

| Cleaning Function                                                      | Description                                                                                                        | Notes                                                                                                                                         |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `df.apply(column,axis)`                                                | Applies a function along a dataframe. Can be applied along in a column, or in a row.                               |                                                                                                                                               |
| `df.drop_duplicates()`                                                 | Remove Duplicate rows (only considers columns)                                                                     |                                                                                                                                               |
| `df.columns = ['a','b','c']`                                           | Renames columns                                                                                                    |                                                                                                                                               |
| `pd.isnull()`                                                          | Checks for null Values, Returns Boolean Array                                                                      |                                                                                                                                               |
| `pd.notnull()`                                                         | Opposite of s is null()                                                                                            |                                                                                                                                               |
| `df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=None)` | Drops all rows that contain null values                                                                            | Thresh argument is an integer, requiring however many non-NA arguments to be dropped (if a row has less NA than the thresh, it will keep it). |
| `df.dropna(axis=1)`                                                    | Drops all columns that contain null values                                                                         |                                                                                                                                               |
| `df.dropna(axis=1,thresh=n)`                                           | Drops all rows have have less than n non null values                                                               |                                                                                                                                               |
| `df.fillna(value='FILL VALUE')`                                        | Replaces all null values with `value`                                                                              |                                                                                                                                               |
| `df.fillna(x)`                                                         | Replaces all null values with x                                                                                    |                                                                                                                                               |
| `s.fillna(s.mean())`                                                   | Replaces all null values with the mean (mean can be replaced with almost any function from the statistics section) |                                                                                                                                               |
| `s.astype(float)`                                                      | Converts the datatype of the series to float                                                                       |                                                                                                                                               |
| `s.replace(1,'one')`                                                   | Replaces all values equal to 1 with 'one'                                                                          |                                                                                                                                               |
| `s.replace([1,3],['one','three'])`                                     | Replaces all 1 with 'one' and 3 with 'three'                                                                       |                                                                                                                                               |
| `df.rename(columns=lambda x: x + 1)`                                   | Mass renaming of columns                                                                                           |                                                                                                                                               |
| `df.rename(columns={'old_name': 'new_ name'})`                         | Selective renaming                                                                                                 |                                                                                                                                               |
| `df.set_index('column_one')`                                           | Changes the index                                                                                                  |                                                                                                                                               |
| `df.rename(index=lambda x: x + 1)`                                     | Mass renaming of index                                                                                             |                                                                                                                                               |

# Imputing Data
- Pandas allows you to apply a function to a dataframe. This lets us impute data, and train a model with incomplete data. The function below assigns an average age to an incomplete age column. 
```python
def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]
    if pd.isnull(Age):
        if Pclass == 1:
            return 37
        elif Pclass == 2:
            return 29
        else:
            return 24
    else:
        return Age
```

To apply the function use `df.apply(column, axis=1)`
```python
train['Age'] = train[['Age','Pclass']].apply(impute_age,axis=1)
```


# Converting Categorical Features
- We need to convert categorical features to dummy variables, otherwise the machine is unable to directly take features as inputs. 