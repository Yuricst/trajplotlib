"""
Example 3D trajectory
"""

import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append("../")  # provide path to library
import trajplotlib


if __name__=="__main__":
	# load data
	data = np.loadtxt('data_traj.csv', delimiter=',')
	xs = data[:, 0]
	ys = data[:, 1]
	zs = data[:, 2]

	# create plot
	ax = trajplotlib.quickplot3(xs,ys,zs, r0=184.0)

	# labels
	ax.set_xlabel('x, km')
	ax.set_ylabel('y, km')
	ax.set_zlabel('z, km')
	ax.set_title("My trajectory")

	plt.show()

	print(type(ax))
