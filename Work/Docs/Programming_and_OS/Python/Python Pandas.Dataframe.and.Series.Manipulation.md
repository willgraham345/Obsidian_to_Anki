---
tags: note/python
type: note
---
# Background
Pandas keeps it easy, no need to make it complicated.


# Examples
## Create a new column based on results from inside current dataframe
```python
# Create a new series by adding the 'A' and 'B' series  
df['D'] = df['A'] + df['B']
```

## Get Values within a Series that Meet a Condition

## Element-Wise Operation on a Dataframe
```python
import pandas as pd  
  
def make_big(x):  
  return x.upper()  
  
data = {  
  "name": ["Sally","Mary","John"],  
  "city": ["London", "Tokyo", "Madrid"]  
}  
  
df = pd.DataFrame(data)  
  
newdf = df.applymap(make_big)  
  
print(newdf)
```


## Map applymap and apply compared
[See here](https://stackoverflow.com/questions/19798153/difference-between-map-applymap-and-apply-methods-in-pandas)