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

# plot trajectory
ax.plot(xs, ys, zs)   # here, xs, ys, zs are the coordinates to be plotted

# create plot with equl axis via boxing
xlims = [min(xs), max(xs)]
ylims = [min(ys), max(ys)]
zlims = [min(zs), max(zs)]
trajplotlib.set_equal_axis(ax, xlims, ylims, zlims)

# labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
```

which generates the following: 

<p align="center">
  <img src="./examples/plot3d_example.png" width="550" title="hover text">
</p>
