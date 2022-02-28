"""
Test plotting ellipsoid
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

import sys
sys.path.append("../")  # provide path to library
import trajplotlib

if __name__=="__main__":
	# construct figure
	fig = plt.figure(figsize=(5,5))
	ax = fig.add_subplot(111, projection='3d')

	# radii in each direction
	rx, ry, rz = 20, 10, 5
	# plot ellipsoid
	trajplotlib.plot_ellipsoid_wireframe(ax, rx, ry, rz)
	# set limits
	xlims = [-rx, rx]
	ylims = [-ry, ry]
	zlims = [-rz, rz]
	trajplotlib.set_equal_axis(ax, xlims, ylims, zlims)
	plt.show()

