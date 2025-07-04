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

# save the state of random
np.random.seed(42) 

# generating 250 random numbers
x = np.random.randn(250) 

# plotting histogram for x
fig = go.Figure(data=[go.Histogram(x=x)]) 

fig.show()

```