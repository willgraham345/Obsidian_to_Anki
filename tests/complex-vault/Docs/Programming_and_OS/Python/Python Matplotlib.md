---
summary: 
headings: 
type: note/library
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Tuesday, July 22nd 2025, 9:34:43 am
tags: [ ]
used_by: ["[[Python Visualization]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Object-Oriented Matplotlib
```python
# Create Figure (empty canvas)
fig = plt.figure()

# Add set of axes to figure
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # left, bottom, width, height (range 0 to 1)

# Plot on that set of axes
axes.plot(x, y, 'b')
axes.set_xlabel('Set X Label') # Notice the use of set_ to begin methods
axes.set_ylabel('Set y Label')
axes.set_title('Set Title')
```

## Good Matplotlib Resources
* http://www.matplotlib.org - The project web page for matplotlib.
* https://github.com/matplotlib/matplotlib - The source code for matplotlib.
* http://matplotlib.org/gallery.html - A large gallery showcaseing various types of plots matplotlib can create. Highly recommended!
* http://www.loria.fr/~rougier/teaching/matplotlib - A good matplotlib tutorial.
* http://scipy-lectures.github.io/matplotlib/matplotlib.html - Another good matplotlib reference.
