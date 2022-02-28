"""
Example 3D trajectory animated
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
	ts = np.linspace(0.0, 1.0, len(data[:, 2]))  # fictitious time-stamp data

	# create plot
	fig, ax, anis = trajplotlib.animate_trajectory_3d(xs,ys,zs,ts)

	# labels
	ax.set_xlabel('x, km')
	ax.set_ylabel('y, km')
	ax.set_zlabel('z, km')
	ax.set_title("My trajectory")

	plt.show()

