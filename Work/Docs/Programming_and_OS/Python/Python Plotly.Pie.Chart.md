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

# different individual parts in 
# total chart
countries=['India', 'canada', 
		'Australia','Brazil',
		'Mexico','Russia',
		'Germany','Switzerland',
		'Texas'] 

# values corresponding to each 
# individual country present in
# countries
values = [4500, 2500, 1053, 500,
		3200, 1500, 1253, 600, 3500] 

# plotting pie chart
fig = go.Figure(data=[go.Pie(labels=countries,
					values=values)])

fig.show()

```