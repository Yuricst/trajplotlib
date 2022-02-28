"""
Example line color
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
    ts = np.linspace(0.0, 1.0, len(data[:, 2]))  # fictitious time-stamp data

    # create plot
    fig, ax = plt.subplots(1,1,figsize=(6,6))
    
    # append data
    lc = trajplotlib.get_lc_traj_singleColor(xs, ys, cs=ts, vmin=min(ts), vmax=max(ts), cmap="viridis")
    line = ax.add_collection(lc)
    fig.colorbar(line, ax=ax, label="Time")

    # labels
    ax.set_xlabel('x, km')
    ax.set_ylabel('y, km')
    ax.set_title("My trajectory")

    # LineCollection doesn't provide matplotlib with measure of appropriate scales!
    ax.set_xlim([1.2*min(xs), 1.2*max(xs)])
    ax.set_ylim([1.2*min(ys), 1.2*max(ys)])
    plt.show()

