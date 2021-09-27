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
            x_circle, y_circle = get_circle_coordinates(radius, center)
            ax.plot(x_circle, y_circle, c="k", linewidth=0.5)
        # equal size grid
        xlims = [min(xs), max(xs)]
        ylims = [min(ys), max(ys)]
        zlims = [min(ys), max(ys)]  # place-holder
        set_equal_axis(ax, xlims, ylims, zlims, scale, dim3=False)
    else:
        fig = None
    # plot trajectory
    ax.plot(xs, ys, linewidth=lw_traj, c=c_traj, zorder=1)
    # scatter at the beginning/end of trajectory
    if scatter_start is True:
        ax.scatter(xs[0], ys[0], marker=marker_start, c=c_start, zorder=2)
    if scatter_end is True:
        ax.scatter(xs[-1], ys[-1], marker=marker_end, c=c_end, zorder=2)
    # return Axes3DSubplot object
    return fig, ax


def get_circle_coordinates(radius, center=None, n=50):
    """Get x,y,z coordinates for circle
    
    Args:
        radius (float): radius
        center (list): x,y,z coordinates of center, if None set to [0.0, 0.0]
    """
    # check if center is provided
    if center is None:
        center = [0.0, 0.0]
    thetas = np.linspace(0, 2*np.pi, n)
    x_circle, y_circle = [], []
    for theta in thetas:
        x_circle.append(center[0] + radius*np.cos(theta))
        y_circle.append(center[1] + radius*np.sin(theta))
    return x_circle, y_circle
