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
	trajplotlib.quickplot3(xs,ys,zs, r0=180.0)
	plt.show()
