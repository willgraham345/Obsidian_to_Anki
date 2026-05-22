---
summary: 
headings: ["[[#Concepts of Note]]"]
type: note/library
down: ["[[Python Plotly.Bar.Plot]]", "[[Python Plotly.Box.Plot]]", "[[Python Plotly.Histogram]]", "[[Python Plotly.Pie.Chart]]", "[[Python Plotly.Scatter.Plot]]"]
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Tuesday, July 22nd 2025, 9:37:34 am
tags: [ ]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note

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
