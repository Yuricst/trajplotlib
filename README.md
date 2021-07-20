# trajplotlib
matplotlib extension functions to plot trajectories


### 3D trajectory with equal size axes

To generate a quick 3D trajectory plot with equal-axis is a one-liner: 

```python
import matplotlib.pyplot as plt
import trajplotlib

# compute/load data for xs, ys, zs

# create plot
trajplotlib.quickplot3(xs,ys,zs, r0=184.0)
plt.show()
```

In the above, `xs`, `ys`, and `zs` are arrays of the trajectory coordinates, and `r0` is an optional value for plotting a sphere of radius `r0`. 

This generates the following: 

<p align="center">
  <img src="./examples/plot3d_example.png" width="550" title="hover text">
</p>
