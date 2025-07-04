---
tags: note/python
type: note
---
# Example
```python
# import all required libraries
import numpy as np
import plotly
import plotly.graph_objects as go
import plotly.offline as pyo
from plotly.offline import init_notebook_mode

init_notebook_mode(connected = True) 

np.random.seed(42)

# generating 50 random numbers
y = np.random.randn(50) 

# generating 50 random numbers
y1 = np.random.randn(50) 
fig = go.Figure() 

# updating the figure with y
fig.add_trace(go.Box(y=y)) 

# updating the figure with y1
fig.add_trace(go.Box(y=y1)) 

fig.show()

```