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

# countries on x-axis
countries=['India', 'canada',
		'Australia','Brazil',
		'Mexico','Russia',
		'Germany','Switzerland',
		'Texas'] 

# plotting corresponding y for each 
# country in x 
fig = go.Figure([go.Bar(x=countries,
						y=[80,70,60,50,
						40,50,60,70,80])]) 

fig.show()

```