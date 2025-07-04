---
tags: note/python
type: note
---
# Dataframes
- Dataframes are the building block of pandas, and are built on numpy arrays. Think of an excel spreadsheet, but python's much better version. 
```python
pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=None)
```

- Dict can contain Series, arrays, constants, dataclass or list-like objects. If data is a dict, column order follows insertion-order. If a dict contains Series which have an index defined, it is aligned by its index. This alignment also occurs if data is a Series or a DataFrame itself. Alignment is done on Series/DataFrame inputs.
- If data is a list of dicts, column order follows insertion-order.

- **index**: Index or array-like
	- Index to use for resulting frame. Will default to RangeIndex if no indexing information part of input data and no index provided.
- **columns**: Index or array-like
	- Column labels to use for resulting frame when data does not have them, defaulting to RangeIndex(0, 1, 2, …, n). If data contains column labels, will perform column selection instead.
- **dtype**: dtype, default None
	- Data type to force. Only a single dtype is allowed. If None, infer.
- **copy**: bool or None, default None
	- Copy data from inputs. For dict data, the default of None behaves like `copy=True`. For DataFrame or 2d ndarray input, the default of None behaves like `copy=False`. If data is a dict containing one or more Series (possibly of different dtypes), `copy=False` will ensure that these inputs are not copied.

### Hierarchical Dataframes
`MultiIndex`
- Lets you have multiple columns acting as a row identifier, while having each index column related to another through a parent/child relationship.
	- Multiple dimensions for every row so you can have a row within a row. 
- Enables you to store and manipulate data with an arbitrary number of dimensions in lower dimensional data structures like `Series` and `Dataframes`
- Can be created from a list of arrays, an array of tuples, a crossed set of iterables, or a dataframe. 

## Other Dataframe Construction Functions

| Function                 | Description                                 | Notes |
| ------------------------ | ------------------------------------------- | ----- |
| `DataFrame.from_records` | Constructor from tuples, also record arrays |       |
| `DataFrame.from_dict`    | From dicts, Series, or arrays               |       |
| `read_clipboard`         | Read text from clipboard into Dataframe     |       |
| `read_table`             | Read general delimited file into Dataframe  |  |






