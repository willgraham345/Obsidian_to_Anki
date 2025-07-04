---
tags: note/python
type: note
---
# Background
There are 3 main modules in plotly
- `plotly.plotly`: Acts as interface between local machine and Plotly. Contains functions that require a response from Plotly's server.
- `plotly.graph_objects`: Module that contains the objects that are responsible for creating the plots. 
	- Figure can be represented as either a `dict`, or instances of `plotly.graph_objects.Figure`. 
- Figures are represented as trees where the root node has the top 3 layer attributes:
	- `data`, `layout`, and `frames`

For a better overall idea, see [this tutorial](https://www.geeksforgeeks.org/using-plotly-for-interactive-data-visualization-in-python/?ref=lbp)

# Older notes
Cufflinks is plugin that combines plotly with dataframe visualizations
- **Good tutorials here**: https://github.com/santosjorge/cufflinks
- 