"""
Example 3D trajectory
"""

import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append("../")
import trajplotlib


if __name__=="__main__":
	# load data
	data = np.loadtxt('data_traj.csv', delimiter=',')
	x = data[:, 0]
	y = data[:, 1]
	z = data[:, 2]

	# create plot
	fig = plt.figure()
	ax = fig.add_subplot(projection='3d')

	# plot trajectory
	ax.plot(x, y, z)
	ax.scatter(x[0], y[0], z[0], marker="x", c="r")
	ax.scatter(x[-1], y[-1], z[-1], marker="*", c="g")

	# create plot with equl axis via boxing
	xlims = [min(x), max(x)]
	ylims = [min(y), max(y)]
	zlims = [min(z), max(z)]
	trajplotlib.set_equal_axis(ax, xlims, ylims, zlims)
	
	# reference sphere
	trajplotlib.plot_sphere_wireframe(ax, radius=230.0, color="k", linewidth=0.5)
	# labels
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')
	plt.show()
