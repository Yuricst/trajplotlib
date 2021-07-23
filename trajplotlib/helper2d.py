"""
2D plots helpers
"""

import numpy as np
import matplotlib.pyplot as plt

from .helper3d import set_equal_axis

def quickplot2(xs, ys, ax=None, n_figsize=5, scale=1.0,
        lw_traj=0.75, c_traj="navy", 
        radius: float=None, center=None,
        scatter_start=True, marker_start="x", c_start="r", 
        scatter_end=True, marker_end="*", c_end="g"):
    """Plot 2D trajectory around body. 
    If `ax` is not provided, a new `matplotlib` trajectory is initialized. 
    If `ax` is provided, the trajectory is appended. 
    
    Args:
        xs (ndarray): x-coordinates of trajectory
        ys (ndarray): y-coordinates of trajectory
        ax (Axes3DSubplot): matplotlib 3D axis, created by `ax = fig.add_subplot(projection='3d')`. If set to None, new set of axis is created. 
        n_figsize (int): fig_size is set to (n_figsize, n_figsize)
        scale (float): scaling factor along x,y,z direction
        lw_traj (float): linewidth for trajectory
        c_traj (str): color for trajectory
        radius (float): radius of sphere at the center
        center (list): x,y,z coordinates of center, if None set to [0.0, 0.0, 0.0]
        scatter_start (bool): whether to plot marker at the beginning of trajectory
        marker_start (str): marker at the beginning of trajectory
        c_start (str): marker color at the beginning of trajectory
        scatter_end (bool): whether to plot marker at the end of trajectory
        marker_end (str): marker at the end of trajectory
        c_end (str): marker color at the end of trajectory
    """
    if ax is None:
        fig = plt.figure(figsize=(n_figsize,n_figsize))
        ax = fig.add_subplot()
        # reference sphere around asteroid
        if radius is not None:
            NOT_IMPLEMENTED_ERROR = 0
            #plot_sphere_wireframe(ax, radius, center=center, color="k", linewidth=0.5)
        # equal size grid
        xlims = [scale*min(xs), scale*max(xs)]
        ylims = [scale*min(ys), scale*max(ys)]
        zlims = [scale*min(ys), scale*max(ys)]  # place-holder
        set_equal_axis(ax, xlims, ylims, zlims, dim3=False)
    # plot trajectory
    ax.plot(xs, ys, linewidth=lw_traj, c=c_traj)
    # scatter at the beginning/end of trajectory
    if (scatter_start is True) and (marker_start is not None):
        ax.scatter(xs[0], ys[0], marker=marker_start, c=c_start)
    if (scatter_end is True) and (marker_end is not None):
        ax.scatter(xs[-1], ys[-1], marker=marker_end, c=c_end)
    # return Axes3DSubplot object
    return ax


