"""
3D plots helpers
"""

import numpy as np
import matplotlib.pyplot as plt


def set_equal_axis(ax, xlims, ylims, zlims, scale=1.0, dim3=True):
    """Helper function to set equal axis
    
    Args:
        ax (Axes3DSubplot): matplotlib 3D axis, created by `ax = fig.add_subplot(projection='3d')`
        xlims (list): 2-element list containing min and max value of x
        ylims (list): 2-element list containing min and max value of y
        zlims (list): 2-element list containing min and max value of z
        scale (float): scaling factor along x,y,z
        dim3 (bool): whether to also set z-limits (True for 3D plots)
    """
    # compute max required range
    max_range = np.array([max(xlims)-min(xlims), max(ylims)-min(ylims), max(zlims)-min(zlims)]).max() / 2.0
    # compute mid-point along each axis
    mid_x = (max(xlims) + min(xlims)) * 0.5
    mid_y = (max(ylims) + min(ylims)) * 0.5
    mid_z = (max(zlims) + min(zlims)) * 0.5
    # set limits to axis
    if dim3==True:
        ax.set_box_aspect((max_range, max_range, max_range))
    ax.set_xlim(mid_x - max_range*scale, mid_x + max_range*scale)
    ax.set_ylim(mid_y - max_range*scale, mid_y + max_range*scale)
    if dim3==True:
        ax.set_zlim(mid_z - max_range*scale, mid_z + max_range*scale)
    return


def get_sphere_coordinates(radius, center=None):
    """Get x,y,z coordinates for sphere

    Args:
        radius (float): sphere radius
        center (list): x,y,z coordinates of center; if None, set to [0.0, 0.0, 0.0]
    
    Returns:
        (tuple): x, y, z coordinates of sphere
    """
    # check if center is provided
    if center is None:
        center = [0.0, 0.0, 0.0]
    # construct reference sphere
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    #u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x_sphere = center[0] + radius*np.cos(u)*np.sin(v)
    y_sphere = center[1] + radius*np.sin(u)*np.sin(v)
    z_sphere = center[2] + radius*np.cos(v)
    return x_sphere, y_sphere, z_sphere


def plot_sphere_wireframe(ax, radius, center=None, color="k", linewidth=0.5):
    """Plot sphere wireframe
    
    Args:
        ax (Axes3DSubplot): matplotlib 3D axis, created by `ax = fig.add_subplot(projection='3d')`
        radius (float): radius
        center (list): x,y,z coordinates of center, if None set to [0.0, 0.0, 0.0]
        color (str): color of wireframe
        linewidth (float): linewidth of wireframe
    """
    x_sphere, y_sphere, z_sphere = get_sphere_coordinates(radius, center)
    ax.plot_wireframe(x_sphere, y_sphere, z_sphere, color=color, linewidth=linewidth)
    return


def get_ellipsoid_coordinates(rx, ry, rz, center=None, n=60):
    """Get x,y,z coordinates for ellipsoid

    Args:
        rx (float): radius in x-direction
        ry (float): radius in y-direction
        rz (float): radius in z-direction
        center (list): x,y,z coordinates of center; if None, set to [0.0, 0.0, 0.0]
        n (int): number of points to be used in each mesh direction

    Returns:
        (tuple): x, y, z coordinates of ellipsoid
    """
    # check if center is provided
    if center is None:
        center = [0.0, 0.0, 0.0]

    # grid setup
    u = np.linspace(0, 2 * np.pi, n)
    v = np.linspace(0, np.pi, n)

    # Cartesian coordinates of ellipsoid
    x_el = center[0] + rx * np.outer(np.cos(u), np.sin(v))
    y_el = center[1] + ry * np.outer(np.sin(u), np.sin(v))
    z_el = center[2] +rz * np.outer(np.ones_like(u), np.cos(v))
    return x_el, y_el, z_el


def plot_ellipsoid_wireframe(ax, rx, ry, rz, center=None, color="k", linewidth=0.5, n=60):
    """Plot ellipsoid wireframe

    Args:
        ax (Axes3DSubplot): matplotlib 3D axis, created by `ax = fig.add_subplot(projection='3d')`
        rx (float): radius in x-direction
        ry (float): radius in y-direction
        rz (float): radius in z-direction
        center (list): x,y,z coordinates of center, if None set to [0.0, 0.0, 0.0]
        color (str): color of wireframe
        linewidth (float): linewidth of wireframe
        n (int): number of points to be used in each mesh direction
    """
    x_el, y_el, z_el = get_ellipsoid_coordinates(rx, ry, rz, center=center, n=n)
    ax.plot_wireframe(x_el, y_el, z_el, color=color, linewidth=linewidth)
    return


def quickplot3(xs, ys, zs, ax=None, n_figsize=5, scale=1.0,
        lw_traj=0.75, c_traj="navy", 
        radius: float=None, center=None,
        scatter_start=True, marker_start="x", c_start="r", 
        scatter_end=True, marker_end="*", c_end="g"):
    """Plot 3D trajectory around body. 
    If `ax` is not provided, a new `matplotlib` trajectory is initialized. 
    If `ax` is provided, the trajectory is appended. 
    
    Args:
        xs (ndarray): x-coordinates of trajectory
        ys (ndarray): y-coordinates of trajectory
        zs (ndarray): z-coordinates of trajectory
        ax (Axes3DSubplot): matplotlib 3D axis, created by `ax = fig.add_subplot(projection='3d')`. If set to None, new set of axis is created. 
        n_figsize (int): fig_size is set to (n_figsize, n_figsize)
        scale (float): scaling factor along x,y,z
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
        ax = fig.add_subplot(projection='3d')
        # reference sphere around asteroid
        if radius is not None:
            plot_sphere_wireframe(ax, radius, center=center, color="k", linewidth=0.5)
        # equal size grid
        xlims = [min(xs), max(xs)]
        ylims = [min(ys), max(ys)]
        zlims = [min(zs), max(zs)]
        set_equal_axis(ax, xlims, ylims, zlims, scale)
    # plot trajectory
    ax.plot(xs, ys, zs, linewidth=lw_traj, c=c_traj)
    # scatter at the beginning/end of trajectory
    if scatter_end is True:
        ax.scatter(xs[0], ys[0], zs[0], marker=marker_start, c=c_start)
    if scatter_end is True:
        ax.scatter(xs[-1], ys[-1], zs[-1], marker=marker_end, c=c_end)
    # return Axes3DSubplot object
    return ax



