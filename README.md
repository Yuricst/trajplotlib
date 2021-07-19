# trajplotlib
matplotlib extension functions to plot trajectories


### 3D trajectory with equal size axes

Create 3D plot, then set enforce equal axis by setting limits on x,y,z using `trajplotlib.set_equal_axis()` 

```python
import matplotlib.pyplot as plt
import trajplotlib

# create 3D plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# create plot with equl axis via boxing
xlims = [-800.0, 800.0]
ylims = [-800.0, 800.0]
zlims = [-250.0, 250.0]
trajplotlib.set_equal_axis(ax, xlims, ylims, zlims)
```

<p align="center">
  <img src="./examples/plot3d_example.png" width="550" title="hover text">
</p>
